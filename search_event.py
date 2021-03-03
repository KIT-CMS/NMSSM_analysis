import ROOT

dyfiles = [
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DY1JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v2/DY1JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v2.root",
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DY1JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1/DY1JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1.root",
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DY2JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v2/DY2JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v2.root",
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DY2JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1/DY2JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1.root",
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DY3JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v1/DY3JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v1.root",
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DY3JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1/DY3JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1.root",
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DY4JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v2/DY4JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v2.root",
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DYJetsToLLM10to50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v2/DYJetsToLLM10to50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v2.root",
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DYJetsToLLM10to50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1/DYJetsToLLM10to50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1.root",
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DYJetsToLLM50_RunIIFall17MiniAODv2_PU2017RECOSIMstep_13TeV_MINIAOD_madgraph-pythia8_ext1-v1/DYJetsToLLM50_RunIIFall17MiniAODv2_PU2017RECOSIMstep_13TeV_MINIAOD_madgraph-pythia8_ext1-v1.root",
    "/ceph/jbechtel/nmssm/ntuples/2017/et/DYJetsToLLM50_RunIIFall17MiniAODv2_PU2017RECOSIMstep_13TeV_MINIAOD_madgraph-pythia8_v1/DYJetsToLLM50_RunIIFall17MiniAODv2_PU2017RECOSIMstep_13TeV_MINIAOD_madgraph-pythia8_v1.root"
] 

for file_ in dyfiles:
    #print(file_)
    rfile = ROOT.TFile(file_,"READ")
    tree = rfile.Get("et_nominal/ntuple")
    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        #print(tree.event)
        if tree.pt_1>45. and tree.pt_1<50.:
            if tree.pt_2>40. and tree.pt_2<45.:
                if tree.m_vis>72. and tree.m_vis<80.:
                    if tree.ptvis>45. and tree.ptvis<50.:
                        if tree.njets>-0.5 and tree.njets<0.5:
                            if tree.bpt_bReg_1>20. and tree.bpt_bReg_1<30.:
                                #if tree.bpt_bReg_2>170. and tree.bpt_bReg_2<180.:
                                    
                                if tree.pt_bb_highCSV_bReg>40. and tree.pt_bb_highCSV_bReg<60.:
                                    if tree.m_ttvisbb_highCSV_bReg>325. and tree.m_ttvisbb_highCSV_bReg<350.:
                                        print(tree.event) 


