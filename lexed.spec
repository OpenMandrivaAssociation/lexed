%define major	%{version}
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		lexed
Version:	4.7
Release:	10
Summary:	Lexicon analyser
Source:		https://gforge.inria.fr/frs/download.php/1489/%{name}-%{version}.tar.bz2
URL:		https://gforge.inria.fr/projects/lingwb/
License:	GPL
Group:		Sciences/Computer science
Requires:	%{libname} = %{version}-%{release}

%description
Lexed allows to search a dictionary entry from a string. The finished
automata-based algorithm is especially fast, and offers a good alternative to
hashes for large dictionnaries.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel < 4.7-10

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING INSTALL NEWS README doc/*.html
%{_bindir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/liblexed-%{version}.so

%files -n %{devname}
%{_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/liblexed.so
%{_datadir}/aclocal/*

%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 4.7-9mdv2011.0
+ Revision: 620063
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 4.7-8mdv2010.0
+ Revision: 429712
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 4.7-7mdv2009.0
+ Revision: 248369
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 4.7-5mdv2008.1
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Pixel <pixel@mandriva.com> 4.7-5mdv2008.0
+ Revision: 74640
- better conflict on older lib

* Wed Aug 29 2007 Pixel <pixel@mandriva.com> 4.7-4mdv2008.0
+ Revision: 74626
- add explicit conflict from liblexed4.7-devel on liblexed4.6-devel

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.7-3mdv2008.0
+ Revision: 67057
- rebuild


* Wed Mar 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.7-2mdv2007.0
+ Revision: 134337
- rebuild

* Mon Jan 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.7-1mdv2007.1
+ Revision: 114862
- new version

* Wed Aug 24 2005 Guillaume Rousse <guillomovitch@mandriva.org> 4.6-4mdk
- fix multiarch
- spec cleanup
- less stric requires
- %%mkrel

* Thu Dec 16 2004 Guillaume Rousse <guillomovitch@mandrake.org> 4.6-3mdk 
- explicit and stricter requires for lib package

* Wed Dec 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 4.6-2mdk 
- fix 10.0 build

* Tue Nov 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 4.6-1mdk 
- new version

* Fri Aug 06 2004 Guillaume Rousse <guillomovitch@mandrake.org> 4.5.0-2mdk 
- fixed major

* Fri Jul 16 2004 Guillaume Rousse <guillomovitch@mandrake.org> 4.5.0-1mdk 
- new version
- rpmbuildupdate aware

* Wed Jun 16 2004 Guillaume Rousse <guillomovitch@mandrake.org> 4.4.4-2mdk 
- rebuild

* Fri Apr 16 2004 Guillaume Rousse <guillomovitch@mandrake.org> 4.4.4-1mdk
- new version

* Wed Apr 14 2004 Guillaume Rousse <guillomovitch@mandrake.org> 4.4.3-1mdk
- new version

* Tue Apr 06 2004 Guillaume Rousse <guillomovitch@mandrake.org> 4.4.2-1mdk
- new version
- updated description

