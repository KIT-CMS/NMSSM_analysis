import numpy as np 
import matplotlib.pyplot as plt


n=50
classes=["emb","tt","misc","ff","NMSSM_MH1000_4"]
nmssm_avg_ratio=np.zeros(n)
emb_avg_ratio=np.zeros(n)
ff_avg_ratio=np.zeros(n)
misc_avg_ratio=np.zeros(n)
tt_avg_ratio=np.zeros(n)

for i in range(n):
    for j,class_ in enumerate(classes):
        true_fold0=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings/sm-htt-analysis/output/ml/2018_tt_1000_4_{test}/fold0_hist_true_None_{class_}.txt".format(test=i+1,class_=class_))
        false_fold0=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings/sm-htt-analysis/output/ml/2018_tt_1000_4_{test}/fold0_hist_false_None_{class_}.txt".format(test=i+1,class_=class_))
        true_fold1=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings/sm-htt-analysis/output/ml/2018_tt_1000_4_{test}/fold1_hist_true_None_{class_}.txt".format(test=i+1,class_=class_))
        false_fold1=np.loadtxt("/work/rschmieder/nmssm_analysis_68trainings/sm-htt-analysis/output/ml/2018_tt_1000_4_{test}/fold1_hist_false_None_{class_}.txt".format(test=i+1,class_=class_))
        sum_=0
        count=0
        for l in range(len(true_fold0)):
            if true_fold0[l] > 1 and false_fold0[l]>1:
                sum_+=true_fold0[l]/false_fold0[l]
                count+=1 
            elif true_fold1[l] > 1 and false_fold1[l]>1:
                sum_+=true_fold1[l]/false_fold1[l]
                count+=1
                
        #print(i,j,sum_,count)
        avg_ratio=sum_/float(count)
        if j==0:
            emb_avg_ratio[i]=avg_ratio
        if j==1:
            tt_avg_ratio[i]=avg_ratio
        if j==2:
            misc_avg_ratio[i]=avg_ratio
        if j==3:
            ff_avg_ratio[i]=avg_ratio
        else:
            nmssm_avg_ratio[i]=avg_ratio
        if i==12:
            print(true_fold0)

ratios=[nmssm_avg_ratio/np.mean(nmssm_avg_ratio),emb_avg_ratio/np.mean(emb_avg_ratio),ff_avg_ratio/np.mean(ff_avg_ratio),misc_avg_ratio/np.mean(misc_avg_ratio), tt_avg_ratio/np.mean(tt_avg_ratio)]

#print(nmssm_avg_ratio[38])
print("nmssm")
print(nmssm_avg_ratio[34], nmssm_avg_ratio[12],nmssm_avg_ratio[36],nmssm_avg_ratio[6])
print("emb")
print(emb_avg_ratio[34],emb_avg_ratio[12],emb_avg_ratio[36],emb_avg_ratio[6])
print("ff")
print(ff_avg_ratio[34],ff_avg_ratio[12],ff_avg_ratio[36],ff_avg_ratio[6])
print("misc")
print(misc_avg_ratio[34],misc_avg_ratio[12],misc_avg_ratio[36],misc_avg_ratio[6])
print("tt")
print(tt_avg_ratio[34],tt_avg_ratio[12],tt_avg_ratio[36],tt_avg_ratio[6])

print("ratios best/worst: nmssm, emb, ff, misc, tt")
print(nmssm_avg_ratio[6]/nmssm_avg_ratio[12],emb_avg_ratio[6]/emb_avg_ratio[12],ff_avg_ratio[6]/ff_avg_ratio[12],misc_avg_ratio[6]/misc_avg_ratio[12],tt_avg_ratio[6]/tt_avg_ratio[12])
print(nmssm_avg_ratio[np.argmax(nmssm_avg_ratio)],nmssm_avg_ratio[np.argmin(nmssm_avg_ratio)])
labels=["nmssm","emb","jetfakes","misc","tt"]
for i,ratio in enumerate(ratios):
    plt.hist(ratio,histtype='step',label=labels[i])
plt.legend()
plt.xlabel("average signal background ratio")
plt.ylabel("number of networks")
plt.savefig("plots/Felix_50_trainings_early_stopping/avg_signal_bkg_ratio.png")
plt.close()
