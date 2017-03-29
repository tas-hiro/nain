# !/usr/bin/perl -l
use strict;
use utf8;
use DBI;
use Encode 'encode';

my $servername='servername';
my $username='username';
my $userid="$username\@$servername";
my $password='password';

# FreeTDS defined by ~/odbc.ini
my $dbh=DBI->connect("dbi:ODBC:FreeTDS",$userid,$password) or die $DBI::errstr;

my $query = "
select
    aiueo
from 
    q_contract_summary
";

my $sth=$dbh->prepare($query) or die $dbh->errstr;

# 出力エラー対策
$sth->{LongTruncOk}=1;
$sth->{LongReadLen}=2000000;

$sth->execute or die $dbh->errstr;

my $header = "aiu\teo\n";
print encode('utf-8', $header);

while(my $arrayref = $sth->fetchrow_arrayref){
    print join("\t", @$arrayref)."\n";

# for_debug
#    use Data::Dumper;
#    print Dumper $arrayref;
}

$sth->finish;
$dbh->disconnect;
