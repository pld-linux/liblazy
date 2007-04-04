Summary:	Liblazy - D-Bus methods provided for convenience
Summary(pl.UTF-8):	Liblazy
Name:		liblazy
Version:	0.1
Release:	1
License:	GPL v2 / LGPL
Group:		Libraries
Source0:	http://people.freedesktop.org/~homac/liblazy/%{name}-%{version}.tar.bz2
# Source0-md5:	aae2f15bc8cc92f0c66d6c7f397d3048
URL:		http://freedesktop.org/wiki/Software_2fliblazy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege. Its features
may grow as needed, though.

%package devel
Summary:	Header files for liblazy
Summary(pl.UTF-8):	Pliki nagłówkowe dla liblazy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for liblazy.

%prep
%setup -q

%build
%configure \
	--enable-static=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_pkgconfigdir}/lazy.pc

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/liblazy.h
