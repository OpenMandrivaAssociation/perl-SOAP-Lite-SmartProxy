%define upstream_name    SOAP-Lite-SmartProxy
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	SOAP::Transport::HTTPX Server/Client side HTTP Smart Proxy for SOAP::Lite
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DY/DYACOB/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Apache/SmartProxy.pm
%{perl_vendorlib}/SOAP/Transport/HTTPX.pm
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 404389
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.11-4mdv2009.0
+ Revision: 241859
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-2mdv2008.0
+ Revision: 86856
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.11-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11-1mdk
- initial Mandriva package

