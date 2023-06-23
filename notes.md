# Test Build Process on Apple Silicon Mac

*Make sure to create and activate a conda build environment with the conda-build and conda-verify packages.*

### Test a Recipe
*In recipe directory:*
```shell
CONDA_SUBDIR=osx-64 conda build . -c conda-forge
```

### Create a Test Environment
**See the path of the test environment:**
```shell
CONDA_SUBDIR=osx-64 conda build . -c conda-forge --output
```
**Create the environment with:**
```shell
CONDA_SUBDIR=osx-64 conda create -n testenv --use-local <path_to_test_environment>
```


# Other Notes

### Create Environment from .yml
```shell
conda env create -f environment.yml
```

*for an x86 environment on Apple Silicon with Rosetta 2 use:*
```shell
CONDA_SUBDIR=osx-64 conda env create -f environment.yml
```


### Delete an environment
```shell
conda remove --name <name> --all
```

### Conda clean
*Useful if random errors start popping up.*
```shell
conda clean --all
```