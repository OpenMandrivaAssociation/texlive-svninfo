# revision 17554
# category Package
# catalog-ctan /macros/latex/contrib/svninfo
# catalog-date 2010-03-23 21:34:59 +0100
# catalog-license lppl1
# catalog-version 0.7.4
Name:		texlive-svninfo
Version:	0.7.4
Release:	8
Summary:	Typeset Subversion keywords
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svninfo
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svninfo.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7.4-2
+ Revision: 756360
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7.4-1
+ Revision: 719618
- texlive-svninfo
- texlive-svninfo
- texlive-svninfo
- texlive-svninfo

