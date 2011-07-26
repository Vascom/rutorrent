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

%prep
%setup -q -n %{name}
tar -xf %{SOURCE1}

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p  $RPM_BUILD_ROOT%{_localstatedir}/www/lighttpd/%{name}/
cp -r %{_builddir}/%{name}/* \
      $RPM_BUILD_ROOT%{_localstatedir}/www/lighttpd/%{name}/

%files
%defattr(-,lighttpd,lighttpd,-)
%{_localstatedir}/www/lighttpd/%{name}/*
%doc



%changelog
* Mon Jul  25 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2-1.R
- initial build