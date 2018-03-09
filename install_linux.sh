#!/usr/bin/bash
if [ "$(id -u)" != "0" ]; then
   echo -e "\e[1;31mThis script must be run as root.\e[00m" 1>&2
   exit 1
fi

if  [ "${1}" == "uninstall" ]; then
	echo -e "\e[1;31mUninstalling ...\e[00m"

	if [ -d "/opt/awolip" ]; then
		echo -e "\e[1;31mRemoving /opt/awolip\e[00m"
		rm -rf /opt/awolip
	else
		echo -e "Nothing to remove..."
	fi

	if [ -f "/usr/bin/awolip" ]; then
		echo -e "\e[1;31mRemoving /usr/bin/awolip\e[00m"
		rm /usr/bin/awolip
	else
		echo -e "Nothing to remove..."
	fi

	echo -e "\e[1;32mFinished!\e[00m"
else
	echo -e "\e[1;32mChecking for dependencies...\e[00m"

	if [ ! -d "/opt/" ]; then
		mkdir /opt/
		echo -e "Created /opt/ "

		mkdir /opt/awolip
		echo -e "Created /opt/awolip"
	fi

	if [ ! -d "/opt/awolip/" ]; then
		mkdir /opt/awolip
		echo -e "Created /opt/awolip"
	else
		echo -e "\e[1;31mError: /opt/awolip already exists.\e[00m"
		echo "Please first uninstall the last version: sudo ./install_linux.sh uninstall"
		exit 1
	fi

	echo "Copying files..."
	cp *.py /opt/awolip

	echo "Creating awolip script..."

	if [ ! -f  /usr/bin/awolip ]; then
		touch /usr/bin/awolip
		chmod +x /usr/bin/awolip

		echo "#!/bin/bash" >> /usr/bin/awolip
		echo "if [ \$# -eq 0 ]; then" >> /usr/bin/awolip
		echo "	echo \"Please see 'awolip -h'.\"" >> /usr/bin/awolip
		echo "else" >> /usr/bin/awolip
		echo "	python3 /opt/awolip/main.py \$@" >> /usr/bin/awolip
		echo "fi" >> /usr/bin/awolip

		echo -e "\e[1;32mFinished!\e[00m"
	else
		echo -e "\e[1;31mError: /usr/bin/awolip already exists. Please remove.\e[00m"
		exit 1
	fi
fi
