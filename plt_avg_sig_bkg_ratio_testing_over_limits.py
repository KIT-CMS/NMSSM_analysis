import json
import argparse
import os
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
parser = argparse.ArgumentParser()
parser.add_argument('--mass', type=str)
args=parser.parse_args()


path='/work/fheyen/nmsmm_framework/NMSSM_analysis_loads_of_nets/output/fitoutput/{}'.format(args.mass)

paths=[]
all_limits=[]
minlim=9999.
maxlim=0.
midlim=0.
mylist=[]


for myfile in os.listdir(path):
    filepath='/work/fheyen/nmsmm_framework/NMSSM_analysis_loads_of_nets/output/fitoutput/{}/{}'.format(args.mass,myfile)
    myobj=open(filepath)
    data=json.load(myobj)
    limit=data['{}.0'.format(args.mass)]['exp0']
    print('file: ' + str(filepath) + ' --- limit: ' + str(limit))  

    number=filepath.split("_")[-4]
    mylist.append([limit,int(number)])
    all_limits.append(limit)
    paths.append(filepath)
    myobj.close()


sort_by_value_list = sorted(mylist, key=lambda x: x[0])
sort_by_number_list = sorted(mylist, key=lambda x: x[1])
limits_by_number = list(map(itemgetter(0),sort_by_number_list))
print(sort_by_number_list)
print(limits_by_number)
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

ratios=[nmssm_avg_ratio,emb_avg_ratio,ff_avg_ratio,misc_avg_ratio, tt_avg_ratio]
tot_ratio=nmssm_avg_ratio/np.mean(nmssm_avg_ratio)+emb_avg_ratio/np.mean(emb_avg_ratio)+ff_avg_ratio/np.mean(ff_avg_ratio)+misc_avg_ratio/np.mean(misc_avg_ratio)+ tt_avg_ratio/np.mean(tt_avg_ratio)
no_mean_ratio=nmssm_avg_ratio+emb_avg_ratio+ff_avg_ratio+misc_avg_ratio+tt_avg_ratio
print(no_mean_ratio[1])
plt.plot(limits_by_number,ratios[0],linestyle="",marker=".",markersize=7)
plt.xlim(0.03,0.08)
plt.xlabel(r"$95 \% \; \mathrm{CL}$")
plt.ylabel(r"$ \langle r \rangle_{\mathrm{NMSSM}}$")
plt.savefig("plots/Felix_50_trainings_early_stopping/total_ratio_over_limits_NMSSM.png")
plt.show()
