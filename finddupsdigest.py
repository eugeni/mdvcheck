#!/usr/bin/python
#
# Finds duplicated files with different digests in mdv packages
#

import sys
import os

def find_dups_digest(digests):
    """Finds duplicated files with different digests in packages"""
    files = {}
    dupes = {}
    with open(digests, "r") as fd:
        for z in fd:
            pkg, f, digest = z.split("|", 2)
            digest = digest.strip()
            if f not in files:
                files[f] = (pkg, digest)
            else:
                # skip conflicts with self due to duplicates
                if pkg == files[f]:
                    continue
                old_pkg, old_digest = files[f]
                if digest != old_digest:
                    dupe = (pkg, old_pkg)
                    if dupe not in dupes:
                        dupes[dupe] = []
                    dupes[dupe].append((f, digest, old_digest))
    return dupes

if __name__ == "__main__":
    dupes = find_dups_digest("digests")
    for pkg in dupes:
        pkg1, pkg2 = pkg
        print "%s has %d duplicated files with %s:" % (pkg1, len(dupes[pkg]), pkg2)
        for f, digest, old_digest in dupes[pkg]:
            print "  %s (%s != %s)" % (f, digest, old_digest)
