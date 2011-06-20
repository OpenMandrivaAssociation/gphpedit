%define name	gphpedit
%define version	0.9.98
%define release %mkrel -c RC1 2

Name: 	 	%{name}
Summary: 	GNOME PHP/HTML/CSS development environment	
Version: 	%{version}
Release: 	%{release}
Source:		http://www.gphpedit.org/sites/default/files/%{name}-%{version}RC1.tar.gz
Patch0:		gphpedit-0.9.91-fix-crash.patch
Patch1:		gphpedit-0.9.91-fix-desktop-entry.patch
Patch2:		gphpedit-0.9.91-fix-str-fmt.patch
URL:		http://www.gphpedit.org/
License:	GPLv2+
Group:		Editors
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	libGConf2-devel
BuildRequires:	webkitgtk-devel
BuildRequires:	intltool

%description
GPHPEdit is a GNOME2 editor that is dedicated to editing PHP files and other
supporting files, like HTML/CSS. It has support for drop-down function lists,
hints showing parameters, and syntax highlighting.

%prep
%setup -qn anoopjohn-gphpedit-fe8a12c
%if 0
%patch0 -p1
%patch1 -p0
%patch2 -p0
%endif

%build
autoreconf -fi
%configure2_5x
perl -p -i -e 's|-Os|%optflags||g' `find -name makefile`
make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO README
%{_bindir}/%name
%{_datadir}/applications/*
%{_datadir}/%name
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/apps/*
