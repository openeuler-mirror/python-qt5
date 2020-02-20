%global python3_dbus_dir %(%{__python3} -c "import dbus.mainloop; print(dbus.mainloop.__path__[0])" 2>/dev/null || echo "%{python3_sitearch}/dbus/mainloop")
%global python2_dbus_dir %(%{__python2} -c "import dbus.mainloop; print(dbus.mainloop.__path__[0])" 2>/dev/null || echo "%{python2_sitearch}/dbus/mainloop")
%ifarch %{?qt5_qtwebengine_arches}%{?!qt5_qtwebengine_arches:%{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}
%global webengine 1
%endif
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global py3_sipdir %{_datadir}/sip/PyQt5
%undefine _strict_symbol_defs_build
%global py2_site_qt5 %{python2_sitearch}/PyQt5
%global py3_site_qt5 %{python3_sitearch}/PyQt5

Name:           python-qt5
Version:        5.11.2
Release:        6
Summary:        PyQt5 is a set of Python bindings for Qt5
License:        GPLv3
Url:            http://www.riverbankcomputing.com/software/pyqt/

%if 0%{?snap:1}
Source0:        http://www.riverbankcomputing.com/static/Downloads/PyQt5/PyQt5_gpl-%{version}%{?snap:.%{snap}}.tar.gz
%else
Source0:        http://downloads.sourceforge.net/project/pyqt/PyQt5/PyQt-%{version}/PyQt5_gpl-%{version}.tar.gz
%endif
Source1:        macros.pyqt5
Source2:        pylupdate5.sh
Source3:        pyrcc5.sh
Source4:        pyuic5.sh

Patch0:         PyQt5-Timeline.patch
Patch1:         PyQt5_gpl-5.11.2-sip_check.patch

BuildRequires:  chrpath findutils dbus-devel dbus-python-devel phonon-qt5-devel qt5-qttools-devel
BuildRequires:  qt5-qtbase-devel >= 5.5 qt5-qtenginio-devel qt5-qtconnectivity-devel  
BuildRequires:  qt5-qtlocation-devel qt5-qtmultimedia-devel qt5-qtdeclarative-devel python2-enum34
BuildRequires:  qt5-qtsensors-devel qt5-qtserialport-devel qt5-qtx11extras-devel python2-devel
BuildRequires:  qt5-qtxmlpatterns-devel qt5-qtwebchannel-devel qt5-qtwebsockets-devel 
BuildRequires:  pulseaudio-devel python2 dbus-python qt5-qtsvg-devel qt5-qtscript-devel
BuildRequires:  python2-sip-devel >= 4.19.12 python2-pyqt5-sip >= 4.19.12
BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion} 
BuildRequires:  python%{python3_pkgversion}-enum34 python%{python3_pkgversion}-pyqt5-sip >= 4.19.12
BuildRequires:  python%{python3_pkgversion}-dbus python%{python3_pkgversion}-sip-devel >= 4.19.12
Obsoletes: python-qt5 < 5.5.1-10

%description
PyQt is a set of Python v2 and v3 bindings for The Qt Company's Qt application framework and runs on 
all platforms supported by Qt including Windows, OS X, Linux, iOS and Android. PyQt5 supports Qt v5.

%global __provides_exclude_from ^(%{_qt5_plugindir}/.*\\.so)$

%package -n python2-qt5
Summary:        Python v2 bindings for Qt5
BuildRequires:  qt5-qtbase-private-devel
Requires:       python2-qt5-base%{?_isa} = %{version}-%{release} python2-enum34
Provides:       PyQt5 = %{version}-%{release} PyQt5%{?_isa} = %{version}-%{release}
Provides:       python2-PyQt5 = %{version}-%{release} python2-PyQt5%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python2-qt5}

%description -n python2-qt5
Python v2 bindings for Qt5.

