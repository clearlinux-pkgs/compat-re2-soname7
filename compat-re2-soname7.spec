#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-re2-soname7
Version  : 2020.07.01
Release  : 18
URL      : https://github.com/google/re2/archive/2020-07-01/re2-2020.07.01.tar.gz
Source0  : https://github.com/google/re2/archive/2020-07-01/re2-2020.07.01.tar.gz
Summary  : RE2 is a fast, safe, thread-friendly regular expression engine.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: compat-re2-soname7-lib = %{version}-%{release}
Requires: compat-re2-soname7-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
This is the source code repository for RE2, a regular expression library.
For documentation about how to install and use RE2,
visit https://github.com/google/re2/.

%package lib
Summary: lib components for the compat-re2-soname7 package.
Group: Libraries
Requires: compat-re2-soname7-license = %{version}-%{release}

%description lib
lib components for the compat-re2-soname7 package.


%package license
Summary: license components for the compat-re2-soname7 package.
Group: Default

%description license
license components for the compat-re2-soname7 package.


%prep
%setup -q -n re2-2020-07-01
cd %{_builddir}/re2-2020-07-01

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596517364
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  includedir=/usr/include libdir=/usr/lib64


%install
export SOURCE_DATE_EPOCH=1596517364
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-re2-soname7
cp %{_builddir}/re2-2020-07-01/LICENSE %{buildroot}/usr/share/package-licenses/compat-re2-soname7/e310076ee4f65219003bfae2427646e0236c5141
cp %{_builddir}/re2-2020-07-01/re2/fuzzing/compiler-rt/LICENSE %{buildroot}/usr/share/package-licenses/compat-re2-soname7/483d1c97dc79ef8741eae507897ca39cfe19da36
%make_install includedir=/usr/include libdir=/usr/lib64
## Remove excluded files
rm -f %{buildroot}/usr/include/re2/filtered_re2.h
rm -f %{buildroot}/usr/include/re2/re2.h
rm -f %{buildroot}/usr/include/re2/set.h
rm -f %{buildroot}/usr/include/re2/stringpiece.h
rm -f %{buildroot}/usr/lib64/libre2.so
rm -f %{buildroot}/usr/lib64/pkgconfig/re2.pc

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libre2.so.7
/usr/lib64/libre2.so.7.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-re2-soname7/483d1c97dc79ef8741eae507897ca39cfe19da36
/usr/share/package-licenses/compat-re2-soname7/e310076ee4f65219003bfae2427646e0236c5141
