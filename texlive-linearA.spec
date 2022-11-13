Name:		texlive-linearA
Version:	63169
Release:	1
Summary:	Linear A script fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/archaic/linearA
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lineara.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lineara.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lineara.source.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/lineara
%{_texmfdistdir}/fonts/map/dvips/lineara
%{_texmfdistdir}/fonts/tfm/public/lineara
%{_texmfdistdir}/fonts/type1/public/lineara
%{_texmfdistdir}/tex/latex/lineara
%doc %{_texmfdistdir}/doc/fonts/lineara
#- source
%doc %{_texmfdistdir}/source/fonts/lineara

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
