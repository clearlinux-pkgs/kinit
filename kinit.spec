#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kinit
Version  : 5.48.0
Release  : 1
URL      : https://download.kde.org/stable/frameworks/5.48/kinit-5.48.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.48/kinit-5.48.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.48/kinit-5.48.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: kinit-bin
Requires: kinit-data
Requires: kinit-license
Requires: kinit-locales
Requires: kinit-man
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kbookmarks-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kcrash-dev
BuildRequires : kdoctools
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kservice-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : kxmlgui-dev
BuildRequires : libcap-dev
BuildRequires : solid-dev

%description
# KInit
Helper library to speed up start of applications on KDE workspaces
## Introduction

%package bin
Summary: bin components for the kinit package.
Group: Binaries
Requires: kinit-data
Requires: kinit-license
Requires: kinit-man

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
Requires: kinit-bin
Requires: kinit-data
Provides: kinit-devel

%description dev
dev components for the kinit package.


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
%setup -q -n kinit-5.48.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532094570
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1532094570
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kinit
cp COPYING.LIB %{buildroot}/usr/share/doc/kinit/COPYING.LIB
cp COPYING.LGPL-2 %{buildroot}/usr/share/doc/kinit/COPYING.LGPL-2
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

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF5Init/KF5InitConfig.cmake
/usr/lib64/cmake/KF5Init/KF5InitConfigVersion.cmake
/usr/lib64/cmake/KF5Init/KF5InitMacros.cmake
/usr/lib64/cmake/KF5Init/kde5init_dummy.cpp.in
/usr/lib64/libkdeinit5_klauncher.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/kinit/COPYING.LGPL-2
/usr/share/doc/kinit/COPYING.LIB

%files man
%defattr(-,root,root,-)
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

