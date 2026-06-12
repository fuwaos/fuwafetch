Name:           fuwafetch
Version:        0.1.0
%global debug_package %{nil}
Release:        1%{?dist}
Summary:        System fetch utility for FuwaOS

License:        MPL-2.0
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rust cargo

%description
Custom system fetch written in Rust.

%prep
%setup -q

%build
cargo build --release

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/bin
install -m 755 target/release/fuwafetch %{buildroot}/usr/bin/

%files
/usr/bin/fuwafetch

%changelog
* Fri Jun 12 2026 Gora <gora@fuwaos> - 0.1.0-1
- Initial build
