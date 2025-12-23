
NuGet package for Inno Setup
============================

[![NuGet Version](https://img.shields.io/nuget/v/Tools.InnoSetup)](https://www.nuget.org/packages/Tools.InnoSetup)
[![NuGet Downloads](https://img.shields.io/nuget/dt/Tools.InnoSetup)](https://www.nuget.org/packages/Tools.InnoSetup)
[![Github Workflow Build Status](https://github.com/vslavik/nuget-tools-innosetup/workflows/Build%20NuGet%20package/badge.svg)](https://github.com/vslavik/nuget-tools-innosetup/actions)

This is an unofficial package of the [Inno Setup](https://jrsoftware.org/isinfo.php) installer, intended for use as
a NuGet dependency. It is published to the
[nuget.org repository](https://www.nuget.org/packages/Tools.InnoSetup/).

This package is kept up to date and with upstream IS releases and includes all its components, including the official translations.

See the [official changelog](https://jrsoftware.org/files/is6-whatsnew.htm) for details on each release.


How to install
--------------

As any other NuGet package, e.g.

```
dotnet add package Tools.InnoSetup
```

The package provides the following properties to aid build integration:
- `$(InnoSetupDir)` points to the tools directory of the installed package, with Inno Setup files
- `$(InnoSetupCompiler)` points directly at the `ISCC.exe` compiler

This allows easy execution as e.g. `<Exec Command="$(InnoSetupCompiler) setup.iss"/>` in MSBuild.


How to build it
---------------

To build the package yourself:

1. Download the Inno Setup installer from https://jrsoftware.org/isdl.php
2. Run the installer with `/verysilent /allusers /dir=inst` flags
3. Package into NuGet with `nuget pack Tools.InnoSetup.nuspec`


License
-------

The license.txt file in this directory applies to Inno Setup itself. The package
spec and other support files are in the public domain.
