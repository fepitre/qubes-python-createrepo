%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

# disable broken /usr/lib/rpm/brp-python-bytecompile
%define __os_install_post %{nil}
%define compdir %(pkg-config --variable=completionsdir bash-completion)
%if "%{compdir}" == ""
%define compdir "/etc/bash_completion.d"
%endif

%global realname createrepo

Summary: Creates a common metadata repository
Name: python2-createrepo
Version: 0.10.3
Release: 1%{?dist}
Epoch: 1000
License: GPLv2
Group: System Environment/Base
Source0: http://createrepo.baseurl.org/download/%{realname}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{realname}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArchitectures: noarch

Requires: python2 >= 2.1, python2-rpm, rpm >= 4.1.1, python2-libxml2
Requires: yum-metadata-parser, yum >= 3.4.3-4, python2-deltarpm, deltarpm, pyliblzma

BuildRequires: python2
BuildRequires: bash-completion

Patch1: ten-changelog-limit.patch
Patch2: createrepo-HEAD.patch
Patch3: 0001-Build-only-python-library.patch

%description
This utility will generate a common metadata repository from a directory of rpm
packages.

%prep
%setup -q -n %{realname}-%{version}
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT sysconfdir=%{_sysconfdir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root,-)
%doc ChangeLog README
%license COPYING COPYING.lib
%(dirname %{compdir})
%{_datadir}/%{realname}/
%{python_sitelib}/createrepo

%changelog
