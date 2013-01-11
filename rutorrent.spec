Name:           rutorrent
Version:        3.5
Release:        1%{?dist}
Summary:        Yet another web front-end for rTorrent
Summary(ru):    Веб-интерфейс для rTorrent

License:        GPLv3
URL:            http://code.google.com/p/rutorrent/
Source0:        http://rutorrent.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        http://rutorrent.googlecode.com/files/plugins-%{version}.tar.gz
Source2:        rutorrent-set-config

BuildArch:      noarch

%description
ruTorrent is a web front-end for the popular Bittorrent client rTorrent

%package        lighttpd
Summary:        Lighttpd config for rutorrent
Requires:       lighttpd-fastcgi
Requires:       %{name}-common

%description    lighttpd
Lighttpd config for rutorrent

%package        common
Summary:        Main rutorrent files
Requires:       rtorrent
Requires:       php-cli

%description    common
Main rutorrent files

%package        plugins
Summary:        Plugins for rutorrent
Requires:       %{name}-common


%description    plugins
All plugins for rutorrent

%prep
%setup -q -n %{name}
tar -xf %{SOURCE1}

%build


%install
mkdir -p  $RPM_BUILD_ROOT%{_localstatedir}/%{name}/
cp -r %{_builddir}/%{name}/* \
      $RPM_BUILD_ROOT%{_localstatedir}/%{name}/
%{__install} -pD -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/rutorrent-set-config


%files lighttpd
%defattr(-,lighttpd,lighttpd,-)
%{_bindir}/rutorrent-set-config

%files common
%defattr(-,lighttpd,lighttpd,-)
%{_localstatedir}/%{name}
%exclude %{_localstatedir}/%{name}/plugins/

%files plugins
%defattr(-,lighttpd,lighttpd,-)
%{_localstatedir}/%{name}/plugins/


%changelog
* Fri Jan 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> 3.5-1.R
- Updated to 3.5

* Thu Oct 04 2012 Vasiliy N. Glazov <vascom2@gmail.com> 3.4-1.R
- Updated to 3.4

* Mon Aug 01 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.3-1.R
- Updated to 3.3

* Thu Jul  28 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2-4.R
- Split script to another package
- Set packages requires

* Wed Jul  27 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2-3.R
- Added config script

* Tue Jul  26 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2-2.R
- Split plugins
- Clean spec

* Mon Jul  25 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2-1.R
- initial build