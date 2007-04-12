%define module	Unicode-MapUTF8
%define name	perl-%{module}
%define version 1.11
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Conversions to and from arbitrary character sets and UTF8
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/S/SN/SNOWHARE/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl(Unicode::Map)
Buildrequires:	perl(Unicode::Map8)
Buildrequires:	perl(Jcode)
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Unicode
%{_mandir}/*/*


