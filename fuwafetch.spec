Name:           fuwafetch
Version:        0.1.0
Release:        1%{?dist}
Summary:        NeoFetch for FuwaOS

License:        BSD-3-Clause license 
URL:            https://fuwaos.duckdns.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo

%description
Кастомный fetch-скрипт на Rust для вывода системной инфы и морды Фувы. 
Жрет ноль ресурсов, работает моментально.

%prep
%setup -q

%build
cargo build --release

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Jun 11 2026 FuwaOS Team <admin@fuwaos.duckdns.org> - 0.1.0-1
- Первый релиз. Добавлена морда маскота и базовая системная инфа.
