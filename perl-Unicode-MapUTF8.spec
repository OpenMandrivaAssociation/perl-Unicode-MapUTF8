%define upstream_name	 Unicode-MapUTF8
%define upstream_version 1.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Conversions to and from arbitrary character sets and UTF8
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SN/SNOWHARE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Unicode::Map)
BuildRequires:	perl(Unicode::Map8)
BuildRequires:	perl(Jcode)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Unicode
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.110.0-4mdv2012.0
+ Revision: 765798
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.110.0-2
+ Revision: 667408
- mass rebuild

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.1
+ Revision: 401994
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.11-5mdv2009.0
+ Revision: 224594
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.11-4mdv2008.1
+ Revision: 180633
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.11-3mdv2008.0
+ Revision: 67546
- rebuild


* Fri Nov 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-2mdv2007.0
+ Revision: 86972
- rebuild
- Import perl-Unicode-MapUTF8

* Thu Oct 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdk
- New release 1.11
- spec cleanup

* Sat May 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.10-1mdk
- 1.10

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-4mdk
- fix buildrequires in a backward compatible way

* Thu Aug 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-3mdk 
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-2mdk
- fixed dir ownership (distlint)

* Tue Dec 09 2003 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-1mdk
- first mdk release

