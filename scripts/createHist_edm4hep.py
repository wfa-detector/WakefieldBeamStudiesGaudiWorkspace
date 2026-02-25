#!/usr/bin/env python3

import ROOT
import sys
import os
import math

# -------------------------
# Configuration
# -------------------------
tree_name = "events"                     # EDM4hep default tree
collections = ["SiVertexBarrelHits","SiVertexEndcapHits","SiTrackerBarrelHits","SiTrackerEndcapHits", "SiTrackerForwardHits"]
output_file = "hist_output.root"

# Histogram settings
nbins_z = 1000
zmin = -2500
zmax = 2500

nbins_r = 800
rmin = 0
rmax = 1600
# -------------------------


def get_root_files(path):
    if os.path.isfile(path) and path.endswith(".root"):
        return [path]
    elif os.path.isdir(path):
        return [os.path.join(path, f)
                for f in os.listdir(path)
                if f.endswith(".root")]
    else:
        print("Invalid input path")
        sys.exit(1)


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python createHist_edm4hep.py file.root")
        print("  python createHist_edm4hep.py /path/to/folder/")
        sys.exit(1)

    input_path = sys.argv[1]
    files = get_root_files(input_path)

    chain = ROOT.TChain(tree_name)
    for f in files:
        chain.Add(f)

    print("Total events:", chain.GetEntries())

    # Create R vs Z histogram
    h_rz = ROOT.TH2F("h_rz", "SimHits;Z [mm];R [mm]",
                     nbins_z, zmin, zmax,
                     nbins_r, rmin, rmax)
    h_vxb_edep = ROOT.TH1F("h_vxb_edep","Vertex Barrel SimHits;Energy deposited [KeV];Entries",1000,0,1000)
    h_vxe_edep = ROOT.TH1F("h_vxe_edep","Vertex Endcap SimHits;Energy deposited [KeV];Entries",1000,0,1000)
    h_tkb_edep = ROOT.TH1F("h_tkb_edep","Tracker Barrel SimHits;Energy deposited [KeV];Entries",1000,0,1000)
    h_tke_edep = ROOT.TH1F("h_tke_edep","Tracker Endcap SimHits;Energy deposited [KeV];Entries",1000,0,1000)
    h_tkf_edep = ROOT.TH1F("h_tkf_edep","Tracker Forward SimHits;Energy deposited [KeV];Entries",1000,0,1000)

    
    # Loop over events
    for event in chain:
        for collection_name in collections:
            hits = getattr(event, collection_name)

            for hit in hits:
                x = hit.position.x
                y = hit.position.y
                z = hit.position.z
                
                r = math.sqrt(x*x + y*y)
                
                h_rz.Fill(z, r)

                if collection_name == "SiVertexBarrel":
                    h_vxb_edep.Fill(hit.eDep*1000000) #in KeV
                if collection_name == "SiVertexEndcap":
                    h_vxe_edep.Fill(hit.eDep*1000000) #in KeV
                if collection_name == "SiTrackerBarrel":
                    h_tkb_edep.Fill(hit.eDep*1000000) #in KeV
                if collection_name == "SiTrackerEndcap":
                    h_tke_edep.Fill(hit.eDep*1000000) #in KeV
                if collection_name == "SiTrackerForward":
                    h_tkf_edep.Fill(hit.eDep*1000000) #in KeV
                    
    # Save output
    fout = ROOT.TFile(output_file, "RECREATE")
    h_rz.Write()
    h_vxb_edep.Write()
    h_vxe_edep.Write()
    h_tkb_edep.Write()
    h_tke_edep.Write()
    h_tkf_edep.Write()

    fout.Close()

    print("Saved:", output_file)


if __name__ == "__main__":
    main()
