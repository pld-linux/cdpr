Summary:	Cisco Discovery Protocol Reporter
Summary(pl):	Cisco Discovery Protocol Reporter
Name:		cdpr
Version:	1.0.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.monkeymental.com/mmfiles/%{name}-%{version}.tgz
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

%description -l pl
cdpr (Cisco Discovery Protocol Reporter) pokazuje stan switcha i
portu, do kt�rego maszyna jest pod��czona, je�eli obs�uguje ona CDP.
Mo�e tak�e dekodowa� ca�y pakiet CDP. cdpr zosta� napisany aby pom�c
administratorom systemu/sieci dowiedzie� si� do jakiego sprz�tu s�
pod��czone maszyny. Jest to robione poprzez przechwytywanie i
dekodowanie pakiet�w Cisco Discovery Protocol (CDP).

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o cdpr cdpr.c -Wall -lpcap

%install
rm -rf $RPM_BUILD_ROOT
install -D cdpr $RPM_BUILD_ROOT%{_sbindir}/cdpr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(754,root,root) %{_sbindir}/cdpr
