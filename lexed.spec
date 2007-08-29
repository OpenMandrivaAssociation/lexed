%define name	lexed
%define version	4.7
%define release	%mkrel 5
%define major	%{version}
%define libname %mklibname %{name} %{major}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Lexicon analyser
Source:		https://gforge.inria.fr/frs/download.php/1489/%{name}-%{version}.tar.bz2
URL:		https://gforge.inria.fr/projects/lingwb/
License:	GPL
Group:		Sciences/Computer science
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Lexed allows to search a dictionary entry from a string. The finished
automata-based algorithm is especially fast, and offers a good alternative to
hashes for large dictionnaries.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{libname}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%{mklibname %{name} 4.6}-devel

%description -n %{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%multiarch_binaries %{buildroot}%{_bindir}/%{name}-config

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README doc/*.html
%{_bindir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liblexed-%{version}.so

%files -n %{libname}-devel
%defattr(-,root,root)
%multiarch %{multiarch_bindir}/%{name}-config
%{_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/liblexed.so
%{_datadir}/aclocal/*


