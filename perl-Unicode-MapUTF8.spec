%define modname	Unicode-MapUTF8
%define modver	1.11

Summary:	Conversions to and from arbitrary character sets and UTF8
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	17
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SN/SNOWHARE/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Unicode::Map)
BuildRequires:	perl(Unicode::Map8)
BuildRequires:	perl(Jcode)
BuildRequires:	perl(Unicode::String)

%description
Provides an adapter layer between core routines for converting to and from UTF8
and other encodings. In essence, a way to give multiple existing Unicode
modules a single common interface so you don't have to know the underlaying
implementations to do simple UTF8 to-from other character set encoding
conversions. As such, it wraps the Unicode::String, Unicode::Map8, Unicode::Map
and Jcode modules in a standardized and simple API.

This also provides general character set conversion operation based on UTF8 -
it is possible to convert between any two compatible and supported character
sets via a simple two step chaining of conversions.

As with most things Perlish - if you give it a few big chunks of text to chew
on instead of lots of small ones it will handle many more characters per
second.

By design, it can be easily extended to encompass any new charset encoding
conversion modules that arrive on the scene.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files 
%doc README
%{perl_vendorlib}/Unicode
%doc %{_mandir}/man3/*

