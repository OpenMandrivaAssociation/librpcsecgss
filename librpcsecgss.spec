%define	major 3
%define libname     %mklibname rpcsecgss %{major}
%define develname	%mklibname rpcsecgss -d

Summary:	Allows secure rpc communication using the rpcsec_gss protocol
Name:		librpcsecgss
Version:	0.19
Release:	5
License:	BSD-like
Group:		System/Libraries
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	gssglue-devel

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
Requires:	%{libname} >= %{version}-%{release}
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

# cleanups
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/*.so.*

%files  -n %{develname}
%{_includedir}/rpcsecgss
%{_libdir}/*.so
%{_libdir}/pkgconfig/librpcsecgss.pc