%package -n python2-qt5-base
Summary:        Python v2 bindings for Qt5 base
Requires:       %{name}-rpm-macros = %{version}-%{release}
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
%{?_sip_api:Requires: python2-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
Requires:       dbus-python
Provides:       python2-PyQt5-base = %{version}-%{release} python2-PyQt5-base%{?_isa} = %{version}-%{release}
Obsoletes:      python-qt5 < 5.5.1-10
%{?python_provide:%python_provide python2-qt5-base}

%description -n python2-qt5-base
Python v2 bindings for Qt5 base.

%package -n python2-qt5-devel
Summary:        Development files for python-qt5
Requires:       python2-qt5%{?_isa} = %{version}-%{release}  python2-sip-devel
Provides:       PyQt5-devel = %{version}-%{release} python2-PyQt5-devel = %{version}-%{release}
%{?python_provide:%python_provide python2-qt5-devel}

%description -n python2-qt5-devel
Development files for python-qt5.

%package rpm-macros
Summary:        RPM macros in python-qt5
Conflicts:      python-qt5 < 5.6 python3-qt5 < 5.6
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
%package -n python2-qt5-webengine
Summary:        Python v2 bindings for Qt5 WebEngine
BuildRequires:  qt5-qtwebengine-devel
Requires:       python2-qt5%{?_isa} = %{version}-%{release}
Obsoletes:      python-qt5 < 5.5.1-10
%{?python_provide:%python_provide python2-qt5-webengine}

%description -n python2-qt5-webengine
Python v2 bindings for Qt5 WebEngine.

%package -n python%{python3_pkgversion}-qt5-webengine
Summary:        Python v3 bindings for Qt5 WebEngine
Requires:       python%{python3_pkgversion}-qt5%{?_isa} = %{version}-%{release}
Obsoletes:      python3-webengine < 5.5.1-13 python3-qt5 < 5.5.1-10
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-webengine}

%description -n python%{python3_pkgversion}-qt5-webengine
Python v3 bindings for Qt5 WebEngine.
%endif

%package -n python2-qt5-webkit
Summary:        Python v2 bindings for Qt5 Webkit
BuildRequires:  qt5-qtwebkit-devel qt5-qtwebkit-devel
Requires:       python2-qt5%{?_isa} = %{version}-%{release}
Obsoletes:      python3-webkit < 5.5.1-12 python-qt5 < 5.5.1-10
%{?python_provide:%python_provide python2-qt5-webkit}

%description -n python2-qt5-webkit
Python v2 bindings for Qt5 Webkit.

%package -n python%{python3_pkgversion}-qt5-webkit
Summary:        Python v3 bindings for Qt5 Webkit
Requires:       python%{python3_pkgversion}-qt5%{?_isa} = %{version}-%{release}
Obsoletes:      python3-qt5 < 5.5.1-10
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-webkit}

%description -n python%{python3_pkgversion}-qt5-webkit
Python v3 bindings for Qt5 Webkit.

%prep
%autosetup -n PyQt5_gpl-%{version}%{?snap:.%{snap}} -p1

%build
export PATH="%{_qt5_bindir}:$PATH"

mkdir %{_target_platform}
cp -a * %{_target_platform}/ ||:
pushd %{_target_platform}
%{__python2} ./configure.py \
  --assume-shared --confirm-license --no-dist-info --qmake=%{_qt5_qmake} --qsci-api \
  --qsci-api-destdir=%{_qt5_datadir}/qsci --verbose QMAKE_CFLAGS_RELEASE="%{optflags}" \
  QMAKE_CXXFLAGS_RELEASE="%{optflags}" QMAKE_LFLAGS_RELEASE="%{?__global_ldflags}"
%make_build
popd

mkdir %{_target_platform}-python3
cp -a * %{_target_platform}-python3/ ||:
pushd %{_target_platform}-python3
%{__python3} ./configure.py \
  --assume-shared --confirm-license --no-dist-info --qmake=%{_qt5_qmake} --no-qsci-api \
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
popd

