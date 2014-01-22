%define		efl_ver		1.7.0

Summary:	Terminology - EFL terminal emulator
Summary(pl.UTF-8):	Terminology - emulator terminala oparty na EFL
Name:		terminology
Version:	0.4.0
Release:	1
License:	BSD
Group:		Applications
Source0:	http://download.enlightenment.org/rel/apps/terminology/%{name}-%{version}.tar.bz2
# Source0-md5:	43bf2164c6849580db2a461ae5fac57a
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1.6
BuildRequires:	ecore-devel >= %{efl_ver}
BuildRequires:	ecore-evas-devel >= %{efl_ver}
BuildRequires:	ecore-file-devel >= %{efl_ver}
BuildRequires:	ecore-imf-devel >= %{efl_ver}
BuildRequires:	ecore-imf-evas-devel >= %{efl_ver}
BuildRequires:	ecore-input-devel >= %{efl_ver}
BuildRequires:	ecore-ipc-devel >= %{efl_ver}
BuildRequires:	edje >= %{efl_ver}
BuildRequires:	edje-devel >= %{efl_ver}
BuildRequires:	eet-devel >= %{efl_ver}
BuildRequires:	efreet-devel >= %{efl_ver}
BuildRequires:	eina-devel >= %{efl_ver}
BuildRequires:	eldbus-devel
BuildRequires:	elementary-devel >= %{efl_ver}
BuildRequires:	emotion-devel >= %{efl_ver}
BuildRequires:	ethumb-devel >= %{efl_ver}
BuildRequires:	evas-devel >= %{efl_ver}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	ecore >= %{efl_ver}
Requires:	ecore-evas >= %{efl_ver}
Requires:	ecore-file >= %{efl_ver}
Requires:	ecore-imf >= %{efl_ver}
Requires:	ecore-imf-evas >= %{efl_ver}
Requires:	ecore-input >= %{efl_ver}
Requires:	ecore-ipc >= %{efl_ver}
Requires:	edje-libs >= %{efl_ver}
Requires:	eet >= %{efl_ver}
Requires:	efreet >= %{efl_ver}
Requires:	eina >= %{efl_ver}
Requires:	elementary >= %{efl_ver}
Requires:	emotion >= %{efl_ver}
Requires:	ethumb >= %{efl_ver}
Requires:	evas >= %{efl_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminology is an EFL terminal emulator with some extra bells and
whistles. It's brand new and was only started near the begining of
June 2012, so expecting it to do everything a mature terminal emulator
does is a bit premature, but considering it's young age, it does a
lot.

%description -l pl.UTF-8
Terminology to emulator terminala oparty na EFL z pewnymi dodatkowymi
wodotryskami. Jest dosyć nowy, powstał na początku czerwca 2012, więc
oczekiwanie do niego funkcji właściwych dojrzałym emulatorom terminali
jest nieco przedwczesne, ale - jak na swój młody wiek - potrafi dużo.

%prep
%setup -q

# non-themable images go to pixmaps dir
%{__sed} -i -e 's,$(datadir)/icons$,$(datadir)/pixmaps,' data/icons/Makefile.am

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
export CFLAGS="%{rpmcflags} $(pkg-config --cflags eldbus)"
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO
%attr(755,root,root) %{_bindir}/terminology
%attr(755,root,root) %{_bindir}/tyalpha
%attr(755,root,root) %{_bindir}/tybg
%attr(755,root,root) %{_bindir}/tycat
%attr(755,root,root) %{_bindir}/tyls
%attr(755,root,root) %{_bindir}/typop
%attr(755,root,root) %{_bindir}/tyq
%{_datadir}/terminology
%{_desktopdir}/terminology.desktop
%{_pixmapsdir}/terminology.png
%{_mandir}/man1/terminology.1*
