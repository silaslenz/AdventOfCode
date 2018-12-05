#!/usr/bin/perl
use strict;
use warnings;

use Path::Tiny;
use autodie; # die if problem reading or writing a file

my $dir = path(".");

my $file = $dir->child("input");

# Read in the entire contents of a file
my $original_data = $file->slurp_utf8();
my $file_handle = $file->openr_utf8();

my $shortest = length $original_data;
my $shortest_char = "";

print length($original_data),"\n";
for my $letter_to_remove ('a' .. 'z'){
    my $data = $original_data;
    $data =~ s/$letter_to_remove//g;
    # print length $data, "\n";
    $letter_to_remove = uc $letter_to_remove;
    $data =~ s/$letter_to_remove//g;
    # print length $data, "\n\n";

    while (1){
            my $lastletter = "";
            my $newdata = $data;
            for my $i ('a' .. 'z') {
                    my $to_replace = $i . uc $i;
                    $newdata =~ s/$to_replace//g;
                    $i = uc $i;
                    $to_replace = $i . lc $i;
                    $newdata =~ s/$to_replace//g;
            }
            if (length $newdata eq length $data){
                    last;
            }
            $data = $newdata;
    }
    if (length $data<$shortest){
        $shortest = length $data;
        $shortest_char = $letter_to_remove;
    }
}

print $shortest - 1, " when removing ", $shortest_char,"\n"