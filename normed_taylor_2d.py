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

args = parser.parse_args()

def taylor_norm(taylor_ranks):
    sum_taylor_ranks=0
    for t in range(taylor_ranks.shape[0]):
        sum_taylor_ranks+=float(taylor_ranks[t][2])
    for t in range(taylor_ranks.shape[0]):
        taylor_ranks[t][2]=float(taylor_ranks[t][2])/sum_taylor_ranks
    return taylor_ranks

if args.era == "all_eras":
    emb=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_emb_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    tt=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_tt_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    ff=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_ff_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    misc=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_misc_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    nmssm=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_NMSSM_2016.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    emb=taylor_norm(emb)
    ff=taylor_norm(ff)
    tt=taylor_norm(tt)
    misc=taylor_norm(misc)
    nmssm=taylor_norm(nmssm)
    for era in ["2017","2018"]:
        emb_era=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_emb_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        tt_era=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_tt_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        ff_era=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_ff_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        misc_era=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_misc_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")
        nmssm_era=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_NMSSM_{era}.txt".format(tag=args.tag,ch=args.channel,era=era),dtype=str,delimiter=":")

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
    emb=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_emb_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    tt=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_tt_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    ff=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_ff_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    misc=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_misc_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    nmssm=np.loadtxt("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/{tag}/all_eras_{ch}/fold0_keras_taylor_ranking_NMSSM_{era}.txt".format(tag=args.tag,ch=args.channel,era=args.era),dtype=str,delimiter=":")
    emb=taylor_norm(emb)
    ff=taylor_norm(ff)
    tt=taylor_norm(tt)
    misc=taylor_norm(misc)
    nmssm=taylor_norm(nmssm)

taylor_ranks=np.vstack((emb,tt,ff,misc,nmssm))

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
    ,"NMSSM_light_mass"
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
    ,"NMSSM_light_mass"
    ,"2016"
    ,"2017"
    ,"2018"]
    ranks=len(vars)**2/2+len(vars)+len(vars)/2

#vars=["pt_1","NMSSM_light_mass"]
vars_dict={}
i=0
for var in vars:
    vars_dict[var]=[]
    for var2 in vars[i:]:
        vars_dict[var+","+var2]=[]
    i+=1




for key in vars_dict:
    if key.find(",") !=-1:
        key_vars=key.split(",")
        for t in range(taylor_ranks.shape[0]):
            if taylor_ranks[t][1].find(",") != -1:
                taylor_vars=taylor_ranks[t][1].replace(" ","").split(",")
                if (key_vars[0] == taylor_vars[0] and key_vars[1] == taylor_vars[1]) or (key_vars[0] == taylor_vars[1] and key_vars[1] == taylor_vars[0]):
                    vars_dict[key].append(float(taylor_ranks[t][2]))
    else:
        for t in range(taylor_ranks.shape[0]):
            if taylor_ranks[t][1].find(",") == -1:
                taylor_vars=taylor_ranks[t][1].replace(" ","")
                if key == taylor_vars:
                    vars_dict[key].append(float(taylor_ranks[t][2]))

i=0
for key in vars_dict:
    if len(vars_dict[key]) != 0:
        i+=1
        vars_dict[key]=round(sum(vars_dict[key])/len(vars_dict[key]),10)
    else:
        vars_dict[key]=0.

coeff=np.zeros(len(vars_dict))
i=0
for value in vars_dict.values():
    coeff[i]=value
    i+=1
coeff_sort=np.sort(coeff)[::-1]
fig = plt.figure()
ax = plt.subplot(111)
i=0
first_order=[]
first_rank=[]
second_order=[]
second_rank=[]
key_sort=[]
for tcoeff in coeff_sort:
    for key in vars_dict:
        if (round(vars_dict[key],10) == round(tcoeff,10)):
            if key.find(",") !=-1:
                second_order.append(vars_dict[key])
                second_rank.append(i)
                key_sort.append(key)
            else:
                first_order.append(vars_dict[key])
                first_rank.append(i)
                key_sort.append(key)
            i+=1

np.savetxt("plots/{tag}/normed_2dtaylorranking_{era}_{channel}.txt".format(tag=args.tag,era=args.era,channel=args.channel),key_sort,fmt="%s")
ax.plot(second_rank,second_order,marker="x", markersize=5, linestyle=" ", markeredgecolor="b" ,label="2. order")
ax.plot(first_rank,first_order,marker="x", markersize=5,linestyle=" ", markeredgecolor="r" ,label="1. order")
plt.legend()
plt.ylabel("normed Taylor score")
plt.xlabel("Taylor rank")
plt.savefig("plots/{tag}/normed_2dtaylorranking_{era}_{channel}.png".format(tag=args.tag,era=args.era,channel=args.channel))
plt.savefig("plots/{tag}/normed_2dtaylorranking_{era}_{channel}.pdf".format(tag=args.tag,era=args.era,channel=args.channel))
#plt.show()