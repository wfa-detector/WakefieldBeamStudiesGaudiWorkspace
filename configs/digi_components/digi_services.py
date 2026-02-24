from Gaudi.Configuration import *
from GaudiKernel.Constants import INFO, WARNING
from Configurables import GeoSvc, UniqueIDGenSvc, EventDataSvc, THistSvc

def set_digi_services(the_args):
    """
    Set up the necessary services for the digitization process.
    
    Parameters:
    the_args: Argument parser object containing configuration parameters.
    """
    geoservice = GeoSvc(
        "GeoSvc",
        detectors = [the_args.DD4hepXMLFile],
        OutputLevel = INFO,
        EnableGeant4Geo = False
    )

    evtsvc = EventDataSvc("EventDataSvc")

    id_service = UniqueIDGenSvc(
        "UniqueIDGenSvc", 
        Seed = the_args.RandSeed
    )
    
    THistSvc().Output = ["histos DATAFILE='digi_histograms.root' TYP='ROOT' OPT='RECREATE'"]
    THistSvc().PrintAll = True
    THistSvc().AutoSave = True
    THistSvc().AutoFlush = True
    THistSvc().OutputLevel = WARNING

    return [evtsvc, geoservice, id_service]
