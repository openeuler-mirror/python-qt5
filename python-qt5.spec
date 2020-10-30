%global python3_dbus_dir %(%{__python3} -c "import dbus.mainloop; print(dbus.mainloop.__path__[0])" 2>/dev/null || echo "%{python3_sitearch}/dbus/mainloop")
%ifarch %{?qt5_qtwebengine_arches}%{?!qt5_qtwebengine_arches:%{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}
%global webengine 1
%endif
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global py3_sipdir %{_datadir}/sip/PyQt5
%undefine _strict_symbol_defs_build
%global py3_site_qt5 %{python3_sitearch}/PyQt5

Name:           python-qt5
Version:        5.11.2
Release:        8
Summary:        PyQt5 is a set of Python bindings for Qt5
License:        GPLv3
Url:            http://www.riverbankcomputing.com/software/pyqt/

%if 0%{?snap:1}
Source0:        http://www.riverbankcomputing.com/static/Downloads/PyQt5/PyQt5_gpl-%{version}%{?snap:.%{snap}}.tar.gz
%else
Source0:        https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-%{version}/PyQt5_gpl-%{version}.tar.gz/download?use_mirror=netactuate#/PyQt5_gpl-%{version}.tar.gz
%endif
Source1:        macros.pyqt5
Source2:        pylupdate5.sh
Source3:        pyrcc5.sh
Source4:        pyuic5.sh

Patch0:         PyQt5-Timeline.patch
Patch1:         PyQt5_gpl-5.11.2-sip_check.patch

BuildRequires:  chrpath findutils dbus-devel dbus-python-devel phonon-qt5-devel qt5-qttools-devel
BuildRequires:  qt5-qtbase-devel >= 5.5 qt5-qtenginio-devel qt5-qtconnectivity-devel  
BuildRequires:  qt5-qtlocation-devel qt5-qtmultimedia-devel qt5-qtdeclarative-devel
BuildRequires:  qt5-qtsensors-devel qt5-qtserialport-devel qt5-qtx11extras-devel
BuildRequires:  qt5-qtxmlpatterns-devel qt5-qtwebchannel-devel qt5-qtwebsockets-devel 
BuildRequires:  pulseaudio-devel dbus-python qt5-qtsvg-devel qt5-qtscript-devel
BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion} 
BuildRequires:  python%{python3_pkgversion}-enum34 python%{python3_pkgversion}-pyqt5-sip >= 4.19.12
BuildRequires:  python%{python3_pkgversion}-dbus python%{python3_pkgversion}-sip-devel >= 4.19.12
Obsoletes: python-qt5 < 5.5.1-10

%description
PyQt is a set of Python v2 and v3 bindings for The Qt Company's Qt application framework and runs on 
all platforms supported by Qt including Windows, OS X, Linux, iOS and Android. PyQt5 supports Qt v5.

%global __provides_exclude_from ^(%{_qt5_plugindir}/.*\\.so)$


%package rpm-macros
Summary:        RPM macros in python-qt5
Conflicts:      python3-qt5 < 5.6
BuildArch:      noarch
%description rpm-macros
RPM macros in python-qt5.

%package -n python%{python3_pkgversion}-qt5
Summary:        Python v3 bindings for Qt5
Requires:       python%{python3_pkgversion}-qt5-base%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5}
Provides:       python%{python3_pkgversion}-PyQt5 = %{version}-%{release}
Provides:       python%{python3_pkgversion}-PyQt5%{?_isa} = %{version}-%{release}
Obsoletes:      python3-qt5 < 5.5.1-10

%description -n python%{python3_pkgversion}-qt5
Python v3 bindings for Qt5.

%package -n python%{python3_pkgversion}-qt5-base
Summary:        Python v3 bindings for Qt5 base
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
%{?_sip_api:Requires: python%{python3_pkgversion}-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
Provides:       python%{python3_pkgversion}-PyQt5-base = %{version}-%{release}
Provides:       python%{python3_pkgversion}-PyQt5-base%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-base}
Requires:       %{name}-rpm-macros = %{version}-%{release} python%{python3_pkgversion}-dbus

