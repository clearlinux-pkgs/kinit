#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kinit
Version  : 5.58.0
Release  : 20
URL      : https://download.kde.org/stable/frameworks/5.58/kinit-5.58.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.58/kinit-5.58.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.58/kinit-5.58.0.tar.xz.sig
Summary  : Process launcher to speed up launching KDE applications
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: kinit-bin = %{version}-%{release}
Requires: kinit-data = %{version}-%{release}
Requires: kinit-lib = %{version}-%{release}
Requires: kinit-license = %{version}-%{release}
Requires: kinit-locales = %{version}-%{release}
Requires: kinit-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : kcompletion-dev
BuildRequires : kcrash-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kservice-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libcap-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : solid-dev

%description
# KInit
Helper library to speed up start of applications on KDE workspaces
## Introduction

%package bin
Summary: bin components for the kinit package.
Group: Binaries
Requires: kinit-data = %{version}-%{release}
Requires: kinit-license = %{version}-%{release}

%description bin
bin components for the kinit package.


%package data
Summary: data components for the kinit package.
Group: Data

%description data
data components for the kinit package.


%package dev
Summary: dev components for the kinit package.
Group: Development
Requires: kinit-lib = %{version}-%{release}
Requires: kinit-bin = %{version}-%{release}
Requires: kinit-data = %{version}-%{release}
Provides: kinit-devel = %{version}-%{release}
Requires: kinit = %{version}-%{release}
Requires: kinit = %{version}-%{release}

%description dev
dev components for the kinit package.


%package lib
Summary: lib components for the kinit package.
Group: Libraries
Requires: kinit-data = %{version}-%{release}
Requires: kinit-license = %{version}-%{release}

%description lib
lib components for the kinit package.


%package license
Summary: license components for the kinit package.
Group: Default

%description license
license components for the kinit package.


%package locales
Summary: locales components for the kinit package.
Group: Default

%description locales
locales components for the kinit package.


%package man
Summary: man components for the kinit package.
Group: Default

%description man
man components for the kinit package.


%prep
%setup -q -n kinit-5.58.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557793585
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557793585
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kinit
cp COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/kinit/COPYING.LGPL-2
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kinit/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kinit5

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/klauncher
/usr/lib64/libexec/kf5/start_kdeinit
/usr/lib64/libexec/kf5/start_kdeinit_wrapper

%files bin
%defattr(-,root,root,-)
/usr/bin/kdeinit5
/usr/bin/kdeinit5_shutdown
/usr/bin/kdeinit5_wrapper
/usr/bin/kshell5
/usr/bin/kwrapper5

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.kde.KLauncher.xml
/usr/share/xdg/kinit.categories

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF5Init/KF5InitConfig.cmake
/usr/lib64/cmake/KF5Init/KF5InitConfigVersion.cmake
/usr/lib64/cmake/KF5Init/KF5InitMacros.cmake
/usr/lib64/cmake/KF5Init/kde5init_dummy.cpp.in

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdeinit5_klauncher.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kinit/COPYING.LGPL-2
/usr/share/package-licenses/kinit/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man8/kdeinit5.8
/usr/share/man/de/man8/kdeinit5.8
/usr/share/man/es/man8/kdeinit5.8
/usr/share/man/it/man8/kdeinit5.8
/usr/share/man/man8/kdeinit5.8
/usr/share/man/nl/man8/kdeinit5.8
/usr/share/man/pt/man8/kdeinit5.8
/usr/share/man/pt_BR/man8/kdeinit5.8
/usr/share/man/sv/man8/kdeinit5.8
/usr/share/man/uk/man8/kdeinit5.8

%files locales -f kinit5.lang
%defattr(-,root,root,-)

