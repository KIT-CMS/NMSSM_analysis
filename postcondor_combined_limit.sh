#script to print the condor output in jsons, combine all jsons and scale them with 0.1

for tag in parametrized_nn_mH1000 #pNN_all_signalrandom_mH1000 pNN_interpol_signalrandom_mH1000 #pNN_interpol_signaltrue_mH1000 #
do 
    for job in 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229
    do
        ./CMSSW_10_2_16_UL/src/create_combined_limit_nmssm_postcondor.sh 2016,2017,2018 all 1000 3 ${job} ${tag}
    done
    #python merge_jsons.py --input fit_output/${tag}/*.json --output fit_output/${tag}/nmssm_all_1000_cmb.json
done 

