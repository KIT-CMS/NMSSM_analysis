import numpy as np 
import matplotlib.pyplot as plt
import argparse

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
        "--tag",
        required=True,
        type=str,
        help="training"
)

parser.add_argument(       
        "--node",
        required=True,
        type=str,
        help="all, or specific outputclass"
)
parser.add_argument(
        "--sorted",
        required=False,
        type=int,
        help="--sorted num, plots the top num variables, if false you need to specify the variables you want to highlight in int_vars"
    )
args = parser.parse_args()

if args.era == "all_eras":
    emb=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_emb_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    tt=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_tt_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    ff=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_ff_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    misc=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_misc_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    nmssm=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_NMSSM_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    for era in ["2017","2018"]:
        emb_era=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_emb_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        tt_era=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_tt_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        ff_era=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_ff_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        misc_era=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_misc_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        nmssm_era=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_NMSSM_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")

        emb=np.vstack((emb,emb_era))
        tt=np.vstack((tt,tt_era))
        ff=np.vstack((ff,ff_era))
        misc=np.vstack((misc,misc_era))
        nmssm=np.vstack((nmssm,nmssm_era))

else: 
    emb=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_emb_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    tt=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_tt_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    ff=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_ff_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    misc=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_misc_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    nmssm=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_NMSSM_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")

if "tt" in args.channel:
    ranks=464
    vars=["pt_1"
    ,"pt_2"
    ,"m_vis"
    ,"ptvis"
    ,"m_sv_puppi"
    ,"nbtag"
    ,"jpt_1"
    ,"njets"
    ,"jdeta"
    ,"mjj"
    ,"dijetpt"
    ,"bpt_bReg_1"
    ,"bpt_bReg_2"
    ,"bm_bReg_1"
    ,"bm_bReg_2"
    ,"bcsv_1"
    ,"bcsv_2"
    ,"jpt_2"
    ,"mbb_highCSV_bReg"
    ,"pt_bb_highCSV_bReg"
    ,"m_ttvisbb_highCSV_bReg"
    ,"kinfit_mH"
    ,"kinfit_mh2"
    ,"kinfit_chi2"
    ,"highCSVjetUsedFordiBJetSystemCSV"
    ,"NMSSM_light_mass"
    ,"2016"
    ,"2017"
    ,"2018"]
else:
    ranks=324
    vars=["pt_1"
    ,"pt_2"
    ,"m_vis"
    ,"ptvis"
    ,"m_sv_puppi"
    ,"nbtag"
    ,"jpt_1"
    ,"njets"
    ,"jdeta"
    ,"mjj"
    ,"dijetpt"
    ,"bpt_bReg_1"
    ,"bpt_bReg_2"
    ,"jpt_2"
    ,"mbb_highCSV_bReg"
    ,"pt_bb_highCSV_bReg"
    ,"m_ttvisbb_highCSV_bReg"
    ,"kinfit_mH"
    ,"kinfit_mh2"
    ,"kinfit_chi2"
    ,"NMSSM_light_mass"
    ,"2016"
    ,"2017"
    ,"2018"]

vars_dict={}
for var in vars:
    vars_dict[var]=[]
if args.node == "all":
    norm=5*len(vars)*ranks
    taylor_ranks=np.vstack((emb,tt,ff,misc,nmssm))
else:
    norm=len(vars)*ranks
    if args.node=="emb":
        taylor_ranks=emb
    elif args.node=="ff":
        taylor_ranks=ff
    elif args.node=="tt":
        taylor_ranks=tt
    elif args.node=="misc":
        taylor_ranks=misc
    elif args.node=="nmssm":
        taylor_ranks=nmssm
if args.era =="all_eras":
    norm=norm*3
for key in vars_dict:
    for t in range(taylor_ranks.shape[0]):
        if taylor_ranks[t][1].find(",") != -1:
            taylor_vars=taylor_ranks[t][1].replace(" ","").split(",")
            if key == taylor_vars[0] or key == taylor_vars[1]:
                vars_dict[key].append(int(taylor_ranks[t][0]))
        else:
            taylor_vars=taylor_ranks[t][1].replace(" ","")
            if key == taylor_vars:
                vars_dict[key].append(int(taylor_ranks[t][0]))
area_dict={}
areas=np.zeros(len(vars))
i=0
for key in vars_dict.keys():
    n,bins,patches=plt.hist(vars_dict[key],bins=range(0,324), cumulative=True,histtype="step")
    area = sum(np.diff(bins)*n)
    area_dict[key]=area
    areas[i]=area
    plt.close()
    i+=1

sort_areas=np.sort(areas)[::-1]
fig = plt.figure()
ax = plt.subplot(111)
if args.sorted:
    top_vars=[]
    for area in sort_areas[:args.sorted]:
        for key in vars_dict:
            if (round(area_dict[key],5) == round(area,5)):
                top_vars.append(key)
    for key in vars_dict:
        if key not in top_vars:
            vars_dict[key].append(ranks+1)
            cnt, edges = np.histogram(vars_dict[key], bins=range(-1,ranks+2))
            ax.step(edges[:-2], cnt[:-1].cumsum(),where="pre",color="lightgrey")  
    for key in top_vars:
        vars_dict[key].append(ranks+1)
        cnt, edges = np.histogram(vars_dict[key], bins=range(-1,ranks+2))
        ax.step(edges[:-2], cnt[:-1].cumsum(),where="pre",label=key+"({area})".format(area=round(area_dict[key]/norm,2)))
else:
    int_vars=["NMSSM_light_mass","kinfit_chi2","m_sv_puppi", "kinfit_mh2", "kinfit_mH","m_vis","pt_1"]
    int_col=["b","g","r","c","m","y","k","darkorange","gold","limegreen","springgreen","royalblue","slategrey","darkviolet"]
    i=0
    for key in vars:
        if key not in int_vars:
            vars_dict[key].append(ranks+1)
            cnt, edges = np.histogram(vars_dict[key], bins=range(-1,ranks+2))
            ax.step(edges[:-2], cnt[:-1].cumsum(),where="pre",color="lightgrey")        
    for key in vars:
        if key in int_vars:      
            vars_dict[key].append(ranks+1)
            cnt, edges = np.histogram(vars_dict[key], bins=range(-1,ranks+2))
            ax.step(edges[:-2], cnt[:-1].cumsum(),where="pre",label=key+"({area})".format(area=round(area_dict[key]/norm,2)),color=int_col[i])
            i+=1

lgd=ax.legend(bbox_to_anchor=(1, 1))
plt.ylabel(r"cumulative count")
plt.xlabel(r"Taylor rank")
plt.title(args.channel+" "+args.era+" "+args.tag+" "+args.node)
#plt.show()
plt.tight_layout()
plt.savefig("plots/{tag}/cumulative_taylorranking_{era}_{channel}_{node}.png".format(tag=args.tag,era=args.era,channel=args.channel,node=args.node))
plt.savefig("plots/{tag}/cumulative_taylorranking_{era}_{channel}_{node}.pdf".format(tag=args.tag,era=args.era,channel=args.channel,node=args.node))



