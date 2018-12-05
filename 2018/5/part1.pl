#!/usr/bin/perl
use strict;
use warnings;

use Path::Tiny;
use autodie; # die if problem reading or writing a file

my $dir = path("."); # /tmp

my $file = $dir->child("input");

# Read in the entire contents of a file
my $data = $file->slurp_utf8();
my $file_handle = $file->openr_utf8();

print length($data),"\n";
while (1){
        my $lastletter = "";
        my $newdata = $data;
        for my $i ('a' .. 'z') {
                my $to_replace = $i . uc $i;
                # print "replacing ", $to_replace, "\n" ;
                $newdata =~ s/$to_replace//g;
                $i = uc $i;
                $to_replace = $i . lc $i;
                # print "replacing ", $to_replace, "\n" ;
                $newdata =~ s/$to_replace//g;
        }
        # print length($newdata)-1, "\n";
        # print $newdata;
        if (length $newdata eq length $data){
                last;
        }
        $data = $newdata;
}

print length $data,"\n"