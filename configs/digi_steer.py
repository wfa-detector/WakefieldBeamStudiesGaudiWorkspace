'''-------------------------------------------------------------'''
'''  Digitization Steering File for the Muon Collider Detector  '''
'''-------------------------------------------------------------'''
from GaudiKernel.Constants import INFO, WARNING

import sys
sys.path.append("../configs")
import digi_components

# Collect Arguements
from digi_components.digi_args import get_digi_args
args = get_digi_args()

# Set Up Services
from digi_components.digi_services import set_digi_services
[evtsvc, geoservice, id_service] = set_digi_services(args)

# Import the Algorithm List
from digiAlgList import makeDigiAlgList
algList = makeDigiAlgList(args)

'''-------------------------------------------------------------'''
'''    Run the Digitization Algorithms in the ApplicationMgr    '''
'''-------------------------------------------------------------'''
# Declare Input and Output for the IOSvc
from k4FWCore import IOSvc, ApplicationMgr
svc = IOSvc(
    "IOSvc",
    Input = ["sim_output.edm4hep.root"],  # Input file from simulation
    Output = "digi_output.edm4hep.root" # Output file for digitization
)

# Run the Application Manager
ApplicationMgr(
    TopAlg = algList,
    EvtSel = 'NONE',
    EvtMax   = -1,
    ExtSvc = [evtsvc, geoservice],
    OutputLevel=INFO
)
