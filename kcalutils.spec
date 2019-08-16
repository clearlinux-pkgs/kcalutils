#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kcalutils
Version  : 19.08.0
Release  : 13
URL      : https://download.kde.org/stable/applications/19.08.0/src/kcalutils-19.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.0/src/kcalutils-19.08.0.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.0/src/kcalutils-19.08.0.tar.xz.sig
Summary  : The KDE calendar utility library
Group    : Development/Tools
License  : GPL-2.0
Requires: kcalutils-data = %{version}-%{release}
Requires: kcalutils-lib = %{version}-%{release}
Requires: kcalutils-license = %{version}-%{release}
Requires: kcalutils-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : grantlee-dev
BuildRequires : kcalcore-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kpimtextedit-dev
BuildRequires : qtbase-dev mesa-dev

%description
# KCalUtils #
This library provides a set of utility functions that help applications
access and use calendar data via the KCalendarCore library.

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
%setup -q -n kcalutils-19.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565927853
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1565927853
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcalutils
cp COPYING %{buildroot}/usr/share/package-licenses/kcalutils/COPYING
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
/usr/include/KF5/KCalUtils/KCalUtils/HtmlExport
/usr/include/KF5/KCalUtils/KCalUtils/ICalDrag
/usr/include/KF5/KCalUtils/KCalUtils/IncidenceFormatter
/usr/include/KF5/KCalUtils/KCalUtils/RecurrenceActions
/usr/include/KF5/KCalUtils/KCalUtils/Stringify
/usr/include/KF5/KCalUtils/KCalUtils/VCalDrag
/usr/include/KF5/KCalUtils/kcalutils/HTMLExportSettings
/usr/include/KF5/KCalUtils/kcalutils/dndfactory.h
/usr/include/KF5/KCalUtils/kcalutils/htmlexport.h
/usr/include/KF5/KCalUtils/kcalutils/htmlexportsettings.h
/usr/include/KF5/KCalUtils/kcalutils/icaldrag.h
/usr/include/KF5/KCalUtils/kcalutils/incidenceformatter.h
/usr/include/KF5/KCalUtils/kcalutils/kcalutils_export.h
/usr/include/KF5/KCalUtils/kcalutils/recurrenceactions.h
/usr/include/KF5/KCalUtils/kcalutils/stringify.h
/usr/include/KF5/KCalUtils/kcalutils/vcaldrag.h
/usr/include/KF5/kcalutils_version.h
/usr/lib64/cmake/KF5CalendarUtils/KF5CalendarUtilsConfig.cmake
/usr/lib64/cmake/KF5CalendarUtils/KF5CalendarUtilsConfigVersion.cmake
/usr/lib64/cmake/KF5CalendarUtils/KF5CalendarUtilsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5CalendarUtils/KF5CalendarUtilsTargets.cmake
/usr/lib64/libKF5CalendarUtils.so
/usr/lib64/qt5/mkspecs/modules/qt_KCalUtils.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/grantlee/5.1/kcalendar_grantlee_plugin.so
/usr/lib64/libKF5CalendarUtils.so.5
/usr/lib64/libKF5CalendarUtils.so.5.12.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcalutils/COPYING

%files locales -f libkcalutils5.lang
%defattr(-,root,root,-)

