%global tl_name powerdot-tuliplab
%global tl_revision 47963

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	A style package for Powerdot to provide the design of TULIP Lab
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/powerdot-tuliplab
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot-tuliplab.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot-tuliplab.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
powerdot-tuliplab is the LaTeX package used in TULIP Lab for
presentation drafting. It comes with several sample .tex files so that
you can quickly start working with it.

