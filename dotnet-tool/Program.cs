using System;
using System.IO;
using System.Linq;
using System.Reflection;

namespace Tools.InnoSetup.Cli;
internal class Program
{
    static void Main()
    {
        var assembly = Assembly.GetExecutingAssembly();

        var dir = Path.GetDirectoryName(assembly.Location);
        var iscc = $"../../InnoSetup/ISCC.exe";
        var fullPath = Path.GetFullPath(Path.Combine(dir, iscc));
        if (File.Exists(fullPath))
        {
            Console.WriteLine(fullPath);
        }
        else
        {
            throw new Exception($"Could not find: {fullPath}");
        }
    }
}