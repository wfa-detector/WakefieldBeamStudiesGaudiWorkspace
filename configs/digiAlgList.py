from GaudiKernel.Constants import INFO, WARNING

def makeDigiAlgList(the_args):
    '''-------------------------------------------------------------'''
    '''    Add the Digitization Algorithms to the Algorithm List    '''
    '''-------------------------------------------------------------'''
    algList = []
    # BIB Overlay
    if the_args.doOverlayFull:
        from digi_components.overlay_full import new_overlay_full
        algList.append(new_overlay_full(the_args))

    # Tracker Digitization
    from digi_components.SiVertex import new_VertexBarrel, new_VertexEndcap
    from digi_components.SiTracker import new_TrackerBarrel, new_TrackerEndcap, new_TrackerForward
    algList.append(new_VertexBarrel(the_args))
    algList.append(new_VertexEndcap(the_args))
    algList.append(new_TrackerBarrel(the_args))
    algList.append(new_TrackerEndcap(the_args))
    algList.append(new_TrackerForward(the_args))

    # EM, Hadronic, Muon Calorimeter Digitization
    from digi_components.calorimetry_EM import new_ECalBarrelDigi, new_ECalBarrelReco
    from digi_components.calorimetry_EM import new_ECalPlugDigi, new_ECalPlugReco
    from digi_components.calorimetry_EM import new_ECalEndcapDigi, new_ECalEndcapReco
    algList.append(new_ECalBarrelDigi(the_args))
    algList.append(new_ECalBarrelReco())
    #algList.append(new_ECalPlugDigi(the_args))
    #algList.append(new_ECalPlugReco())
    algList.append(new_ECalEndcapDigi(the_args))
    algList.append(new_ECalEndcapReco())
    from digi_components.calorimetry_HAD import new_HCalBarrelDigi, new_HCalBarrelReco
    from digi_components.calorimetry_HAD import new_HCalEndcapDigi, new_HCalEndcapReco
    from digi_components.calorimetry_HAD import new_HCalRingDigi, new_HCalRingReco
    algList.append(new_HCalBarrelDigi(the_args))
    algList.append(new_HCalBarrelReco())
    algList.append(new_HCalEndcapDigi(the_args))
    algList.append(new_HCalEndcapReco())
    #algList.append(new_HCalRingDigi(the_args))
    #algList.append(new_HCalRingReco())
    from digi_components.calorimetry_MU import new_MuonBarrelDigi, new_MuonEndcapDigi
    algList.append(new_MuonBarrelDigi(the_args))
    algList.append(new_MuonEndcapDigi(the_args))

    return algList
