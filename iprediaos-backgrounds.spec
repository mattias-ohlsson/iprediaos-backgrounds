%global iprediaos_release_name winston
%global IprediaOS_Release_Name Winston
Name:		%{iprediaos_release_name}-backgrounds
Version:	1
Release:	1%{?dist}
Summary:	%{IprediaOS_Release_Name} desktop backgrounds

Group:		Applications/Multimedia
License:	CC-BY-SA
URL:		http://ipredia.org
Source0:	%{iprediaos_release_name}.png
Source1: 	%{iprediaos_release_name}.xml
Source2: 	desktop-backgrounds-%{iprediaos_release_name}.xml
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:	noarch

#BuildRequires:	
#Requires:	

%description
This package contains desktop backgrounds for the IprediaOS theme.

%package        single
Summary:        Single screen images for IprediaOS Backgrounds
Group:          Applications/Multimedia
License:        CC-BY-SA

%description    single
This package contains single screen images for IprediaOS Backgrounds


%package        gnome
Summary:        IprediaOS Wallpapers for Gnome
Group:          Applications/Multimedia

Requires:       %{name}-single = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the IprediaOS theme. 

%prep
#%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT

# Install background
mkdir -p $RPM_BUILD_ROOT/usr/share/backgrounds/%{iprediaos_release_name}/default/standard
cp %{SOURCE0} $RPM_BUILD_ROOT/usr/share/backgrounds/%{iprediaos_release_name}/default/standard/ 
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/share/backgrounds/%{iprediaos_release_name}/default/
mkdir -p $RPM_BUILD_ROOT/usr/share/gnome-background-properties
cp %{SOURCE2} $RPM_BUILD_ROOT/usr/share/gnome-background-properties/


%clean


%files single
%defattr(-,root,root,-)
%doc
%{_datadir}/backgrounds/%{iprediaos_release_name}/default/standard/%{iprediaos_release_name}.png

%files gnome
%{_datadir}/backgrounds/%{iprediaos_release_name}/default/%{iprediaos_release_name}.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-%{iprediaos_release_name}.xml


%changelog
* Tue May 17 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1-1
- Initial package
