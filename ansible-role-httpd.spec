Name:       ansible-role-httpd
Version:    0.0.1
Release:    1%{?dist}
Summary:    ansible-role-httpd
License:    ASL 2.0
URL:        https://github.com/Spredzy/ansible-role-httpd
Source0:    ansible-role-httpd-%{version}.tar.gz

BuildArch:  noarch
Requires:   ansible

%description
An Ansible module for the Apache HTTPD Webserver

%prep
%setup -qc


%build

%install
mkdir -p %{buildroot}%{_datadir}/ansible/roles/httpd
chmod 755 %{buildroot}%{_datadir}/ansible/roles/httpd

cp -r defaults %{buildroot}%{_datadir}/ansible/roles/httpd
cp -r handlers %{buildroot}%{_datadir}/ansible/roles/httpd
cp -r meta %{buildroot}%{_datadir}/ansible/roles/httpd
cp -r tasks %{buildroot}%{_datadir}/ansible/roles/httpd
cp -r vars %{buildroot}%{_datadir}/ansible/roles/httpd


%files
%doc README.md
%license LICENSE
%{_datadir}/ansible/roles/httpd


%changelog
* Wed Apr 26 2017 Yanis Guenane <yguenane@redhat.com> - 0.0.1-1
- Initial release
