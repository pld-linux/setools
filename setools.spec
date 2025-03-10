Summary:	Policy analysis tools for SELinux
Summary(pl.UTF-8):	Narzędzia do analizy polityk SELinuksa
Name:		setools
Version:	4.4.4
Release:	2
License:	GPL v2+ (tools), LGPL v2.1+ (libraries)
Group:		Applications/System
#Source0Download: https://github.com/SELinuxProject/setools/releases
Source0:	https://github.com/SELinuxProject/setools/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	ec0ba9630dd6800dc4313fe0e5357253
URL:		https://github.com/SELinuxProject/setools/wiki
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libsepol-devel >= 2.7
BuildRequires:	libsepol-static >= 2.7
BuildRequires:	python3-Cython >= 0.27
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	swig-python >= 2.0.12
Suggests:	policy-sources
Requires:	python3-setools = %{version}-%{release}
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
Requires:	python3-setoolsgui = %{version}-%{release}

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

%package -n python3-setools
Summary:	Python 3 bindings for SELinux policy analysis libraries
Summary(pl.UTF-8):	Wiązania Pythona 3 do bibliotek analizy polityk SELinuksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3
Requires:	python3-networkx >= 1.8
Suggests:	python3-selinux
Obsoletes:	python-setools < 4.2

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
Obsoletes:	python-setoolsgui < 4.2

%description -n python3-setoolsgui
SETools GUI modules for Python 3.

%description -n python3-setoolsgui -l pl.UTF-8
Moduły graficznego interfejsu użytkownika SETools dla Pythona 3.

%prep
%setup -q -n %{name}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

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
%lang(ru) %{_mandir}/ru/man1/sediff.1*
%lang(ru) %{_mandir}/ru/man1/sedta.1*
%lang(ru) %{_mandir}/ru/man1/seinfo.1*
%lang(ru) %{_mandir}/ru/man1/seinfoflow.1*
%lang(ru) %{_mandir}/ru/man1/sesearch.1*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apol
%attr(755,root,root) %{_bindir}/sechecker
%{_mandir}/man1/apol.1*
%{_mandir}/man1/sechecker.1*
%lang(ru) %{_mandir}/ru/man1/apol.1*

%files -n python3-setools
%defattr(644,root,root,755)
%doc COPYING ChangeLog KNOWN-BUGS README.md
%dir %{py3_sitedir}/setools
%{py3_sitedir}/setools/diff
%attr(755,root,root) %{py3_sitedir}/setools/policyrep.cpython-*.so
%{py3_sitedir}/setools/*.py
%{py3_sitedir}/setools/checker
%{py3_sitedir}/setools/perm_map
%{py3_sitedir}/setools/policyrep.pyi
%{py3_sitedir}/setools/py.typed
%{py3_sitedir}/setools/__pycache__
%{py3_sitedir}/setools-%{version}-py*.egg-info

%files -n python3-setoolsgui
%defattr(644,root,root,755)
%{py3_sitedir}/setoolsgui
