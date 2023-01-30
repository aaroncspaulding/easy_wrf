export CONDADIR={{conda_environment_path}}

export PATH={{conda_environment_path}}/bin:$PATH
export CPPFLAGS=$CPPFLAGS" -I${CONDADIR}/include"
export LDFLAGS=$LDFLAGS" -L${CONDADIR}/lib"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${CONDADIR}/lib

export CC={{conda_environment_path}}/bin/gcc
export CXX={{conda_environment_path}}/bin/g++
export FC={{conda_environment_path}}/bin/gfortran
export FCFLAGS=-m64
export F77={{conda_environment_path}}/bin/gfortran
export FFLAGS=-m64
export JASPERLIB={{conda_environment_path}}/lib
export JASPERINC={{conda_environment_path}}/include
export LIBS=$LIBS" -lnetcdf"
export NETCDF={{conda_environment_path}}