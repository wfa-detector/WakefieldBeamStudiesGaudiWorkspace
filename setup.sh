if [ ${#} != 0 ] && [ ${#} != 1 ]; then
    echo "usage: ${0} [build]"
    return 1
fi

#
# Check for build directory
MYBUILD=build
if [ ! -d "${MYBUILD}" ]; then
    echo "Install directory ${MYBUILD} does not exist - creating it..."
    mkdir -p "${MYBUILD}" || { echo "Failed to create ${MYBUILD}"; exit 1; }
fi

#
# Check for install directory
MYINSTALL=install
if [ ! -d "${MYINSTALL}" ]; then
    echo "Install directory ${MYINSTALL} does not exist - creating it..."
    mkdir -p "${MYINSTALL}" || { echo "Failed to create ${MYINSTALL}"; exit 1; }
fi

# Convert to absolute path
export MYINSTALL=$(realpath ${MYINSTALL})

# Set paths
export PATH=${MYINSTALL}/bin:$PATH
export LD_LIBRARY_PATH=${MYINSTALL}/lib:${MYINSTALL}/lib64:$LD_LIBRARY_PATH

# Spack hashes change when the container is rebuilt. Resolve the runtime
# libraries by SONAME instead of keeping image-specific absolute paths here.
for wakefield_library in 'libgsl.so.*' 'libCLHEP-*.so' 'libboost_thread.so.*'; do
    wakefield_library_path=$(find /opt/spack/opt/spack -name "${wakefield_library}" -print -quit 2>/dev/null)
    if [ -n "${wakefield_library_path}" ]; then
        wakefield_library_dir=$(dirname "${wakefield_library_path}")
        export LD_LIBRARY_PATH=${wakefield_library_dir}:${LD_LIBRARY_PATH}
    else
        echo "Warning: ${wakefield_library} was not found under /opt/spack/opt/spack"
    fi
done
unset wakefield_library wakefield_library_path wakefield_library_dir

export ROOT_INCLUDE_PATH=${MYINSTALL}/include:$ROOT_INCLUDE_PATH
export PYTHONPATH=${PWD}/configs:${MYINSTALL}/python:$PYTHONPATH
export CMAKE_PREFIX_PATH=${MYINSTALL}:$CMAKE_PREFIX_PATH