%description -n python%{python3_pkgversion}-qt5-base
Python v3 bindings for Qt5 base.

%package -n python%{python3_pkgversion}-qt5-devel
Summary:        Development files for python3-qt5
Requires:       python%{python3_pkgversion}-qt5%{?_isa} = %{version}-%{release} 
Requires:       python%{python3_pkgversion}-sip-devel
Provides:       python%{python3_pkgversion}-PyQt5-devel = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-devel}

%description -n python%{python3_pkgversion}-qt5-devel
Development files for python3-qt5.

%package help
Summary:        Documentation for python-qt5
Provides:       PyQt5-doc = %{version}-%{release} %{name}-doc = %{version}-%{release}
Obsoletes:      %{name}-doc < %{version}-%{release}
BuildArch:      noarch

%description help
Documentation for python-qt5.

%if 0%{?webengine}
%package -n python%{python3_pkgversion}-qt5-webengine
Summary:        Python v3 bindings for Qt5 WebEngine
BuildRequires:  qt5-qtwebengine-devel
Requires:       python%{python3_pkgversion}-qt5%{?_isa} = %{version}-%{release}
Obsoletes:      python3-webengine < 5.5.1-13 python3-qt5 < 5.5.1-10
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-webengine}

%description -n python%{python3_pkgversion}-qt5-webengine
Python v3 bindings for Qt5 WebEngine.
%endif

%package -n python%{python3_pkgversion}-qt5-webkit
Summary:        Python v3 bindings for Qt5 Webkit
BuildRequires:  qt5-qtwebkit-devel qt5-qtwebkit-devel
Requires:       python%{python3_pkgversion}-qt5%{?_isa} = %{version}-%{release}
Obsoletes:      python3-qt5 < 5.5.1-10
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-webkit}

%description -n python%{python3_pkgversion}-qt5-webkit
Python v3 bindings for Qt5 Webkit.

%prep
%autosetup -n PyQt5_gpl-%{version}%{?snap:.%{snap}} -p1

%build
export PATH="%{_qt5_bindir}:$PATH"

mkdir %{_target_platform}-python3
cp -a * %{_target_platform}-python3/ ||:
pushd %{_target_platform}-python3
%{__python3} ./configure.py \
  --assume-shared --confirm-license --no-dist-info --qmake=%{_qt5_qmake} \
  --qsci-api --qsci-api-destdir=%{_qt5_datadir}/qsci \
  %{?py3_sipdir:--sipdir=%{py3_sipdir}} --verbose QMAKE_CFLAGS_RELEASE="%{optflags}" \
  QMAKE_CXXFLAGS_RELEASE="%{optflags}" QMAKE_LFLAGS_RELEASE="%{?__global_ldflags}"
