# Generated by rust2rpm 26
%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

%global __brp_mangle_shebangs /usr/bin/true

Name:           lowfi
Version:        1.3.5
Release:        %autorelease
Summary:        Extremely simple lofi player

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-2-Clause OR MIT OR Apache-2.0
# BSD-3-Clause OR MIT OR Apache-2.0
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR MIT OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
SourceLicense:  MIT

URL:            https://github.com/talwat/lowfi
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(openssl)

%global _description %{expand:
An extremely simple lofi player.}

%description %{_description}

%prep
%autosetup -n %{name}-%{version} -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies cargo-vendor.txt
%doc README.md
%{_bindir}/lowfi

%changelog
%autochangelog
