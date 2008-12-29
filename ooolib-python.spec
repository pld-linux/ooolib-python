%define 	module	ooolib
Summary:	Python module for creating OpenDocument documents (sp.sheet/text)
Name:		python-%{module}
Version:	0.0.16
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/ooolib/ooolib-python-%{version}.tar.gz
# Source0-md5:	63ee28caeeb7b1b88ce0e6c9ac19e00b
URL:		http://ooolib.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ooolib is a python module to be used to create simple OpenDocument
spreadsheet and text documents. 

%prep
%setup -q -n ooolib-python-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -D ooolib.py $RPM_BUILD_ROOT%{py_sitedir}/ooolib.py

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO *example*.py
%{py_sitedir}/*.py[co]
