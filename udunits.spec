#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : udunits
Version  : 2.2.26
Release  : 3
URL      : ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-2.2.26.tar.gz
Source0  : ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-2.2.26.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: udunits-bin = %{version}-%{release}
Requires: udunits-data = %{version}-%{release}
Requires: udunits-info = %{version}-%{release}
Requires: udunits-lib = %{version}-%{release}
Requires: udunits-license = %{version}-%{release}
BuildRequires : CUnit-dev
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : expat-dev
BuildRequires : flex
BuildRequires : gfortran

%description
This package provides support for units of physical quantities. Its main
components are:
1) A C library, "libudunits2", for:
a) Obtaining a binary representation of a unit;
b) Manipulating units arithmetically; and
c) Obtaining a converter of numeric values between compatible units;
2) A utility, "udunits2", for
a) Obtaining the definition of a unit; and
b) Converting a numeric value between compatible units; and
3) An extensive database of units.

%package bin
Summary: bin components for the udunits package.
Group: Binaries
Requires: udunits-data = %{version}-%{release}
Requires: udunits-license = %{version}-%{release}

%description bin
bin components for the udunits package.


%package data
Summary: data components for the udunits package.
Group: Data

%description data
data components for the udunits package.


%package dev
Summary: dev components for the udunits package.
Group: Development
Requires: udunits-lib = %{version}-%{release}
Requires: udunits-bin = %{version}-%{release}
Requires: udunits-data = %{version}-%{release}
Provides: udunits-devel = %{version}-%{release}
Requires: udunits = %{version}-%{release}

%description dev
dev components for the udunits package.


%package doc
Summary: doc components for the udunits package.
Group: Documentation
Requires: udunits-info = %{version}-%{release}

%description doc
doc components for the udunits package.


%package info
Summary: info components for the udunits package.
Group: Default

%description info
info components for the udunits package.


%package lib
Summary: lib components for the udunits package.
Group: Libraries
Requires: udunits-data = %{version}-%{release}
Requires: udunits-license = %{version}-%{release}

%description lib
lib components for the udunits package.


%package license
Summary: license components for the udunits package.
Group: Default

%description license
license components for the udunits package.


%prep
%setup -q -n udunits-2.2.26
cd %{_builddir}/udunits-2.2.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605120626
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1605120626
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/udunits
cp %{_builddir}/udunits-2.2.26/COPYRIGHT %{buildroot}/usr/share/package-licenses/udunits/1201ba41648bc95438bc2529ba3691dbc76438ef
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/udunits2

%files data
%defattr(-,root,root,-)
/usr/share/udunits/udunits2-accepted.xml
/usr/share/udunits/udunits2-base.xml
/usr/share/udunits/udunits2-common.xml
/usr/share/udunits/udunits2-derived.xml
/usr/share/udunits/udunits2-prefixes.xml
/usr/share/udunits/udunits2.xml

%files dev
%defattr(-,root,root,-)
/usr/include/converter.h
/usr/include/udunits.h
/usr/include/udunits2.h
/usr/lib64/libudunits2.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/udunits/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/udunits2.info
/usr/share/info/udunits2lib.info
/usr/share/info/udunits2prog.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libudunits2.so.0
/usr/lib64/libudunits2.so.0.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/udunits/1201ba41648bc95438bc2529ba3691dbc76438ef