%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}
pushd %{buildroot}
for i in .%{py2_site_qt5}/*.so .%{python2_dbus_dir}/pyqt5.so ; do
    test -x $i || chmod a+rx $i
done

rm -rfv .%{py2_site_qt5}/uic/port_v3/
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
  -e "s|@PYTHON2@|%{__python2}|g" \
  .%{_bindir}/{pyrcc5,pylupdate5,pyuic5}
popd

%files -n python2-qt5
%defattr(-,root,root)
%{_bindir}/pylupdate5
%{_bindir}/pyrcc5
%{_bindir}/pyuic5
%{_qt5_plugindir}/PyQt5/
%{_qt5_plugindir}/designer/libpyqt5.so
%{py2_site_qt5}/Enginio.so
%{py2_site_qt5}/QtBluetooth.so
%{py2_site_qt5}/QtDesigner.so
%{py2_site_qt5}/QtHelp.so
%{py2_site_qt5}/QtLocation.so
%{py2_site_qt5}/QtMultimedia.so
%{py2_site_qt5}/QtMultimediaWidgets.so
%{py2_site_qt5}/QtNfc.so
%{py2_site_qt5}/QtPositioning.so
%{py2_site_qt5}/QtQml.so
%{py2_site_qt5}/QtQuick.so
%{py2_site_qt5}/QtQuickWidgets.so
%{py2_site_qt5}/QtSensors.so
%{py2_site_qt5}/QtSerialPort.so
%{py2_site_qt5}/QtSvg.so
%{py2_site_qt5}/QtWebChannel.so
%{py2_site_qt5}/QtWebSockets.so
%{py2_site_qt5}/QtX11Extras.so
%{py2_site_qt5}/QtXmlPatterns.so
%{py2_site_qt5}/uic/
%{py2_site_qt5}/pylupdate.so
%{py2_site_qt5}/pylupdate_main.py*
%{py2_site_qt5}/pyrcc.so
%{py2_site_qt5}/pyrcc_main.py*

%files -n python2-qt5-base
%defattr(-,root,root)
%doc NEWS README
%license LICENSE
%{python2_dbus_dir}/pyqt5.so
%dir %{py2_site_qt5}/
%{py2_site_qt5}/__init__.py*
%{py2_site_qt5}/Qt.so
%{py2_site_qt5}/QtCore.so
%{py2_site_qt5}/QtDBus.so
%{py2_site_qt5}/QtGui.so
%{py2_site_qt5}/QtNetwork.so
%{py2_site_qt5}/QtOpenGL.so
%{py2_site_qt5}/QtPrintSupport.so
%{py2_site_qt5}/QtSql.so
%{py2_site_qt5}/QtTest.so
%{py2_site_qt5}/QtWidgets.so
%{py2_site_qt5}/QtXml.so
%{py2_site_qt5}/_QOpenGLFunctions_*.so

%if 0%{?webengine}
%files -n python2-qt5-webengine
%defattr(-,root,root)
%{py2_site_qt5}/QtWebEngine*
%endif

%files -n python2-qt5-webkit
%defattr(-,root,root)
%{py2_site_qt5}/QtWebKit*

%files rpm-macros
%defattr(-,root,root)
%{rpm_macros_dir}/macros.pyqt5

%files -n python2-qt5-devel
%defattr(-,root,root)
%{_datadir}/sip/PyQt5/

%files -n python%{python3_pkgversion}-qt5
%defattr(-,root,root)
%{_bindir}/pylupdate5
%{_bindir}/pyrcc5
%{_bindir}/pyuic5
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
%doc %{_qt5_datadir}/qsci/api/python/PyQt5.api
%dir %{_qt5_datadir}/qsci/
%dir %{_qt5_datadir}/qsci/api/
%dir %{_qt5_datadir}/qsci/api/python/

%changelog
* Wed Feb 12 2020 Jiangping Hu <hujp1985@foxmail.com> - 5.11.2-6
- Package init
