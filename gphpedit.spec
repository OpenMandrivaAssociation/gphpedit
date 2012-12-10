%define name	gphpedit
%define version	0.9.98
%define release %mkrel -c RC1 2

Name: 	 	%{name}
Summary: 	GNOME PHP/HTML/CSS development environment	
Version: 	%{version}
Release: 	%{release}
Source0:		http://www.gphpedit.org/sites/default/files/%{name}-%{version}RC1.tar.gz
Patch0:		gphpedit-0.9.91-fix-crash.patch
Patch1:		gphpedit-0.9.91-fix-desktop-entry.patch
Patch2:		gphpedit-0.9.91-fix-str-fmt.patch
URL:		http://www.gphpedit.org/
License:	GPLv2+
Group:		Editors
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(webkit-1.0)
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
export LIBS=" -lgmodule-2.0"
autoreconf -fi
%configure2_5x
perl -p -i -e 's|-Os|%optflags||g' `find -name makefile`
make
										
%install
%makeinstall_std

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS TODO README
%{_bindir}/%name
%{_datadir}/applications/*
%{_datadir}/%name
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/apps/*


%changelog
* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 0.9.98-0.RC1.2mdv2011.0
+ Revision: 686165
- rebuild for new webkit

* Thu Sep 23 2010 Funda Wang <fwang@mandriva.org> 0.9.98-0.RC1.1mdv2011.0
+ Revision: 580780
- update BRs
- New version 0.9.98 RC1

* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 0.9.91-5mdv2010.1
+ Revision: 507388
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9.91-4mdv2009.0
+ Revision: 246539
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Dec 09 2007 Funda Wang <fwang@mandriva.org> 0.9.91-2mdv2008.1
+ Revision: 116748
- add patch from debian to avoid crash
- fix desktop entry

  + Thierry Vignaud <tv@mandriva.org>
    - import gphpedit


* Thu Jul  6 2006 Austin Acton <austin@mandriva.org> 0.9.91-1mdv2007.0
- 0.9.91
- mkrel
- fix opt flags

* Fri Mar 31 2006 Austin Acton <austin@mandriva.org> 0.9.80-3mdk
- Rebuild

* Sat Nov 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.80-2mdk
- Fix BuildRequires

* Fri Nov 4 2005 Austin Acton <austin@mandriva.org> 0.9.80-1mdk
- 0.9.80

* Tue Apr 26 2005 Austin Acton <austin@mandriva.org> 0.9.50-1mdk
- initial package
