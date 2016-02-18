%global srcname backports_abc
%global sum A backport of recent additions to the 'collections.abc' module

Name:           python-%{srcname}
Version:        0.4
Release:        2%{?dist}
Summary:        %{sum}

License:        Python
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
# Should be in the next release
Source1:        https://raw.githubusercontent.com/cython/backports_abc/master/LICENSE

BuildArch:      noarch
BuildRequires:  python2-devel python%{python3_pkgversion}-devel

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
cp -p %SOURCE1 .


%build
%py2_build
%py3_build


%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
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
* Thu Feb 18 2016 Orion Poplawski <orion@cora.nwra.com> - 0.4-3
- Use %%{python3_pkgversion}

* Tue Feb 2 2016 Orion Poplawski <orion@cora.nwra.com> - 0.4-2
- Fix python3 package file ownership

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 0.4-1
- Initial package
