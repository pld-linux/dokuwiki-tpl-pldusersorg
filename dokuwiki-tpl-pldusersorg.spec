%define		tpl	pldusersorg
Summary:	PLD-Users.org template for DokuWiki
Summary(pl.UTF-8):	Szablon PLD-users.org dla DokuWiki
Name:		dokuwiki-tpl-%{tpl}
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	pldusersorg.tar.gz
# Source0-md5:	c1cc75f5359b2c05fd71eec9c775163a
Source1:	dokuwiki-find-lang.sh
URL:		http://pld-users.org
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dokuwiki >= 20070626
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		tpldir		%{dokudir}/lib/tpl/%{tpl}

%description
Default PLD-Users.org template.

%description -l pl.UTF-8
Domyślny szablon serwisu PLD-Users.org.

%prep
%setup -q -n %{tpl}

rm -f LICENSE # GPL v2
rm -f *~

cat > INSTALL <<'EOF'
To activate this template add the following to your conf/local.php file:
$conf['template'] = '%{tpl}';
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tpldir}
cp -a . $RPM_BUILD_ROOT%{tpldir}
rm -f $RPM_BUILD_ROOT%{tpldir}/{INSTALL,README}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc INSTALL README
%dir %{tpldir}
%{tpldir}/*.php
%{tpldir}/*.css
%{tpldir}/*.html
%{tpldir}/script.js
%{tpldir}/style.ini
%{tpldir}/conf
%{tpldir}/images
%{tpldir}/sidebars
