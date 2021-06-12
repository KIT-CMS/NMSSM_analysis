#script to print the condor output in jsons, combine all jsons and scale them with 0.1

# tag=$1

# for job in 203 218 223 229 #203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 
# do
#     ./CMSSW_10_2_16_UL/src/create_combined_limit_nmssm_postcondor.sh 2016,2017,2018 all 1000 0 ${job} ${tag}
# done

tag=$1
for job in 48 132 #5 18 29 38 62 73 85 108 125 145 172 193 292 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229
do 
    ./CMSSW_10_2_16_UL/src/create_combined_limit_nmssm_postcondor.sh 2016,2017,2018 all 1000 0 ${job} ${tag}
done

# for lm in 60 70 75 80 85 90 95 100 110 120 130 150 170 190 250 300 350 400 450 500 550 600 650 700 750 800 850
# do 
#     cp fit_output/${tag}/${lm}/*.json fit_output/${tag}/
# done
#python merge_jsons.py --input fit_output/${tag}/*cmb.json --output fit_output/${tag}/nmssm_all_1000_cmb.json
#python merge_jsons.py --input fit_output/${tag}/nmssm_all_1000_0_1000* --output fit_output/${tag}/nmssm_all_1000_cmb.json
#mkdir -p plots/${tag}/limits/

#python CMSSW_10_2_16_UL/src/CombineHarvester/MSSMvsSMRun2Legacy/scripts/compare_nmssm_limits.py /work/jbechtel/postprocessing/nmssm/train_all/limit_jsons/nmssm_combined_all_1000_cmb.json  fit_output/10_onenet/nmssm_all_1000_cmb.json:exp0:Title="Expected (14 classes)",LineStyle=7,LineWidth=3,LineColor=46,MarkerSize=0 fit_output/${tag}/nmssm_all_1000_cmb.json:exp0:Title="Expected (14 classes/1 signalclass)",LineStyle=7,LineWidth=3,LineColor=36,MarkerSize=0 --cms-sub "Own Work" --title-right "137 fb^{-1} (13 TeV)" --y-axis-min 0.001 --y-axis-max 1.0  --show exp  --output plots/${tag}/limits/comparison --logy --process "nmssm" --title-left "all" --xmax 850.0  --logx --ratio-to /work/jbechtel/postprocessing/nmssm/train_all/limit_jsons/nmssm_combined_all_1000_cmb.json:exp0

# python CMSSW_10_2_16_UL/src/CombineHarvester/MSSMvsSMRun2Legacy/scripts/compare_nmssm_limits.py nmssm_combined_all_1000_batch4.json  pNN_balanced.json:exp0:Title="Expected (pNN balanced batches)",LineStyle=7,LineWidth=3,LineColor=46,MarkerSize=0 fit_output/pNN_balanced_batch4_mH1000/nmssm_all_1000_cmb.json:exp0:Title="Expected (pNN balanced batch 4)",LineStyle=7,LineWidth=3,LineColor=36,MarkerSize=0 --cms-sub "Own Work" --title-right "137 fb^{-1} (13 TeV)" --y-axis-min 0.001 --y-axis-max 1.0  --show exp  --output plots/pNN_balanced_batch4_mH1000/limits/comparison --logy --process "nmssm" --title-left "all" --xmax 850.0  --logx --ratio-to nmssm_combined_all_1000_batch4.json:exp0

#fit_output/${tag}/nmssm_all_1000_cmb.json:exp0:Title="Expected (pNN batch 4)",LineStyle=7,LineWidth=3,LineColor=36,MarkerSize=0
