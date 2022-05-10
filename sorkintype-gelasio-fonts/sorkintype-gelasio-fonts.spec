# SPDX-License-Identifier: MIT
%global forgeurl https://github.com/SorkinType/Gelasio
%global commit   45b816432931142b0bb78f5a968d3bd27b9e8d2f
%forgemeta

Version: 1.006
Release: 3%{?dist}
URL:     %{forgeurl}

%global foundry       SorkinType
%global fontlicense   OFL
%global fontlicenses  OFL.txt
%global fontdocs      *txt *md
%global fontdocsex    %{fontlicenses} requirements.txt

%global fontfamily    Gelasio
%global fontsummary   Gelasio is an original typeface which is metrics compatible with Georgia
%global fonts         fonts/ttf/*ttf
%global fontconfs     %{SOURCE10}
%global fontpkgheader %{expand:
Provides:  gelasio-fonts
Obsoletes: gelasio-fonts < %{version}-%{release}
}
%global fontdescription %{expand:
Gelasio is an original typeface which is metrics compatible with Georgia
in its Regular, Bold, Italic and Bold Italic weights. It supports the
Google Fonts Latin Pro glyph set, enabling the typesetting of English,
Western, Eastern and Southern European languages as well as Vietnamese
and 130+ other languages.}

Source0: %{forgesource}
Source10: 60-%{fontpkgname}.conf

%fontpkg

%package doc
Summary: Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shippend with
%{name}.

%prep
%forgesetup
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc Test*Documents/*pdf

%changelog
* Tue May 10 2022 Jeffrey Serio <hyperreal@fedoraproject.org> - 1.006-4
- Change commit hash for sorkintype-gelasio-fonts.spec

* Mon Nov 02 2020 Dawid Zych <dawid.zych@yandex.com> - 1.006-3
- Skip variable fonts
- Add additional docs

* Mon Nov 02 2020 Dawid Zych <dawid.zych@yandex.com> - 1.006-2
- Initial packaging
