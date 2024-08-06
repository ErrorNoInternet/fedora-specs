# Generated by rust2rpm 26
%bcond_without check

%global crate wallust
%global cargo_install_lib 0

Name:           wallust
Version:        3.0.0
Release:        1%{?dist}
Summary:        Generate a 16 color scheme based on an image
License:        MIT

URL:            https://codeberg.org/explosion-mental/wallust
Source:         %{url}/archive/%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26

Recommends:     ImageMagick

%global _description %{expand:
Generate a 16 color scheme based on an image.}

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
%autosetup -n %{crate} -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

install -Dpm644 man/wallust-cs.1 %{buildroot}%{_mandir}/man1/wallust-cs.1
install -Dpm644 man/wallust-run.1 %{buildroot}%{_mandir}/man1/wallust-run.1
install -Dpm644 man/wallust-theme.1 %{buildroot}%{_mandir}/man1/wallust-theme.1
install -Dpm644 man/wallust.1 %{buildroot}%{_mandir}/man1/wallust.1
install -Dpm644 man/wallust.5 %{buildroot}%{_mandir}/man5/wallust.5

install -Dpm644 completions/wallust.bash %{buildroot}%{bash_completions_dir}/wallust
install -Dpm644 completions/wallust.fish %{buildroot}%{fish_completions_dir}/wallust.fish
install -Dpm644 completions/_wallust %{buildroot}%{zsh_completions_dir}/_wallust

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc docs/README.md docs/v3.md
%{_bindir}/wallust
%{_mandir}/man1/wallust-cs.1*
%{_mandir}/man1/wallust-run.1*
%{_mandir}/man1/wallust-theme.1*
%{_mandir}/man1/wallust.1*
%{_mandir}/man5/wallust.5*

%files bash-completion
%{bash_completions_dir}/wallust

%files zsh-completion
%{zsh_completions_dir}/_wallust

%files fish-completion
%{fish_completions_dir}/wallust.fish

%changelog
%autochangelog
