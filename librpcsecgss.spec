%define	major 3
%define libname     %mklibname rpcsecgss %{major}
%define develname	%mklibname rpcsecgss -d

Summary:	Allows secure rpc communication using the rpcsec_gss protocol
Name:		librpcsecgss
Version:	0.19
Release:	%mkrel 5
License:	BSD-like
Group:		System/Libraries
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	gssglue-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Allows secure rpc communication using the rpcsec_gss protocol
librpcsecgss allows secure rpc communication using the rpcsec_gss
protocol.

%package -n	%{libname}
Summary:	Allows secure rpc communication using the rpcsec_gss protocol
Group:		System/Libraries

%description -n	%{libname}
Allows secure rpc communication using the rpcsec_gss protocol
librpcsecgss allows secure rpc communication using the rpcsec_gss
protocol.

%package -n	%{develname}
Summary:	Static library and header files for the librpcsecgss library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	rpcsecgss-devel = %{version}-%{release}
Obsoletes:	%{mklibname rpcsecgss 1}-devel
Obsoletes:	%{mklibname rpcsecgss 2}-devel
Obsoletes:	%{mklibname rpcsecgss 3}-devel

%description -n	%{develname}
Allows secure rpc communication using the rpcsec_gss protocol
librpcsecgss allows secure rpc communication using the rpcsec_gss
protocol.

This package contains the static librpcsecgss library and its
header files.

%prep
%setup -q -n librpcsecgss-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/*.so.*

%files  -n %{develname}
%defattr(-,root,root)
%{_includedir}/rpcsecgss
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/librpcsecgss.pc


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.19-4mdv2011.0
+ Revision: 660279
- mass rebuild

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0.19-3mdv2011.0
+ Revision: 601059
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.19-2mdv2010.1
+ Revision: 519029
- rebuild

* Sat Aug 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2010.0
+ Revision: 422157
- update to new version 0.19

* Thu Dec 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.18-2mdv2009.1
+ Revision: 315591
- rebuild

* Fri Jun 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2009.0
+ Revision: 227544
- update to new version 0.18

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.17-2mdv2009.0
+ Revision: 222974
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2008.1
+ Revision: 106229
- new version

* Thu Sep 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2008.0
+ Revision: 81051
- new version
  drop patch 0, merged upstream
  patch 1: fix pkgconfig file

* Thu Sep 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2008.0
+ Revision: 80683
- fix build
- new version
  spec cleanup


* Mon Jan 22 2007 Andreas Hasenack <andreas@mandriva.com> 0.14-1mdv2007.0
+ Revision: 111820
- updated to version 0.14
- new soname

* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.12-3mdv2007.1
+ Revision: 63382
- rebuild
- Import librpcsecgss

* Wed Jun 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.12-2mdv2007.0
- fix deps

* Wed Jun 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.12-1mdv2007.0
- 0.12
- new major
- fix deps

* Fri Mar 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8-2mdk
- use correct major (1)

* Fri Mar 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8-1mdk
- 0.8
- fix deps

* Fri Feb 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7-2mdk
- fix naming

* Sat Dec 17 2005 Stefan van der Eijk <stefan@eijk.nu> 0.7-1mdk
- 0.7
- %%mkrel

* Wed May 11 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5-1mdk
- 0.5
- fix naming
- lib64 fixes
- drop P0 as it's not needed anymore
- major is zero now

* Sun Jan 09 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.1-1mdk
- initial mandrake package

