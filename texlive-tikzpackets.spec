Name:		texlive-tikzpackets
Version:	55827
Release:	1
Summary:	Display network packets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikzpackets
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpackets.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpackets.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to easily display network packets
graphically.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikzpackets
%doc %{_texmfdistdir}/doc/latex/tikzpackets

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
