%define upstream_name    SOAP-Lite-SmartProxy
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	SOAP::Transport::HTTPX Server/Client side HTTP Smart Proxy for SOAP::Lite
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DY/DYACOB/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The SmartProxy package is intended for use in a multi-server
setting where one or more servers may not be directly accessible
to client side scripts. The SmartProxy package makes request
redirection and forwarding on a per class basis easy.  Client
scripts need not know which server is appropriate for a specific
request and may make all requests from a single master server
which can be relied upon to redirect clients to the server
currently fulfilling a given request.  The relieves a maintenance
burden on the client side.  The server may also redirect clients
to a new class name or fully qualified action URI (methods and
arguments are assumed to remain constant however).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Apache/SmartProxy.pm
%{perl_vendorlib}/SOAP/Transport/HTTPX.pm
%{_mandir}/*/*
