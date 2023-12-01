import re
import sys

if len(sys.argv) <= 2:
    print("Invalid number of arguments")
    sys.exit(1)

list_txt = sys.argv[1]
versions_txt = sys.argv[2]

def extract_package_versions(text):
    package_versions = {}
    for line in text.split('\n'):
        match = re.search(r'([a-zA-Z0-9-_.]+)\s+(\d+\.\d+(\.\d+)?)', line)
        if match:
            package = match.group(1)
            version = match.group(2)
            package_versions[package] = version
    return package_versions

# Read the pip list output from the first file
with open(list_txt, 'r') as file:
    list_txt_content = file.read()

# Read the versions from the second file
with open(versions_txt, 'r') as file:
    versions_txt_content = file.read()

list_txt_versions = extract_package_versions(list_txt_content)
versions_txt_versions = extract_package_versions(versions_txt_content)

# Verify that versions.txt is a subset of pip list 
# (i.e. every package is there and correct version), if not test fails
mismatched_versions = []
matched_versions = []
for package, version in versions_txt_versions.items():
    if package in list_txt_versions:
        if list_txt_versions[package] != version:
            mismatched_versions.append((package, list_txt_versions[package], version))
        else:
            matched_versions.append((package, list_txt_versions[package], version))
    else: # missing package in config
        mismatched_versions.append((package, "MISSING", version))

if not mismatched_versions:
    print("PASS ")
    for package, version1, version2 in matched_versions:
        print(f"{package}: {version1} == {version2}")
else:
    print("Versions not matching: format is <container_verion> != <frozen_version>")
    for package, version1, version2 in mismatched_versions:
        print(f"{package}: {version1} != {version2}")
