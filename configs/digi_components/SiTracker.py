from GaudiKernel.Constants import INFO, WARNING
from Configurables import DDPlanarDigi, MuonCVXDDigitiser

def new_TrackerBarrel(args):
    """
    Create a new tracker barrel digitiser instance with the given parameters.
    """
    if args.doOverlayFull:
        inputHitCollections = ["OverlayTrackerBarrelCollection"]
    else:
        inputHitCollections = ["SiTrackerBarrelHits"]

    if args.doTrkDigiSimple:
        return DDPlanarDigi(
            "TrackerBarrelDigitiser",
            CorrectTimesForPropagation = True,
            IsStrip = True,
            ResolutionT = [0.0],
            ResolutionU = [0.014],
            ResolutionV = [2.89],
            SubDetectorName = "SiTrackerBarrel",
            TimeWindowMax = [0.3],
            TimeWindowMin = [-0.18],
            UseTimeWindow = False,
            SimTrackHitCollectionName = inputHitCollections,
            SimTrkHitRelCollection = ["TrackerBarrelHitsRelations"],
            TrackerHitCollectionName = ["TrackerBarrelHits"],
            OutputLevel = INFO
        )
    else:
        return MuonCVXDDigitiser(
            "TrackerBarrelDigitiser",
            OutputLevel=INFO,
            ChargeDigitizeBinning=1,
            ChargeDigitizeNumBits=4,
            ChargeMaximum=60000.,
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
            SimHitLocCollectionName=["TrackerBarrelRawHits"],
            OutputCollectionName=["TrackerBarrelHits"],
            PixelSizeX="0.050",
            PixelSizeY="10.0",
            PoissonSmearing=1,
            RelationColName=["TrackerBarrelHitsRelations"],
            ReadoutName="SiTrackerBarrelHits",
            RawHitsLinkColName=["TrackerBarrelRawHitRelations"],
            SegmentLength=0.005,
            SensorThickness=0.300,
            StoreFiredPixels=0,
            SubDetectorName="SiTrackerBarrel",
            TanLorentz=0.8,
            TanLorentzY=0.0,
            Threshold=500,
            ThresholdSmearSigma=25,
            TimeDigitizeBinning=0,
            TimeDigitizeNumBits=10,
            TimeMaximum=15.0,
            TimeSmearingSigma=0.03,
            LayerIDs=[1, 2, 3, 4, 5]
        )
     

def new_TrackerEndcap(args):
    """
    Create a new tracker endcap digitiser instance with the given parameters.
    """
    if args.doOverlayFull:
        inputHitCollections = ["OverlayTrackerEndcapCollection"]
    else:
        inputHitCollections = ["SiTrackerEndcapHits"]

    if args.doTrkDigiSimple:
        return DDPlanarDigi(
            "TrackerEndcapDigitiser",
            CorrectTimesForPropagation = True,
            IsStrip = True,
            ResolutionT = [0.0],
            ResolutionU = [0.014],
            ResolutionV = [2.89],
            SubDetectorName = "SiTrackerEndcap",
            TimeWindowMax = [0.3],
            TimeWindowMin = [-0.18],
            UseTimeWindow = False,
            SimTrackHitCollectionName = inputHitCollections,
            SimTrkHitRelCollection = ["TrackerEndcapHitsRelations"],
            TrackerHitCollectionName = ["TrackerEndcapHits"],
            OutputLevel = INFO
        )

    else:
        return MuonCVXDDigitiser(
            "TrackerEndcapDigitiser",
            OutputLevel=INFO,
            ChargeDigitizeBinning=1,
            ChargeDigitizeNumBits=4,
            ChargeMaximum=60000.,
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
            SimHitLocCollectionName=["TrackerEndcapRawHits"],
            OutputCollectionName=["TrackerEndcapHits"],
            PixelSizeX="0.050",
            PixelSizeY="10.0",
            PoissonSmearing=1,
            RelationColName=["TrackerEndcapHitsRelations"],
            ReadoutName="SiTrackerEndcapHits",
            RawHitsLinkColName=["TrackerEndcapRawHitRelations"],
            SegmentLength=0.005,
            SensorThickness=0.300,
            StoreFiredPixels=0,
            SubDetectorName="SiTrackerEndcap",
            TanLorentz=0.8,
            TanLorentzY=0.0,
            Threshold=500,
            ThresholdSmearSigma=25,
            TimeDigitizeBinning=0,
            TimeDigitizeNumBits=10,
            TimeMaximum=15.0,
            TimeSmearingSigma=0.03,
            LayerIDs=[1, 2, 3, 4]
        )


def new_TrackerForward(args):
    """                                                                                                                                                                                
    Create a new tracker forward digitiser instance with the given parameters.                                                                                                          
    """
    if args.doOverlayFull:
        inputHitCollections = ["OverlayTrackerForwardCollection"]
    else:
        inputHitCollections = ["SiTrackerForwardHits"]

    if args.doTrkDigiSimple:
        return DDPlanarDigi(
            "TrackerForwardDigitiser",
            CorrectTimesForPropagation = True,
            IsStrip = False,
            ResolutionT = [0.0],
            ResolutionU = [0.007],
            ResolutionV = [0.09],
            SubDetectorName = "SiTrackerForward",
            TimeWindowMax = [0.3],
            TimeWindowMin = [-0.18],
            UseTimeWindow = False,
            SimTrackHitCollectionName = inputHitCollections,
            SimTrkHitRelCollection = ["TrackerForwardHitsRelations"],
            TrackerHitCollectionName = ["TrackerForwardHits"],
            OutputLevel = INFO
        )

    else:
        return MuonCVXDDigitiser(
            "TrackerForwardDigitiser",
            OutputLevel=INFO,
            ChargeDigitizeBinning=1,
            ChargeDigitizeNumBits=4,
	    ChargeMaximum=60000.,
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
            SimHitLocCollectionName=["TrackerForwardRawHits"],
            OutputCollectionName=["TrackerForwardHits"],
            PixelSizeX="0.020",
            PixelSizeY="0.020",
            PoissonSmearing=1,
            RelationColName=["TrackerForwardHitsRelations"],
            ReadoutName="SiTrackerForwardHits",
            RawHitsLinkColName=["TrackerForwardRawHitRelations"],
            SegmentLength=0.005,
            SensorThickness=0.020,
            StoreFiredPixels=0,
            SubDetectorName="SiTrackerForward",
            TanLorentz=0.8,
            TanLorentzY=0.0,
            Threshold=500,
            ThresholdSmearSigma=25,
            TimeDigitizeBinning=0,
            TimeDigitizeNumBits=10,
            TimeMaximum=15.0,
            TimeSmearingSigma=0.03,
            LayerIDs=[1, 2, 3]
        )
