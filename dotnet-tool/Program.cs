using System;
using System.Diagnostics;
using System.IO;

namespace Tools.InnoSetup;
internal class Program
{
    static void Main()
    {
        using var currentProcess = Process.GetCurrentProcess();
        var dir = Path.GetDirectoryName(currentProcess.MainModule.FileName);
        var iscc = $".store/tools.innosetup/{Versions.InnoSetup}/tools.innosetup/{Versions.InnoSetup}/tools/ISCC.exe";
        var fullPath = Path.Combine(dir, iscc);
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