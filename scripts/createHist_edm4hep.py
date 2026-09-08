#!/usr/bin/env python3

import ROOT
import sys
import os
import math

# -------------------------
# Configuration
# -------------------------
tree_name = "events"                     # EDM4hep default tree
collections = ["SiVertexBarrelHits","SiVertexEndcapHits","SiTrackerBarrelHits","SiTrackerEndcapHits", "SiTrackerForwardHits", "ECalBarrelCollection", "ECalEndcapCollection", "HCalBarrelCollection", "HCalEndcapCollection", "MuonBarrelHits", "MuonEndcapHits"]
output_file = "hist_egun20GeV_sim_SiD.edm4hep.root"

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
        print(f"Analyzing file... {f}")
        chain.Add(f)

    print("Total events:", chain.GetEntries())

    # Create R vs Z histogram
    h_theta = ROOT.TH1F("h_simhits_theta","SimHits;#theta [radians];Entries",500,0,5)
    h_tracker_rz = ROOT.TH2F("h_tracker_rz", "SimHits;Z [mm];R [mm]", 1000, -2500, 2500, 800, 0, 1600)
    h_full_rz = ROOT.TH2F("h_full_rz", "SimHits;Z [mm];R [mm]", 4000, -10000, 10000, 5000, 0, 10000)
    h_vxb_edep = ROOT.TH1F("h_vxb_edep","Vertex Barrel SimHits;Energy deposited [KeV];Entries",1000,0,1000)
    h_vxe_edep = ROOT.TH1F("h_vxe_edep","Vertex Endcap SimHits;Energy deposited [KeV];Entries",1000,0,1000)
    h_tkb_edep = ROOT.TH1F("h_tkb_edep","Tracker Barrel SimHits;Energy deposited [KeV];Entries",1000,0,1000)
    h_tke_edep = ROOT.TH1F("h_tke_edep","Tracker Endcap SimHits;Energy deposited [KeV];Entries",1000,0,1000)
    h_tkf_edep = ROOT.TH1F("h_tkf_edep","Tracker Forward SimHits;Energy deposited [KeV];Entries",1000,0,1000)
    h_vxb_thetaedep = ROOT.TH2F("h_vxb_thetaEdep", "SimHits;#theta [radians];Energy deposited [KeV]", 500, 0, 5, 1000, 0, 1000)
    h_vxe_thetaedep = ROOT.TH2F("h_vxe_thetaEdep", "SimHits;#theta [radians];Energy deposited [KeV]", 500, 0, 5, 1000, 0, 1000)
    h_tkb_thetaedep = ROOT.TH2F("h_tkb_thetaEdep", "SimHits;#theta [radians];Energy deposited [KeV]", 500, 0, 5, 1000, 0, 1000)
    h_tke_thetaedep = ROOT.TH2F("h_tke_thetaEdep", "SimHits;#theta [radians];Energy deposited [KeV]", 500, 0, 5, 1000, 0, 1000)
    h_tkf_thetaedep = ROOT.TH2F("h_tkf_thetaEdep", "SimHits;#theta [radians];Energy deposited [KeV]", 500, 0, 5, 1000, 0, 1000)
    h_vxb_redep = ROOT.TH2F("h_vxb_rEdep", "SimHits;#theta [radians];r [mm]", 500, 0, 5, 2000, 0, 2000)
    h_vxe_redep = ROOT.TH2F("h_vxe_rEdep", "SimHits;#theta [radians];r [mm]", 500, 0, 5, 2000, 0, 2000)
    h_tkb_redep = ROOT.TH2F("h_tka_rEdep", "SimHits;#theta [radians];r [mm]", 500, 0, 5, 2000, 0, 2000)
    h_tke_redep = ROOT.TH2F("h_tkd_rEdep", "SimHits;#theta [radians];r [mm]", 500, 0, 5, 2000, 0, 2000)
    h_tkf_redep = ROOT.TH2F("h_tke_rEdep", "SimHits;#theta [radians];r [mm]", 500, 0, 5, 2000, 0, 2000)
    h_vxb_zedep = ROOT.TH2F("h_vxb_zEdep", "SimHits;z [mm];#theta [radians]", 2000, 0, 2000, 500, 0, 5)
    h_vxe_zedep = ROOT.TH2F("h_vxe_zEdep", "SimHits;z [mm];#theta [radians]", 2000, 0, 2000, 500, 0, 5)
    h_tkb_zedep = ROOT.TH2F("h_tka_zEdep", "SimHits;z [mm];#theta [radians]", 2000, 0, 2000, 500, 0, 5)
    h_tke_zedep = ROOT.TH2F("h_tkd_zEdep", "SimHits;z [mm];#theta [radians]", 2000, 0, 2000, 500, 0, 5)
    h_tkf_zedep = ROOT.TH2F("h_tke_zEdep", "SimHits;z [mm];#theta [radians]", 2000, 0, 2000, 500, 0, 5)
    h_vxb_time = ROOT.TH1F("h_vxb_hitTime","SimHits;Time [ns];Entries",10000,0,1000)
    h_vxe_time = ROOT.TH1F("h_vxe_hitTime","SimHits;Time [ns];Entries",1000,0,1000)
    h_tkb_time = ROOT.TH1F("h_tkb_hitTime","SimHits;Time [ns];Entries",1000,0,1000)
    h_tke_time = ROOT.TH1F("h_tke_hitTime","SimHits;Time [ns];Entries",1000,0,1000)
    h_tkf_time = ROOT.TH1F("h_tkf_hitTime","SimHits;Time [ns];Entries",1000,0,1000)
    h_calDen = ROOT.TH2F("h_calDensity_theta", "SimHits;#theta [radians]; Simulated hit energy density [MeV/cm^{2}]", 50, 0, 5, 1000, 0, 10)

    wt = 150
    
    # Loop over events
    for event in chain:
        for collection_name in collections:

            if not event.GetListOfBranches().FindObject(collection_name):
                print(f"Skipping missing collection: {collection_name}")
                continue
            hits = getattr(event, collection_name)
            
            for hit in hits:
                x = hit.position.x
                y = hit.position.y
                z = hit.position.z                
                r = math.sqrt(x*x + y*y)
                h_full_rz.Fill(z, r, wt)
                lvec = ROOT.TLorentzVector()
                lvec.SetXYZT(x,y,z,0) # x,y,z in metres, time doesn't matter
                h_theta.Fill(lvec.Theta(), wt)
                
                if collection_name == "SiVertexBarrelHits":
                    h_vxb_edep.Fill(hit.eDep*1000000, wt) #in KeV
                    h_tracker_rz.Fill(z,r, wt)
                    h_vxb_thetaedep.Fill(lvec.Theta(),hit.eDep*1000000, wt)
                    h_vxb_zedep.Fill(z*1000,hit.eDep*1000000, wt) #z in mm
                    h_vxb_redep.Fill(hit.eDep*1000000, r*1000, wt) #r in mm
                    if r<0.02: #first barrel layer
                        h_vxb_time.Fill(hit.time, wt)
                if collection_name == "SiVertexEndcapHits":
                    h_vxe_edep.Fill(hit.eDep*1000000, wt) #in KeV
                    h_tracker_rz.Fill(z,r, wt)
                    h_vxe_thetaedep.Fill(lvec.Theta(),hit.eDep*1000000, wt)
                    h_vxe_zedep.Fill(z*1000,hit.eDep*1000000, wt) #z in mm                                                                                                             
                    h_vxe_redep.Fill(hit.eDep*1000000, r*1000, wt) #r in mm
                    h_vxe_time.Fill(hit.time, wt)
                if collection_name == "SiTrackerBarrelHits":
                    h_tkb_edep.Fill(hit.eDep*1000000, wt) #in KeV
                    h_tracker_rz.Fill(z,r, wt)
                    h_tkb_thetaedep.Fill(lvec.Theta(),hit.eDep*1000000, wt)
                    h_tkb_zedep.Fill(z*1000,hit.eDep*1000000, wt) #z in mm                                                                                                             
                    h_tkb_redep.Fill(hit.eDep*1000000, r*1000, wt) #r in mm
                    h_tkb_time.Fill(hit.time, wt)
                if collection_name == "SiTrackerEndcapHits":
                    h_tke_edep.Fill(hit.eDep*1000000, wt) #in KeV
                    h_tracker_rz.Fill(z,r, wt)
                    h_tke_thetaedep.Fill(lvec.Theta(),hit.eDep*1000000, wt)
                    h_tke_zedep.Fill(z*1000,hit.eDep*1000000, wt) #z in mm                                                                                                             
                    h_tke_redep.Fill(hit.eDep*1000000, r*1000, wt) #r in mm
                    h_tke_time.Fill(hit.time, wt)
                if collection_name == "SiTrackerForwardHits":
                    h_tkf_edep.Fill(hit.eDep*1000000, wt) #in KeV
                    h_tracker_rz.Fill(z,r, wt)
                    h_tkf_thetaedep.Fill(lvec.Theta(),hit.eDep*1000000, wt)
                    h_tkf_zedep.Fill(z*1000,hit.eDep*1000000, wt) #z in mm
                    h_tkf_redep.Fill(hit.eDep*1000000, r*1000, wt) #r in mm
                    h_tkf_time.Fill(hit.time, wt)
                if "Cal" in collection_name:
                    eDensity = 0.
                    if "ECAL" in collection_name:
                        edensity = (hit.energy*1000*1000)/(5.1*5.1*0.5) #energy in MeV per cm^3 volume of ecal cell
                    else:
                        edensity = (hit.energy*1000*1000)/(30*30*3) #energy in MeV per cm^3 volume of hcal cell
                    h_calDen.Fill(lvec.Theta(),edensity,wt)
                    
    # Save output
    fout = ROOT.TFile(output_file, "RECREATE")
    h_tracker_rz.Write()
    h_full_rz.Write()
    h_vxb_edep.Write()
    h_vxe_edep.Write()
    h_tkb_edep.Write()
    h_tke_edep.Write()
    h_tkf_edep.Write()
    h_theta.Write()
    h_vxb_thetaedep.Write()
    h_vxe_thetaedep.Write()
    h_tkb_thetaedep.Write()
    h_tke_thetaedep.Write()
    h_tkf_thetaedep.Write()
    h_vxb_redep.Write()
    h_vxb_zedep.Write()
    h_vxe_redep.Write()
    h_vxe_zedep.Write()
    h_tkb_redep.Write()
    h_tkb_zedep.Write()
    h_tke_redep.Write()
    h_tke_zedep.Write()
    h_tkf_redep.Write()
    h_tkf_zedep.Write()
    h_vxb_time.Write()
    h_vxe_time.Write()
    h_tkb_time.Write()
    h_tke_time.Write()
    h_tkf_time.Write()
    h_calDen.Write()

    fout.Close()

    print("Saved:", output_file)


if __name__ == "__main__":
    main()
