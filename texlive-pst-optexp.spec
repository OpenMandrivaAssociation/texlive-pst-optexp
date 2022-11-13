Name:		texlive-pst-optexp
Version:	62977
Release:	1
Summary:	Drawing optical experimental setups
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-optexp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.source.r%{version}.tar.xz
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
%{_texmfdistdir}/dvips/pst-optexp
%{_texmfdistdir}/tex/latex/pst-optexp
%doc %{_texmfdistdir}/doc/latex/pst-optexp
#- source
%doc %{_texmfdistdir}/source/latex/pst-optexp

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
