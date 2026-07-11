%global tl_name svninfo
%global tl_revision 62157

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7.4
Release:	%{tl_revision}.1
Summary:	Typeset Subversion keywords
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/svninfo
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for incorporating the values of Subversion keywords into
typeset documents. Information about Subversion (a replacement for CVS)
is available from the project's home site.

