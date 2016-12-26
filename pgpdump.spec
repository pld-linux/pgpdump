Summary:	PGP packet visualizer
Name:		pgpdump
Version:	0.31
Release:	1
License:	MIT-like
Group:		Applications/File
Source0:	http://www.mew.org/~kazu/proj/pgpdump//%{name}-%{version}.tar.gz
# Source0-md5:	a68e04a73a01c050bc83343bb0dd2ba0
URL:		http://www.mew.org/~kazu/proj/pgpdump/en/
BuildRequires:	autoconf
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGP packet visualizer which displays the packet format of OpenPGP
(RFC 4880) and PGP version 2 (RFC 1991).

%prep
%setup -q

%build
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
