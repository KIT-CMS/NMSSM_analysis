#script to print the condor output in jsons, combine all jsons and scale them with 0.1

# for tag in pNN_balanced_lm_mH1000_pseudodata_shapebasis #${tag} #parametrized_nn_mH1000 #pNN_all_signalrandom_mH1000 pNN_interpol_signalrandom_mH1000 #pNN_interpol_signaltrue_mH1000 #
# do 
#     for job in 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229  # #2 10 23 31 47 49 61 72 76 85 106 132 142 176 198 213 249 269 285 324 349 369 407
#     #210 # 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229
#     do
#         ./CMSSW_10_2_16_UL/src/create_combined_limit_nmssm_postcondor.sh 2016,2017,2018 all 1000 0 ${job} ${tag}
#     done
#     #python merge_jsons.py --input fit_output/${tag}/*.json --output fit_output/${tag}/nmssm_all_1000_cmb.json
# done 
tag=pNN_balanced_lm_mH1000_pseudodata_shapebasis
for lm in 60 70 75 80 85 90 95 100 110 120 130 150 170 190 250 300 350 400 450 500 550 600 650 700 750 800 850
do 
    cp fit_output/${tag}/${lm}/*.json fit_output/${tag}/
done
python merge_jsons.py --input fit_output/${tag}/*.json --output fit_output/${tag}/nmssm_all_1000_cmb.json