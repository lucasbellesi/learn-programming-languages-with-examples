// Module focus: Use a small value type to group coordinates and related behavior.
// Why it matters: structs are useful when the data is compact and value-like.

using System;

readonly struct Coordinate
{
    public Coordinate(int x, int y)
    {
        X = x;
        Y = y;
    }

    public int X { get; }
    public int Y { get; }

    public int ManhattanDistanceFromOrigin()
    {
        return Math.Abs(X) + Math.Abs(Y);
    }

    public override string ToString()
    {
        return $"({X}, {Y})";
    }
}