%make_build
popd

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}-python3
pushd %{buildroot}
%if "%py3_sipdir" == "%{_datadir}/sip/PyQt5"
mkdir -p .%{_datadir}/python3-sip
cp -alf .%{py3_sipdir} .%{_datadir}/python3-sip/PyQt5
%endif
for i in .%{py3_site_qt5}/*.so .%{python3_dbus_dir}/pyqt5.so ; do
    test -x $i  || chmod a+rx $i
done

rm -rfv .%{py3_site_qt5}/uic/port_v2/

install -p -m644 -D %{SOURCE1} .%{rpm_macros_dir}/macros.pyqt5
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  .%{rpm_macros_dir}/macros.pyqt5

rm -fv .%{_bindir}/{pyrcc5,pylupdate5,pyuic5}
install -p -m755 -D %{SOURCE2} .%{_bindir}/pylupdate5
install -p -m755 -D %{SOURCE3} .%{_bindir}/pyrcc5
install -p -m755 -D %{SOURCE4} .%{_bindir}/pyuic5
sed -i \
  -e "s|@PYTHON3@|%{__python3}|g" \
  .%{_bindir}/{pyrcc5,pylupdate5,pyuic5}
popd

%files rpm-macros
%defattr(-,root,root)
%{rpm_macros_dir}/macros.pyqt5

%files -n python%{python3_pkgversion}-qt5
%defattr(-,root,root)
%{_bindir}/pylupdate5
%{_bindir}/pyrcc5
%{_bindir}/pyuic5
%{_qt5_plugindir}/PyQt5
%{_qt5_plugindir}/designer/libpyqt5.so
%{py3_site_qt5}/Enginio.*
%{py3_site_qt5}/QtBluetooth.*
%{py3_site_qt5}/QtDesigner.*
%{py3_site_qt5}/QtHelp.*
%{py3_site_qt5}/QtLocation.*
%{py3_site_qt5}/QtMultimedia.*
%{py3_site_qt5}/QtMultimediaWidgets.*
%{py3_site_qt5}/QtNfc.*
%{py3_site_qt5}/QtPositioning.*
%{py3_site_qt5}/QtQml.*
%{py3_site_qt5}/QtQuick.*
%{py3_site_qt5}/QtQuickWidgets.*
%{py3_site_qt5}/QtSensors.*
%{py3_site_qt5}/QtSerialPort.*
%{py3_site_qt5}/QtSvg.*
%{py3_site_qt5}/QtWebChannel.*
%{py3_site_qt5}/QtWebSockets.*
%{py3_site_qt5}/QtX11Extras.*
%{py3_site_qt5}/QtXmlPatterns.*
%{py3_site_qt5}/uic/
%{py3_site_qt5}/pylupdate.so
%{py3_site_qt5}/pylupdate_main.py*
%{py3_site_qt5}/pyrcc.so
%{py3_site_qt5}/pyrcc_main.py*

%files -n python%{python3_pkgversion}-qt5-base
%defattr(-,root,root)
%doc NEWS README
%license LICENSE
%{python3_dbus_dir}/pyqt5.so
%dir %{py3_site_qt5}/
%{py3_site_qt5}/__pycache__/
%{py3_site_qt5}/__init__.py*
%{py3_site_qt5}/Qt.*
%{py3_site_qt5}/QtCore.*
%{py3_site_qt5}/QtDBus.*
%{py3_site_qt5}/QtGui.*
%{py3_site_qt5}/QtNetwork.*
%{py3_site_qt5}/QtOpenGL.*
%{py3_site_qt5}/QtPrintSupport.*
%{py3_site_qt5}/QtSql.*
%{py3_site_qt5}/QtTest.*
%{py3_site_qt5}/QtWidgets.*
%{py3_site_qt5}/QtXml.*
%{py3_site_qt5}/_QOpenGLFunctions_*

%if 0%{?webengine}
%files -n python%{python3_pkgversion}-qt5-webengine
%defattr(-,root,root)
%{py3_site_qt5}/QtWebEngine*
%endif

%files -n python%{python3_pkgversion}-qt5-webkit
%defattr(-,root,root)
%{py3_site_qt5}/QtWebKit*

%files -n python%{python3_pkgversion}-qt5-devel
%defattr(-,root,root)
%{py3_sipdir}/
%dir %{_datadir}/python3-sip/
%{_datadir}/python3-sip/PyQt5/

%files help
%defattr(-,root,root)
%doc examples/
%dir %{_qt5_datadir}/qsci/
%dir %{_qt5_datadir}/qsci/api/
%dir %{_qt5_datadir}/qsci/api/python/
%doc %{_qt5_datadir}/qsci/api/python/PyQt5.api

%changelog
* Tue Oct 27 2020 wangxiao <wangxiao65@huawei.com> - 5.11.2-8
- drop python2 packages

* Tue Sep 15 2020 Ge Wang <wangge20@huawei.com> - 5.11.2-7
- Modify Source0 Url

* Wed Feb 12 2020 Jiangping Hu <hujp1985@foxmail.com> - 5.11.2-6
- Package init
