#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Type
%define		pnam	Tiny
Summary:	Type::Tiny - tiny, yet Moo(se)-compatible type constraint
Name:		perl-Type-Tiny
Version:	1.006000
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/T/TO/TOBYINK/Type-Tiny-%{version}.tar.gz
# Source0-md5:	d0b0ccc7b55cf6c54a2476bf0c264b59
URL:		http://search.cpan.org/dist/Type-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Exporter-Tiny >= 0.026
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Type::Tiny is a tiny class for creating Moose-like type constraint
objects which are compatible with Moo, Moose and Mouse.

Maybe now we won't need to have separate MooseX, MouseX and MooX
versions of everything? We can but hope...

This documents the internals of Type::Tiny. Type::Tiny::Manual is a
better starting place if you're new.

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
%doc Changes CREDITS INSTALL NEWS README TODO
%{perl_vendorlib}/Devel/TypeTiny
%{perl_vendorlib}/Error/TypeTiny.pm
%{perl_vendorlib}/Error/TypeTiny
%{perl_vendorlib}/Eval/TypeTiny.pm
%{perl_vendorlib}/Reply/Plugin/TypeTiny.pm
%{perl_vendorlib}/Test/TypeTiny.pm
%{perl_vendorlib}/Type
%{perl_vendorlib}/Types
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
