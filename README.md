# Easy WRF

The Weather Research and Forecasting (WRF) Model has many dependencies and is often challenging to install and set up. This package automatically installs all WRF dependencies and generates install scripts and configuration files for WRF.

This package has been tested on the UConn HPC cluster and the Heaviside cluster operating on Red Hat Enterprise Linux 8 and Ubuntu 22.  

## Installation Steps
Please visit the [NCAR tutorial here.](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP4) All steps are similar except that dependencies are installed with anaconda in a user account. This guide skips the included tests.

### 1. Install Anaconda
You must have a working version of anaconda or miniconda. [This guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) may be helpful.

### 2. Create and activate your 'wrf' environment with the WRF dependencies
You can select any name you want
```shell
conda create -n wrf -c conda-forge easy_wrf
conda activate wrf
```
We will need the installation location. You can run ```which python``` to find the installation location. You can save this location with ```export CONDADIR="~/miniconda3/envs/wrf"```

### 3. Environment Variables
Set the ```CONDADIR``` variable

```shell
export PATH=$CONDADIR/bin:$PATH
export CPPFLAGS=$CPPFLAGS" -I${CONDADIR}/include"
export LDFLAGS=$LDFLAGS" -L${CONDADIR}/lib"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${CONDADIR}/lib
export CC=$CONDADIR/bin/gcc
export CXX=$CONDADIR/bin/g++
export FC=$CONDADIR/bin/gfortran
export FCFLAGS=-m64
export F77=$CONDADIR/bin/gfortran
export FFLAGS=-m64
export JASPERLIB=$CONDADIR/lib
export JASPERINC=$CONDADIR/include
export LIBS=$LIBS" -lnetcdf"
export NETCDF=$CONDADIR
```

### 4. Install WRF
Version numbers may be changed for your version.
```shell
wget https://github.com/wrf-model/WRF/archive/refs/tags/v4.2.2.tar.gz
tar xzvf ./v4.2.2.tar.gz
cd ./WRF-4.2.2/
echo 34 |  ./configure
```
**You must modify a section of the 'configure.wrf' file:**
```shell
COMPRESSION_LIBS    = -L/home/acs14007/miniconda3/envs/wrf/lib -ljasper -lpng -lz
COMPRESSION_INC     = -I/home/acs14007/miniconda3/envs/wrf/include
FDEFS               = -DUSE_JPEG2000 -DUSE_PNG
SFC                 = ~/miniconda3/envs/wrf/bin/gfortran
SCC                 = ~/miniconda3/envs/wrf/bin/gcc
DM_FC               = ~/miniconda3/envs/wrf/bin/mpif90 -f90=$(SFC)
DM_CC               = ~/miniconda3/envs/wrf/bin/mpicc -cc=$(SCC)
FC                  = $(SFC) 
CC                  = $(SCC)
LD                  = $(FC)
FFLAGS              = -ffree-form -O -fconvert=big-endian -frecord-marker=4 -fallow-argument-mismatch
```

```shell
./compile em_real >& log.compile
cd ./main
```

Make sure to set the ```WRF_DIR``` variable.

### 5. Install WPS
```shell
wget https://github.com/wrf-model/WPS/archive/refs/tags/v4.3.tar.gz
tar xzvf ./v4.3.tar.gz
cd ./WPS-4.3/
./clean
echo 29 |  ./configure
```
**Modify the configuration file again**
```shell
./compile >& log.compile
```


