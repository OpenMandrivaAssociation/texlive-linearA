Name:		texlive-linearA
Version:	20061201
Release:	1
Summary:	Linear A script fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/archaic/linearA
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linearA.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linearA.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linearA.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The linearA package provides a simple interface to two fonts
which include all known symbols, simple and complex, of the
Linear A script. This way one can easily replicate Linear A
"texts" using modern typographic technology. Note that the
Linear A script has not been deciphered yet and probably never
will be deciphered.

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