import uproot
from hnl_mva_tools import *

if __name__ == '__main__':

    ntuples = read_json_file("cfg/ntuples.json")
    histograms = read_json_file("cfg/histograms.json")
    treename = "final_tree"

    stree = uproot.open(ntuples["signal"][0])[treename]
    btrees = [uproot.open(bfn)[treename] for bfn in ntuples["background"]]

    weight_name = "tot_weight"

    for histo in histograms:
        column_name = histo["column_name"]
        nbins = histo["nbins"]
        xlow = histo["xlow"]
        xhigh = histo["xhigh"]
        xlabel = histo["xlabel"]
        plot(column_name,weight_name,stree,btrees,nbins,xlow,xhigh,xlabel)

