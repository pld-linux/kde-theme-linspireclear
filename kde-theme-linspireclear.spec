# TODO: Check if the icons are distributable
#	Write usable descriptions

%bcond_with	weHaveCheckedIfTheIconsAreDistributable

%define		_name	linspireclear

%define		_common_ver	0.0.0.50
%define		_style_ver	1.11
%define		_icons_ver	1.7
Summary:	KDE theme - %{_name}
Summary(pl):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	%{_common_ver}
Release:	0.1
License:	LGPL/GPL/Proprietary
Group:		Themes
Source0:	http://software.linspire.com/pool-src/los/los-linspireclear-style/los-%{_name}-style_%{_style_ver}-%{_common_ver}.linspire0.1.tar.gz
# Source0-md5:	1e2cc6f0febf17b294d8306ccce8db51
Source1:	http://software.linspire.com/pool-src/los/los-clear-e-icons/los-clear-e-icons_%{_icons_ver}-%{_common_ver}.linspire0.1.tar.gz
# NoSource1-md5:	14d2ea49f2ebb47eb9690d69fcc6c7f2
%if %{without weHaveCheckedIfTheIconsAreDistributable}
NoSource:	1
%endif
Patch0:		kde-common-PLD.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TODO

%description -l pl
TODO

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Version:	%{_style_ver}
License:	LGPL
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
TODO

%description -n kde-style-%{_name} -l pl
TODO

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl):	Schemat kolor�w do stylu KDE - %{_name}
Version:        %{_style_ver}
License:        LGPL
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
TODO

%description -n kde-colorscheme-%{_name} -l pl
TODO

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - %{_name}
Summary(pl):	Dekoracja kwin - %{_name}
Version:	%{_style_ver}
License:	GPL
Group:		Themes
Requires:	kdebase-desktop-libs >= 9:3.2.0

%description -n kde-decoration-%{_name}
TODO

%description -n kde-decoration-%{_name} -l pl
TODO

%package -n kde-icons-%{_name}
Summary:        KDE icons - %{_name}
Summary(pl):    Motyw ikon KDE - %{_name}
Version:        %{_icons_ver}
Group:          Themes
License:       	Proprietary (See copyright)
Requires:       kdelibs

%description -n kde-icons-%{_name}
TODO

%description -n kde-icons-%{_name} -l pl
TODO


%prep
%if %{with weHaveCheckedIfTheIconsAreDistributable}
%setup -q -n marlin_build_los-%{_name}-style-1 -a1
%else
%setup -q -n marlin_build_los-%{_name}-style-1
%endif
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-qt-libraries=%{_libdir} \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}" \
	kde_libs_htmldir="%{_kdedocdir}"

%if %{with weHaveCheckedIfTheIconsAreDistributable}
install -d $RPM_BUILD_ROOT%{_iconsdir}
cp -drf marlin_build_los-clear-e-icons-1/clear-e $RPM_BUILD_ROOT%{_iconsdir}/clear-e
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*.themerc

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc

%if %{with weHaveCheckedIfTheIconsAreDistributable}
%files -n kde-icons-%{_name}
%defattr(644,root,root,755)
%doc marlin_build_los-clear-e-icons-1/debian/copyright
%{_iconsdir}/clear-e
%endif
