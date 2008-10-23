Summary:	OpenSync SyncML plugin
Summary(pl.UTF-8):	Wtyczka SyncML do OpenSync
Name:		libopensync-plugin-syncml
Version:	0.37
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opensync.org/download/releases/0.37/%{name}-%{version}
# Source0-md5:	4a7690b7d34ee1a1937fab9e746483aa
URL:		http://www.opensync.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cmake
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	libopensync-devel >= 1:%{version}
BuildRequires:	libsoup-devel >= 2.2.91
BuildRequires:	libsyncml-devel >= 0.4.4
BuildRequires:	libxml2-devel >= 1:2.0
BuildRequires:	openobex-devel >= 1.1
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.385
BuildRequires:	pkgconfig
Obsoletes:	multisync-syncml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains SyncML plugin for OpenSync framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkę SyncML dla szkieletu OpenSync.

%prep
%setup -q

%build
mkdir build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libopensync1/plugins/syncml-plugin.so
%{_datadir}/libopensync1/defaults/syncml-obex-client

# devel
#%{_includedir}/opensync-1.0/opensync/syncml_plugin.h
