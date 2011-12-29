# revision 16037
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-optexp
# catalog-date 2009-11-06 14:30:35 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-pst-optexp
Version:	2.1
Release:	1
Summary:	Drawing optical experimental setups
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-optexp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package pst-optexp is a collection of optical components
that facilitate easy sketching of optical experimental setups.
Mechanisms for proper alignment of different components are
provided internally. This way the user does not have to care
for proper orientation of the elements.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-optexp/pst-optexp.pro
%{_texmfdistdir}/tex/generic/pst-optexp/pst-optexp.tex
%{_texmfdistdir}/tex/latex/pst-optexp/pst-optexp.sty
%doc %{_texmfdistdir}/doc/generic/pst-optexp/Changes
%doc %{_texmfdistdir}/doc/generic/pst-optexp/README
%doc %{_texmfdistdir}/doc/generic/pst-optexp/parque-nacional.eps
%doc %{_texmfdistdir}/doc/generic/pst-optexp/pst-optexp-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-optexp/pst-optexp-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
