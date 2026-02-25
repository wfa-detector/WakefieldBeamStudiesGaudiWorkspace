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
output_file = "hist_rz_output.root"

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

    # Save output
    fout = ROOT.TFile(output_file, "RECREATE")
    h_rz.Write()
    fout.Close()

    print("Saved:", output_file)


if __name__ == "__main__":
    main()
