# Generated by rust2rpm 26
%bcond_without check

%global crate hwatch
%global cargo_install_lib 0

Name:           yazi
Version:        0.2.5
Release:        %autorelease
Summary:        Blazing fast terminal file manager
License:        MIT

URL:            https://github.com/sxyazi/yazi
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  make
Buildrequires:  gcc

%global _description %{expand:
%{summary}.}

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
%cargo_install --path yazi-cli
%cargo_install --path yazi-fm

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/ya
%{_bindir}/yazi

%changelog
%autochangelog
