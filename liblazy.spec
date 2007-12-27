Summary:	Liblazy - D-Bus methods provided for convenience
Summary(pl.UTF-8):	liblazy - metody D-Bus dla wygody
Name:		liblazy
Version:	0.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://people.freedesktop.org/~homac/liblazy/%{name}-%{version}.tar.bz2
# Source0-md5:	d1a91efd155dcd1467c2768447d01e42
URL:		http://freedesktop.org/wiki/Software_2fliblazy
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege. Its features
may grow as needed, though.

%description -l pl.UTF-8
liblazy to prosta i łatwa w użyciu biblioteka udostępniająca wygodne
funkcje do wysyłania komunikatów poprzez demona D-Bus, kolejkowania
informacji z HAL-a lub odpytywania PolicyKit o uprawnienia. Możliwości
biblioteki mogą jednak rosnąć w razie potrzeby.

%package devel
Summary:	Header files for liblazy
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liblazy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 1.0

%description devel
Header files for liblazy.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liblazy.

%package static
Summary:	Static liblazy library
Summary(pl.UTF-8):	Statyczna bibliotekia liblazy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liblazy library.

%description static -l pl.UTF-8
Statyczna biblioteka liblazy.

%prep
%setup -q

%build
%configure
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/liblazy.h
%{_pkgconfigdir}/lazy.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblazy.a
