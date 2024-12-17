%global commit     9fd0577cf1231e61c9801c81499e5d16d0743806
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20241128
%global gitrel      .%{commit_date}.git%{shortcommit}
%global debug_package %{nil}

Name:           mps-kit
Version:        1.118.90
Release:        %autorelease
Summary:        Ravenbrook Memory Pooling System for building garbage collectors
License:        BSD-2-Clause
URL:            https://www.ravenbrook.com/project/mps 
Source:         https://github.com/Ravenbrook/mps/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  gcc
BuildRequires:  make

%description
The GNU Hello program produces a familiar, friendly greeting. Yes, this is
another implementation of the classic program that prints "Hello, world!" when
you run it.

%undefine _auto_set_build_flags

%prep
%setup -q -n mps-%{commit}

%build
gcc -O2 -flto=auto -ffat-lto-objects -fPIC  -g -pipe -grecord-gcc-switches -m64 -march=x86-64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -mtls-dialect=gnu2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -Wno-error=dangling-pointer -c code/mps.c
gcc-ar rvs libmps.a mps.o 

%install
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
install -m 644 libmps.a %{buildroot}/%{_libdir}
install -m 644 code/mps.h %{buildroot}/%{_includedir}

%files
%{_libdir}/libmps.a
%{_includedir}/mps.h
%license license.txt

%changelog
%autochangelog
