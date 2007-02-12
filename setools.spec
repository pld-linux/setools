Summary:	SELinux tools for managing policy
Summary(pl.UTF-8):   Narzędzia do zarządzania polityką SELinux
Name:		setools
Version:	2.4
Release:	0.1
License:	GPL
Group:		Base
#Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tar.bz2
Source0:	http://tresys.com/files/setools/%{name}-%{version}.tar.bz2
# Source0-md5:	4b3d22e07fc92a5c1321bf08958dda81
Patch0:		%{name}-opt.patch
URL:		http://www.tresys.com/selinux/selinux_policy_tools.html
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libselinux-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3.0.8
BuildRequires:	tk-devel
Requires:	checkpolicy
Requires:	policy-sources
Requires:	policycoreutils
Requires:	tk-BWidget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains some tools and libraries for Security-enhanced
Linux (a project with enhanced security functionality designed to add
mandatory access controls to Linux). This package includes the
following utilities:
- apol: The GUI-based policy analysis tool.
- sepcut: A basic GUI-based policy configuration, browsing, editing,
  and testing tool, intended to provide a complete, single user
  interface for viewing the source files of a policy, configuring policy
  program modules, editing policy files, and making and testing the
  policy.
- seuser: A GUI and command line user manager tool for SELinux. This
  is a tool that actually manages a portion of a running policy (i.e.,
  user accounts).
- seuser scripts: A set of shell scripts: seuseradd, seusermod, and
  seuserdel. These scripts combine the functions of the associated s*
  commands with seuser to provide a single interface to manage users in
  SE Linux.

And the following tool which can serve as building blocks for the
development of additional tools:
- awish: A version of the Tcl/Tk wish interpreter that includes the
  setools libraries. It's used to test SELinux GUIs (apol and seuser
  have the interpreter compiled within them). One could conceivably
  write one's own GUI tools using Tcl/Tk as extended via awish.
- libapol: The main policy.conf analysis library, which is the core
  library for all our tools.
- libseuser: The primary logic used for seuser.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia i biblioteki dla Linuksa w wersji
Security-enhanced (jest to projekt z rozszerzoną funkcjonalnością
związaną z bezpieczeństwem opracowaną w celu dodania mandatowej
kontroli dostępu do Linuksa). Ten pakiet zawiera następujące
narzędzia:
- apol - narzędzie do analizy polityki z graficznym interfejsem.
- sepcut - podstawowe graficzne narzędzie do konfiguracji,
  przeglądania, edycji i testowania polityki, mające zapewnić kompletny
  interfejs do przeglądania plików źródłowych polityki, konfigurowania
  modułów programu polityki, edycji plików polityki oraz tworzenia i
  testowania polityki.
- seuser - graficzne oraz działające z linii poleceń narzędzie do
  zarządzania użytkownikami dla SELinuksa. Jest to narzędzie
  zarządzające częścią funkcjonującej polityki (czyli kontami
  użytkowników).
- skrypty seuser - zbiór skryptów powłoki: seuseradd, seusermod oraz
  seuserdel. Łączą one funkcjonalność poleceń s* z seuser, aby zapewnić
  pojedynczy interfejs do zarządzania użytkownikami w SELinuksie.
- libapol - główna biblioteka analizy policy.conf, która jest rdzeniem
  wszystkich narzędzi z setools.
- libseuser - podstawowa logika używana przez seuser.

Pakiet zawiera także narzędzie mogące służyć jako część do budowania
innych narzędzi - jest to awish, czyli wersja interpretera wish z
Tcl/Tk zawierająca biblioteki setools. Jest używany do testowania GUI
dla SELinuksa (apol i seuser mają interpreter wkompilowany). Można
pisać własne graficzne narzędzia przy użyciu awisha.

%package devel
Summary:	Header files for setools libraries
Summary(pl.UTF-8):   Pliki nagłówkowe bibliotek setools
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for setools libraries: libapol, libseaudit, libsefs,
libseuser.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek setools: libapol, libseaudit, libsefs,
libseuser.

%package static
Summary:	Static setools libraries
Summary(pl.UTF-8):   Statyczne bibliotek setools
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static setools libraries.

%description static -l pl.UTF-8
Statyczne bibliotek setools.

%prep
%setup -q
%patch0 -p1

%build
%{__make} all \
	DYNAMIC=1 \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	TCL_LIBINC="" \
	TCL_LIBS="-ltk -ltcl -lfl -lm -ldl"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SHARED_LIB_INSTALL_DIR=$RPM_BUILD_ROOT%{_libdir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc KNOWN-BUGS README apol/*.txt seaudit/seaudit_help.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/%{name}-%{version}
%{_mandir}/man[18]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
