# revision 33077
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-optexp
# catalog-date 2014-02-28 20:10:22 +0100
# catalog-license lppl
# catalog-version 4.8
Name:		texlive-pst-optexp
Version:	4.8
Release:	5
Summary:	Drawing optical experimental setups
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-optexp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is a collection of optical components that
facilitate easy sketching of optical experimental setups. The
package uses PSTricks for its output. A wide range of free-ray
and fibre components is provided, the alignment, positioning
and labelling of which can be achieved in very simple and
flexible ways. The components may be connected with fibers or
beams, and realistic raytraced beam paths are also possible.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-optexp/pst-optexp.pro
%{_texmfdistdir}/tex/latex/pst-optexp/pst-optexp.sty
%doc %{_texmfdistdir}/doc/latex/pst-optexp/Changes
%doc %{_texmfdistdir}/doc/latex/pst-optexp/README
%doc %{_texmfdistdir}/doc/latex/pst-optexp/pst-optexp-DE.pdf
%doc %{_texmfdistdir}/doc/latex/pst-optexp/pst-optexp-quickref.pdf
%doc %{_texmfdistdir}/doc/latex/pst-optexp/pst-optexp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pst-optexp/Makefile
%doc %{_texmfdistdir}/source/latex/pst-optexp/pst-optexp.dtx
%doc %{_texmfdistdir}/source/latex/pst-optexp/pst-optexp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
