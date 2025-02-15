#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: e36a856
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kparts
Version  : 6.11.0
Release  : 86
URL      : https://download.kde.org/stable/frameworks/6.11/kparts-6.11.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.11/kparts-6.11.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.11/kparts-6.11.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : Document centric plugin system
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kparts-data = %{version}-%{release}
Requires: kparts-lib = %{version}-%{release}
Requires: kparts-license = %{version}-%{release}
Requires: kparts-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
How To Build This Project
-=-=-=-=-=-=-=-=-=-=-=-=-=
--- On Unix:
cd %{dest}
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$PROJECTINSTALLDIR -DCMAKE_BUILD_TYPE=Debug ..      <- do not forget the ..
make
make install or su -c 'make install'

%package data
Summary: data components for the kparts package.
Group: Data

%description data
data components for the kparts package.


%package dev
Summary: dev components for the kparts package.
Group: Development
Requires: kparts-lib = %{version}-%{release}
Requires: kparts-data = %{version}-%{release}
Provides: kparts-devel = %{version}-%{release}
Requires: kparts = %{version}-%{release}

%description dev
dev components for the kparts package.


%package lib
Summary: lib components for the kparts package.
Group: Libraries
Requires: kparts-data = %{version}-%{release}
Requires: kparts-license = %{version}-%{release}

%description lib
lib components for the kparts package.


%package license
Summary: license components for the kparts package.
Group: Default

%description license
license components for the kparts package.


%package locales
Summary: locales components for the kparts package.
Group: Default

%description locales
locales components for the kparts package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kparts-6.11.0
cd %{_builddir}/kparts-6.11.0
pushd ..
cp -a kparts-6.11.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739578052
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
%cmake ..   -G 'Unix Makefiles'
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
%cmake ..   -G 'Unix Makefiles'
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
export SOURCE_DATE_EPOCH=1739578052
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kparts
cp %{_builddir}/kparts-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kparts/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kparts-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kparts/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kparts-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kparts/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kparts-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kparts/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kparts-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kparts/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kparts-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kparts/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kparts-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kparts/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kparts-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kparts/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kparts-%{version}/templates/kparts6-app/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kparts/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
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
%find_lang kparts6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kdevappwizard/templates/kparts6-app.tar.bz2
/usr/share/qlogging-categories6/kparts.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KParts/KParts/FileInfoExtension
/usr/include/KF6/KParts/KParts/GUIActivateEvent
/usr/include/KF6/KParts/KParts/ListingFilterExtension
/usr/include/KF6/KParts/KParts/ListingNotificationExtension
/usr/include/KF6/KParts/KParts/MainWindow
/usr/include/KF6/KParts/KParts/NavigationExtension
/usr/include/KF6/KParts/KParts/OpenUrlArguments
/usr/include/KF6/KParts/KParts/OpenUrlEvent
/usr/include/KF6/KParts/KParts/Part
/usr/include/KF6/KParts/KParts/PartActivateEvent
/usr/include/KF6/KParts/KParts/PartBase
/usr/include/KF6/KParts/KParts/PartLoader
/usr/include/KF6/KParts/KParts/PartManager
/usr/include/KF6/KParts/KParts/ReadOnlyPart
/usr/include/KF6/KParts/KParts/ReadWritePart
/usr/include/KF6/KParts/KParts/StatusBarExtension
/usr/include/KF6/KParts/kde_terminal_interface.h
/usr/include/KF6/KParts/kparts/fileinfoextension.h
/usr/include/KF6/KParts/kparts/guiactivateevent.h
/usr/include/KF6/KParts/kparts/kparts_export.h
/usr/include/KF6/KParts/kparts/listingfilterextension.h
/usr/include/KF6/KParts/kparts/listingnotificationextension.h
/usr/include/KF6/KParts/kparts/mainwindow.h
/usr/include/KF6/KParts/kparts/navigationextension.h
/usr/include/KF6/KParts/kparts/openurlarguments.h
/usr/include/KF6/KParts/kparts/openurlevent.h
/usr/include/KF6/KParts/kparts/part.h
/usr/include/KF6/KParts/kparts/partactivateevent.h
/usr/include/KF6/KParts/kparts/partbase.h
/usr/include/KF6/KParts/kparts/partloader.h
/usr/include/KF6/KParts/kparts/partmanager.h
/usr/include/KF6/KParts/kparts/readonlypart.h
/usr/include/KF6/KParts/kparts/readwritepart.h
/usr/include/KF6/KParts/kparts/statusbarextension.h
/usr/include/KF6/KParts/kparts_version.h
/usr/lib64/cmake/KF6Parts/KF6PartsConfig.cmake
/usr/lib64/cmake/KF6Parts/KF6PartsConfigVersion.cmake
/usr/lib64/cmake/KF6Parts/KF6PartsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Parts/KF6PartsTargets.cmake
/usr/lib64/libKF6Parts.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Parts.so.6.11.0
/usr/lib64/libKF6Parts.so.6
/usr/lib64/libKF6Parts.so.6.11.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kparts/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kparts/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kparts/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kparts/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kparts/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kparts/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kparts6.lang
%defattr(-,root,root,-)

