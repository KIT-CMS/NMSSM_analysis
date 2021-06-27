import numpy as np 
import matplotlib.pyplot as plt
import json
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

#  import seaborn as sns
#  import pandas as pd
def main():
    files=[]
    exp_limits_procs = ["240_90" , 
                "280_120",
                "320_110",
                "360_80",
                #"360_190",
                "400_190",
                "450_120",
                "500_90",
                "550_150",
                "600_130",
                "600_400",
                "700_150",
                "700_500",
                "800_400",
                "900_300",
                "1000_150",
                "1000_800",
                "1600_600",        
                ]

    

    stats=[]
    stats2=[]
    for procs in exp_limits_procs:
        heavy_mass=procs.split("_")[0]+".0"
        light_mass=procs.split("_")[1]+".0"
        new_file= "fit_output/10_onenet/nmssm_all_1000_0_{procs}_cmb.json".format(procs=procs)
        ref_file="/work/jbechtel/postprocessing/nmssm/train_all/limit_jsons/nmssm_combined_all_{hm}_cmb.json".format(hm=procs.split("_")[0])
        stand_file=  "fit_output/10_onenet_summed_0_5/nmssm_all_1000_0_{procs}_cmb.json".format(procs=procs)
        with open(new_file,"r") as f:
            in_dict = json.load(f)
        with open(ref_file,"r") as f:
            ref_dict = json.load(f)
        with open(stand_file,"r") as f:
            stand_dict = json.load(f)
        temp_dict={}
        temp_dict["label"]=procs
        temp_dict2={}
        temp_dict2["label"]=procs
        for key in ref_dict[light_mass].keys():
            if 'exp-2' in key:
                temp_dict["whislo"]=ref_dict[light_mass][key]/ref_dict[light_mass]["exp0"]  
                temp_dict2["whislo"]=ref_dict[light_mass][key]/ref_dict[light_mass]["exp0"]
            elif 'exp-1' in key:
                temp_dict["q1"]=ref_dict[light_mass][key]/ref_dict[light_mass]["exp0"]  
                temp_dict2["q1"]=ref_dict[light_mass][key]/ref_dict[light_mass]["exp0"]  
            elif 'exp0' in key:
                temp_dict["med"]=in_dict[light_mass][key]*0.1/ref_dict[light_mass][key]    
                temp_dict2["med"]=stand_dict[light_mass][key]*0.1/ref_dict[light_mass][key]
            elif 'exp+1' in key:
                temp_dict["q3"]=ref_dict[light_mass][key]/ref_dict[light_mass]["exp0"] 
                temp_dict2["q3"]=ref_dict[light_mass][key]/ref_dict[light_mass]["exp0"]
            elif 'exp+2' in key:
                temp_dict["whishi"]=ref_dict[light_mass][key]/ref_dict[light_mass]["exp0"]  
                temp_dict2["whishi"]=ref_dict[light_mass][key]/ref_dict[light_mass]["exp0"]
        stats.append(temp_dict)
        stats2.append(temp_dict2)
    medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')
    medianprops2 = dict(linestyle='-.', linewidth=2.5, color='b')
    fig,axes=plt.subplots(figsize=(8,8))
    axes.bxp(stats,showfliers=False,vert=False,medianprops=medianprops)
    axes.bxp(stats2,showfliers=False,vert=False,medianprops=medianprops2)
    plt.vlines(1,0.5, len(exp_limits_procs)+0.5,linestyles="dashed")
    plt.xlabel("ratio",fontsize=16)
    plt.ylabel(r'$\mathrm{m(H)}$'+'_'+r'$\mathrm{m(h_{S})}$',fontsize=16)
    plt.xlabel("ratio",fontsize=16)
    plt.subplots_adjust(bottom=.1, left=.15)
    legend_elements = [Line2D([], [], color='firebrick', marker='|', linestyle='None',
                          markersize=10, markeredgewidth=2, label='added scores'),
                           Line2D([], [], color='b', marker='|', linestyle='None',
                           markersize=10, markeredgewidth=2, label='added scores from 0.5')]
    axes.legend(handles=legend_elements)
    #plt.show()
    plt.savefig("plots/10_onenet_summed_0_5/limits/ratio.png")
    
    
if __name__ == "__main__":
    main()
