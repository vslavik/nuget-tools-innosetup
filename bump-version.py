#!/usr/bin/env python3
"""
Script to bump the Inno Setup version
Usage: ./bump-version.py <version>
Example: ./bump-version.py 6.8.0
"""

import sys
import re
from pathlib import Path


def bump_version_in_nuspec(version: str) -> None:
    """Update version in Tools.InnoSetup.nuspec file."""
    nuspec_file = Path(__file__).parent / "Tools.InnoSetup.nuspec"

    if not nuspec_file.exists():
        raise FileNotFoundError(f"File not found: {nuspec_file}")

    content = nuspec_file.read_text(encoding='latin-1')

    # Replace version tag
    new_content = re.sub(
        r'(<version>)[^<]+(</version>)',
        rf'\g<1>{version}\g<2>',
        content
    )

    if content == new_content:
        print(f"Warning: No version found in {nuspec_file}")
    else:
        nuspec_file.write_text(new_content, encoding='latin-1')
        print(f"✓ Updated version to {version} in Tools.InnoSetup.nuspec")


def bump_version_in_workflow(version: str) -> None:
    """Update version in .github/workflows/build-package.yml file."""
    workflow_file = Path(__file__).parent / ".github" / "workflows" / "build-package.yml"

    if not workflow_file.exists():
        raise FileNotFoundError(f"File not found: {workflow_file}")

    content = workflow_file.read_text(encoding='latin-1')

    # Replace INNO_VERSION environment variable
    new_content = re.sub(
        r'(INNO_VERSION:\s*)[^\s]+',
        rf'\g<1>{version}',
        content
    )

    if content == new_content:
        print(f"Warning: No INNO_VERSION found in {workflow_file}")
    else:
        workflow_file.write_text(new_content, encoding='latin-1')
        print(f"✓ Updated INNO_VERSION to {version} in .github/workflows/build-package.yml")


def validate_version(version: str) -> bool:
    """Validate that version follows semantic versioning format."""
    pattern = r'^\d+\.\d+\.\d+(?:\.\d+)?$'
    return bool(re.match(pattern, version))


def main():
    if len(sys.argv) != 2:
        print("Usage: python bump-version.py <version>")
        print("Example: python bump-version.py 6.8.0")
        sys.exit(1)

    version = sys.argv[1]

    if not validate_version(version):
        print(f"Error: Invalid version format '{version}'")
        print("Expected format: X.Y.Z or X.Y.Z.W (e.g., 6.8.0 or 6.8.0.1)")
        sys.exit(1)

    try:
        bump_version_in_nuspec(version)
        bump_version_in_workflow(version)
        print(f"\n✓ Successfully bumped version to {version}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
