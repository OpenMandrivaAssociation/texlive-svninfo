# revision 17554
# category Package
# catalog-ctan /macros/latex/contrib/svninfo
# catalog-date 2010-03-23 21:34:59 +0100
# catalog-license lppl1
# catalog-version 0.7.4
Name:		texlive-svninfo
Version:	0.7.4
Release:	1
Summary:	Typeset Subversion keywords
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svninfo
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package for incorporating the values of Subversion keywords
into typeset documents. Information about Subversion (a
replacement for CVS) is available from
http://subversion.tigris.org/.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
