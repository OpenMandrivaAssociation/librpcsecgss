%define	major	3
%define libname	%mklibname rpcsecgss %{major}
%define devname	%mklibname rpcsecgss -d

Summary:	Allows secure rpc communication using the rpcsec_gss protocol
Name:		librpcsecgss
Version:	0.19
Release:	7
License:	BSD-like
Group:		System/Libraries
Url:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/%{name}/%{name}-%{version}.tar.gz
Patch0:		librpcsecgss-0.19-libtirpc.patch
BuildRequires:	pkgconfig(libgssglue)
BuildRequires:	pkgconfig(libtirpc)

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

%package -n	%{devname}
Summary:	Development library and header files for the librpcsecgss library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	rpcsecgss-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the development librpcsecgss library and its
header files.

%prep
%setup -q
%patch0 -p1 -b .tirpc~
autoreconf -fi

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.*

%files  -n %{devname}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_includedir}/rpcsecgss
%{_libdir}/*.so
%{_libdir}/pkgconfig/librpcsecgss.pc

