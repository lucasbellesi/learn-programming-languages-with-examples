// Module focus: Tracking ownership and lifetime when multiple references can observe the same value.
// Why it matters: practicing smart pointers in depth patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for smart pointers in depth; this keeps the walkthrough readable.
sealed record Report(string Title);

sealed class ReportOwner
{
    public ReportOwner(string name, Report? current) => (Name, Current) = (name, current);

    public string Name { get; }
    public Report? Current { get; private set; }

    public void TransferTo(ReportOwner destination)
    {
        // Empty owners cannot transfer ownership, so make that state explicit.
        if (Current is null)
        {
            Console.WriteLine($"{Name} has nothing to transfer.");
            return;
        }

        // Report output values so learners can verify the smart pointers in depth result.
        Console.WriteLine($"{Name} transfers {Current.Title} to {destination.Name}.");
        destination.Current = Current;
        Current = null;
    }

    public void Describe() =>
        Console.WriteLine($"{Name}: {(Current is null ? "empty" : Current.Title)}");
}

sealed class PreviewPane
{
    private readonly WeakReference<Report> currentReport;

    public PreviewPane(Report report) => currentReport = new WeakReference<Report>(report);

    public void Describe()
    {
        // Weak observers must check whether the target is still alive.
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
    // Walk through ownership transfer and weak observation in one fixed scenario.
    static void Main()
    {
        // Start with one owner holding the report and one empty destination.
        ReportOwner inbox = new ReportOwner("Inbox", new Report("Quarterly Summary"));
        ReportOwner archive = new ReportOwner("Archive", null);

        // After transfer, the source is empty and the destination owns the report.
        inbox.Describe();
        inbox.TransferTo(archive);
        inbox.Describe();
        archive.Describe();

        PreviewPane preview = CreatePreview();
        preview.Describe();

        // Force collection so the weak-reference branch is visible in this tiny example.
        GC.Collect();
        GC.WaitForPendingFinalizers();
        GC.Collect();

        preview.Describe();
    }

    static PreviewPane CreatePreview()
    {
        // The preview does not keep this transient report alive after the method returns.
        return new PreviewPane(new Report("Transient Draft"));
    }
}
