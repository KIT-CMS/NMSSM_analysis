import numpy as np 
import matplotlib.pyplot as plt

n=50
nmssm_avg_score=np.zeros(n)
emb_avg_score=np.zeros(n)
ff_avg_score=np.zeros(n)
misc_avg_score=np.zeros(n)
tt_avg_score=np.zeros(n)
nmssm_avg_score_true=np.zeros(n)
emb_avg_score_true=np.zeros(n)
ff_avg_score_true=np.zeros(n)
misc_avg_score_true=np.zeros(n)
tt_avg_score_true=np.zeros(n)
#tot_avg_score=np.zeros(n)
for i in range(n):
    data = np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings/sm-htt-analysis/output/ml/2018_tt_1000_4_{test}/fold0_summed_score_None.txt".format(test=i+1))
    emb_avg_score[i]=data[0][0]/data[0][1]
    ff_avg_score[i]=data[3][0]/data[3][1]
    misc_avg_score[i]=data[2][0]/data[2][1]
    tt_avg_score[i]= data[1][0]/data[1][1]
    nmssm_avg_score[i] = data[4][0]/data[4][1]
    # tot_avg_score[i]=np.mean([data[0][1]/data[0][2],data[1][1]/data[1][2],data[4][1]/data[4][2],data[2][1]/data[2][2],data[3][1]/data[3][2]])
    print(i,emb_avg_score[i],ff_avg_score[i],misc_avg_score[i],tt_avg_score[i],nmssm_avg_score[i])
print("")
for i in range(n):
    data = np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings/sm-htt-analysis/output/ml/2018_tt_1000_4_{test}/fold0_summed_score_None_true_positives.txt".format(test=i+1))
    emb_avg_score_true[i]=data[0][0]/data[0][1]
    ff_avg_score_true[i]=data[3][0]/data[3][1]
    misc_avg_score_true[i]=data[2][0]/data[2][1]
    tt_avg_score_true[i]= data[1][0]/data[1][1]
    nmssm_avg_score_true[i] = data[4][0]/data[4][1]
    # tot_avg_score_true[i]=np.mean([data[0][1]/data[0][2],data[1][1]/data[1][2],data[4][1]/data[4][2],data[2][1]/data[2][2],data[3][1]/data[3][2]])
    print(i,emb_avg_score_true[i],ff_avg_score_true[i],misc_avg_score_true[i],tt_avg_score_true[i],nmssm_avg_score_true[i])

#print(emb_avg_score/np.mean(emb_avg_score),ff_avg_score/np.mean(ff_avg_score),misc_avg_score/np.mean(misc_avg_score),tt_avg_score/np.mean(tt_avg_score),nmssm_avg_score/np.mean(nmssm_avg_score))
scores=[nmssm_avg_score,emb_avg_score,ff_avg_score,misc_avg_score,tt_avg_score]
scores_true=[nmssm_avg_score_true,emb_avg_score_true,ff_avg_score_true,misc_avg_score_true,tt_avg_score_true]
print(nmssm_avg_score[6]/nmssm_avg_score[12],emb_avg_score[6]/emb_avg_score[12],ff_avg_score[6]/ff_avg_score[12],misc_avg_score[6]/misc_avg_score[12],tt_avg_score[6]/tt_avg_score[12])
print(nmssm_avg_score_true[6]/nmssm_avg_score_true[12],emb_avg_score_true[6]/emb_avg_score_true[12],ff_avg_score_true[6]/ff_avg_score_true[12],misc_avg_score_true[6]/misc_avg_score_true[12],tt_avg_score_true[6]/tt_avg_score_true[12])
labels=["nmssm","emb","jetfakes","misc","tt"]
for i,score in enumerate(scores):
    plt.hist(score/np.mean(score),histtype='step',label=labels[i])
plt.legend()
plt.xlabel("average score")
plt.ylabel("number of networks")
plt.savefig("plots/Felix_50_trainings_early_stopping/all_scores.png")
plt.close()

for i,score in enumerate(scores_true):
    plt.hist(score/np.mean(score),histtype='step',label=labels[i])
plt.legend()
plt.xlabel("average score")
plt.ylabel("number of networks")
plt.savefig("plots/Felix_50_trainings_early_stopping/all_scores_true.png")