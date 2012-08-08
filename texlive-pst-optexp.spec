# revision 27202
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-optexp
# catalog-date 2012-07-27 12:36:40 +0200
# catalog-license lppl
# catalog-version 3.2
Name:		texlive-pst-optexp
Version:	3.2
Release:	1
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
