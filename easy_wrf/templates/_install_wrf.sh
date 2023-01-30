# Installs WRF into the correct path

#{{wrf_version}} # 4.2.2

# Download and install WRF
wget https://github.com/wrf-model/WRF/archive/refs/tags/v4.2.2.tar.gz
tar xzvf ./v4.2.2.tar.gz
cd ./WRF-4.2.2/
echo 34 |  ./configure  # Configure and select option 34
./compile em_real >& log.compile
cd ./main

if [ ! -f "main/wrf.exe" ]; then
	echo "WRF INSTALLED FAILURE."
	exit 1
else
	echo "WRF INSTALLED SUCCESS!"
fi



