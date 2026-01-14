#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	PostScript
%define		pnam	Font
Summary:	PostScript::Font - Perl module to fetch data from PostScript fonts
Summary(pl.UTF-8):	PostScript::Font - moduł Perla do wyciągania informacji z czcionek postsctiptowych
Name:		perl-PostScript-Font
Version:	1.10
Release:	3
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	226785389aeffbbf34eb7a4c9cb41e3c
URL:		http://search.cpan.org/dist/PostScript-Font/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript::Font Perl module reads PostScript font files and stores
the information in memory.

%description -l pl.UTF-8
Moduł Perla PostScript::Font czyta pliki czcionek postscriptowych i
przechowuje w pamięci zawarte w nich informacje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man[13]/*
