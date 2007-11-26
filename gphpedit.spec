%define name	gphpedit
%define version	0.9.91
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	GNOME PHP/HTML/CSS development environment	
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://www.gphpedit.org/
License:	GPL
Group:		Editors
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libgnomeui2-devel libgnome-vfs2-devel libgtkhtml2-devel
BuildRequires:	ImageMagick

%description
GPHPEdit is a GNOME2 editor that is dedicated to editing PHP files and other
supporting files, like HTML/CSS. It has support for drop-down function lists,
hints showing parameters, and syntax highlighting.

%prep
%setup -q
perl -p -i -e 's|/usr/local/share|/usr/share||g' src/main.h

%build
%configure2_5x
perl -p -i -e 's|-Os|%optflags||g' `find -name makefile`
make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="GPHPEdit" longtitle="PHP Editor" section="More Applications/Editors"
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/%name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/%name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/%name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO README
%{_bindir}/%name
%{_datadir}/applications/*
%{_datadir}/%name
%{_datadir}/pixmaps/*
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

