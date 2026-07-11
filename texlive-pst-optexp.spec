%global tl_name pst-optexp
%global tl_revision 62977

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.1
Release:	%{tl_revision}.1
Summary:	Drawing optical experimental setups
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-optexp
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optexp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a collection of optical components that facilitate easy
sketching of optical experimental setups. The package uses PSTricks for
its output. A wide range of free-ray and fibre components is provided,
the alignment, positioning and labelling of which can be achieved in
very simple and flexible ways. The components may be connected with
fibers or beams, and realistic raytraced beam paths are also possible.

