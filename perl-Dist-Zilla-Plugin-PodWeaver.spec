%define upstream_name    Dist-Zilla-Plugin-PodWeaver
Name:		perl-%{upstream_name}
Version:	4.010
Release:	2

Summary:	Do horrible things to POD, producing better docs

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/rjbs/Dist-Zilla-Plugin-PodWeaver
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Dist-Zilla-Plugin-PodWeaver-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Pod::Elemental::PerlMunger)
BuildRequires:	perl(Pod::Weaver)

BuildArch:	noarch

# not auto-detected
Requires:	perl(Pod::Elemental::PerlMunger)

%description
PodWeaver is a work in progress, which rips apart your kinda-POD and
reconstructs it as boring old real POD.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


