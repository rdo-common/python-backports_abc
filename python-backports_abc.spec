%global srcname backports_abc
%global sum A backport of recent additions to the 'collections.abc' module

Name:           python-%{srcname}
Version:        0.5
Release:        2%{?dist}
Summary:        %{sum}

License:        Python
URL:            https://pypi.python.org/pypi/backports_abc
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python%{python3_pkgversion}-devel
BuildRequires:  python-setuptools python%{python3_pkgversion}-setuptools

%description
%{sum}.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{sum}.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{sum}.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%check
%{__python2} setup.py test
%{__python3} setup.py test


%files -n python2-%{srcname}
%license LICENSE
%doc CHANGES.rst README.rst
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc CHANGES.rst README.rst
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}*.egg-info/
%{python3_sitelib}/__pycache__/*


%changelog
* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.5-2
- Rebuild for Python 3.6

* Tue Nov 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.5-1
- Update to 0.5

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 18 2016 Orion Poplawski <orion@cora.nwra.com> - 0.4-3
- Use %%{python3_pkgversion}

* Tue Feb 2 2016 Orion Poplawski <orion@cora.nwra.com> - 0.4-2
- Fix python3 package file ownership

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 0.4-1
- Initial package
