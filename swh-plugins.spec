Summary: A set of audio plugins for LADSPA
Name: swh-plugins
Version: 0.4.15
Release: %mkrel 1
License: GPL
Group: Sound
Source: http://plugin.org.uk/releases/%version/%name-%version.tar.bz2
Patch: swh-plugins-0.4.4-build.patch
BuildRoot: %_tmppath/%{name}-buildroot
BuildRequires: ladspa-devel fftw-devel
URL: http://plugin.org.uk/
%description
A set of audio plugins for LADSPA (see http://plugin.org.uk/ for more
details).

%prep
%setup -q
%patch -p1

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


