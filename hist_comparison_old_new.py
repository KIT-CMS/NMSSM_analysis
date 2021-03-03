import ROOT
import numpy as np
import matplotlib.pyplot as pyplot
import argparse
import Dumbledraw.dumbledraw as dd
import Dumbledraw.styles as styles
import yaml
import logging
import os
logger = logging.getLogger("")

def setup_logging(output_file, level=logging.DEBUG):
    logger.setLevel(level)
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    file_handler = logging.FileHandler(output_file, "w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

#arguments: era and channel
parser = argparse.ArgumentParser(description='compare histograms in old and new framework in nmssm analysis')
parser.add_argument(       
        "--era",
        required=True,
        type=str,
        help="Experiment era."
)
parser.add_argument(       
        "--channel",
        required=True,
        type=str,
        help="Channel to be considered."
)

parser.add_argument(       
        "--analysis-shapes",
        required=False,
        action="store_true",
        help="If true NMSSM analysis shapes are considered"
)

parser.add_argument(       
        "--nominals",
        required=False,
        action="store_true",
        help="If true only nominal shapes are considered"
)



args = parser.parse_args()

# variables=[
#         "pt_1",
#         "pt_2",
#         "m_vis",
#         "ptvis",
#         "m_sv_puppi",
#         "jpt_1",
#         "njets",
#         "jdeta",
#         "mjj",
#         "dijetpt",
#         "bpt_bReg_1",
#         "bpt_bReg_2",
#         "jpt_2",
#         "mbb_highCSV_bReg",
#         "pt_bb_highCSV_bReg",
#         "m_ttvisbb_highCSV_bReg",
#         "kinfit_mH",
#         "kinfit_mh2",
#         "kinfit_chi2",
#         "nbtag",
#         "bm_bReg_1",
#         "bm_bReg_2",
#         "bcsv_1",
#         "bcsv_2",
#         "highCSVjetUsedFordiBJetSystemCSV"
#         "{channel}_max_score".format(channel=args.channel)
# ]

#setup_logging("ratio_plot.log", logging.DEBUG)
variables=["{ch}_max_score".format(ch=args.channel)]
#variables=["pt_1"]
hist_ratios=np.array([])
#rfile_new = ROOT.TFile("/work/rschmieder/nmssm_newframework/nmssm_newframework_analysis/output/et16/shapes-analysis-{era}-{channel}.root".format(era=args.era, channel=args.channel),"READ")
#rfile_new = ROOT.TFile("/work/rschmieder/nmssm_newframework/nmssm_newframework_analysis/output/et16/shapes-analysis-{era}-{channel}.root".format(era=args.era, channel=args.channel),"READ")
nn_categories=["emb",
                "tt",
                "misc",
                "ff",
                "NMSSM_MH500_3"
                ]

dms=[0, 1, 10, 11] 

ff_variations_lt=["ff_tt_morphedChannel_Era_",
                "ff_tt_sfChannel_Era_",
                "ff_corr_tt_syst_Channel_Era_",
                "ff_frac_w_Channel_Era_",
                "ff_qcd_dm0_njet0_morphed_stat_Channel_Era_", 
                "ff_qcd_dm0_njet1_morphed_stat_Channel_Era_", 
                "ff_qcd_dm0_njet2_morphed_stat_Channel_Era_", 
                "ff_w_dm0_njet0_morphed_stat_Channel_Era_", 
                "ff_w_dm0_njet1_morphed_stat_Channel_Era_", 
                "ff_w_dm0_njet2_morphed_stat_Channel_Era_",
                "ff_tt_dm0_njet0_morphed_stat_Channel_Era_", 
                "ff_tt_dm0_njet1_morphed_stat_Channel_Era_",
                "ff_w_lepPt_Channel_Era_",
                "ff_corr_w_lepPt_Channel_Era_",
                "ff_w_mc_Channel_Era_",
                "ff_corr_w_mt_Channel_Era_",
                "ff_w_mt_Channel_Era_",
                "ff_qcd_mvis_Channel_Era_",
                "ff_qcd_mvis_osss_Channel_Era_",
                "ff_corr_qcd_mvis_Channel_Era_",
                "ff_corr_qcd_mvis_osss_Channel_Era_",
                "ff_corr_qcd_muiso_Channel_Era_",
                "ff_qcd_mc_Channel_Era_",
                "CMS_prefiring",
                "CMS_htt_dyShape_Era",
                "CMS_htt_ttbarShape",
                "CMS_scale_j_Absolute",
                "CMS_scale_j_Absolute_Era",
                "CMS_scale_j_BBEC1",
                "CMS_scale_j_BBEC1_Era",
                "CMS_scale_j_EC2",
                "CMS_scale_j_EC2_Era",
                "CMS_scale_j_HF",
                "CMS_scale_j_HF_Era",
                "CMS_scale_j_FlavorQCD",
                "CMS_scale_j_RelativeBal",
                "CMS_scale_j_RelativeSample_Era",
                "CMS_res_j_Era",
                "CMS_scale_met_unclustered",
                "CMS_htt_boson_res_met_Era",
                "CMS_htt_boson_scale_met_Era",
                "CMS_htt_eff_b_Era",
                "CMS_htt_mistag_b_Era",
]


electron=["CMS_fake_e_BA_{era}".format(era=args.era),
        "CMS_fake_e_EC_{era}".format(era=args.era)
]

electron_ZL=["CMS_ZLShape_et_1prong_barrel_Era",
        "CMS_ZLShape_et_1prong_endcap_Era",
        "CMS_ZLShape_et_1prong1pizero_barrel_Era",
        "CMS_ZLShape_et_1prong1pizero_endcap_Era",
        ]

mt_fake=["WH1","WH2","WH3","WH4","WH5"]


muon_ZL=["CMS_ZLShape_mt_1prong_Era",
        "CMS_ZLShape_mt_1prong1pizero_Era"        
]

muon_fake=["CMS_fake_m_{wh}_{era}".format(wh=wh,era=args.era) for wh in mt_fake] 
muon=muon_fake+["ff_qcd_muisoChannel_Era_"]
ff_variations_tt=[# "ff_qcd_syst",
                # "ff_qcd_dm0_njet0{ch}_stat{era}{shift}",
                # "ff_qcd_dm0_njet1{ch}_stat{era}{shift}",
                # "ff_qcd_dm0_njet0_morphed_stat", 
                # "ff_qcd_dm0_njet1_morphed_stat", 
                # "ff_qcd_dm0_njet2_morphed_stat",
                # "ff_w_syst",
                # "ff_tt_syst",
                # # "ff_w_frac_syst",
                # # "ff_tt_frac_syst",
                # "ff_qcd_mvis",
                # "ff_qcd_mvis_osss",
                # "ff_corr_qcd_mvis",
                # "ff_corr_qcd_mvis_osss",
                # "ff_qcd_tau2_pt",
                # "ff_corr_qcd_tau2_pt",
                # "ff_qcd_mc",
                "CMS_prefiring",
                "CMS_htt_dyShape_Era",
                #"CMS_htt_ttbarShape",
                "CMS_scale_j_Absolute",
                "CMS_scale_j_Absolute_Era",
                "CMS_scale_j_BBEC1",
                "CMS_scale_j_BBEC1_Era",
                "CMS_scale_j_EC2",
                "CMS_scale_j_EC2_Era",
                "CMS_scale_j_HF",
                "CMS_scale_j_HF_Era",
                "CMS_scale_j_FlavorQCD",
                "CMS_scale_j_RelativeBal",
                "CMS_scale_j_RelativeSample_Era",
                "CMS_res_j_Era",
                "CMS_scale_met_unclustered",
                "CMS_htt_boson_res_met_Era",
                "CMS_htt_boson_scale_met_Era",
                "CMS_htt_fake_j_Era",
                "CMS_htt_eff_b_Era",
                "CMS_htt_mistag_b_Era",
                "CMS_htt_fake_j_Era"    
        ]
        
ff_variations_tt=ff_variations_tt+["CMS_eff_trigger_tt_dm{dm}_Era".format(dm=dm) for dm in dms]+["CMS_eff_trigger_emb_tt_dm{dm}_Era".format(dm=dm) for dm in dms]+["CMS_eff_t_dm{dm}_Era".format(dm=dm) for dm in dms]

tt_prong=["CMS_scale_t_3prong1pizero_Era",
        "CMS_scale_t_1prong_Era",
        "CMS_scale_t_1prong1pizero_Era", ]

tt_emb=["CMS_scale_t_emb_3prong_Era",
        "CMS_scale_t_emb_3prong1pizero_Era",
        "CMS_scale_t_emb_1prong1pizero_Era",
        "CMS_3ProngEff_Era",
        "CMS_1ProngPi0Eff_Era"       
]
tt_emb=tt_emb+[ "CMS_eff_t_emb_dm{dm}_Era".format(dm=dm) for dm in dms]

lt=["CMS_eff_trigger_{ch}_{era}".format(ch=args.channel, era=args.era),
"CMS_eff_xtrigger_l_{ch}_{era}".format(ch=args.channel, era=args.era)
]
lt=lt+["CMS_eff_xtrigger_t_{ch}_dm{dm}_{era}".format(ch=args.channel,dm=dm, era=args.era) for dm in dms]

lt_emb=["CMS_eff_trigger_emb_{ch}_{era}".format(ch=args.channel, era=args.era),
"CMS_eff_xtrigger_l_emb_{ch}_{era}".format(ch=args.channel, era=args.era)
]
lt_emb=lt_emb+["CMS_eff_xtrigger_t_{ch}_dm{dm}_{era}".format(ch=args.channel,dm=dm, era=args.era) for dm in dms]

ggh_var = [
        "THU_ggH_Mig01", "THU_ggH_Mig12", "THU_ggH_Mu", "THU_ggH_PT120",
        "THU_ggH_PT60", "THU_ggH_Res", "THU_ggH_VBF2j", "THU_ggH_VBF3j",
        "THU_ggH_qmtop"
]

qqh_var = ["THU_qqH_25", "THU_qqH_JET01", "THU_qqH_Mjj1000", "THU_qqH_Mjj120",
            "THU_qqH_Mjj1500", "THU_qqH_Mjj350", "THU_qqH_Mjj60", "THU_qqH_Mjj700",
            "THU_qqH_PTH200", "THU_qqH_TOT"
]

shifts=["Up","Down"]
# mass_dict = {
#     "heavy_mass": [240, 280, 320, 360, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2500, 3000],
#     "light_mass_coarse": [60, 70, 80, 90, 100, 120, 150, 170, 190, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800],
#     "light_mass_fine": [60, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 150, 170, 190, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850],
# }
# mass_dict = {
#     "heavy_mass": [320,500,900],
#     "light_mass_fine": [60,85,90,95,100,750],
#     "light_mass_coarse": [60,100,750],
# }

mass_dict = {
    "heavy_mass": [320],
    "light_mass_fine": [60],
    "light_mass_coarse": [60],
}


def light_masses(heavy_mass):
        if heavy_mass > 1001:
            return mass_dict["light_mass_coarse"]
        else:
            return mass_dict["light_mass_fine"]


def all_ratios_one(a):
        if round(max(a),6)==1 and round(min(a),6)==1:
                return 1
        else:
                return 0


def DrawText(x, y, text, textsize=0.03):
        ypos = 0.8
        latex2 = ROOT.TLatex()
        latex2.SetNDC()
        latex2.SetTextAngle(0)
        latex2.SetTextColor(ROOT.kBlack)
        latex2.SetTextSize(textsize)
        latex2.DrawLatex(x, y, text)


def two_hist_plot(hist_old,hist_new,era,channel,variable):
        c =ROOT.TCanvas()
        c.cd()
        integral_old=hist_old.Integral()
        integral_new=hist_new.Integral()
        entries_old=hist_old.GetEntries()
        entries_new=hist_new.GetEntries()
        hist_old.SetLineColor(ROOT.kBlack)
        hist_new.SetLineColor(ROOT.kRed)        
        hist_old.SetStats(0)
        hist_old.SetTitle("{era}-{channel}-{var}".format(era=args.era,channel=args.channel, var=variable))  
        hist_old.SetXTitle("{var} (GeV)".format(var=variable))      
        hist_old.SetYTitle("N_{Events}")
        legend=ROOT.TLegend(.45,.7,0.9,.9)
        legend.SetTextSize(0.03)
        legend.AddEntry(hist_old,"old, entries {ent}, integral {int}".format(ent=entries_old, int=integral_old))
        legend.AddEntry(hist_new,"new, entries {ent}, integral {int}".format(ent=entries_new, int=integral_new))
        hist_old.Draw()
        hist_new.Draw("SAME")        
        legend.Draw()
        #ratio_plot=ROOT.TRatioPlot(hist_old,hist_new)
        #ratio_plot.Draw()
        #DrawText(0.55,0.8,"black:old, Entries {ent}, Integral {int}".format(ent=entries_old, int=integral_old))
        #DrawText(0.55,0.75,"red:new, Entries {ent}, Integral {int}".format(ent=entries_new, int=integral_new))
        c.SaveAs("comparison_hist/check/comparison_{era}_{channel}_{var}.png".format(era=args.era,channel=args.channel, var=variable))
        #raw_input('enter')

def ratio_plot(hist_old,hist_new,era,channel,variable,category,Ratio,nncat):
        integral_old=round(hist_old.Integral(),1)
        integral_new=round(hist_new.Integral(),1)
        entries_old=round(hist_old.GetEntries(),1)
        entries_new=round(hist_new.GetEntries(),1)
        width = 600
        plot = dd.Plot([[0.30, 0.28]], "ModTDR", r=0.04, l=0.14, width=width)
        plot.add_hist(hist_old, "process_name1", "hist_old")
        plot.setGraphStyle("process_name1",
                "hist",
                fillcolor=0,
                linecolor=1)
        plot.add_hist(hist_new, "process_name2", "hist_new")
        plot.setGraphStyle("process_name2",
                "hist",
                fillcolor=0,
                linecolor=2)
                
        # build ratio
        plot.subplot(1).add_hist( "hist_old_ratio")
        plot.subplot(0).get_hist("hist_old")
        plot.subplot(1).add_hist("hist_new_ratio")
        plot.subplot(0).get_hist("hist_new")
        plot.subplot(1).setGraphStyle("hist_old_ratio",
                                "L",
                                linecolor=ROOT.kBlack,
                                linewidth=2)
        plot.subplot(1).setGraphStyle("data_obs", "e0")
        plot.subplot(1).normalize(
        ["hist_old_ratio"],
        "hist_new_ratio")
        plot.subplot(1).setXlabel("{var} (GeV)".format(var=variable))
        plot.subplot(0).setYlabel("Events")
        plot.subplot(1).setYlabel("Ratio")
        if category.find("QCD")>-0.5 and channel=="tt":
                ymin=0.99
                ymax=1.01
        else:
                ymin=0.
                ymax=2.
        plot.subplot(1).setYlims(ymin,ymax)
        plot.scaleYLabelSize(0.75)
        plot.scaleXLabelSize(0.75)
        plot.scaleYTitleSize(0.75)
        plot.scaleXTitleSize(0.75)
        procs_to_draw = ["hist_old", "hist_new"]
        plot.subplot(0).Draw(procs_to_draw)
        plot.subplot(1).Draw(["hist_old_ratio"])
        plot.add_legend(width=0.4, height=0.20, pos=3)
        #plot.legend(0).add_entry(0, "process_name1", "#splitline{#splitline{hist_old}{entries:"+" {entries_old}".format(entries_old=entries_old)+"}}{integral:"+" {integral_old}".format(integral_old=integral_old)+"}", 'l')
        #plot.legend(0).add_entry(0, "process_name2", "#splitline{#splitline{hist_new}{entries:"+" {entries_new}".format(entries_new=entries_new)+"}}{integral:"+" {integral_new}".format(integral_new=integral_new)+"}", 'l')
        plot.legend(0).add_entry(0, "process_name1", "hist_old", 'l')
        plot.legend(0).add_entry(0, "process_name2", "hist_new", 'l')
        plot.legend(0).setNColumns(2)
        plot.legend(0).Draw()
        plot.add_legend(reference_subplot=1, width=0.65, height=0.03, pos=1)
        plot.legend(1).add_entry(1, "hist_old_ratio", "ratio", 'L')
        plot.legend(1).setNColumns(1)
        plot.legend(1).setAlpha(0.0)
        plot.legend(1).Draw()
        # DrawText(0.55,0.8,"old: Entries {ent}, Integral {int}".format(ent=entries_old, int=integral_old))
        # DrawText(0.55,0.75,"new: Entries {ent}, Integral {int}".format(ent=entries_new, int=integral_new))
        # draw additional labels
        plot.DrawCMS()#
        if args.era == "2016":
                plot.DrawLumi("35.9 fb^{-1} (2016, 13 TeV)", textsize=0.5)
        elif args.era == "2017":
                plot.DrawLumi("41.5 fb^{-1} (2017, 13 TeV)", textsize=0.5)
        elif args.era == "2018":
                plot.DrawLumi("59.7 fb^{-1} (2018, 13 TeV)", textsize=0.5)
        else:
                plot.DrawLumi("137.2 fb^{-1} (13 TeV)", textsize=0.5)

        plot.DrawChannelCategoryLabel("{era}-{channel}-{var}-{cat}".format(era=args.era,channel=args.channel, cat=category, nn_cat=nncat,var=variable),textsize=0.03)
        #plot.save("hist_comparison/nn_shapes/{era}_{channel}/ratio_{var}_{cat}_{nn_cat}.png".format(era=args.era, channel=args.channel, cat=category, nn_cat=nncat, var=variable))

        if all_ratios_one(Ratio) == 0:
                plot.save("hist_comparison/diff_hist/ratio_{era}_{channel}_{var}_{cat}.png".format(era=args.era,channel=args.channel,cat=category, var=variable))
        else:
                plot.save("hist_comparison/same_hist/ratio_{era}_{channel}_{var}_{cat}.png".format(era=args.era,channel=args.channel,cat=category, var=variable))



def hist_comp_data_nominal():
        for variable in variables:
                rfile_old=ROOT.TFile("/work/rschmieder/nmssm_oldframework/sm-htt-analysis/output/shapes/{era}_{channel}_{var}/{era}-{era}_{channel}_{var}-{channel}-shapes.root".format(era=args.era, channel=args.channel, var=variable),"READ")        
                hist_old=rfile_old.Get("#{channel}#{channel}_{var}#data_obs#smhtt#Run{era}#{var}#125#".format(era=args.era, channel=args.channel, var=variable))
                hist_new=rfile_new.Get("data#{channel}#Nominal#{var}".format(channel=args.channel, var=variable))
                ratio=np.zeros(hist_old.GetNbinsX()+1)
                for i in range(hist_old.GetNbinsX()+1):        
                        if round(hist_new.GetBinContent(i),6)!=0.0 :
                                ratio[i]=(hist_old.GetBinContent(i)/hist_new.GetBinContent(i))
                        elif round(hist_old.GetBinContent(i),6)==0.0 and round(hist_new.GetBinContent(i),6)==0.0:
                                ratio[i]=1
                        else:
                                ratio[i]=0                        
                ratio_plot(hist_old,hist_new,args.era,args.channel,variable,"data_Nominal")            
        #hist_ratios.append(["{var}".format(var=variable),all_ratios_one(ratio)])


def hist_comp_all():
        for variable in variables:
                print(variable)
                same_sign="abcd_anti_iso" if "tt" in args.channel else "same_sign"
                ss="_B" if "tt" in args.channel else "_ss"  
                area={"Nominal" : "",
                        same_sign : ss ,
                        "anti_iso" : "_FF"
                } 
                if args.analysis_shapes:
                        categories={}                           
                        for nn_cat in nn_categories:                             
                                categories["qqH#{channel}-qqH125-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}#qqH125#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat,var=variable,era =args.era)
                                categories["ggH#{channel}-ggH125-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}#ggH125#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat,var=variable,era =args.era)
                                categories["TT#{channel}-TT-TTT-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}#TTT#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable, era =args.era)
                                categories["TT#{channel}-TT-TTJ-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat, var=variable)] = "#{channel}#{channel}_{nncat}#TTJ#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era)
                                categories["TT#{channel}-TT-TTJ-{nncat}#{same_sign}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable,same_sign=same_sign)] = "#{channel}#{channel}_{nncat}{cat_old}#TTJ#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era, cat_old=area[same_sign])                
                                categories["DY#{channel}-DY-ZTT-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}#ZTT#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era)
                                categories["DY#{channel}-DY-ZJ-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}#ZJ#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era)
                                categories["DY#{channel}-DY-ZJ-{nncat}#{same_sign}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable,same_sign=same_sign)] = "#{channel}#{channel}_{nncat}{cat_old}#ZJ#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,cat_old=area[same_sign])                
                                categories["VV#{channel}-VV-VVT-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}#VVT#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era)                
                                categories["VV#{channel}-VV-VVJ-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}#VVJ#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era)
                                categories["VV#{channel}-VV-VVJ-{nncat}#{same_sign}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable,same_sign=same_sign)] = "#{channel}#{channel}_{nncat}{cat_old}#VVJ#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,cat_old=area[same_sign])
                                categories["W#{channel}-W-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}#W#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era)
                                categories["W#{channel}-W-{nncat}#{same_sign}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable,same_sign=same_sign)] = "#{channel}#{channel}_{nncat}{cat_old}#W#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,cat_old=area[same_sign])
                                categories["QCD#{channel}-QCD-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}#QCD#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era)
                                categories["jetFakes#{channel}-jetFakes-{nncat}#Nominal#{var}".format(channel=args.channel, nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}#jetFakes#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era)
                                
                                for cat_new in area.keys():   
                                        categories["VV#{channel}-VV-VVL-{nncat}#{cat_new}#{var}".format(channel=args.channel, nncat=nn_cat,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{nncat}{cat_old}#VVL#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat,cat_old=area[cat_new], var=variable,era =args.era)
                                        categories["EMB#{channel}-Embedded-{nncat}#{cat_new}#{var}".format(channel=args.channel, nncat=nn_cat,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{nncat}{cat_old}#EMB#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat,cat_old=area[cat_new], var=variable,era =args.era)
                                        categories["DY#{channel}-DY-ZL-{nncat}#{cat_new}#{var}".format(channel=args.channel, nncat=nn_cat,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{nncat}{cat_old}#ZL#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat,cat_old=area[cat_new], var=variable,era =args.era)
                                        categories["TT#{channel}-TT-TTL-{nncat}#{cat_new}#{var}".format(channel=args.channel, nncat=nn_cat,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{nncat}{cat_old}#TTL#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat,cat_old=area[cat_new], var=variable,era =args.era)
                                        categories["data#{channel}-{nncat}#{cat_new}#{var}".format(channel=args.channel,cat_new=cat_new , nncat=nn_cat,var=variable)] = "#{channel}#{channel}_{nncat}{cat_old}#data_obs#smhtt#Run{era}#{var}#125#".format(channel=args.channel, nncat=nn_cat,cat_old=area[cat_new], var=variable,era =args.era)  

                                for heavy_mass in mass_dict["heavy_mass"]:
                                        for light_mass in light_masses(heavy_mass):
                                                if light_mass+125<heavy_mass:
                                                        categories["NMSSM_{heavy_mass}_125_{light_mass}#{channel}-NMSSM-{nncat}#Nominal#{var}".format(heavy_mass=heavy_mass, light_mass=light_mass, channel=args.channel, nncat=nn_cat, var=variable)] = "#{channel}#{channel}_{nncat}#NMSSM_{heavy_mass}_125_{light_mass}#smhtt#Run{era}#{var}#125#".format(heavy_mass=heavy_mass, light_mass=light_mass, channel=args.channel, nncat=nn_cat, var=variable, era=args.era)

                else:
                        categories={
                "qqH#{channel}-qqH125#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#qqH125#smhtt#Run{era}#{var}#125#".format(channel =args.channel,var=variable,era =args.era),
                "ggH#{channel}-ggH125#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#ggH125#smhtt#Run{era}#{var}#125#".format(channel =args.channel,var=variable,era =args.era),
                "TT#{channel}-TT-TTT#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#TTT#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable, era =args.era),
                "TT#{channel}-TT-TTJ#Nominal#{var}".format(channel =args.channel, var=variable) : "#{channel}#{channel}_{var}#TTJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "TT#{channel}-TT-TTJ#{same_sign}#{var}".format(channel =args.channel,var=variable,same_sign=same_sign) : "#{channel}#{channel}_{var}{cat_old}#TTJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era, cat_old=area[same_sign]),                
                "DY#{channel}-DY-ZTT#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#ZTT#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "DY#{channel}-DY-ZJ#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#ZJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "DY#{channel}-DY-ZJ#{same_sign}#{var}".format(channel =args.channel,var=variable,same_sign=same_sign) : "#{channel}#{channel}_{var}{cat_old}#ZJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era,cat_old=area[same_sign]),                
                "VV#{channel}-VV-VVT#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#VVT#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),                
                "VV#{channel}-VV-VVJ#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#VVJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "VV#{channel}-VV-VVJ#{same_sign}#{var}".format(channel =args.channel,var=variable,same_sign=same_sign) : "#{channel}#{channel}_{var}{cat_old}#VVJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era,cat_old=area[same_sign]),
                "W#{channel}-W#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#W#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "W#{channel}-W#{same_sign}#{var}".format(channel =args.channel,var=variable,same_sign=same_sign) : "#{channel}#{channel}_{var}{cat_old}#W#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era,cat_old=area[same_sign]),
                "QCD#{channel}-QCD#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#QCD#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "jetFakes#{channel}-jetFakes#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#jetFakes#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era)
                        }
                        for cat_new in area.keys():   
                                categories["VV#{channel}-VV-VVL#{cat_new}#{var}".format(channel =args.channel,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{var}{cat_old}#VVL#smhtt#Run{era}#{var}#125#".format(channel =args.channel,cat_old=area[cat_new], var=variable,era =args.era)
                                categories["EMB#{channel}-Embedded#{cat_new}#{var}".format(channel =args.channel,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{var}{cat_old}#EMB#smhtt#Run{era}#{var}#125#".format(channel =args.channel,cat_old=area[cat_new], var=variable,era =args.era)
                                categories["DY#{channel}-DY-ZL#{cat_new}#{var}".format(channel =args.channel,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{var}{cat_old}#ZL#smhtt#Run{era}#{var}#125#".format(channel =args.channel,cat_old=area[cat_new], var=variable,era =args.era)
                                categories["TT#{channel}-TT-TTL#{cat_new}#{var}".format(channel =args.channel,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{var}{cat_old}#TTL#smhtt#Run{era}#{var}#125#".format(channel =args.channel,cat_old=area[cat_new], var=variable,era =args.era)
                                categories["data#{channel}#{cat_new}#{var}".format(channel =args.channel,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{var}{cat_old}#data_obs#smhtt#Run{era}#{var}#125#".format(channel =args.channel,cat_old=area[cat_new], var=variable,era =args.era)  

                        for heavy_mass in mass_dict["heavy_mass"]:
                                for light_mass in light_masses(heavy_mass):
                                        if light_mass+125<heavy_mass:
                                                categories["NMSSM_{heavy_mass}_125_{light_mass}#{channel}-NMSSM#Nominal#{var}".format(heavy_mass=heavy_mass, light_mass=light_mass, channel=args.channel, var=variable)] = "#{channel}#{channel}_{var}#NMSSM_{heavy_mass}_125_{light_mass}#smhtt#Run{era}#{var}#125#".format(heavy_mass=heavy_mass, light_mass=light_mass, channel=args.channel, var=variable, era=args.era)
                
                #print(categories)
                #rfile_old=ROOT.TFile("/work/rschmieder/nmssm_oldframework/sm-htt-analysis/output/shapes/{era}_{channel}_{var}/{era}-{era}_{channel}_{var}-{channel}-shapes.root".format(era=args.era, channel=args.channel, var=variable),"READ")  
                #rfile_old=ROOT.TFile("/work/rschmieder/nmssm_oldframework/sm-htt-analysis/output/uncert_shapes/{era}_{channel}_{var}/{era}-{era}_{channel}_{var}-{channel}-shapes.root".format(era=args.era, channel=args.channel, var=variable),"READ")    
                rfile_old = ROOT.TFile("/work/rschmieder/nmssm_newframework/nmssm_newframework_analysis/output/uncert_shapes/2016-et-control-shapes/shapes-analysis-2016-et.root".format(era=args.era,ch=args.channel),"READ")
                for process in categories.keys(): 
                        hist_old=rfile_old.Get(process)
                        hist_new=rfile_new.Get(process)
                        # print(process,categories[process])
                        # print(hist_new,hist_old)
                        # print("")
                        ratio=np.zeros(hist_old.GetNbinsX())
                        for i in range(1,hist_old.GetNbinsX()+1):        
                                if round(hist_new.GetBinContent(i),7)!=0.0 :
                                        ratio[i-1]=round((hist_old.GetBinContent(i)/hist_new.GetBinContent(i)),5)
                                elif round(hist_old.GetBinContent(i),7)==0.0 and round(hist_new.GetBinContent(i),7)==0.0:
                                        ratio[i-1]=1
                                else:
                                        ratio[i-1]=0  
                        if all_ratios_one(ratio)==0: #
                                print(process,categories[process])
                                print("ratio")
                                print(ratio)

                                #print("bincontent: old/new")       
                                # for j in range(1,hist_old.GetNbinsX()+1):
                                #         print(hist_old.GetBinContent(j),hist_new.GetBinContent(j))
                                # print("new Integral","old Integral", "new-old Integral")
                                # print(hist_new.Integral(),hist_old.Integral(), hist_new.Integral()-hist_old.Integral())  
                                # print(hist_old.GetEntries(), hist_new.GetEntries())
                        # for r in range(len(ratio)):
                        #         if round(ratio[r],4) != 1.0:
                        #                 bin_c=hist_new.GetBinCenter(r+1)
                        #                 bin_l=hist_new.GetBinLowEdge(r+1)
                       # print(categories[process],process)
                        #                 print("index","bin_center","bin_low_edge")
                        #                 print(r+1,bin_c,bin_l)
                        #print(ratio)                     
                        #                 print("")

                        # if process.find("Nominal")>1:
                        #         if process.find("data")>-0.5:
                        #                 pro="data-Nominal"
                        #         else:
                        #                 pro=process[process[:process.rfind("-")].rfind("-")+1:process.rfind("-")]+"-Nominal" 
                        # elif process.find("#anti_iso")>1:
                        #         if process.find("data")>-0.5:
                        #                 pro="data-anti_iso"
                        #         else:
                        #                 pro=process[process[:process.rfind("-")].rfind("-")+1:process.rfind("-")]+"-anti_iso"
                        # elif process.find("#same_sign")>1:
                        #         if process.find("data")>-0.5:
                        #                 pro="data-same_sign"
                        #         else:
                        #                 pro=process[process[:process.rfind("-")].rfind("-")+1:process.rfind("-")]+"-same_sign"
                        # elif process.find("abcd_anti_iso")>1:
                        #         if process.find("data")>-0.5:
                        #                 pro="data-abcd_ai"
                        #         else:
                        #                 pro=process[process[:process.rfind("-")].rfind("-")+1:process.rfind("-")]+"-abcd_ai"
                        
                        # for nncat in nn_categories:
                        #         if process.find("{nn}".format(nn=nncat))>1:
                        #                 nn_cat=nncat
                        
                        # ratio_plot(hist_old,hist_new,args.era,args.channel,variable,pro,ratio,nn_cat)

                        # print("histogramm entries old/new")
                        # print(hist_old.GetEntries(), hist_new.GetEntries())
                        # print("")
                        # print("bincontent: old/new")       
                        # for j in range(1,hist_old.GetNbinsX()+1):
                        #         print(hist_old.GetBinContent(j),hist_new.GetBinContent(j))
                        # print("")
                        # print(" ------ ")
                        # print("")
                                
                                #         print(hist_new.GetBinContent(j))
                               # hist_ratios=np.append(hist_ratios,"{cat}".format(var=variable,cat=categories.keys()))                                   
                        #ratio_plot(hist_old,hist_new,args.era,args.channel,variable,categories.keys())
            
                       
                #print(hist_ratios)
def QCD():
        for variable in variables:
                same_sign="abcd_same_sign" if "tt" in args.channel else "same_sign"
                ss="_B" if "tt" in args.channel else "_ss"  
                area={"Nominal" : "",
                        same_sign : ss ,
                        "anti_iso" : "_FF"
                }                                     
                categories={
                "qqH#{channel}-qqH125#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#qqH125#smhtt#Run{era}#{var}#125#".format(channel =args.channel,var=variable,era =args.era),
                "ggH#{channel}-ggH125#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#ggH125#smhtt#Run{era}#{var}#125#".format(channel =args.channel,var=variable,era =args.era),
                "TT#{channel}-TT-TTT#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#TTT#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable, era =args.era),
                "TT#{channel}-TT-TTJ#Nominal#{var}".format(channel =args.channel, var=variable) : "#{channel}#{channel}_{var}#TTJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "TT#{channel}-TT-TTJ#{same_sign}#{var}".format(channel =args.channel,var=variable,same_sign=same_sign) : "#{channel}#{channel}_{var}{cat_old}#TTJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era, cat_old=area[same_sign]),                
                "DY#{channel}-DY-ZTT#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#ZTT#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "DY#{channel}-DY-ZJ#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#ZJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "DY#{channel}-DY-ZJ#{same_sign}#{var}".format(channel =args.channel,var=variable,same_sign=same_sign) : "#{channel}#{channel}_{var}{cat_old}#ZJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era,cat_old=area[same_sign]),                
                "VV#{channel}-VV-VVT#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#VVT#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),                
                "VV#{channel}-VV-VVJ#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#VVJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "VV#{channel}-VV-VVJ#{same_sign}#{var}".format(channel =args.channel,var=variable,same_sign=same_sign) : "#{channel}#{channel}_{var}{cat_old}#VVJ#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era,cat_old=area[same_sign]),
                "W#{channel}-W#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#W#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "W#{channel}-W#{same_sign}#{var}".format(channel =args.channel,var=variable,same_sign=same_sign) : "#{channel}#{channel}_{var}{cat_old}#W#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era,cat_old=area[same_sign]),
                "QCD#{channel}-QCD#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#QCD#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era),
                "jetFakes#{channel}-jetFakes#Nominal#{var}".format(channel =args.channel,var=variable) : "#{channel}#{channel}_{var}#jetFakes#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era)
                }

                for cat_new in area.keys():   
                        categories["VV#{channel}-VV-VVL#{cat_new}#{var}".format(channel =args.channel,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{var}{cat_old}#VVL#smhtt#Run{era}#{var}#125#".format(channel =args.channel,cat_old=area[cat_new], var=variable,era =args.era)
                        categories["EMB#{channel}-Embedded#{cat_new}#{var}".format(channel =args.channel,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{var}{cat_old}#EMB#smhtt#Run{era}#{var}#125#".format(channel =args.channel,cat_old=area[cat_new], var=variable,era =args.era)
                        categories["DY#{channel}-DY-ZL#{cat_new}#{var}".format(channel =args.channel,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{var}{cat_old}#ZL#smhtt#Run{era}#{var}#125#".format(channel =args.channel,cat_old=area[cat_new], var=variable,era =args.era)
                        categories["TT#{channel}-TT-TTL#{cat_new}#{var}".format(channel =args.channel,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{var}{cat_old}#TTL#smhtt#Run{era}#{var}#125#".format(channel =args.channel,cat_old=area[cat_new], var=variable,era =args.era)
                        categories["data#{channel}#{cat_new}#{var}".format(channel =args.channel,cat_new=cat_new,var=variable)] = "#{channel}#{channel}_{var}{cat_old}#data_obs#smhtt#Run{era}#{var}#125#".format(channel =args.channel,cat_old=area[cat_new], var=variable,era =args.era)  

                for heavy_mass in mass_dict["heavy_mass"]:
                        for light_mass in light_masses(heavy_mass):
                                 if light_mass+125<heavy_mass:
                                         categories["NMSSM_{heavy_mass}_125_{light_mass}#{channel}-NMSSM#Nominal#{var}".format(heavy_mass=heavy_mass, light_mass=light_mass, channel=args.channel, var=variable)] = "#{channel}#{channel}_{var}#NMSSM_{heavy_mass}_125_{light_mass}#smhtt#Run{era}#{var}#125#".format(heavy_mass=heavy_mass, light_mass=light_mass, channel=args.channel, var=variable, era=args.era)
     

                
                rfile_old=ROOT.TFile("/work/rschmieder/nmssm_oldframework/sm-htt-analysis/output/shapes/{era}_{channel}_{var}/{era}-{era}_{channel}_{var}-{channel}-shapes.root".format(era=args.era, channel=args.channel, var=variable),"READ")   
                hist_new_data_ss= rfile_new.Get("data#{channel}#same_sign#{var}".format(channel =args.channel,var=variable))
                hist_qcd_new=rfile_new.Get("QCD#{channel}-QCD#Nominal#{var}".format(channel =args.channel,var=variable))
                hist_qcd_old=rfile_old.Get("#{channel}#{channel}_{var}#QCD#smhtt#Run{era}#{var}#125#".format(channel =args.channel, var=variable,era =args.era))
                diff=np.zeros(hist_new_data_ss.GetNbinsX())
                qcd_new=np.zeros(hist_qcd_new.GetNbinsX())
                qcd_old=np.zeros(hist_qcd_old.GetNbinsX())
                ratio=np.zeros(hist_qcd_new.GetNbinsX())
                for j in range(1,hist_new_data_ss.GetNbinsX()+1):
                        diff[j-1]=hist_new_data_ss.GetBinContent(j)
                for process in categories.keys():                        
                        if process.find("same_sign") > -0.5 and process.find("data") < -0.5:
                                hist_old=rfile_old.Get(categories[process])
                                hist_new=rfile_new.Get(process)
                                for i in range(1,hist_new.GetNbinsX()+1):        
                                        diff[i-1]-=hist_new.GetBinContent(i)
                                        qcd_new[i-1]=hist_qcd_new.GetBinContent(i)
                                        qcd_old[i-1]=hist_qcd_old.GetBinContent(i)
                for i in range(len(qcd_new)):        
                        if round(qcd_new[i],6)!=0.0 :
                                ratio[i]=round((qcd_old[i]/qcd_new[i]),5)
                        elif round(qcd_old[i],6)==0.0 and round(qcd_new[i],6)==0.0:
                                ratio[i]=1
                        else:
                                ratio[i]=0
                print("{var}".format(var=variable))
                print("entries old/new")
                print(hist_qcd_old.GetEntries(),hist_qcd_new.GetEntries())
                print("ratio")
                print(ratio)
                print("")
                print("difference: data_same_sign - process_same_sign")
                print(diff)
                print("")
                print("QCD Estimation old framework")
                print(qcd_old)
                print("")
                print("QCD Estimation new framework")
                print(qcd_new)
                print("")
                print("---------")
                print("")


def hist_uncert():
        categories={} 
        if args.channel=="tt":
                variations=ff_variations_tt                                
        else:
                variations=ff_variations_lt
                if "et" in args.channel:
                        variations=variations+electron
                else:
                        variations=variations+muon                          
        for nn_cat in nn_categories:
                for shift in shifts: 
                        for vari in variations:                                   
                                categories["qqH#{channel}-qqH125-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#qqH125#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat,var=variable,era =args.era, vari=vari, shift=shift)
                                categories["ggH#{channel}-ggH125-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#ggH125#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat,var=variable,era =args.era, vari=vari, shift=shift)
                                categories["TT#{channel}-TT-TTT-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#TTT#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat,var=variable,era =args.era, vari=vari, shift=shift)
                                categories["TT#{channel}-TT-TTJ-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat, var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#TTJ#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat,var=variable,era =args.era, vari=vari, shift=shift)                                      
                                categories["DY#{channel}-DY-ZTT-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#ZTT#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)
                                categories["DY#{channel}-DY-ZJ-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#ZJ#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)                        
                                categories["VV#{channel}-VV-VVT-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#VVT#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)                
                                categories["VV#{channel}-VV-VVJ-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#VVJ#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)                                        
                                categories["W#{channel}-W-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#W#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)                                        
                                #categories["QCD#{channel}-QCD-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#QCD#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)
                                #categories["jetFakes#{channel}-jetFakes-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}{channel}_{nncat}#jetFakes#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)                                   
                                categories["VV#{channel}-VV-VVL-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#VVL#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)
                                categories["EMB#{channel}-Embedded-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#EMB#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)
                                categories["DY#{channel}-DY-ZL-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#ZL#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)
                                categories["TT#{channel}-TT-TTL-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#TTL#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)
                                categories["data#{channel}-{nncat}#{vari}{shift}#{var}".format(channel=args.channel,nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#data_obs#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)  

                                for heavy_mass in mass_dict["heavy_mass"]:
                                                        for light_mass in light_masses(heavy_mass):
                                                                if light_mass+125<heavy_mass:
                                                                        categories["NMSSM_{heavy_mass}_125_{light_mass}#{channel}-NMSSM-{nncat}#{vari}{shift}#{var}".format(heavy_mass=heavy_mass, light_mass=light_mass, channel=args.channel, nncat=nn_cat, var=variable,vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#NMSSM_{heavy_mass}_125_{light_mass}#smhtt#Run{era}#{var}#125#{vari}{shift}".format(heavy_mass=heavy_mass, light_mass=light_mass, channel=args.channel, nncat=nn_cat, var=variable, era=args.era,vari=vari, shift=shift)
        for key in categories.keys():
                if "EMB" in key:
                        if "tt" in args.channel:
                                for vari in tt_emb:
                                        categories["EMB#{channel}-Embedded-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#EMB#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)
                        else:
                                for var in lt_emb:
                                        categories["EMB#{channel}-Embedded-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#EMB#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)
                else:
                        if "tt" in args.channel:
                                for vari in tt_prong:
                                        categories["EMB#{channel}-Embedded-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#EMB#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)
                        else:
                                for vari in lt:
                                        categories["EMB#{channel}-Embedded-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#EMB#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)      
                if "ggH" in key:
                        for vari in ggh_var:
                                categories["ggH#{channel}-ggH125-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#ggH125#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat,var=variable,era =args.era, vari=vari, shift=shift)
                if "qqH" in key:
                        for vari in qqh_var:
                                categories["qqH#{channel}-qqH125-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#qqH125#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat,var=variable,era =args.era, vari=vari, shift=shift)
                if "ZL" in key:
                        if "et" in args.channel:
                                for vari in electron_ZL:
                                        categories["DY#{channel}-DY-ZL-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#ZL#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)
                        if "mt" in args.channel:
                                for vari in muon_ZL:
                                        categories["DY#{channel}-DY-ZL-{nncat}#{vari}{shift}#{var}".format(channel=args.channel, nncat=nn_cat,var=variable, vari=vari, shift=shift)] = "#{channel}#{channel}_{nncat}#ZL#smhtt#Run{era}#{var}#125#{vari}{shift}".format(channel=args.channel, nncat=nn_cat, var=variable,era =args.era,vari=vari, shift=shift)




        
        rfile_old=ROOT.TFile("/work/rschmieder/nmssm_oldframework/sm-htt-analysis/output/uncert_shapes/{era}_{channel}_{var}/{era}-{era}_{channel}_{var}-{channel}-shapes.root".format(era=args.era, channel=args.channel, var=variable),"READ")  
        #rfile_old = ROOT.TFile("/work/rschmieder/nmssm_newframework/nmssm_newframework_analysis/output/2uncert_shapes/{era}-{channel}-control-shapes/shapes-analysis-{era}-{channel}.root".format(era=args.era, channel=args.channel),"READ")  
        for process in categories.keys(): 
                if "Channel_Era_" in categories[process]:
                        categories[process]=categories[process].replace("Channel", args.channel).replace("Era", args.era)
                if "_Era" in categories[process]:
                        categories[process]=categories[process].replace("Era", args.era)
                hist_old=rfile_old.Get(categories[process])
                hist_new=rfile_new.Get(process)
                print(categories[process],process)
                #print(hist_new,hist_old)
                # print("")
                ratio=np.zeros(hist_old.GetNbinsX())
                for i in range(1,hist_old.GetNbinsX()+1):        
                        if round(hist_new.GetBinContent(i),7)!=0.0 :
                                ratio[i-1]=round((hist_old.GetBinContent(i)/hist_new.GetBinContent(i)),5)
                        elif round(hist_old.GetBinContent(i),7)==0.0 and round(hist_new.GetBinContent(i),7)==0.0:
                                ratio[i-1]=1
                        else:
                                ratio[i-1]=0  
                #if all_ratios_one(ratio)==0: #
                #print(process)
                print("ratio")
                print(ratio)
                print("")



def hist_uncert2():
        #rfile_new = ROOT.TFile("/work/rschmieder/nmssm_newframework/nmssm_newframework_analysis/output/uncert_shapes/et17_emb_tau_trigger_wstring_2017et/{era}-{ch}-synced-NMSSM.root".format(era=args.era,ch=args.channel),"READ")
        #rfile_new = ROOT.TFile("/work/rschmieder/nmssm_newframework/nmssm_newframework_analysis/output/uncert_shapes/synced_shapes/{era}-{ch}-synced-NMSSM.root".format(era=args.era,ch=args.channel),"READ")
        rfile_new=ROOT.TFile("/work/jbechtel/postprocessing/nmssm/train_all/CMSSW_10_2_16_UL/src/CombineHarvester/MSSMvsSMRun2Legacy/shapes/htt_{ch}.inputs-nmssm-{era}-{ch}_max_score_500_3.root".format(era=args.era,ch=args.channel),"READ")
        rfile_old=ROOT.TFile("/work/rschmieder/nmssm_oldframework/sm-htt-analysis/output/uncert_shapes/channel_classdict/htt_{ch}.inputs-nmssm-{era}-{ch}_max_score_500_3.root".format(era=args.era,ch=args.channel),"READ")
        #rfile_old=ROOT.TFile("/work/rschmieder/nmssm_oldframework/sm-htt-analysis/output/uncert_shapes/et17_pt1_eta1_emb_tau_trigger_wstring_2017et/{era}-{ch}-synced-ML.root".format(era=args.era,ch=args.channel),"READ")
        nn_categories=["NMSSM_MH500_3"]

        def find_element(keylist,element):
                if element in keylist:
                        return True
                return False

        for nn_cat in nn_categories:
                old_file=rfile_old.Get("{ch}_{nn_cat}".format(ch=args.channel, nn_cat=nn_cat))
                new_file=rfile_new.Get("{ch}_{nn_cat}".format(ch=args.channel, nn_cat=nn_cat))
                for key in old_file.GetListOfKeys():
                        histkey=key.GetName()
                        if "NMSSM" in histkey:
                                continue
                        #print(new_file.GetListOfKeys())
                       # skips=["scale_j_RelativeSampleDown","scale_j_RelativeSampleUp","mistag_b_2016_mt","htt_eff_b_2016_mt", "CMS_htt_dyShape_{era}Down".format(era=args.era),"CMS_htt_dyShape_{era}Up".format(era=args.era),"ZL_CMS_eff_t_dm","CMS_htt_dyShapeDown".format(era=args.era),"CMS_htt_dyShapeUp".format(era=args.era),"CMS_htt_boson_res_metDown","CMS_htt_boson_res_metUp","CMS_htt_boson_scale_metDown","CMS_htt_boson_scale_metUp","TTT_CMS_htt_emb_ttbar_2018Down","TTT_CMS_htt_emb_ttbar_2018Up","CMS_eff_trigger_mt_2018Down","CMS_eff_trigger_mt_2018Up","xtrigger_l_mt_2018Down","xtrigger_l_mt_2018Up","VHBB","_2018"] #
                        # if find_element(newlist,histkey)==False:
                        #         #print(key)
                        #         continue
                        
                        #
                        # continue
                        #
                        if histkey.find("_")>-0.5 and args.nominals==False:
                                # if not find_element(new_file.GetListOfKeys(), histkey):
                                #         print(histkey)# 
                                # if histkey.find("EMB_CMS_eff_xtrigger_l_et_2017Down")>-0.5:
                                #         #print(histkey)
                                #         hist_old=old_file.Get("EMB_CMS_eff_xtrigger_l_emb_et_2017Down")
                                # else:
                                hist_old=old_file.Get(histkey)
                                             
                                hist_new=new_file.Get(histkey)
                                if "TH1D" not in str(type(hist_new)):
                                        continue
                                #print(histkey)
                                # # print(old_file)
                                # if "NMSSM" not in histkey:
                                #         print(histkey)
                                #print(hist_old,hist_new)
                                ratio=np.zeros(hist_old.GetNbinsX())
                                for i in range(1,hist_old.GetNbinsX()+1):        
                                        if round(hist_new.GetBinContent(i),7)!=0.0 :
                                                ratio[i-1]=round((hist_old.GetBinContent(i)/hist_new.GetBinContent(i)),5)
                                        elif round(hist_old.GetBinContent(i),7)==0.0 and round(hist_new.GetBinContent(i),7)==0.0:
                                                ratio[i-1]=1
                                        else:
                                                ratio[i-1]=0  
                                if all_ratios_one(ratio)==0: # and "NMSSM" not in histkey: # or ("NMSSM_320_125_60" in histkey and all_ratios_one(ratio)==0): # or "NMSSM_320_125_60" in histkey:
                                #if "NMSSM_2500_125_600" in histkey:
                                        print(histkey)
                                        # for i in range(1,hist_old.GetNbinsX()+1):
                                        #         print(hist_old.GetBinContent(i),hist_new.GetBinContent(i))
                                #         #print(nn_cat)
                                        
                                # 
                                        #print(histkey)
                                #         for i in range(1,hist_old.GetNbinsX()+1):
                                #                  print(hist_old.GetBinContent(i),hist_new.GetBinContent(i))
                                        # print("ratio")
                                        #print(ratio)
                                        #print("")
                        elif  ("NMSSM" in histkey and len(histkey)<20):      #(histkey.find("_")<-0.5 and args.nominals==True) or  
                                hist_old=old_file.Get(histkey)
                                hist_new=new_file.Get(histkey)  
                                #print(nn_cat)
                                print(histkey)
                                # print(hist_old,hist_new)
                                ratio=np.zeros(hist_old.GetNbinsX())
                                for i in range(1,hist_old.GetNbinsX()+1):        
                                        if round(hist_new.GetBinContent(i),7)!=0.0 :
                                                ratio[i-1]=round((hist_old.GetBinContent(i)/hist_new.GetBinContent(i)),5)
                                        elif round(hist_old.GetBinContent(i),7)==0.0 and round(hist_new.GetBinContent(i),7)==0.0:
                                                ratio[i-1]=1
                                        else:
                                                ratio[i-1]=0  
                                        #print("old/new")
                                        #print(hist_old.GetBinContent(i),hist_new.GetBinContent(i))
                                if all_ratios_one(ratio)==0: #
                                #if "EMB" in histkey:
                                        #print(histkey)
                                        for i in range(1,hist_old.GetNbinsX()+1):
                                                 print(hist_old.GetBinContent(i),hist_new.GetBinContent(i))
                                        print(nn_cat)
                                        print(histkey)
                                        print("binentries")
                                        print(hist_old.Integral(), hist_old.GetEntries(), hist_new.Integral(),hist_new.GetEntries())
                                        print("ratio")
                                        print(ratio)
                                        print("")             


#hist_comp_all()
hist_uncert2()       
