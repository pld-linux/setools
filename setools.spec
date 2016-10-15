#
# Conditional build:
%bcond_without	java	# Java bindings
%bcond_without	python	# Python bindings
#
Summary:	Policy analysis tools for SELinux
Summary(pl.UTF-8):	Narzędzia do analizy polityk SELinuksa
Name:		setools
Version:	3.3.8
Release:	5
License:	GPL v2+ (tools), LGPL v2.1+ (libraries)
Group:		Applications/System
#Source0Download: https://github.com/TresysTechnology/setools3/wiki/Download
Source0:	https://raw.githubusercontent.com/wiki/TresysTechnology/setools3/files/dists/%{name}-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	d68d0d4e4da0f01da0f208782ff04b91
Source1:	seaudit.pamd
Patch0:		%{name}-swig.patch
Patch1:		%{name}-sh.patch
Patch2:		%{name}-tcl.patch
Patch3:		%{name}-format.patch
Patch4:		%{name}-swig-part2.patch
Patch5:		%{name}-link.patch
Patch6:		%{name}-x32.patch
Patch7:		%{name}-swig-version.patch
Patch8:		%{name}-sepol.patch
Patch9:		%{name}-selinux.patch
Patch10:	python-prefix.patch
URL:		https://github.com/TresysTechnology/setools3/wiki
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	flex
BuildRequires:	gcc >= 5:3.2
BuildRequires:	gtk+2-devel >= 2:2.8
%{?with_java:BuildRequires:	jdk >= 1.2}
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libselinux-devel >= 1.30
BuildRequires:	libsepol-devel >= 2.4
BuildRequires:	libsepol-static >= 2.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2
BuildRequires:	perl-base
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel >= 1:2.7}
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sqlite3-devel >= 3.2.0
BuildRequires:	swig >= 2.0.0
%{?with_python:BuildRequires:	swig-python >= 2.0.0}
BuildRequires:	swig-tcl >= 2.0.0
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
Requires:	%{name}-libs = %{version}-%{release}
Suggests:	policy-sources
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pkgdatadir	%{_datadir}/%{name}-3.3

# python modules use Py* symbols, some of .so files are versioned
%define		skip_post_check_so	.*%{py_sitedir}/setools/.*

%description
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

The base package includes the following console tools:
- seaudit-report: audit log analysis tool
- sechecker: SELinux policy checking tool
- secmds command line tools: seinfo, sesearch, findcon, replcon, and
  indexcon
- sediff: semantic policy difference tool

%description -l pl.UTF-8
SETools to zbiór narzędzi graficznych, narzędzi linii poleceń oraz
bibliotek mających na celu ułatwienie analizy polityk SELinuksa.

Pakiet podstawowy zawiera narzędzia terminalowe:
- seaudit-report - narzędzie do analizy logu audytowego
- sechecker - narzędzie do sprawdzania polityk SELinuksa
- narzędzia linii poleceń secmds: seinfo, sesearch, findcon, replcon
  oraz indexcon
- sediff - narzędzie do znajdywania różnic semantycznych polityk

%package gui
Summary: Policy analysis graphical tools for SELinux
Summary(pl.UTF-8):	Graficzne narzędzia do analizy polityk SELinuksa
License:	GPL v2+
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.8
Requires:	tk >= 8.4
Requires:	tk-BWidget >= 1.8

%description gui
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following graphical tools:
- apol: policy analysis tool
- seaudit: audit log analysis tool
- sediffx: semantic policy difference tool

%description gui -l pl.UTF-8
SETools to zbiór narzędzi graficznych, narzędzi linii poleceń oraz
bibliotek mających na celu ułatwienie analizy polityk SELinuksa.

Ten pakiet zawiera narzędzia graficzne:
- apol - narzędzie do analizy polityk
- seaudit - narzędzie do analizy logu audytowego
- sediffx - narzędzie do znajdywania różnic semantycznych polityk

%package libs
Summary:	Policy analysis support libraries for SELinux
Summary(pl.UTF-8):	Biblioteki wspierające analizę polityk SELinuksa
License:	LGPL v2.1+
Group:		Libraries
Requires:	libselinux >= 2.4
Requires:	libsepol >= 2.4
Requires:	sqlite3 >= 3.2.0

