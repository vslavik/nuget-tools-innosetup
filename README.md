
NuGet package for Inno Setup
============================

[![NuGet Version and Downloads count](https://buildstats.info/nuget/Tools.InnoSetup)](https://www.nuget.org/packages/Tools.InnoSetup)  [![Github Workflow Build Status](https://github.com/vslavik/nuget-tools-innosetup/workflows/Build%20NuGet%20package/badge.svg)](https://github.com/vslavik/nuget-tools-innosetup/actions)

This is an unofficial package of the Inno Setup installer, intended for use as
a NuGet dependency. It is published to the
[nuget.org repository](https://www.nuget.org/packages/Tools.InnoSetup/).

This package is kept up to date and with upstream IS releases and includes the
following:

 - Unicode build of Inno Setup
 - Inno Setup Preprocessor
 - encryption support
 - official translations of Inno Setup


How to install
--------------

```
dotnet add package Tools.InnoSetup
```


How to use
----------

1. Create your Inno Setup Script, let's name it `MyInnoSetupScript.iss`.
2. Add the target to the end of your `.csproj` file:
```xml
<Project ...>
  ...
  <Target Name="AfterBuild">
    <Exec Command="$(InnoSetupCompiler) MyInnoSetupScript.iss" />
  </Target>
</Project>
```
3. Build your project. The installer file will be generated according to the settings in the Inno Setup Script file.


How to build it
---------------

To build the package yourself:

1. Download the Inno Setup QuickStart Pack from https://jrsoftware.org/isdl.php
2. Run the installer with `/verysilent /allusers /dir=inst` flags
3. Package into NuGet with `nuget pack Tools.InnoSetup.nuspec`


License
-------

The license.txt file in this directory applies to Inno Setup itself. The package
spec and other support files are in the public domain.
