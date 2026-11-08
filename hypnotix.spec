Name:		hypnotix
Version:	5.7
Release:	2
Summary:	IPTV Player
License:        GPL-3+
URL:            https://github.com/linuxmint/hypnotix
Source0:	https://github.com/linuxmint/hypnotix/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Group:		Graphical desktop/Other

BuildRequires:  make
BuildRequires:  gettext
BuildRequires:	python

Requires:       typelib(XApp)
Requires:       python
Requires:       python-gi
Requires:	python-requests
Requires:       python-setproctitle
Requires:	python-unidecode
Requires:	xapp	
Requires:	lib64mpv       
#Requires:       lib64mpv1
Requires:	python-gi-cairo
#circle-flags maybe later
Requires:	yt-dlp


%description
IPTV Player

%prep
%autosetup -p1

%build
%make_build

%install
cp -a usr %{buildroot}/
install -d %{buildroot}/usr/lib64
mv %{buildroot}/usr/lib/hypnotix %{buildroot}/usr/lib64/hypnotix
find %{buildroot}/usr/bin %{buildroot}/usr/lib64 %{buildroot}/usr/share -type f -exec sed -i 's|/usr/lib/hypnotix|/usr/lib64/hypnotix|g' {} +
find %{buildroot} -type f -exec sed -i -e "s/__DEB_VERSION__/%{version}/g" {} +

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%{_datadir}/applications/hypnotix.desktop
%{_datadir}/glib-2.0/schemas/org.x.hypnotix.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/hypnotix.svg
%{_datadir}/hypnotix/*
/usr/lib64/hypnotix/*
%{_bindir}/hypnotix
