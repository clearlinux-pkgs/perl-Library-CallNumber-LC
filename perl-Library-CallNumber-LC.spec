#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Library-CallNumber-LC
Version  : 0.23
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/D/DB/DBWELLS/Library-CallNumber-LC-0.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DB/DBWELLS/Library-CallNumber-LC-0.23.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblibrary-callnumber-lc-perl/liblibrary-callnumber-lc-perl_0.23-1.debian.tar.xz
Summary  : 'Deal with Library-of-Congress call numbers'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
Library-CallNumber-LC
Library::CallNumber::LC is mostly designed to do call number normalization, with the following goals:

%package dev
Summary: dev components for the perl-Library-CallNumber-LC package.
Group: Development
Provides: perl-Library-CallNumber-LC-devel = %{version}-%{release}

%description dev
dev components for the perl-Library-CallNumber-LC package.


%prep
%setup -q -n Library-CallNumber-LC-0.23
cd ..
%setup -q -T -D -n Library-CallNumber-LC-0.23 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Library-CallNumber-LC-0.23/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Library/CallNumber/LC.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Library::CallNumber::LC.3
