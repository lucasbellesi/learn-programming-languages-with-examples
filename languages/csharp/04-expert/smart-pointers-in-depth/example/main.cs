// This example shows tracking ownership and lifetime when multiple references can observe the same value.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
sealed class Report
{
    public Report(string title)
    {
        Title = title;
        Console.WriteLine($"Created report: {title}");
    }

    public string Title { get; }
}

sealed class ReportOwner
{
    public ReportOwner(string name, Report? current)
    {
        Name = name;
        Current = current;
    }

    public string Name { get; }

    public Report? Current { get; private set; }

    public void TransferTo(ReportOwner destination)
    {
        if (Current is null)
        {
            Console.WriteLine($"{Name} has nothing to transfer.");
            return;
        }

        Console.WriteLine($"{Name} transfers {Current.Title} to {destination.Name}.");
        destination.Current = Current;
        Current = null;
    }

    public void Describe()
    {
        Console.WriteLine($"{Name}: {(Current is null ? "empty" : Current.Title)}");
    }
}

sealed class PreviewPane
{
    private readonly WeakReference<Report> currentReport;

    public PreviewPane(Report report)
    {
        currentReport = new WeakReference<Report>(report);
    }

    public void Describe()
    {
        if (currentReport.TryGetTarget(out Report? report))
        {
            Console.WriteLine($"Preview can still see: {report.Title}");
            return;
        }

        Console.WriteLine("Preview target expired.");
    }
}

class Program
{
    // Run one deterministic scenario so the console output makes tracking ownership and lifetime when multiple references can observe the same value easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        ReportOwner inbox = new ReportOwner("Inbox", new Report("Quarterly Summary"));
        ReportOwner archive = new ReportOwner("Archive", null);

        inbox.Describe();
        archive.Describe();
        inbox.TransferTo(archive);
        inbox.Describe();
        archive.Describe();

        PreviewPane preview = CreatePreview();
        preview.Describe();

        GC.Collect();
        GC.WaitForPendingFinalizers();
        GC.Collect();

        preview.Describe();
    }

    static PreviewPane CreatePreview()
    {
        Report transient = new Report("Transient Draft");
        return new PreviewPane(transient);
    }
}
