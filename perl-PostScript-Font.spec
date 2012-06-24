%include	/usr/lib/rpm/macros.perl
%define	pdir	PostScript
%define	pnam	Font
Summary:	PostScript::Font - Perl module to fetch data from PostScript fonts
Summary(pl):	PostScript::Font - modu� Perla do wyci�gania informacji z czcionek postsctiptowych
Name:		perl-PostScript-Font
Version:	1.08
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	497b07fcc148408c32bb057abac11e0c
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript::Font Perl module reads PostScript font files and stores
the information in memory.

%description -l pl
Modu� Perla PostScript::Font czyta pliki czcionek postscriptowych i
przechowuje w pami�ci zawarte w nich informacje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/PostScript/*.pm
%{perl_sitelib}/PostScript/Font
%{_mandir}/man[13]/*
