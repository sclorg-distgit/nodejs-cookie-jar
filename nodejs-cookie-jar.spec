%{?scl:%scl_package nodejs-cookie-jar}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-cookie-jar
Epoch:          1
Version:        0.3.0
Release:        3.2%{?dist}
Summary:        A cookie handling and cookie jar library for Node.js
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

Group:          System Environment/Libraries
#ASL 2.0 added upstream
#https://github.com/mikeal/cookie-jar/blob/master/LICENSE
License:        ASL 2.0
URL:            https://github.com/mikeal/cookie-jar
Source0:        http://registry.npmjs.org/cookie-jar/-/cookie-jar-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#this needs to get renamed to nodejs-cookie-jar soon
Provides:       %{?scl_prefix}nodejs-tobi-cookie = %{epoch}:%{version}
Obsoletes:      %{?scl_prefix}nodejs-tobi-cookie < 1:0.2.0-3

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%summary.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/cookie-jar
cp -p index.js jar.js package.json %{buildroot}%{nodejs_sitelib}/cookie-jar

%nodejs_symlink_deps

%check
%{?scl:scl enable %{scl} "}
%{__nodejs} tests/run.js
%{?scl:"}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/cookie-jar

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1:0.3.0-3.2
- rebuilt

* Fri Jan 10 2014 Tomas Hrcka <thrcka@redhat.com> - 1:0.3.0-3.2
- Obsolete tobie-cookie with scl_prefix

* Thu Nov 07 2013 Tomas Hrcka <thrcka@redhat.com> - 1:0.3.0-2.1
- Software collections support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.3.0-1
- new upstream release 0.3.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.0-6
- restrict to compatible arches

* Tue Apr 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.0-5
- run tests

* Fri Apr 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.0-4
- fix Obsoletes as sugessted during rename review

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.0-3
- rename to nodejs-cookie-jar

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.1-1
- now unbundled from tobi, called cookie-jar upstream

* Sat Jan 26 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.2-2
- add missing build section

* Tue Jan 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.2-1
- initial package
