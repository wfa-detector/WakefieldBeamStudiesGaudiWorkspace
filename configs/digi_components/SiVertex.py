from GaudiKernel.Constants import INFO, WARNING
from Configurables import DDPlanarDigi, MuonCVXDDigitiser

def new_VertexBarrel(args):
    """
    Create a new vertex barrel instance with the given parameters.
    """
    if args.doOverlayFull:
        inputHitCollections = ["OverlayVertexBarrelCollection"]
    else:
        inputHitCollections = ["SiVertexBarrelHits"]

    if args.doTrkDigiSimple:
        return DDPlanarDigi(
            "VXDBarrelDigitiser",
            CorrectTimesForPropagation = True,
            IsStrip = False,
            ResolutionT = [0.03],
            ResolutionU = [0.005],
            ResolutionV = [0.005],
            SubDetectorName = "SiVertexBarrel",
            TimeWindowMax = [0.15],
            TimeWindowMin = [-0.09],
            UseTimeWindow = False,
            SimTrackHitCollectionName = inputHitCollections,
            SimTrkHitRelCollection = ["VertexBarrelHitsRelations"],
            TrackerHitCollectionName = ["VertexBarrelHits"],
            OutputLevel = INFO
        )
    else:
        return MuonCVXDDigitiser(
            "VXDBarrelDigitiser",
            ChargeDigitizeBinning=1,
            ChargeDigitizeNumBits=4,
            ChargeMaximum=15000.,
            CollectionName=inputHitCollections,
            CutOnDeltaRays=0.030,
            #Diffusion=0.07,
            DigitizeCharge=1,
            DigitizeTime=0,
            ElectronicEffects=1,
            ElectronicNoise=80,
            ElectronsPerKeV=270.3,
            EnergyLoss=280.0,
            MaxEnergyDelta=100.0,
            MaxTrackLength=10.0,
            OutputCollectionName=["VertexBarrelHits"],
            PixelSizeX="0.020",
            PixelSizeY="0.020",
            PoissonSmearing=1,
            RelationColName=["VertexBarrelHitsRelations"],
            SegmentLength=0.005,
            StoreFiredPixels=1,
            SubDetectorName="SiVertexBarrel",
            TanLorentz=0.8,
            TanLorentzY=0.0,
            Threshold=500,
            ThresholdSmearSigma=25,
            TimeDigitizeBinning=0,
            TimeDigitizeNumBits=10,
            TimeMaximum=15.0,
            TimeSmearingSigma=0.03,
            LayerIDs=["1","2","3","4","5"]
        )

def new_VertexEndcap(args):
    """
    Create a new vertex endcap instance with the given parameters.
    """
    if args.doOverlayFull:
        inputHitCollections = ["OverlayVertexEndcapCollection"]
    else:
        inputHitCollections = ["SiVertexEndcapHits"]

    if args.doTrkDigiSimple:
        return DDPlanarDigi(
            "VXDEndcapDigitiser",
            CorrectTimesForPropagation = True,
            IsStrip = False,
            ResolutionT = [0.03],
            ResolutionU = [0.005],
            ResolutionV = [0.005],
            SubDetectorName = "SiVertexEndcap",
            TimeWindowMax = [0.15],
            TimeWindowMin = [-0.09],
            UseTimeWindow = True,
            SimTrackHitCollectionName = inputHitCollections,
            SimTrkHitRelCollection = ["VertexEndcapHitsRelations"],
            TrackerHitCollectionName = ["VertexEndcapHits"],
            OutputLevel = INFO
        )

    else:
        return MuonCVXDDigitiser(
            "VXDEndcapDigitiser",
            ChargeDigitizeBinning=1,
            ChargeDigitizeNumBits=4,
            ChargeMaximum=15000.,
            CollectionName=inputHitCollections,
            CutOnDeltaRays=0.030,
            #Diffusion=0.07,
            DigitizeCharge=1,
            DigitizeTime=0,
            ElectronicEffects=1,
            ElectronicNoise=80,
            ElectronsPerKeV=270.3,
            EnergyLoss=280.0,
            MaxEnergyDelta=100.0,
            MaxTrackLength=10.0,
            OutputCollectionName=["VertexEndcapHits"],
            PixelSizeX="0.020",
            PixelSizeY="0.020",
            PoissonSmearing=1,
            RelationColName=["VertexEndcapHitsRelations"],
            SegmentLength=0.005,
            StoreFiredPixels=1,
            SubDetectorName="SiVertexEndcap",
            TanLorentz=0.0,
            TanLorentzY=0.0,
            Threshold=500,
            ThresholdSmearSigma=25,
            TimeDigitizeBinning=0,
            TimeDigitizeNumBits=10,
            TimeMaximum=15.0,
            TimeSmearingSigma=0.03,
            LayerIDs=["1","2","3","4"]
        )

