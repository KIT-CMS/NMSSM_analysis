
# for ch in tt
# do
#     for era in 2016 2017 2018
#     do
#         ./utils/fit_cmssw.sh ${era} ${ch} 500 3 500 110
#     done 
# done #
mkdir condor_inter_rand
cd condor_inter_rand
for tag in  pNN_interpol_signalrandom_mH1000 #pNN_interpol_signalrandom_mH1000 pNN_interpol_signaltrue_mH1000 pNN_all_signalrandom_mH1000#
do 
    for job in 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229
    do
        .././CMSSW_10_2_16_UL/src/create_combined_limit_nmssm_condor_tag.sh 2016,2017,2018 all 1000 3 ${job} condor ${tag}
    done
done 