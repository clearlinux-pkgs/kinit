#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kinit
Version  : 5.99.0
Release  : 59
URL      : https://download.kde.org/stable/frameworks/5.99/kinit-5.99.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.99/kinit-5.99.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.99/kinit-5.99.0.tar.xz.sig
Summary  : Process launcher to speed up launching KDE applications
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kinit-bin = %{version}-%{release}
Requires: kinit-data = %{version}-%{release}
Requires: kinit-lib = %{version}-%{release}
Requires: kinit-license = %{version}-%{release}
Requires: kinit-locales = %{version}-%{release}
Requires: kinit-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kservice-dev
BuildRequires : kwindowsystem-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libcap-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kinit-5.99.0
cd %{_builddir}/kinit-5.99.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665439146
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
export SOURCE_DATE_EPOCH=1665439146
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kinit
cp %{_builddir}/kinit-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kinit/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kinit-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kinit/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kinit-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kinit/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kinit-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kinit/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kinit-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kinit/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kinit-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kinit/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kinit-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kinit/e458941548e0864907e654fa2e192844ae90fc32 || :
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
/usr/share/qlogging-categories5/kinit.categories
/usr/share/qlogging-categories5/kinit.renamecategories

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
/usr/share/package-licenses/kinit/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kinit/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kinit/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kinit/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kinit/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kinit/e458941548e0864907e654fa2e192844ae90fc32

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man8/kdeinit5.8
/usr/share/man/ca@valencia/man8/kdeinit5.8
/usr/share/man/de/man8/kdeinit5.8
/usr/share/man/es/man8/kdeinit5.8
/usr/share/man/fr/man8/kdeinit5.8
/usr/share/man/it/man8/kdeinit5.8
/usr/share/man/man8/kdeinit5.8
/usr/share/man/nl/man8/kdeinit5.8
/usr/share/man/pt/man8/kdeinit5.8
/usr/share/man/pt_BR/man8/kdeinit5.8
/usr/share/man/sv/man8/kdeinit5.8
/usr/share/man/uk/man8/kdeinit5.8

%files locales -f kinit5.lang
%defattr(-,root,root,-)

