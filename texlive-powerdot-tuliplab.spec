Name:		texlive-powerdot-tuliplab
Version:	47963
Release:	1
Summary:	A style package for Powerdot to provide the design of TULIP Lab
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/powerdot-tuliplab
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot-tuliplab.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot-tuliplab.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
powerdot-tuliplab is the LaTeX package used in TULIP Lab for
presentation drafting. It comes with several sample .tex files
so that you can quickly start working with it.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/powerdot-tuliplab
%doc %{_texmfdistdir}/doc/latex/powerdot-tuliplab

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
