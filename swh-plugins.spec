Summary: A set of audio plugins for LADSPA
Name: swh-plugins
Version: 0.4.15
Release: 7
License: GPL
Group: Sound
Source: http://plugin.org.uk/releases/%version/%name-%version.tar.bz2
Patch: swh-plugins-0.4.15-build.patch
BuildRoot: %_tmppath/%{name}-buildroot
BuildRequires: ladspa-devel fftw-devel
URL: http://plugin.org.uk/
%description
A set of audio plugins for LADSPA (see http://plugin.org.uk/ for more
details).

%prep
%setup -q
%patch -p1 -b .build

%build
%configure2_5x
%make CFLAGS="%optflags -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib %buildroot%_libdir
%endif
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%_libdir/ladspa/*.so
%dir %_datadir/ladspa/
%dir %_datadir/ladspa/rdf/
%_datadir/ladspa/rdf/*.rdf




%changelog
* Mon Sep 03 2012 Frank Kober <emuse@mandriva.org> 0.4.15-6mdv2012.0
+ Revision: 816238
- rebuild to resolve dependencies

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - rediff the patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.4.15-4mdv2009.0
+ Revision: 261304
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.4.15-3mdv2009.0
+ Revision: 253855
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.4.15-1mdv2008.1
+ Revision: 140904
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.15-1mdv2007.0
+ Revision: 92190
- Import swh-plugins

* Fri Dec 08 2006 Götz Waschk <waschk@mandriva.org> 0.4.15-1mdv2007.1
- New version 0.4.15

* Fri Sep 23 2005 Götz Waschk <waschk@mandriva.org> 0.4.14-1mdk
- drop patch 1
- New release 0.4.14

* Tue May 10 2005 Götz Waschk <waschk@mandriva.org> 0.4.13-2mdk
- patch for gcc 4
- fix build on x86_64

* Fri Apr 15 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 0.4.13-1mdk
- New release 0.4.13

* Thu Nov 11 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.11-1mdk
- fix installation
- New release 0.4.11

* Wed Jul 21 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.4.7-1mdk
- New release 0.4.7

* Fri Jul 09 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.4-1mdk
- fix build
- right configure macro
- fix source URL
- New release 0.4.4

* Thu Dec 11 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4.3-1mdk
- new version

