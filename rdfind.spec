Summary:	Redundant Data Find - tool for finding duplicate files
Summary(pl.UTF-8):	Narzędzie do wyszukiwania duplikatów plików
Name:		rdfind
Version:	1.8.0
Release:	1
License:	GPL v2+
Group:		Applications/File
Source0:	https://rdfind.pauldreik.se/%{name}-%{version}.tar.gz
# Source0-md5:	1650dd2f24a2b0a14a0417fca9e426d8
URL:		https://rdfind.pauldreik.se/
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	nettle-devel
BuildRequires:	xxHash-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdfind (Redundant Data Find) is a tool for finding duplicate files.

%description -l pl.UTF-8
rdfind (Redundant Data Find - wyszukiwanie nadmiarowych danych) to
narzędzie do wyszukiwania duplikatów plików.
%prep
%setup -q

%build
%configure \
	--with-xxhash
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README TODO
%attr(755,root,root) %{_bindir}/rdfind
%{_mandir}/man1/rdfind.1*
