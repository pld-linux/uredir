Summary:	Redirect UDP connections
Summary(pl):	Przekierowywanie po³±czeñ UDP
Name:		uredir
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ibiblio.org/pub/Linux/system/network/misc/%{name}-%{version}.tar.gz
Patch:		uredir-fn_name.patch
Vendor:		Id Est <id-est@home.com> 
#BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Redir redirects udp connections coming in to a local port to a
specified address/port combination.

%description -l pl
Redir przekierowuje po³±czenia udp przychodz±ce na okre¶lony lokalny
port na podany inny adres oraz port.

%prep
%setup  -q
%patch0 -p1

%build
%{__make} OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install uredir		$RPM_BUILD_ROOT%{_sbindir}

gzip -9nf README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
