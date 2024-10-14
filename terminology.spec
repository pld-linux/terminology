Summary:	Terminology - EFL terminal emulator
Summary(pl.UTF-8):	Terminology - emulator terminala oparty na EFL
Name:		terminology
Version:	1.13.0
Release:	1
License:	BSD
Group:		Applications
Source0:	https://download.enlightenment.org/rel/apps/terminology/%{name}-%{version}.tar.xz
# Source0-md5:	81e24535c1cf0ac9a506c711c9d621f7
URL:		http://enlightenment.org/
BuildRequires:	efl-devel >= 1.27.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.726
BuildRequires:	xz
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

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README.md TODO
%doc COLORSCHEMES.md THEMES.md
%attr(755,root,root) %{_bindir}/terminology
%attr(755,root,root) %{_bindir}/tyalpha
%attr(755,root,root) %{_bindir}/tybg
%attr(755,root,root) %{_bindir}/tycat
%attr(755,root,root) %{_bindir}/tyls
%attr(755,root,root) %{_bindir}/typop
%attr(755,root,root) %{_bindir}/tyq
%attr(755,root,root) %{_bindir}/tysend
%{_datadir}/terminology
%{_desktopdir}/terminology.desktop
%{_iconsdir}/hicolor/128x128/apps/terminology.png
%{_mandir}/man1/terminology.1*
%{_mandir}/man1/terminology-helpers.1*
%{_mandir}/man1/tyalpha.1*
%{_mandir}/man1/tybg.1*
%{_mandir}/man1/tycat.1*
%{_mandir}/man1/tyls.1*
%{_mandir}/man1/typop.1*
%{_mandir}/man1/tyq.1*
%{_mandir}/man1/tysend.1*
