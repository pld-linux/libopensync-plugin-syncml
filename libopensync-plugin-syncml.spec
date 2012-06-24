Summary:	OpenSync SyncML plugin
Summary(pl):	Wtyczka SyncML do OpenSync
Name:		libopensync-plugin-syncml
Version:	0.19
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.gz?format=raw
# Source0-md5:	925ee4cfa0a7e308065174f56e3c10d0
URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	libsyncml-devel >= 0.4.1
BuildRequires:	libxml2 >= 1:2.0
Obsoletes:	multisync-syncml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains SyncML plugin for OpenSync framework.

%description -l pl
OpenSync to niezale�ny od platformy i dystrybucji szkielet do
synchronizacji danych.

Sk�ada si� z r�nych wtyczek, kt�rych mo�na u�ywa� do ��czenia z
urz�dzeniami, pot�nego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczk� SyncML dla szkieletu OpenSync.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/plugins/*.la
%{_datadir}/opensync/defaults/*