%description libs
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following run-time libraries:
- libapol: policy analysis library
- libpoldiff: semantic policy difference library
- libqpol: library that abstracts policy internals
- libseaudit: parse and filter SELinux audit messages in log files
- libsefs: SELinux file contexts library

%description libs -l pl.UTF-8
SETools to zbiór narzędzi graficznych, narzędzi linii poleceń oraz
bibliotek mających na celu ułatwienie analizy polityk SELinuksa.

Ten pakiet zawiera biblioteki uruchomieniowe:
- libapol - analizy polityk
- libpoldiff - różnic semantycznych polityk
- libqpol - abstrakcji wnętrzności polityk
- libseaudit - analizy i filtrowania komunikatów audytowych SELinuksa
  z plików logów
- libsefs - kontekstów plików SELinuksa

%package devel
Summary:	Header files for SETools libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek SETools
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for SETools libraries: libapol, libpoldiff, libqpol,
libseaudit, libsefs.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek SETools: libapol, libpoldiff, libqpol,
libseaudit, libsefs.

%package static
Summary:	Static SETools libraries
Summary(pl.UTF-8):	Statyczne biblioteki SETools
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SETools libraries.

%description static -l pl.UTF-8
Statyczne biblioteki SETools.

%package -n java-setools
Summary:	Java bindings for SELinux policy analysis libraries
Summary(pl.UTF-8):	Wiązania Javy do bibliotek analizy polityk SELinuksa
License:	LGPL v2.1+
Group:		Libraries/Java
Requires:	%{name}-libs = %{version}-%{release}
Requires:	jre >= 1.2

%description -n java-setools
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Java bindings for the following libraries:
- libapol: policy analysis library
- libpoldiff: semantic policy difference library
- libqpol: library that abstracts policy internals
- libseaudit: parse and filter SELinux audit messages in log files
- libsefs: SELinux file contexts library

%description -n java-setools -l pl.UTF-8
SETools to zbiór narzędzi graficznych, narzędzi linii poleceń oraz
bibliotek mających na celu ułatwienie analizy polityk SELinuksa.

Ten pakiet zawiera wiązania Javy do bibliotek uruchomieniowych:
- libapol - analizy polityk
- libpoldiff - różnic semantycznych polityk
- libqpol - abstrakcji wnętrzności polityk
- libseaudit - analizy i filtrowania komunikatów audytowych SELinuksa
  z plików logów
- libsefs - kontekstów plików SELinuksa

%package -n python-setools
Summary:	Python bindings for SELinux policy analysis libraries
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek analizy polityk SELinuksa
License:	LGPL v2.1+ (core modules), GPL v2+ (seinfo and sesearch)
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-setools
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Python bindings for the following libraries:
- libapol: policy analysis library
- libpoldiff: semantic policy difference library
- libqpol: library that abstracts policy internals
- libseaudit: parse and filter SELinux audit messages in log files
- libsefs: SELinux file contexts library

%description -n python-setools -l pl.UTF-8
SETools to zbiór narzędzi graficznych, narzędzi linii poleceń oraz
bibliotek mających na celu ułatwienie analizy polityk SELinuksa.

Ten pakiet zawiera wiązania Pythona do bibliotek uruchomieniowych:
- libapol - analizy polityk
- libpoldiff - różnic semantycznych polityk
- libqpol - abstrakcji wnętrzności polityk
- libseaudit - analizy i filtrowania komunikatów audytowych SELinuksa
  z plików logów
- libsefs - kontekstów plików SELinuksa

%package -n tcl-setools
Summary:	Tcl bindings for SELinux policy analysis libraries
Summary(pl.UTF-8):	Wiązania Tcl-a do bibliotek analizy polityk SELinuksa
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	tcl >= 8.4

%description -n tcl-setools
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Tcl bindings for the following libraries:
- libapol: policy analysis library
- libpoldiff: semantic policy difference library
- libqpol: library that abstracts policy internals
- libseaudit: parse and filter SELinux audit messages in log files
- libsefs: SELinux file contexts library

%description -n tcl-setools -l pl.UTF-8
SETools to zbiór narzędzi graficznych, narzędzi linii poleceń oraz
bibliotek mających na celu ułatwienie analizy polityk SELinuksa.

