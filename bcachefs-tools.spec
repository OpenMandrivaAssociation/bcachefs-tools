%undefine _debugsource_packages

Name: bcachefs-tools
Version: 1.20.0
Release: 1
# repository: https://evilpiepirate.org/git/bcachefs-tools.git
Source0: https://github.com/koverstreet/bcachefs-tools/archive/refs/tags/v%{version}.tar.gz
# Official download location
#Source0: https://evilpiepirate.org/bcachefs-tools/bcachefs-tools-%{version}.tar.zst
# Not using this right now because of https://github.com/koverstreet/bcachefs-tools/issues/170
Summary: Tools for working with the bcachefs filesystem
URL: https://bcachefs.org/
License: GPL-2.0
Group: System
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(liburcu)
BuildRequires: pkgconfig(libsodium)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libkeyutils)
BuildRequires: libaio-devel

%description
Tools for working with the bcachefs filesystem

%prep
%autosetup -p1

%build
# Building the rust bindings is broken in 1.3.1
%make_build PREFIX=%{_prefix} NO_RUST=1 ROOT_SBINDIR=%{_sbindir}

%install
%make_install PREFIX=%{_prefix} NO_RUST=1 ROOT_SBINDIR=%{_sbindir}

# We don't currently have initramfs-tools, this needs to be
# ported to dracut (unless we decide to switch)
rm -rf %{buildroot}%{_datadir}/initramfs-tools

%files
%{_sbindir}/bcachefs
%{_sbindir}/fsck.bcachefs
%{_sbindir}/fsck.fuse.bcachefs
%{_sbindir}/mkfs.bcachefs
%{_sbindir}/mkfs.fuse.bcachefs
%{_sbindir}/mount.bcachefs
%{_sbindir}/mount.fuse.bcachefs
%{_mandir}/man8/bcachefs.8*
