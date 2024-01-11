%bcond_with bootstrap

Name:           plexus-classworlds
Version:        2.6.0
Release:        12%{?dist}
Summary:        Plexus Classworlds Classloader Framework
License:        ASL 2.0 and Plexus
URL:            https://github.com/codehaus-plexus/plexus-classworlds
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap-openjdk8
%else
BuildRequires:  maven-local-openjdk8
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
%endif

%description
Classworlds is a framework for container developers
who require complex manipulation of Java's ClassLoaders.
Java's native ClassLoader mechanisms and classes can cause
much headache and confusion for certain types of
application developers. Projects which involve dynamic
loading of components or otherwise represent a 'container'
can benefit from the classloading control provided by
classworlds.

%{?javadoc_package}

%prep
%setup -q -n %{name}-%{name}-%{version}
%mvn_file : %{name} plexus/classworlds
%mvn_alias : classworlds:classworlds

%pom_add_dep junit:junit:4.13.1:test

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-dependency-plugin

# These tests depend on artifacts that are not packaged
sed -i /testConfigure_Valid/s/./@org.junit.Ignore/ $(find -name ConfiguratorTest.java)
sed -i /testConfigure_Optionally_Existent/s/./@org.junit.Ignore/ $(find -name ConfiguratorTest.java)

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt LICENSE-2.0.txt

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 29 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6.0-11
- Add missing test dependency on JUnit 4

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.6.0-10
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6.0-7
- Bootstrap build
- Non-bootstrap build

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.6.0-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6.0-4
- Build with OpenJDK 8

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6.0-3
- Mass rebuild for javapackages-tools 201902

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6.0-2
- Mass rebuild for javapackages-tools 201901

* Tue May 14 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6.0-1
- Update to upstream version 2.6.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Michael Simacek <msimacek@redhat.com> - 2.5.2-7
- Add missing BRs

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.2-5
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.2-2
- Update upstream URL

* Sat Aug 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.2-1
- Update to upstream version 2.5.2

* Thu Jun 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-5
- Obsolete classworlds

* Mon Jun  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-4
- Add alias for classworlds:classworlds

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5.1-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-1
- Update to upstream version 2.5.1

* Mon Aug 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-1
- Update to upstream version 2.5
- Update to current packaging guidelines

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Mat Booth <fedora@matbooth.co.uk> - 2.4.2-4
- Remove superfluous BRs, fixes rhbz #915616

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.4.2-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 22 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4.2-1
- Update to latest bugfix release 2.4.2 (#895445)

* Wed Nov 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-11
- Install required ASL 2.0 license text

* Wed Nov 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-10
- Revert change from 2.4-9

* Tue Nov 20 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-9
- Provide and obsolete classworlds

* Mon Nov 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-8
- Fix source URL to be stable

* Tue Aug  7 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-7
- Export only proper OSGI packages
- Do not generate "uses" OSGI clauses

* Mon Aug 06 2012 Gerard Ryan <galileo@fedoraproject.org> - 2.4-6
- Generate OSGI info using maven-plugin-bundle

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr  5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-4
- Update to maven 3
- Remove rpm bug workaround

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-1
- Update to latest upstream version
- Drop ant build parts
- Versionless jars & javadocs
- Enable tests again

* Tue Dec 21 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2.3-2
- Fix FTBFS.

* Tue Jul 13 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.3-1
- Version bump
- Fix few small packaging guidelines violations

* Thu Aug 20 2009 Andrew Overholt <overholt@redhat.com> 0:1.2-0.a9.8
- Bump release.

* Wed Aug 19 2009 Andrew Overholt <overholt@redhat.com> 0:1.2-0.a9.7
- Document sources and patches

* Wed Aug 19 2009 Andrew Overholt <overholt@redhat.com> 0:1.2-0.a9.6
- Update tarball-building instructions
- Remove gcj support
- Remove unnecessary post requirements

* Thu May 14 2009 Fernando Nasser <fnasser@redhat.com> 0:1.2-0.a9.6
- Fix license specification

* Tue Apr 28 2009 Yong Yang <yyang@redhat.com> 0:1.2-0.a9.5
- Add BRs maven2-plugin-surfire*, maven-doxia*
- Rebuild with maven2-2.0.8 built in non-bootstrap mode

* Mon Mar 16 2009 Yong Yang <yyang@redhat.com> 0:1.2-0.a9.4
- rebuild with new maven2 2.0.8 built in bootstrap mode

* Tue Jan 13 2009 Yong Yang <yyang@redhat.com> 0:1.2-0.a9.3jpp.1
- re-build with maven

* Tue Jan 06 2009 Yong Yang <yyang@redhat.com> 0:1.2-0.a9.2jpp.1
- Imported into devel from dbhole's maven 2.0.8 packages

* Wed Jan 30 2008 Deepak Bhole <dbhole@redhat.com> 0:1.2-0.a9.1jpp.1
- Initial build -- merged from JPackage
