#!/usr/bin/python
#
# Finds duplicated files in mdv packages
#

import sys
import os

def find_dups(pattern):
    """Finds duplicated files in packages"""
    files = {}
    dupes = {}
    with os.popen("urpmf %s" % pattern, "r") as fd:
        for z in fd:
            pkg, f = z.strip().split(":",1)
            if f not in files:
                files[f] = pkg
            else:
                if files[f] == pkg:
                    continue
                if pkg.find('lib') == 0:
                    continue
                dupe = (pkg, files[f])
                if dupe not in dupes:
                    dupes[dupe] = []
                dupes[dupe].append(f)
    return dupes

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s [search parameters]" % sys.argv[0]
        sys.exit(1)
    for lists in sys.argv[1:]:
        dupes = find_dups(lists)
        for pkg in dupes:
            pkg1, pkg2 = pkg
            print "%s has %d duplicated files with %s:" % (pkg1, len(dupes[pkg]), pkg2)
            for f in dupes[pkg]:
                print "  %s" % f
