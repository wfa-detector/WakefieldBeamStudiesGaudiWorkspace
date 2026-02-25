# WakefieldBeamStudiesGaudiWorkspace
A native-gaudi based Key4hep software setup to perform detector R&D studies for wakefield-based colliders

## Repository Structure
- `packages/` All custom native gaudi key4hep packages linked using git submodules.
- 'configs/' All important configuration files are present here

### Container
All commands are compatible and should be run inside the latest the docker container setup using the image "angirar/wcd:main-gaudi-alma9". The image is public and should be available to download via the "docker pull" command.
To start a shifter container instead, refer to the repository `https://github.com/wfa-detector/wcd-gaudi-docker`

### Setup and build Instructions
- Git clone this repository for e.g. `git clone git@github.com:wfa-detector/WakefieldBeamStudiesGaudiWorkspace.git`
- cd WakefieldBeamStudiesGaudiWorkspace
- git submodule update --init --recursive
- Run the following commands from inside your container:
```bash
source setup.sh
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../install 
cmake --build . -t install
```

##Generation
e.g. 100 GeV electron gun events
```
python configs/pgun_edm4hep.py egun_gen.root -p 100 -e 100 --pdg 11 --theta 0 180
```

##Simulation
Set the `geometryFile` variable in `configs/ddsim_steer_baseline.py` to point to the initial 10 TeV detector design present here - `/path/to/packages/k4geo/Wakefield/compact/Wakefield_v0/Wakefield_v0.xml`. Then run:
```
ddsim --steeringFile configs/ddsim_steer_baseline.py --inputFile egun_gen.root --outputFile egun_sim.root --numberOfEvents 100
```

##Digitization
```
k4run configs/digi_steer.py --IOSvc.Input egun_sim.root --IOSvc.Output egun_digi.root --DD4hepXMLFile /path/to/packages/k4geo/Wakefield/compact/Wakefield_v0/Wakefield_v0.xml --doTrkDigiSimple
```

##Reconstruction
Coming up soon!!


