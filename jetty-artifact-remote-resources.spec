Name:           jetty-artifact-remote-resources
Version:        1.0
Release:        9%{?dist}
Summary:        Jetty toolchain artifact remote resources

License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
# rpmlint config file (fedpkg lint will use this)
Source1:        .rpmlint
BuildArch:      noarch

Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:        http://www.eclipse.org/legal/epl-v10.html

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin >= 1.2.1-3
BuildRequires:  jetty-toolchain

%description
Jetty toolchain artifact remote resources

%prep
%setup -q
cp -p %{SOURCE2} %{SOURCE3} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt epl-v10.html
%dir %{_javadir}/%{name}

%changelog
* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-9
- Migrate away from mvn-rpmbuild (#997458)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Oct 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-6
- Install license files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  8 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-3
- Change remote-resources version compare from > to >=
- Removed generation of javadocs (wasn't working anyway)

* Mon Nov  7 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-2
- Added maven-surefire-provider-junit to BR

* Thu Nov  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-1
- Initial version of the package
