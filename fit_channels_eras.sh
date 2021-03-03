
# for ch in tt
# do
#     for era in 2016 2017 2018
#     do
#         ./utils/fit_cmssw.sh ${era} ${ch} 500 3 500 110
#     done 
# done

for job in 219 223 224 225
do
    ./CMSSW_10_2_16_UL/src/create_combined_limit_nmssm.sh 2016,2017,2018 all 1000 3 ${job}
done
