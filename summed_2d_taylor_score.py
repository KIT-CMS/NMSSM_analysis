import numpy as np 
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='sum up all taylor 1d and 2d scores')
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

def taylor_norm(taylor_ranks):
    sum_taylor_ranks=0
    for t in range(taylor_ranks.shape[0]):
        sum_taylor_ranks+=float(taylor_ranks[t][2])
    for t in range(taylor_ranks.shape[0]):
        taylor_ranks[t][2]=float(taylor_ranks[t][2])/sum_taylor_ranks
    return taylor_ranks

if args.era == "all_eras":
    emb=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_emb_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    tt=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_tt_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    ff=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_ff_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    misc=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_misc_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    nmssm=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_NMSSM_MH500_3_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    emb=taylor_norm(emb)
    ff=taylor_norm(ff)
    tt=taylor_norm(tt)
    misc=taylor_norm(misc)
    nmssm=taylor_norm(nmssm)
    for era in ["2017","2018"]:
        emb_era=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_emb_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        tt_era=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_tt_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        ff_era=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_ff_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        misc_era=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_misc_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        nmssm_era=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_NMSSM_MH500_3_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        emb_era=taylor_norm(emb_era)
        ff_era=taylor_norm(ff_era)
        tt_era=taylor_norm(tt_era)
        misc_era=taylor_norm(misc_era)
        nmssm_era=taylor_norm(nmssm_era)
        emb=np.vstack((emb,emb_era))
        tt=np.vstack((tt,tt_era))
        ff=np.vstack((ff,ff_era))
        misc=np.vstack((misc,misc_era))
        nmssm=np.vstack((nmssm,nmssm_era))


else: 
    emb=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_emb_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    tt=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_tt_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    ff=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_ff_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    misc=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_misc_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    nmssm=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings_gpu_py3/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}_500_3/fold0_keras_taylor_ranking_NMSSM_MH500_3_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    emb=taylor_norm(emb)
    ff=taylor_norm(ff)
    tt=taylor_norm(tt)
    misc=taylor_norm(misc)
    nmssm=taylor_norm(nmssm)

# print(np.mean(((emb[:,2].astype(np.float))/np.sum(emb[:,2].astype(np.float)))[0]+((tt[:,2].astype(np.float))/np.sum(tt[:,2].astype(np.float)))[0]+((ff[:,2].astype(np.float))/np.sum(ff[:,2].astype(np.float)))[0]+((misc[:,2].astype(np.float))/np.sum(misc[:,2].astype(np.float)))[0]+((nmssm[:,2].astype(np.float))/np.sum(nmssm[:,2].astype(np.float)))[0]))
if "tt" in args.channel:
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
    #,"NMSSM_light_mass"
    ,"2016"
    ,"2017"
    ,"2018"]
    ranks=len(vars)**2/2+len(vars)+len(vars)/2
else:
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
    #,"NMSSM_light_mass"
    ,"2016"
    ,"2017"
    ,"2018"]
    ranks=len(vars)**2/2+len(vars)+len(vars)/2

vars_dict={}
for var in vars:
    vars_dict[var]=[]
if args.node == "all":
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

for key in vars_dict:
    for t in range(taylor_ranks.shape[0]):
        if taylor_ranks[t][1].find(",") != -1:
            taylor_vars=taylor_ranks[t][1].replace(" ","").split(",")
            if key == taylor_vars[0] or key == taylor_vars[1]:
                vars_dict[key].append(float(taylor_ranks[t][2]))
        else:
            taylor_vars=taylor_ranks[t][1].replace(" ","")
            if key == taylor_vars:
                vars_dict[key].append(float(taylor_ranks[t][2]))
sums={}
for i,key in enumerate(vars_dict.keys()):
    sums[key]=sum(vars_dict[key])

sort=sorted(sums.items(), key=lambda item: item[1])
sorted_dict = {k: v for k, v in sort}

normed_summed_coeff=np.asarray(list(sorted_dict.values()))/np.sum(np.asarray(list(sorted_dict.values())))
print(list(sorted_dict.keys()))
print(normed_summed_coeff)
plt.plot(normed_summed_coeff,range(len(sorted_dict)),marker=".",markersize=7 ,linestyle="")
plt.yticks(range(len(sorted_dict)),list(sorted_dict.keys()))
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.xlabel("normalized sum of taylor coefficients",fontsize=16)
plt.ylabel("variable",fontsize=16)
plt.savefig("plots/{tag}/summed_2d_taylorscore_{era}_{channel}_{node}.png".format(tag=args.tag,era=args.era,channel=args.channel,node=args.node))
plt.savefig("plots/{tag}/summed_2d_taylorscore_{era}_{channel}_{node}.pdf".format(tag=args.tag,era=args.era,channel=args.channel,node=args.node))
#plt.show()
