%global _default_patch_fuzz 2

# Generated by rust2rpm 26
%bcond_without check

%global crate satty
%global cargo_install_lib 0

Name:           satty
Version:        0.16.0
Release:        1%{?dist}
Summary:        Modern Screenshot Annotation
License:        MPL-2.0

URL:            https://github.com/gabm/satty
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Patch:          remove-extra-log.diff

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  fontconfig-devel
BuildRequires:  libepoxy-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-gobject-devel
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel

%global _description %{expand:
Modern Screenshot Annotation. A Screenshot Annotation Tool inspired by
Swappy and Flameshot.}

%description %{_description}

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{name}
Provides:       %{name}-bash-completion = %{version}-%{release}

Requires:       bash-completion
Requires:       %{name} = %{version}-%{release}

%description bash-completion
This package installs Bash completion files for %{name}

%package fish-completion
BuildArch:      noarch
Summary:        Fish completion files for %{name}
Provides:       %{name}-fish-completion = %{version}-%{release}

Requires:       fish
Requires:       %{name} = %{version}-%{release}

%description fish-completion
This package installs Fish completion files for %{name}

%package zsh-completion
BuildArch:      noarch
Summary:        Zsh completion files for %{name}
Provides:       %{name}-zsh-completion = %{version}-%{release}

Requires:       zsh
Requires:       %{name} = %{version}-%{release}

%description zsh-completion
This package installs Zsh completion files for %{name}

%prep
%autosetup -n Satty-%{version} -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

install -Dpm644 satty.desktop %{buildroot}%{_datadir}/applications/satty.desktop

install -Dpm644 completions/satty.bash %{buildroot}%{bash_completions_dir}/satty
install -Dpm644 completions/satty.fish %{buildroot}%{fish_completions_dir}/satty.fish
install -Dpm644 completions/_satty %{buildroot}%{zsh_completions_dir}/_satty

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/satty
%{_datadir}/applications/satty.desktop

%files bash-completion
%{bash_completions_dir}/satty

%files fish-completion
%{fish_completions_dir}/satty.fish

%files zsh-completion
%{zsh_completions_dir}/_satty

%changelog
%autochangelog
