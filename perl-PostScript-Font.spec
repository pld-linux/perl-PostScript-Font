%include	/usr/lib/rpm/macros.perl
%define	pdir	PostScript
%define	pnam	Font
Summary:	PostScript::Font perl module
Summary(pl):	Modu³ perla PostScript::Font
Name:		perl-PostScript-Font
Version:	1.05
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript::Font - module to fetch data from PostScript fonts.

%description -l pl
PostScript::Font - modu³ do wyci±gania informacji z czcionek
PostScriptowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/PostScript/*.pm
%{_mandir}/man[13]/*
