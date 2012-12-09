# revision 15878
# category Package
# catalog-ctan /fonts/archaic/linearA
# catalog-date 2006-12-01 16:33:32 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-linearA
Version:	20061201
Release:	2
Summary:	Linear A script fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/archaic/linearA
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linearA.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linearA.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linearA.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The linearA package provides a simple interface to two fonts
which include all known symbols, simple and complex, of the
Linear A script. This way one can easily replicate Linear A
"texts" using modern typographic technology. Note that the
Linear A script has not been deciphered yet and probably never
will be deciphered.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/linearA/LinearA.afm
%{_texmfdistdir}/fonts/afm/public/linearA/LinearACmplxSigns.afm
%{_texmfdistdir}/fonts/map/dvips/linearA/linearA.map
%{_texmfdistdir}/fonts/tfm/public/linearA/LinearA.tfm
%{_texmfdistdir}/fonts/tfm/public/linearA/LinearACmplxSigns.tfm
%{_texmfdistdir}/fonts/type1/public/linearA/LinearA.pfb
%{_texmfdistdir}/fonts/type1/public/linearA/LinearACmplxSigns.pfb
%{_texmfdistdir}/tex/latex/linearA/linearA.sty
%doc %{_texmfdistdir}/doc/fonts/linearA/README
%doc %{_texmfdistdir}/doc/fonts/linearA/linearA_glyphs.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/linearA/linearA.dtx
%doc %{_texmfdistdir}/source/fonts/linearA/linearA.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061201-2
+ Revision: 753310
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061201-1
+ Revision: 718860
- texlive-linearA
- texlive-linearA
- texlive-linearA
- texlive-linearA

