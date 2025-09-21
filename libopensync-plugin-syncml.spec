Summary:	OpenSync SyncML plugin
Summary(pl.UTF-8):	Wtyczka SyncML do OpenSync
Name:		libopensync-plugin-syncml
Version:	0.39
Release:	2
License:	LGPL v2.1+
Group:		Libraries
# originally http://opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	02922ebeec8b9eab77b1cffbb19c81be
# dead domain
#URL:		http://www.opensync.org/
BuildRequires:	cmake
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	libopensync-devel >= 1:%{version}
BuildRequires:	libsoup-devel >= 2.2.91
BuildRequires:	libsyncml-devel >= 0.5.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	libsyncml >= 0.5.0
Obsoletes:	multisync-syncml < 0.90
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
install -d build
cd build
%cmake ..

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
%{_datadir}/libopensync1/defaults/syncml-http-client
%{_datadir}/libopensync1/defaults/syncml-http-server
%{_datadir}/libopensync1/defaults/syncml-obex-client
