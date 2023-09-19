#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcalutils
Version  : 23.08.1
Release  : 61
URL      : https://download.kde.org/stable/release-service/23.08.1/src/kcalutils-23.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.1/src/kcalutils-23.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.1/src/kcalutils-23.08.1.tar.xz.sig
Summary  : The KDE calendar utility library
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1
Requires: kcalutils-data = %{version}-%{release}
Requires: kcalutils-lib = %{version}-%{release}
Requires: kcalutils-license = %{version}-%{release}
Requires: kcalutils-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : grantlee-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kpimtextedit-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

%package data
Summary: data components for the kcalutils package.
Group: Data

%description data
data components for the kcalutils package.


%package dev
Summary: dev components for the kcalutils package.
Group: Development
Requires: kcalutils-lib = %{version}-%{release}
Requires: kcalutils-data = %{version}-%{release}
Provides: kcalutils-devel = %{version}-%{release}
Requires: kcalutils = %{version}-%{release}

%description dev
dev components for the kcalutils package.


%package lib
Summary: lib components for the kcalutils package.
Group: Libraries
Requires: kcalutils-data = %{version}-%{release}
Requires: kcalutils-license = %{version}-%{release}

%description lib
lib components for the kcalutils package.


%package license
Summary: license components for the kcalutils package.
Group: Default

%description license
license components for the kcalutils package.


%package locales
Summary: locales components for the kcalutils package.
Group: Default

%description locales
locales components for the kcalutils package.


%prep
%setup -q -n kcalutils-23.08.1
cd %{_builddir}/kcalutils-23.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695095712
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1695095712
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcalutils
cp %{_builddir}/kcalutils-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/kcalutils/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcalutils/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcalutils/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcalutils/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kcalutils/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kcalutils-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kcalutils/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/kcalutils-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kcalutils/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang libkcalutils5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kcalutils.categories
/usr/share/qlogging-categories5/kcalutils.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim5/KCalUtils/KCalUtils/DndFactory
/usr/include/KPim5/KCalUtils/KCalUtils/ICalDrag
/usr/include/KPim5/KCalUtils/KCalUtils/IncidenceFormatter
/usr/include/KPim5/KCalUtils/KCalUtils/RecurrenceActions
/usr/include/KPim5/KCalUtils/KCalUtils/Stringify
/usr/include/KPim5/KCalUtils/KCalUtils/VCalDrag
/usr/include/KPim5/KCalUtils/kcalutils/dndfactory.h
/usr/include/KPim5/KCalUtils/kcalutils/icaldrag.h
/usr/include/KPim5/KCalUtils/kcalutils/incidenceformatter.h
/usr/include/KPim5/KCalUtils/kcalutils/kcalutils_export.h
/usr/include/KPim5/KCalUtils/kcalutils/recurrenceactions.h
/usr/include/KPim5/KCalUtils/kcalutils/stringify.h
/usr/include/KPim5/KCalUtils/kcalutils/vcaldrag.h
/usr/include/KPim5/KCalUtils/kcalutils_version.h
/usr/lib64/cmake/KPim5CalendarUtils/KPim5CalendarUtilsConfig.cmake
/usr/lib64/cmake/KPim5CalendarUtils/KPim5CalendarUtilsConfigVersion.cmake
/usr/lib64/cmake/KPim5CalendarUtils/KPim5CalendarUtilsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5CalendarUtils/KPim5CalendarUtilsTargets.cmake
/usr/lib64/libKPim5CalendarUtils.so
/usr/lib64/qt5/mkspecs/modules/qt_KCalUtils.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/grantlee/5.3/kcalendar_grantlee_plugin.so
/V3/usr/lib64/libKPim5CalendarUtils.so.5.24.1
/usr/lib64/grantlee/5.3/kcalendar_grantlee_plugin.so
/usr/lib64/libKPim5CalendarUtils.so.5
/usr/lib64/libKPim5CalendarUtils.so.5.24.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcalutils/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcalutils/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kcalutils/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kcalutils/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kcalutils/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kcalutils/cadc9e08cb956c041f87922de84b9206d9bbffb2

%files locales -f libkcalutils5.lang
%defattr(-,root,root,-)

