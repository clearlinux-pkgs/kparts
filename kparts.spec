#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kparts
Version  : 5.64.0
Release  : 21
URL      : https://download.kde.org/stable/frameworks/5.64/kparts-5.64.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.64/kparts-5.64.0.tar.xz
Source1 : https://download.kde.org/stable/frameworks/5.64/kparts-5.64.0.tar.xz.sig
Summary  : Document centric plugin system
Group    : Development/Tools
License  : LGPL-2.1
Requires: kparts-data = %{version}-%{release}
Requires: kparts-lib = %{version}-%{release}
Requires: kparts-license = %{version}-%{release}
Requires: kparts-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kparts-5.64.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573423840
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
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573423840
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kparts
cp %{_builddir}/kparts-5.64.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kparts/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang kparts5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kdevappwizard/templates/kpartsapp.tar.bz2
/usr/share/kservicetypes5/browserview.desktop
/usr/share/kservicetypes5/kpart.desktop
/usr/share/kservicetypes5/krop.desktop
/usr/share/kservicetypes5/krwp.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KParts/KParts/BrowserArguments
/usr/include/KF5/KParts/KParts/BrowserExtension
/usr/include/KF5/KParts/KParts/BrowserHostExtension
/usr/include/KF5/KParts/KParts/BrowserInterface
/usr/include/KF5/KParts/KParts/BrowserOpenOrSaveQuestion
/usr/include/KF5/KParts/KParts/BrowserRun
/usr/include/KF5/KParts/KParts/Event
/usr/include/KF5/KParts/KParts/FileInfoExtension
/usr/include/KF5/KParts/KParts/GUIActivateEvent
/usr/include/KF5/KParts/KParts/HistoryProvider
/usr/include/KF5/KParts/KParts/HtmlExtension
/usr/include/KF5/KParts/KParts/HtmlSettingsInterface
/usr/include/KF5/KParts/KParts/ListingFilterExtension
/usr/include/KF5/KParts/KParts/ListingNotificationExtension
/usr/include/KF5/KParts/KParts/LiveConnectExtension
/usr/include/KF5/KParts/KParts/MainWindow
/usr/include/KF5/KParts/KParts/OpenUrlArguments
/usr/include/KF5/KParts/KParts/OpenUrlEvent
/usr/include/KF5/KParts/KParts/Part
/usr/include/KF5/KParts/KParts/PartActivateEvent
/usr/include/KF5/KParts/KParts/PartBase
/usr/include/KF5/KParts/KParts/PartManager
/usr/include/KF5/KParts/KParts/PartSelectEvent
/usr/include/KF5/KParts/KParts/Plugin
/usr/include/KF5/KParts/KParts/ReadOnlyPart
/usr/include/KF5/KParts/KParts/ReadWritePart
/usr/include/KF5/KParts/KParts/ScriptableExtension
/usr/include/KF5/KParts/KParts/SelectorInterface
/usr/include/KF5/KParts/KParts/StatusBarExtension
/usr/include/KF5/KParts/KParts/TextExtension
/usr/include/KF5/KParts/KParts/WindowArgs
/usr/include/KF5/KParts/kde_terminal_interface.h
/usr/include/KF5/KParts/kparts/browserarguments.h
/usr/include/KF5/KParts/kparts/browserextension.h
/usr/include/KF5/KParts/kparts/browserhostextension.h
/usr/include/KF5/KParts/kparts/browserinterface.h
/usr/include/KF5/KParts/kparts/browseropenorsavequestion.h
/usr/include/KF5/KParts/kparts/browserrun.h
/usr/include/KF5/KParts/kparts/event.h
/usr/include/KF5/KParts/kparts/fileinfoextension.h
/usr/include/KF5/KParts/kparts/guiactivateevent.h
/usr/include/KF5/KParts/kparts/historyprovider.h
/usr/include/KF5/KParts/kparts/htmlextension.h
/usr/include/KF5/KParts/kparts/htmlsettingsinterface.h
/usr/include/KF5/KParts/kparts/kparts_export.h
/usr/include/KF5/KParts/kparts/listingfilterextension.h
/usr/include/KF5/KParts/kparts/listingnotificationextension.h
/usr/include/KF5/KParts/kparts/liveconnectextension.h
/usr/include/KF5/KParts/kparts/mainwindow.h
/usr/include/KF5/KParts/kparts/openurlarguments.h
/usr/include/KF5/KParts/kparts/openurlevent.h
/usr/include/KF5/KParts/kparts/part.h
/usr/include/KF5/KParts/kparts/partactivateevent.h
/usr/include/KF5/KParts/kparts/partbase.h
/usr/include/KF5/KParts/kparts/partmanager.h
/usr/include/KF5/KParts/kparts/partselectevent.h
/usr/include/KF5/KParts/kparts/plugin.h
/usr/include/KF5/KParts/kparts/readonlypart.h
/usr/include/KF5/KParts/kparts/readwritepart.h
/usr/include/KF5/KParts/kparts/scriptableextension.h
/usr/include/KF5/KParts/kparts/selectorinterface.h
/usr/include/KF5/KParts/kparts/statusbarextension.h
/usr/include/KF5/KParts/kparts/textextension.h
/usr/include/KF5/KParts/kparts/windowargs.h
/usr/include/KF5/kparts_version.h
/usr/lib64/cmake/KF5Parts/KF5PartsConfig.cmake
/usr/lib64/cmake/KF5Parts/KF5PartsConfigVersion.cmake
/usr/lib64/cmake/KF5Parts/KF5PartsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Parts/KF5PartsTargets.cmake
/usr/lib64/libKF5Parts.so
/usr/lib64/qt5/mkspecs/modules/qt_KParts.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Parts.so.5
/usr/lib64/libKF5Parts.so.5.64.0
/usr/lib64/qt5/plugins/notepadpart.so
/usr/lib64/qt5/plugins/spellcheckplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kparts/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f kparts5.lang
%defattr(-,root,root,-)

