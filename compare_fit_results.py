import json
import matplotlib.pyplot as plt
import numpy as np 

obs_new=np.zeros(9)
obs_old=np.zeros(9)
obs_janek=np.zeros(9)
ratio_new=np.zeros(9)
ratio_janek=np.zeros(9)

i=0
for era in ["2016","2017","2018"]:
    for ch in ["et","mt","tt"]:
        if "tt" in ch:
            old=open("fit_output/old_framework/other_limits_50_50/output_{era}_{ch}_500_3_nmssm_500_110/nmssm_{ch}_500_3_500_110_cmb.json".format(era=era, ch=ch))

        else:
            old=open("fit_output/old_framework/output_{era}_{ch}_500_3_nmssm_500_110/nmssm_{ch}_500_3_500_110_cmb.json".format(era=era, ch=ch))
        new=open("fit_output/new_framework/output_{era}_{ch}_500_3_nmssm_500_110/nmssm_{ch}_500_3_500_110_cmb.json".format(era=era, ch=ch))

        #old=open("fit_output/old_framework/output_{era}_{ch}_500_3_nmssm_500_110/nmssm_{ch}_500_3_500_110_cmb.json".format(era=era, ch=ch))
        janek=open("fit_output/old_framework/janekfile_output_{era}_{ch}_500_3_nmssm_500_110/nmssm_{ch}_500_3_500_110_cmb.json".format(era=era, ch=ch))
        newfile=json.load(new)
        oldfile=json.load(old)
        janekfile=json.load(janek)
        print(era, ch)
        newfile=newfile["110.0"]
        oldfile=oldfile["110.0"]
        janekfile=janekfile["110.0"]
        obs_old[i]=oldfile["obs"]
        obs_new[i]=newfile["obs"]
        obs_janek[i]=janekfile["obs"]
        i+=1
        print(oldfile["exp+1"],oldfile["exp+2"],oldfile["exp-1"],oldfile["exp-2"],oldfile["exp0"], oldfile["obs"])
        print(newfile["exp+1"],newfile["exp+2"],newfile["exp-1"],newfile["exp-2"],newfile["exp0"], newfile["obs"])        
        print(janekfile["exp+1"],janekfile["exp+2"],janekfile["exp-1"],janekfile["exp-2"],janekfile["exp0"], janekfile["obs"])

era_ch=["et16","mt16","tt16","et17","mt17","tt17","et18","mt18","tt18"]
plt.plot(era_ch,obs_new/obs_old,label="new/old")
plt.plot(era_ch,obs_janek/obs_old,label="janekfile/old")
plt.legend()
plt.ylabel("ratio")
plt.xlabel("channel_era")
plt.savefig("fit_sync50.png")

