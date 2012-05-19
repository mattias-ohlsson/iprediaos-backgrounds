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

%prep
#%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT

# Install background
mkdir -p $RPM_BUILD_ROOT/usr/share/backgrounds/%{iprediaos_release_name}/default/standard
cp %{SOURCE0} $RPM_BUILD_ROOT/usr/share/backgrounds/%{iprediaos_release_name}/default/standard/ 

%clean


%files single
%defattr(-,root,root,-)
%doc
%{_datadir}/backgrounds/%{iprediaos_release_name}/default/standard/%{iprediaos_release_name}.png


%changelog
* Tue May 17 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1-1
- Initial package