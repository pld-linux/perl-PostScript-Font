%include	/usr/lib/rpm/macros.perl
Summary:	PostScript-Font perl module
Summary(pl):	Modu� perla PostScript-Font
Name:		perl-PostScript-Font
Version:	1.02
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/PostScript/PostScript-Font-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript-Font - module to fetch data from PostScript fonts.

%description -l pl
PostScript-Font - modu� do wyci�gania informacji z czcionek
PostScriptowych.

%prep
%setup -q -n PostScript-Font-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*

%{perl_sitelib}/PostScript/*.pm
%{perl_sitearch}/auto/PostScript/Font

%{_mandir}/man[13]/*
