Summary:	Redirect UDP connections
Summary(pl.UTF-8):   Przekierowywanie połączeń UDP
Name:		uredir
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ibiblio.org/pub/Linux/system/network/misc/%{name}-%{version}.tar.gz
# Source0-md5:	408c1172839368c5631ecef9df18778b
Patch0:		%{name}-fn_name.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Redir redirects udp connections coming in to a local port to a
specified address/port combination.

%description -l pl.UTF-8
Redir przekierowuje połączenia udp przychodzące na określony lokalny
port na podany inny adres oraz port.

%prep
%setup  -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install uredir		$RPM_BUILD_ROOT%{_sbindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
