Name:           surfacepro4-firmware
Version:        1.0 
Release:        1%{?dist}
Summary:        Packaged IPTS and Wifi firmware for Surface Pro 4 

License:        GPLv3+ 
#URL:            
Source0:        https://github.com/jakeday/linux-surface/raw/master/firmware/i915_firmware_skl.zip
Source1:	https://github.com/jakeday/linux-surface/raw/master/firmware/ipts_firmware_v78.zip
#Source2:	https://github.com/jakeday/linux-surface/raw/master/firmware/mrvl_firmware.zip
#Source3:	https://github.com/jakeday/linux-surface/raw/master/firmware/mwlwifi_firmware.zip 

BuildArch:	noarch

#BuildRequires:  
Requires:      unzip 

%description
Test

%install
mkdir -p %{buildroot}/lib/firmware/intel/ipts
unzip -o %{SOURCE0} -d %{buildroot}/lib/firmware/intel/ipts/

mkdir -p %{buildroot}/lib/firmware/1915
unzip -o %{SOURCE1} -d %{buildroot}/lib/firmware/1915/

#mkdir -p %{buildroot}/lib/firmware/mrvl/
#unzip -o %{SOURCE2} -d %{buildroot}/lib/firmware/mrvl/

#mkdir -p %{buildroot}/lib/firmware/mwlwifi
#unzip -o %{SOURCE3} -d %{buildroot}/lib/firmware/mwlwifi

%files
%defattr(0644, root, root)
/lib/firmware/intel/ipts
/lib/firmware/1915
#/lib/firmware/mrvl
#/lib/firmware/mwlwifi

%changelog
* Fri May 24 2019 alex
- 
