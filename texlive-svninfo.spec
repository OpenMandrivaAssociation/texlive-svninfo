Name:		texlive-svninfo
Version:	62157
Release:	1
Summary:	Typeset Subversion keywords
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svninfo
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for incorporating the values of Subversion keywords
into typeset documents. Information about Subversion (a
replacement for CVS) is available from
http://subversion.tigris.org/.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/svninfo/svninfo.cfg
%{_texmfdistdir}/tex/latex/svninfo/svninfo.sty
%doc %{_texmfdistdir}/doc/latex/svninfo/README
%doc %{_texmfdistdir}/doc/latex/svninfo/svninfo.init
%doc %{_texmfdistdir}/doc/latex/svninfo/svninfo.pdf
#- source
%doc %{_texmfdistdir}/source/latex/svninfo/Makefile
%doc %{_texmfdistdir}/source/latex/svninfo/svninfo.dtx
%doc %{_texmfdistdir}/source/latex/svninfo/svninfo.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
