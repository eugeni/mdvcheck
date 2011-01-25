#!/usr/bin/perl
#
# Copyright, (C) Per Oyvind Karlsen, 2011
#

use URPM;

my $urpm = new URPM;

my @hdlists = ('/tmp/hdlist.cz');

foreach my $hdlist (@hdlists) {
    $urpm->parse_hdlist($hdlist);
}

$urpm->traverse(sub {
	my ($pkg) = @_;

	my $pname = $pkg->fullname;
	my @digests = $pkg->files_digest();
	my @files = $pkg->files();
	my $i = 0;
	foreach my $file (@files) {
    	    print "$pname|$file|" . $digests[$i++] . "\n";
    }
    });

