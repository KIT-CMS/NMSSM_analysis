import ROOT
import os

path="/ceph/rschmieder/nmssm/friends/2016/et/NNScore_train_all/parametrized_nn_mH1000/NNScore_workdir/NNScore_collected/"
dicts=os.listdir(path)
maxind="et_max_index"

for proc in dicts:
    # if "DY" in proc or "EWK" in proc:
    #     print(proc)
    rfile = ROOT.TFile(path+proc+"/"+proc+".root","READ")
    histlist=rfile.GetListOfKeys()
    for hist in histlist:
        tree=rfile.Get(hist.GetName()+"/ntuple")               
        leaf_list=tree.GetListOfLeaves()
        drin=False
        for leaf in leaf_list:
            if maxind in leaf.GetName():
                drin=True
        if drin==False:
            print(hist)


