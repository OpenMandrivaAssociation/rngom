%_javapackages_macros
Name: rngom
Version: 201103
Release: 0.8.20120119svn.0%{?dist}
Summary: Java library for parsing RELAX NG grammars

License: MIT
URL: https://rngom.dev.java.net

# svn export -r 70 https://svn.java.net/svn/rngom~svn/trunk/rngom rngom-201103
# find rngom-201103/ -name '*.class' -delete
# find rngom-201103/ -name '*.jar' -delete
# tar czf rngom-201103.tar.gz rngom-201103
Source0: %{name}-%{version}.tar.gz
Patch0: %{name}-%{version}-pom.patch

BuildRequires: bsf
BuildRequires: bsh
BuildRequires: stax2-api
BuildRequires: javacc
BuildRequires: javacc-maven-plugin
BuildRequires: jpackage-utils
BuildRequires: junit4
BuildRequires: maven-local
BuildRequires: maven-clean-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: msv-xsdlib
BuildRequires: relaxngDatatype
BuildRequires: sonatype-oss-parent
BuildRequires: xmlunit

Requires: stax2-api
Requires: jpackage-utils
Requires: msv-xsdlib
Requires: relaxngDatatype

BuildArch: noarch


%description
RNGOM is an open-source Java library for parsing RELAX NG grammars.

In particular, RNGOM can:
* parse the XML syntax
* parse the compact syntax
* check all the semantic restrictions as specified in the specification
* parse RELAX NG into application-defined data structures
* build a default data structure based around the binarized simple syntax or
  another data structure that preserves more of the parsed information
* parse foreign elements/attributes in a schema
* parse comments in a schema


%package javadoc

Summary: Javadoc for %{name}
Requires: jpackage-utils


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
%patch0 -p1


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
cp -p target/rngom-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%files javadoc
%{_javadocdir}/*
