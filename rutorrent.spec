Name:           rutorrent
Version:        3.2
Release:        1%{?dist}.R
Summary:        Yet another web front-end for rTorrent

License:        GPLv3
URL:            http://code.google.com/p/rutorrent/
Source0:        http://rutorrent.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        http://rutorrent.googlecode.com/files/plugins-%{version}.tar.gz
  
Requires:       lighttpd-fastcgi
Requires:       rtorrent

BuildArch:      noarch

%description
ruTorrent is a front-end for the popular Bittorrent client rTorrent

%description    plugins
Plugins for rutorrent

%prep
%setup -q -n rutorrent
tar -xf %{SOURCE1}

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p  $RPM_BUILD_ROOT%{_localstatedir}/www/lighttpd/rutorrent/
cp -r %{_builddir}/%{name}/* \
      $RPM_BUILD_ROOT%{_localstatedir}/www/lighttpd/rutorrent/

%files
%defattr(-,lighttpd,lighttpd,-)
%{_localstatedir}/www/lighttpd/rutorrent/conf/*
%{_localstatedir}/www/lighttpd/rutorrent/css/*
%{_localstatedir}/www/lighttpd/rutorrent/images/*
%{_localstatedir}/www/lighttpd/rutorrent/js/*
%{_localstatedir}/www/lighttpd/rutorrent/lang/*
%{_localstatedir}/www/lighttpd/rutorrent/php/*
%{_localstatedir}/www/lighttpd/rutorrent/share/*
%{_localstatedir}/www/lighttpd/rutorrent/index.html
%{_localstatedir}/www/lighttpd/rutorrent/favicon.ico

%files plugins
%{_localstatedir}/www/lighttpd/rutorrent/plugins/*


%changelog
* Mon Jul  25 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2-1.R
- initial build