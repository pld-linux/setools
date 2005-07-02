Summary:	SELinux tools for managing policy
Summary(pl):	Narzêdzia do zarz±dzania polityk± SELinux
Name:		setools
Version:	2.1.1
Release:	0.1
License:	GPL
Group:		Base
#Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tar.bz2
#Source0Download: http://www.tresys.com/selinux/selinux_policy_tools.html
Source0:	http://www.tresys.com/Downloads/selinux-tools/%{name}-%{version}.tar.bz2
# Source0-md5:	b90ea097e39d01695cfc4033623d322e
Patch0:		%{name}-opt.patch
URL:		http://www.tresys.com/selinux/selinux_policy_tools.html
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libselinux-devel
BuildRequires:	perl-base
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
  interface for viewing the source files of a policy, configuring
  policy program modules, editing policy files, and making and testing
  the policy.
- seuser: A GUI and command line user manager tool for SELinux. This
  is a tool that actually manages a portion of a running policy (i.e.,
  user accounts).
- seuser scripts: A set of shell scripts: seuseradd, seusermod, and
  seuserdel. These scripts combine the functions of the associated s*
  commands with seuser to provide a single interface to manage users
  in SE Linux.

And the following tool which can serve as building blocks for the
development of additional tools:
- awish: A version of the Tcl/Tk wish interpreter that includes the
  setools libraries. It's used to test SELinux GUIs (apol and seuser
  have the interpreter compiled within them). One could conceivably
  write one's own GUI tools using Tcl/Tk as extended via awish.
- libapol: The main policy.conf analysis library, which is the core
  library for all our tools.
- libseuser: The primary logic used for seuser.

%description -l pl
Ten pakiet zawiera narzêdzia i biblioteki dla Linuksa w wersji
Security-enhanced (jest to projekt z rozszerzon± funkcjonalno¶ci±
zwi±zan± z bezpieczeñstwem opracowan± w celu dodania mandatowej
kontroli dostêpu do Linuksa). Ten pakiet zawiera nastêpuj±ce
narzêdzia:
- apol - narzêdzie do analizy polityki z graficznym interfejsem.
- sepcut - podstawowe graficzne narzêdzie do konfiguracji,
  przegl±dania, edycji i testowania polityki, maj±ce zapewniæ
  kompletny interfejs do przegl±dania plików ¼ród³owych polityki,
  konfigurowania modu³ów programu polityki, edycji plików polityki
  oraz tworzenia i testowania polityki.
- seuser - graficzne oraz dzia³aj±ce z linii poleceñ narzêdzie do
  zarz±dzania u¿ytkownikami dla SELinuksa. Jest to narzêdzie
  zarz±dzaj±ce czê¶ci± funkcjonuj±cej polityki (czyli kontami
  u¿ytkowników).
- skrypty seuser - zbiór skryptów pow³oki: seuseradd, seusermod oraz
  seuserdel. £±cz± one funkcjonalno¶æ poleceñ s* z seuser, aby
  zapewniæ pojedynczy interfejs do zarz±dzania u¿ytkownikami w
  SELinuksie.
- libapol - g³ówna biblioteka analizy policy.conf, która jest rdzeniem
  wszystkich narzêdzi z setools.
- libseuser - podstawowa logika u¿ywana przez seuser.

Pakiet zawiera tak¿e narzêdzie mog±ce s³u¿yæ jako czê¶æ do budowania
innych narzêdzi - jest to awish, czyli wersja interpretera wish z
Tcl/Tk zawieraj±ca biblioteki setools. Jest u¿ywany do testowania
GUI dla SELinuksa (apol i seuser maj± interpreter wkompilowany).
Mo¿na pisaæ w³asne graficzne narzêdzia przy u¿yciu awisha.

%package devel
Summary:	Header files for setools libraries
Summary(pl):	Pliki nag³ówkowe bibliotek setools
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for setools libraries: libapol, libseaudit, libsefs,
libseuser.

%description devel -l pl
Pliki nag³ówkowe bibliotek setools: libapol, libseaudit, libsefs,
libseuser.

%package static
Summary:	Static setools libraries
Summary(pl):	Statyczne bibliotek setools
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static setools libraries.

%description static -l pl
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/setools

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/setools

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
