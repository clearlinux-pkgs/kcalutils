#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcalutils
Version  : 25.04.2
Release  : 86
URL      : https://download.kde.org/stable/release-service/25.04.2/src/kcalutils-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/kcalutils-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/kcalutils-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : grantlee-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kpimtextedit-dev
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kcalutils-25.04.2
cd %{_builddir}/kcalutils-25.04.2
pushd ..
cp -a kcalutils-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749567583
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749567583
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcalutils
cp %{_builddir}/kcalutils-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/kcalutils/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcalutils/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcalutils/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcalutils/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kcalutils/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kcalutils-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kcalutils/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/kcalutils-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kcalutils/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libkcalutils6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kcalutils.categories
/usr/share/qlogging-categories6/kcalutils.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KCalUtils/KCalUtils/DndFactory
/usr/include/KPim6/KCalUtils/KCalUtils/ICalDrag
/usr/include/KPim6/KCalUtils/KCalUtils/IncidenceFormatter
/usr/include/KPim6/KCalUtils/KCalUtils/RecurrenceActions
/usr/include/KPim6/KCalUtils/KCalUtils/Stringify
/usr/include/KPim6/KCalUtils/KCalUtils/VCalDrag
/usr/include/KPim6/KCalUtils/kcalutils/dndfactory.h
/usr/include/KPim6/KCalUtils/kcalutils/icaldrag.h
/usr/include/KPim6/KCalUtils/kcalutils/incidenceformatter.h
/usr/include/KPim6/KCalUtils/kcalutils/kcalutils_export.h
/usr/include/KPim6/KCalUtils/kcalutils/recurrenceactions.h
/usr/include/KPim6/KCalUtils/kcalutils/stringify.h
/usr/include/KPim6/KCalUtils/kcalutils/vcaldrag.h
/usr/include/KPim6/KCalUtils/kcalutils_version.h
/usr/lib64/cmake/KPim6CalendarUtils/KPim6CalendarUtilsConfig.cmake
/usr/lib64/cmake/KPim6CalendarUtils/KPim6CalendarUtilsConfigVersion.cmake
/usr/lib64/cmake/KPim6CalendarUtils/KPim6CalendarUtilsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6CalendarUtils/KPim6CalendarUtilsTargets.cmake
/usr/lib64/libKPim6CalendarUtils.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6CalendarUtils.so.6.4.2
/V3/usr/lib64/qt6/plugins/kf6/ktexttemplate/kcalendar_grantlee_plugin.so
/usr/lib64/libKPim6CalendarUtils.so.6
/usr/lib64/libKPim6CalendarUtils.so.6.4.2
/usr/lib64/qt6/plugins/kf6/ktexttemplate/kcalendar_grantlee_plugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcalutils/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcalutils/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kcalutils/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kcalutils/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kcalutils/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kcalutils/cadc9e08cb956c041f87922de84b9206d9bbffb2

%files locales -f libkcalutils6.lang
%defattr(-,root,root,-)