(generatorWeight)*(puweight)*(idWeight_1*idWeight_2)*(isoWeight_1*isoWeight_2)*(trackWeight_1*trackWeight_2)*(eleTauFakeRateWeight*muTauFakeRateWeight)*(((trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27)*(singleTriggerDataEfficiencyWeightKIT_1/singleTriggerMCEfficiencyWeightKIT_1)+(pt_1>25 && pt_1<28 && trg_crossele_ele24tau30)*(crossTriggerDataEfficiencyWeight_1*((byMediumDeepTau2017v2p1VSjet_2<0.5 && byVVVLooseDeepTau2017v2p1VSjet_2>0.5)*crossTriggerDataEfficiencyWeight_vloose_DeepTau_2 + (byMediumDeepTau2017v2p1VSjet_2>0.5)*crossTriggerDataEfficiencyWeight_medium_DeepTau_2)/(crossTriggerMCEfficiencyWeight_1*((byMediumDeepTau2017v2p1VSjet_2<0.5 && byVVVLooseDeepTau2017v2p1VSjet_2>0.5)*crossTriggerMCEfficiencyWeight_vloose_DeepTau_2 + (byMediumDeepTau2017v2p1VSjet_2>0.5)*crossTriggerMCEfficiencyWeight_medium_DeepTau_2)+(1.0)*(!(pt_1>25 && pt_1<28 && trg_crossele_ele24tau30))))))*(((gen_match_2 == 5)*tauIDScaleFactorWeight_tight_DeepTau2017v2p1VSjet_2 + (gen_match_2 != 5)))*((trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27 || trg_crossele_ele24tau30)*0.991 + (!(trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27 || trg_crossele_ele24tau30))*1.0)*(1.0)*(prefiringweight)*(41.529 * 1000.0)*(((genbosonmass >= 50.0)*6.2139e-05*((npartons == 0 || npartons >= 5)*1.0 + (npartons == 1)*0.1743 + (npartons == 2)*0.3556 + (npartons == 3)*0.2273 + (npartons == 4)*0.2104) + (genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight)*(zPtReweightWeight)


#ntuple->Scan("(generatorWeight)*(puweight)*(idWeight_1*idWeight_2)*(isoWeight_1*isoWeight_2)*(trackWeight_1*trackWeight_2)*(eleTauFakeRateWeight*muTauFakeRateWeight)*(trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27)*(singleTriggerDataEfficiencyWeightKIT_1/singleTriggerMCEfficiencyWeightKIT_1)*(gen_match_2 != 5)*((trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27 || trg_crossele_ele24tau30)*0.991)*(1.0)*(prefiringweight)*(41.529 * 1000.0)*(genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight*(zPtReweightWeight)","event == 3831555")

shape_producer.cutstring.Weights
	Weight("generatorWeight" : "generatorWeight")
	Weight("z_stitching_weight" : "((genbosonmass >= 50.0)*6.2139e-05*((npartons == 0 || npartons >= 5)*1.0 + (npartons == 1)*0.1743 + (npartons == 2)*0.3556 + (npartons == 3)*0.2273 + (npartons == 4)*0.2104) + (genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight)")
	Weight("puweight" : "puweight")
	Weight("idweight" : "idWeight_1*idWeight_2")
	Weight("isoweight" : "isoWeight_1*isoWeight_2")
	Weight("trackweight" : "trackWeight_1*trackWeight_2")
	Weight("triggerweight" : "((trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27)*singleTriggerDataEfficiencyWeightKIT_1+(pt_1>25 && pt_1<28 && trg_crossele_ele24tau30)*crossTriggerDataEfficiencyWeight_1*((byMediumDeepTau2017v2p1VSjet_2<0.5 && byVVVLooseDeepTau2017v2p1VSjet_2>0.5)*crossTriggerDataEfficiencyWeight_vloose_DeepTau_2 + (byMediumDeepTau2017v2p1VSjet_2>0.5)*crossTriggerDataEfficiencyWeight_medium_DeepTau_2))/((trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27)*singleTriggerMCEfficiencyWeightKIT_1+(pt_1>25 && pt_1<28 && trg_crossele_ele24tau30)*crossTriggerMCEfficiencyWeight_1*((byMediumDeepTau2017v2p1VSjet_2<0.5 && byVVVLooseDeepTau2017v2p1VSjet_2>0.5)*crossTriggerMCEfficiencyWeight_vloose_DeepTau_2 + (byMediumDeepTau2017v2p1VSjet_2>0.5)*crossTriggerMCEfficiencyWeight_medium_DeepTau_2))")
	Weight("leptonTauFakeRateWeight" : "eleTauFakeRateWeight*muTauFakeRateWeight")
	Weight("taubyIsoIdWeight" : "((gen_match_2 == 5)*tauIDScaleFactorWeight_medium_DeepTau2017v2p1VSjet_2 + (gen_match_2 != 5))")
	Weight("eleHLTZvtxWeight" : "(trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27 || trg_crossele_ele24tau30)*0.991 + (!(trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27 || trg_crossele_ele24tau30))*1.0")
	Weight("zPtReweightWeight" : "zPtReweightWeight")
	Weight("prefireWeight" : "prefiringweight")
	Weight("lumi" : "41529.0")

ntuple->Scan("(generatorWeight)*(puweight)*(idWeight_1*idWeight_2)*(isoWeight_1*isoWeight_2)*(trackWeight_1*trackWeight_2)*((genbosonmass >= 50.0)*6.2139e-05*((npartons == 0 || npartons >= 5)*1.0 + (npartons == 1)*0.1743 + (npartons == 2)*0.3556 + (npartons == 3)*0.2273 + (npartons == 4)*0.2104) + (genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight)*((trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27)*singleTriggerDataEfficiencyWeightKIT_1+(pt_1>25 && pt_1<28 && trg_crossele_ele24tau30)*crossTriggerDataEfficiencyWeight_1*((byMediumDeepTau2017v2p1VSjet_2<0.5 && byVVVLooseDeepTau2017v2p1VSjet_2>0.5)*crossTriggerDataEfficiencyWeight_vloose_DeepTau_2 + (byMediumDeepTau2017v2p1VSjet_2>0.5)*crossTriggerDataEfficiencyWeight_medium_DeepTau_2))/((trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27)*singleTriggerMCEfficiencyWeightKIT_1+(pt_1>25 && pt_1<28 && trg_crossele_ele24tau30)*crossTriggerMCEfficiencyWeight_1*((byMediumDeepTau2017v2p1VSjet_2<0.5 && byVVVLooseDeepTau2017v2p1VSjet_2>0.5)*crossTriggerMCEfficiencyWeight_vloose_DeepTau_2 + (byMediumDeepTau2017v2p1VSjet_2>0.5)*crossTriggerMCEfficiencyWeight_medium_DeepTau_2))*eleTauFakeRateWeight*muTauFakeRateWeight*((gen_match_2 == 5)*tauIDScaleFactorWeight_medium_DeepTau2017v2p1VSjet_2 + (gen_match_2 != 5))*((trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27 || trg_crossele_ele24tau30)*0.991 + (!(trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27 || trg_crossele_ele24tau30))*1.0)*zPtReweightWeight*prefiringweight*41529.0","event == 3831555")

ntuple->Scan("1.0*zPtReweightWeight*prefiringweight*41529.0","event == 3831555")
