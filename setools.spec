#
# Conditional build:
%bcond_without	python2	# Python 2.x modules
%bcond_without	python3	# Python 3.x modules
#
Summary:	Policy analysis tools for SELinux
Summary(pl.UTF-8):	Narzędzia do analizy polityk SELinuksa
Name:		setools
Version:	4.1.1
Release:	1
License:	GPL v2+ (tools), LGPL v2.1+ (libraries)
Group:		Applications/System
#Source0Download: https://github.com/TresysTechnology/setools/releases
Source0:	https://github.com/TresysTechnology/setools/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	54cf5c0ca2aa4ef7c6ac153981af34cd
# https://github.com/TresysTechnology/setools/issues/174
# https://github.com/bigon/setools/commit/e41adf01647c695b80b112b337e76021bb9f30c3.patch
Patch0:		%{name}-format-truncation.patch
URL:		https://github.com/TresysTechnology/setools4/wiki
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libsepol-devel >= 2.7
BuildRequires:	libsepol-static >= 2.7
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	swig-python >= 2.0.12
Suggests:	policy-sources
%if %{with python2}
Requires:	python-setools = %{version}-%{release}
%else
Requires:	python3-setools = %{version}-%{release}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%if %{with python2}
Requires:	python-setoolsgui = %{version}-%{release}
%else
Requires:	python3-setoolsgui = %{version}-%{release}
%endif

%description gui
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following graphical tools:
- apol: policy analysis tool

%description gui -l pl.UTF-8
SETools to zbiór narzędzi graficznych, narzędzi linii poleceń oraz
bibliotek mających na celu ułatwienie analizy polityk SELinuksa.

Ten pakiet zawiera narzędzia graficzne:
- apol - narzędzie do analizy polityk

%package -n python-setools
Summary:	Python 2 bindings for SELinux policy analysis libraries
Summary(pl.UTF-8):	Wiązania Pythona 2 do bibliotek analizy polityk SELinuksa
License:	LGPL v2.1+ (core modules), GPL v2+ (seinfo and sesearch)
Group:		Libraries/Python
Requires:	python-enum34
Requires:	python-modules >= 1:2.7
Requires:	python-networkx >= 1.8
Suggests:	python-selinux

%description -n python-setools
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Python bindings for SELinux policy analysis
libraries.

%description -n python-setools -l pl.UTF-8
SETools to zbiór narzędzi graficznych, narzędzi linii poleceń oraz
bibliotek mających na celu ułatwienie analizy polityk SELinuksa.

Ten pakiet zawiera wiązania Pythona do bibliotek analizy polityk
SELinuksa.

%package -n python-setoolsgui
Summary:	SETools GUI modules for Python 2
Summary(pl.UTF-8):	Moduły graficznego interfejsu użytkownika SETools dla Pythona 2
Group:		Libraries/Python
Requires:	python-setools = %{version}-%{release}
Requires:	python-PyQt5 >= 5

%description -n python-setoolsgui
SETools GUI modules for Python 2.

%description -n python-setoolsgui -l pl.UTF-8
Moduły graficznego interfejsu użytkownika SETools dla Pythona 2.

%package -n python3-setools
Summary:	Python 3 bindings for SELinux policy analysis libraries
Summary(pl.UTF-8):	Wiązania Pythona 3 do bibliotek analizy polityk SELinuksa
Group:		Libraries/Python
%if "%{py3_ver}" < "3.4"
Requires:	python3-enum34
%endif
Requires:	python3-modules >= 1:3.3
Requires:	python3-networkx >= 1.8
Suggests:	python3-selinux

%description -n python3-setools
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Python bindings for SELinux policy analysis
libraries.

%description -n python3-setools -l pl.UTF-8
SETools to zbiór narzędzi graficznych, narzędzi linii poleceń oraz
bibliotek mających na celu ułatwienie analizy polityk SELinuksa.

Ten pakiet zawiera wiązania Pythona do bibliotek analizy polityk
SELinuksa.

%package -n python3-setoolsgui
Summary:	SETools GUI modules for Python 3
Summary(pl.UTF-8):	Moduły graficznego interfejsu użytkownika SETools dla Pythona 3
Group:		Libraries/Python
Requires:	python3-setools = %{version}-%{release}
Requires:	python3-PyQt5 >= 5

%description -n python3-setoolsgui
SETools GUI modules for Python 3.

%description -n python3-setoolsgui -l pl.UTF-8
Moduły graficznego interfejsu użytkownika SETools dla Pythona 3.

%prep
%setup -q
%patch0 -p1

%build
export SEPOL=%{_libdir}/libsepol.a

%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

export SEPOL=%{_libdir}/libsepol.a

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py_install

%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sediff
%attr(755,root,root) %{_bindir}/sedta
%attr(755,root,root) %{_bindir}/seinfo
%attr(755,root,root) %{_bindir}/seinfoflow
%attr(755,root,root) %{_bindir}/sesearch
%{_mandir}/man1/sediff.1*
%{_mandir}/man1/sedta.1*
%{_mandir}/man1/seinfo.1*
%{_mandir}/man1/seinfoflow.1*
%{_mandir}/man1/sesearch.1*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apol
%{_mandir}/man1/apol.1*

%if %{with python2}
%files -n python-setools
%defattr(644,root,root,755)
%doc COPYING ChangeLog KNOWN-BUGS README.md
%dir %{py_sitedir}/setools
%{py_sitedir}/setools/diff
%dir %{py_sitedir}/setools/policyrep
%attr(755,root,root) %{py_sitedir}/setools/policyrep/_qpol.so
%{py_sitedir}/setools/policyrep/*.py[co]
%{py_sitedir}/setools/*.py[co]
%{py_sitedir}/setools/perm_map
%{py_sitedir}/setools-%{version}-py*.egg-info

%files -n python-setoolsgui
%defattr(644,root,root,755)
%{py_sitedir}/setoolsgui
%endif

%if %{with python3}
%files -n python3-setools
%defattr(644,root,root,755)
%doc COPYING ChangeLog KNOWN-BUGS README.md
%dir %{py3_sitedir}/setools
%{py3_sitedir}/setools/diff
%dir %{py3_sitedir}/setools/policyrep
%attr(755,root,root) %{py3_sitedir}/setools/policyrep/_qpol.cpython-*.so
%{py3_sitedir}/setools/policyrep/*.py
%{py3_sitedir}/setools/policyrep/__pycache__
%{py3_sitedir}/setools/*.py
%{py3_sitedir}/setools/perm_map
%{py3_sitedir}/setools/__pycache__
%{py3_sitedir}/setools-%{version}-py*.egg-info

%files -n python3-setoolsgui
%defattr(644,root,root,755)
%{py3_sitedir}/setoolsgui
%endif
