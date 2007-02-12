# TODO:
# - prepare subpackage with cdp server
#
Summary:	Cisco Discovery Protocol Reporter
Summary(pl.UTF-8):   Cisco Discovery Protocol Reporter - narzędzie do śledzenia CDP
Name:		cdpr
Version:	2.2.0
Release:	3
License:	GPL v2
Group:		Applications/System
Source0:	http://www.monkeymental.com/mmfiles/%{name}-%{version}.tar.gz
# Source0-md5:	023b8bd6d399204a66ad728f2aa11ca3
URL:		http://www.monkeymental.com/nuke/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cdpr (Cisco Discovery Protocol Reporter) shows the switch and port
that a machine is connected to, provided that the device supports CDP.
It can also optionally decode the full CDP packet. cdpr was written to
help network/system administrators find out about the equipment that a
machine is connected to. This is done by capturing and decoding a
Cisco Discovery Protocol (CDP) packet.

%description -l pl.UTF-8
cdpr (Cisco Discovery Protocol Reporter) pokazuje stan switcha i
portu, do którego maszyna jest podłączona, jeżeli obsługuje ona CDP.
Może także dekodować cały pakiet CDP. cdpr został napisany aby pomóc
administratorom systemu/sieci dowiedzieć się do jakiego sprzętu są
podłączone maszyny. Jest to robione poprzez przechwytywanie i
dekodowanie pakietów Cisco Discovery Protocol (CDP).

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o cdpr cdpr.c cdprs.c conffile.c -Wall -lpcap

%install
rm -rf $RPM_BUILD_ROOT

install -D cdpr $RPM_BUILD_ROOT%{_sbindir}/cdpr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* cdpr.conf cdprs
%attr(754,root,root) %{_sbindir}/cdpr
