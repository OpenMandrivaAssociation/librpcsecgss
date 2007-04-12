%define	major 3
%define libname	%mklibname rpcsecgss %{major}

Summary:	Allows secure rpc communication using the rpcsec_gss protocol
Name:		librpcsecgss
Version:	0.14
Release:	%mkrel 1
License:	BSD-like
Group:		System/Libraries
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/librpcsecgss/librpcsecgss-%{version}.tar.gz
#BuildRequires:	krb5-devel >= 1.3
BuildRequires:	libgssapi-devel >= 0.9
BuildRequires:  automake1.7
BuildRequires:  autoconf2.5
BuildRequires:  pkgconfig
BuildRequires:  libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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

%package -n	%{libname}-devel
Summary:	Static library and header files for the librpcsecgss library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	librpcsecgss-devel = %{version}
Provides:	rpcsecgss-devel = %{version}
Obsoletes:	%{mklibname rpcsecgss 1}-devel
Obsoletes:	%{mklibname rpcsecgss 2}-devel

%description -n	%{libname}-devel
Allows secure rpc communication using the rpcsec_gss protocol
librpcsecgss allows secure rpc communication using the rpcsec_gss
protocol.

This package contains the static librpcsecgss library and its
header files.

%prep

%setup -q -n librpcsecgss-%{version}

# lib64 fix
perl -pi -e "s|/lib/|/%{_lib}/|g" configure*

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/*.so.*

%files  -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/rpcsecgss
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/librpcsecgss.pc


