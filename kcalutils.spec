#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcalutils
Version  : 22.12.0
Release  : 50
URL      : https://download.kde.org/stable/release-service/22.12.0/src/kcalutils-22.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.0/src/kcalutils-22.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.0/src/kcalutils-22.12.0.tar.xz.sig
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
BuildRequires : kcodecs-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kwidgetsaddons-dev

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
%setup -q -n kcalutils-22.12.0
cd %{_builddir}/kcalutils-22.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670543321
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1670543321
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcalutils
cp %{_builddir}/kcalutils-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/kcalutils/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kcalutils-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kcalutils/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcalutils/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcalutils/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcalutils/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcalutils-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kcalutils/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kcalutils-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kcalutils/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/kcalutils-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kcalutils/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build
%make_install
popd
%find_lang libkcalutils5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kcalutils.categories
/usr/share/qlogging-categories5/kcalutils.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KCalUtils/KCalUtils/DndFactory
/usr/include/KF5/KCalUtils/KCalUtils/HTMLExportSettings
/usr/include/KF5/KCalUtils/KCalUtils/HtmlExport
/usr/include/KF5/KCalUtils/KCalUtils/ICalDrag
/usr/include/KF5/KCalUtils/KCalUtils/IncidenceFormatter
/usr/include/KF5/KCalUtils/KCalUtils/RecurrenceActions
/usr/include/KF5/KCalUtils/KCalUtils/Stringify
/usr/include/KF5/KCalUtils/KCalUtils/VCalDrag
/usr/include/KF5/KCalUtils/kcalutils/dndfactory.h
/usr/include/KF5/KCalUtils/kcalutils/htmlexport.h
/usr/include/KF5/KCalUtils/kcalutils/htmlexportsettings.h
/usr/include/KF5/KCalUtils/kcalutils/icaldrag.h
/usr/include/KF5/KCalUtils/kcalutils/incidenceformatter.h
/usr/include/KF5/KCalUtils/kcalutils/kcalutils_export.h
/usr/include/KF5/KCalUtils/kcalutils/recurrenceactions.h
/usr/include/KF5/KCalUtils/kcalutils/stringify.h
/usr/include/KF5/KCalUtils/kcalutils/vcaldrag.h
/usr/include/KF5/KCalUtils/kcalutils_version.h
/usr/lib64/cmake/KF5CalendarUtils/KF5CalendarUtilsConfig.cmake
/usr/lib64/cmake/KF5CalendarUtils/KF5CalendarUtilsConfigVersion.cmake
/usr/lib64/cmake/KF5CalendarUtils/KF5CalendarUtilsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5CalendarUtils/KF5CalendarUtilsTargets.cmake
/usr/lib64/libKF5CalendarUtils.so
/usr/lib64/qt5/mkspecs/modules/qt_KCalUtils.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/grantlee/5.2/kcalendar_grantlee_plugin.so
/usr/lib64/libKF5CalendarUtils.so.5
/usr/lib64/libKF5CalendarUtils.so.5.22.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcalutils/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcalutils/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kcalutils/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kcalutils/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kcalutils/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kcalutils/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/kcalutils/cadc9e08cb956c041f87922de84b9206d9bbffb2

%files locales -f libkcalutils5.lang
%defattr(-,root,root,-)