Ten pakiet zawiera wiązania Tcl-a do bibliotek uruchomieniowych:
- libapol - analizy polityk
- libpoldiff - różnic semantycznych polityk
- libqpol - abstrakcji wnętrzności polityk
- libseaudit - analizy i filtrowania komunikatów audytowych SELinuksa
  z plików logów
- libsefs - kontekstów plików SELinuksa

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CLASSPATH=. \
	TCLSH_PROG=/usr/bin/tclsh \
	WISH_PROG=/usr/bin/wish \
	--disable-bwidget-check \
	--disable-selinux-check \
	%{?with_java:--enable-swig-java} \
	%{?with_python:--enable-swig-python} \
	--with-java-prefix=%{java_home}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},/etc/pam.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/seaudit
cp -p packages/rpm/*.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p apol/apol.png seaudit/seaudit.png sediff/sediffx.png $RPM_BUILD_ROOT%{_pixmapsdir}

# let rpm autodetect dependencies
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so* \
	$RPM_BUILD_ROOT%{_libdir}/setools/*/*.so*
%if %{with python}
chmod 755 $RPM_BUILD_ROOT%{py_sitedir}/setools/*.so*
%py_comp $RPM_BUILD_ROOT%{py_sitedir}/setools
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/setools
%py_postclean
%endif

%if %{with java}
# replace symlinks with direct jars
%{__mv} $RPM_BUILD_ROOT%{pkgdatadir}/*.jar $RPM_BUILD_ROOT%{_javadir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n java-setools -p /sbin/ldconfig
%postun	-n java-setools -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/findcon
%attr(755,root,root) %{_bindir}/indexcon
%attr(755,root,root) %{_bindir}/replcon
%attr(755,root,root) %{_bindir}/seaudit-report
%attr(755,root,root) %{_bindir}/sechecker
%attr(755,root,root) %{_bindir}/sediff
%attr(755,root,root) %{_bindir}/seinfo
%attr(755,root,root) %{_bindir}/sesearch
%dir %{pkgdatadir}
%{pkgdatadir}/sechecker-profiles
%{pkgdatadir}/sechecker_help.txt
%{pkgdatadir}/seaudit-report-service
%{pkgdatadir}/seaudit-report.conf
%{pkgdatadir}/seaudit-report.css
%{_mandir}/man1/findcon.1*
%{_mandir}/man1/indexcon.1*
%{_mandir}/man1/replcon.1*
%{_mandir}/man1/sechecker.1*
%{_mandir}/man1/sediff.1*
%{_mandir}/man1/seinfo.1*
%{_mandir}/man1/sesearch.1*
%{_mandir}/man8/seaudit-report.8*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apol
%attr(755,root,root) %{_bindir}/sediffx
%attr(755,root,root) %{_sbindir}/seaudit
%dir %{_libdir}/setools/apol_tcl
%attr(755,root,root) %{_libdir}/setools/apol_tcl/libapol_tcl.so.*.*
%{_libdir}/setools/apol_tcl/pkgIndex.tcl
%{pkgdatadir}/apol.gif
%{pkgdatadir}/apol_help.txt
%{pkgdatadir}/apol_perm_mapping_*
%{pkgdatadir}/domaintrans_help.txt
%{pkgdatadir}/dot_seaudit
%{pkgdatadir}/file_relabel_help.txt
%{pkgdatadir}/infoflow_help.txt
%{pkgdatadir}/sediff_help.txt
%{pkgdatadir}/seaudit_help.txt
%{pkgdatadir}/types_relation_help.txt
%{pkgdatadir}/*.glade
%{pkgdatadir}/*.png
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/seaudit
%{_desktopdir}/apol.desktop
%{_desktopdir}/seaudit.desktop
%{_desktopdir}/sediffx.desktop
%{_pixmapsdir}/apol.png
%{_pixmapsdir}/seaudit.png
%{_pixmapsdir}/sediffx.png
%{_mandir}/man1/apol.1*
%{_mandir}/man1/sediffx.1*
%{_mandir}/man8/seaudit.8*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog KNOWN-BUGS NEWS README TODO
%attr(755,root,root) %{_libdir}/libapol.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libapol.so.4
%attr(755,root,root) %{_libdir}/libpoldiff.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpoldiff.so.1
%attr(755,root,root) %{_libdir}/libqpol.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpol.so.1
%attr(755,root,root) %{_libdir}/libseaudit.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libseaudit.so.4
%attr(755,root,root) %{_libdir}/libsefs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsefs.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libapol.so
%attr(755,root,root) %{_libdir}/libpoldiff.so
%attr(755,root,root) %{_libdir}/libqpol.so
%attr(755,root,root) %{_libdir}/libseaudit.so
%attr(755,root,root) %{_libdir}/libsefs.so
%{_includedir}/apol
%{_includedir}/poldiff
%{_includedir}/qpol
%{_includedir}/seaudit
%{_includedir}/sefs
%{_pkgconfigdir}/libapol.pc
%{_pkgconfigdir}/libpoldiff.pc
%{_pkgconfigdir}/libqpol.pc
%{_pkgconfigdir}/libseaudit.pc
%{_pkgconfigdir}/libsefs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libapol.a
%{_libdir}/libpoldiff.a
%{_libdir}/libqpol.a
%{_libdir}/libseaudit.a
%{_libdir}/libsefs.a

%if %{with java}
%files -n java-setools
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjapol.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libjapol.so.4
%attr(755,root,root) %{_libdir}/libjapol.so
%attr(755,root,root) %{_libdir}/libjpoldiff.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjpoldiff.so.1
%attr(755,root,root) %{_libdir}/libjpoldiff.so
%attr(755,root,root) %{_libdir}/libjqpol.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libjqpol.so.1
%attr(755,root,root) %{_libdir}/libjqpol.so
%attr(755,root,root) %{_libdir}/libjseaudit.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libjseaudit.so.4
%attr(755,root,root) %{_libdir}/libjseaudit.so
%attr(755,root,root) %{_libdir}/libjsefs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjsefs.so.4
%attr(755,root,root) %{_libdir}/libjsefs.so
%{_javadir}/apol.jar
%{_javadir}/poldiff.jar
%{_javadir}/qpol.jar
%{_javadir}/seaudit.jar
%{_javadir}/sefs.jar
%endif

%if %{with python}
%files -n python-setools
%defattr(644,root,root,755)
%dir %{py_sitedir}/setools
%attr(755,root,root) %{py_sitedir}/setools/_apol.so*
%attr(755,root,root) %{py_sitedir}/setools/_poldiff.so*
%attr(755,root,root) %{py_sitedir}/setools/_qpol.so*
%attr(755,root,root) %{py_sitedir}/setools/_seaudit.so*
%attr(755,root,root) %{py_sitedir}/setools/_sefs.so*
%attr(755,root,root) %{py_sitedir}/setools/_seinfo.so
%attr(755,root,root) %{py_sitedir}/setools/_sesearch.so
%{py_sitedir}/setools/__init__.py[co]
%{py_sitedir}/setools/apol.py[co]
%{py_sitedir}/setools/poldiff.py[co]
%{py_sitedir}/setools/qpol.py[co]
%{py_sitedir}/setools/seaudit.py[co]
%{py_sitedir}/setools/sefs.py[co]
%{py_sitedir}/setools-1.0-py*.egg-info
%dir %{py_sitescriptdir}/setools
%{py_sitescriptdir}/setools/__init__.py[co]
%endif

%files -n tcl-setools
%defattr(644,root,root,755)
%dir %{_libdir}/setools
%dir %{_libdir}/setools/apol
%attr(755,root,root) %{_libdir}/setools/apol/libtapol.so.*.*
%{_libdir}/setools/apol/pkgIndex.tcl
%dir %{_libdir}/setools/poldiff
%attr(755,root,root) %{_libdir}/setools/poldiff/libtpoldiff.so.*.*.*
%{_libdir}/setools/poldiff/pkgIndex.tcl
%dir %{_libdir}/setools/qpol
%attr(755,root,root) %{_libdir}/setools/qpol/libtqpol.so.*.*
%{_libdir}/setools/qpol/pkgIndex.tcl
%dir %{_libdir}/setools/seaudit
%attr(755,root,root) %{_libdir}/setools/seaudit/libtseaudit.so.*.*
%{_libdir}/setools/seaudit/pkgIndex.tcl
%dir %{_libdir}/setools/sefs
%attr(755,root,root) %{_libdir}/setools/sefs/libtsefs.so.*.*.*
%{_libdir}/setools/sefs/pkgIndex.tcl
