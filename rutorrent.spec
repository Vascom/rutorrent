Name:           rutorrent
Version:        3.2
Release:        3%{?dist}.R
Summary:        Yet another web front-end for rTorrent

License:        GPLv3
URL:            http://code.google.com/p/rutorrent/
Source0:        http://rutorrent.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        http://rutorrent.googlecode.com/files/plugins-%{version}.tar.gz
Source2:        rutorrent-set-config
  
Requires:       lighttpd-fastcgi
Requires:       rtorrent
Requires:       php-cli

BuildArch:      noarch

%description
ruTorrent is a web front-end for the popular Bittorrent client rTorrent

%package        plugins
Summary:        Plugins for rutorrent
Requires:       %{name}

%description    plugins
All plugins for rutorrent

%prep
%setup -q -n %{name}
tar -xf %{SOURCE1}

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p  $RPM_BUILD_ROOT%{_localstatedir}/www/lighttpd/%{name}/
cp -r %{_builddir}/%{name}/* \
      $RPM_BUILD_ROOT%{_localstatedir}/www/lighttpd/%{name}/
%{__install} -pD -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/rutorrent-set-config

%files
%defattr(-,lighttpd,lighttpd,-)
%{_localstatedir}/www/lighttpd/%{name}/conf/*
%{_localstatedir}/www/lighttpd/%{name}/css/*
%{_localstatedir}/www/lighttpd/%{name}/images/*
%{_localstatedir}/www/lighttpd/%{name}/js/*
%{_localstatedir}/www/lighttpd/%{name}/lang/*
%{_localstatedir}/www/lighttpd/%{name}/php/*
%{_localstatedir}/www/lighttpd/%{name}/share/*
%{_localstatedir}/www/lighttpd/%{name}/index.html
%{_localstatedir}/www/lighttpd/%{name}/favicon.ico
%{_localstatedir}/www/lighttpd/%{name}/conf/.htaccess
%{_localstatedir}/www/lighttpd/%{name}/share/.htaccess
%{_bindir}/rutorrent-set-config

%files plugins
%defattr(-,lighttpd,lighttpd,-)
%{_localstatedir}/www/lighttpd/%{name}/plugins/*


%changelog
* Wed Jul  27 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2-3.R
- Added config script

* Tue Jul  26 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2-2.R
- Split plugins
- Clean spec

* Mon Jul  25 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2-1.R
- initial build