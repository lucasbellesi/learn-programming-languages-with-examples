// Module focus: Tracking ownership and lifetime when multiple references can observe the same value.
// Why it matters: practicing smart pointers in depth patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for smart pointers in depth; this keeps the walkthrough readable.
sealed class Report
{
    public Report(string title)
    {
        Title = title;
        // Report output values so learners can verify the smart pointers in depth result.
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
    // Walk through one fixed scenario so smart pointers in depth behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key smart pointers in depth path.
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
