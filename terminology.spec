Summary:	Terminology - EFL terminal emulator
Summary(pl.UTF-8):	Terminology - emulator terminala oparty na EFL
Name:		terminology
Version:	0.2.0
Release:	1
License:	BSD
Group:		Applications
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	188995667d64f86e0c938c7f8eded5a1
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1.6
BuildRequires:	ecore-devel >= 1.7.0
BuildRequires:	ecore-imf-devel >= 1.7.0
BuildRequires:	ecore-imf-evas-devel >= 1.7.0
BuildRequires:	ecore-input-devel >= 1.7.0
BuildRequires:	edje >= 1.7.0
BuildRequires:	edje-devel >= 1.7.0
BuildRequires:	eet-devel >= 1.7.0
BuildRequires:	efreet-devel >= 1.7.0
BuildRequires:	eina-devel >= 1.7.0
BuildRequires:	elementary-devel >= 1.7.0
BuildRequires:	emotion-devel >= 1.7.0
BuildRequires:	evas-devel >= 1.7.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	ecore >= 1.7.0
Requires:	ecore-imf >= 1.7.0
Requires:	ecore-imf-evas >= 1.7.0
Requires:	ecore-input >= 1.7.0
Requires:	edje-libs >= 1.7.0
Requires:	eet >= 1.7.0
Requires:	efreet >= 1.7.0
Requires:	eina >= 1.7.0
Requires:	elementary >= 1.7.0
Requires:	emotion >= 1.7.0
Requires:	evas >= 1.7.0
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
%{_datadir}/terminology
%{_desktopdir}/terminology.desktop
%{_pixmapsdir}/terminology.png
