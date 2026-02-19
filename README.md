# Template Workspace

Template for developing custom key4hep packages. Fork this repository and rename to create your own project.

## Repository Structure
- `exts/` External packages not included with the key4hep framework.
- `packages/` All custom packages linked using git submodules.

## Setup Instructions

### Container
All commands are compatible and should be run inside the latest `gitlab-registry.cern.ch/muon-collider/muoncollider-docker/mucoll-sim-alma9:(NEW IMAGE)`

#### Apptainer
If you have CVMFS available, then it is recommended to use the unpacked version.

```bash
apptainer shell --cleanenv /cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:(NEW IMAGE)
```

Alternatively you can download and convert the Docker image yourself.

```bash
apptainer shell --cleanenv gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:(NEW IMAGE)
```

#### Shifter
```bash
shifter --image gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:(NEW IMAGE) /bin/bash
```

### Build Instructions
Run the following commands from inside your container. The same commands will also work with a local installation of the ILC and Key4Hep software, with the exception of the first line.
```bash
source /opt/setup_mucoll.sh # Setup software
source setup.sh
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../install 
cmake --build . -t install
```
