#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Type
%define		pnam	Tiny
Summary:	Type::Tiny - tiny, yet Moo(se)-compatible type constraint
Summary(pl.UTF-8):	Type::Tiny - mały, ale zgodny z Moo(se) moduł ograniczeń typów
Name:		perl-Type-Tiny
Version:	2.010000
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/T/TO/TOBYINK/Type-Tiny-%{version}.tar.gz
# Source0-md5:	a5a1eae7158fc1d46a57dd5cfa9c95d1
URL:		https://metacpan.org/dist/Type-Tiny
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.17
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Exporter-Tiny >= 1.006
BuildRequires:	perl-Test-Simple >= 0.96
%endif
Conflicts:	perl-Kavorka <= 0.013
Conflicts:	perl-Types-ReadOnly <= 0.001
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Type::Tiny is a tiny class for creating Moose-like type constraint
objects which are compatible with Moo, Moose and Mouse.

%description -l pl.UTF-8
Type::Tiny to mała klasa do tworzenia obiektów ograniczeń typów w
stylu Moose, będących zgodnych z Moo, Moose i Mouse.

%package -n perl-Reply-Plugin-TypeTiny
Summary:	Reply::Plugin::TypeTiny - improved type constraint exceptions in Reply
Summary(pl.UTF-8):	Reply::Plugin::TypeTiny - ulepszone wyjątki z ograniczeniami typów w Reply
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-Reply-Plugin-TypeTiny
This is a small plugin to improve error messages in Reply.

%description -n perl-Reply-Plugin-TypeTiny -l pl.UTF-8
Mała wtyczka poprawiająca komunikaty błędów w Reply.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT CREDITS Changes NEWS README
%{perl_vendorlib}/Devel/TypeTiny
%{perl_vendorlib}/Error/TypeTiny.pm
%{perl_vendorlib}/Error/TypeTiny
%{perl_vendorlib}/Eval/TypeTiny.pm
%dir %{perl_vendorlib}/Eval/TypeTiny
%{perl_vendorlib}/Eval/TypeTiny/CodeAccumulator.pm
%{perl_vendorlib}/Test/TypeTiny.pm
%{perl_vendorlib}/Type
%{perl_vendorlib}/Types
%{_mandir}/man3/Error::TypeTiny*.3*
%{_mandir}/man3/Eval::TypeTiny.3*
%{_mandir}/man3/Eval::TypeTiny::CodeAccumulator.3*
%{_mandir}/man3/Test::TypeTiny.3*
%{_mandir}/man3/Type::*.3*
%{_mandir}/man3/Types::*.3*
%{_examplesdir}/%{name}-%{version}

%files -n perl-Reply-Plugin-TypeTiny
%defattr(644,root,root,755)
%{perl_vendorlib}/Reply/Plugin/TypeTiny.pm
%{_mandir}/man3/Reply::Plugin::TypeTiny.3*
