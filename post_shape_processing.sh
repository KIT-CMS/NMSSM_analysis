ulimit -s unlimited
TAG=68_onenet_1nmssmclass
source /cvmfs/sft.cern.ch/lcg/views/LCG_98python3/x86_64-centos7-gcc9-opt/setup.sh
#source /cvmfs/sft-nightlies.cern.ch/lcg/views/dev3/latest/x86_64-centos7-gcc10-opt/setup.sh
export PYTHONPATH=$PWD:$PYTHONPATH

for era in 2018 #2016 2017 2018
do 
    for ch in  tt #et mt #tt
    do
        #echo "${era}-${ch}"
        mkdir -p output/${TAG}/uncert_shapes/
        for proc in data emb ggh qqh vh tth zl ttl vvl ttt NMSSM_1000_125_60 NMSSM_1000_125_70 NMSSM_1000_125_75 NMSSM_1000_125_80 NMSSM_1000_125_85 NMSSM_1000_125_90 NMSSM_1000_125_95 NMSSM_1000_125_100 NMSSM_1000_125_110 NMSSM_1000_125_120 NMSSM_1000_125_130 NMSSM_1000_125_150 NMSSM_1000_125_170 NMSSM_1000_125_190 NMSSM_1000_125_250 NMSSM_1000_125_300 NMSSM_1000_125_350 NMSSM_1000_125_400 NMSSM_1000_125_450 NMSSM_1000_125_500 NMSSM_1000_125_550 NMSSM_1000_125_600 NMSSM_1000_125_650 NMSSM_1000_125_700 NMSSM_1000_125_750 NMSSM_1000_125_800 NMSSM_1000_125_850
        #data emb ggh qqh vh tth ztt zl zj ttt ttl ttj vvt vvl vvj w 
        do
            #echo $proc
            for dic in output/shapes/analysis_unit_graphs-${TAG}-${era}-${ch}-${proc}-*
            do
                for input in ${dic}/*
                do
                    #echo "${input}"
                    python shapes/sort_hists.py --era ${era} --channel ${ch} --input ${input} --output output/${TAG}/uncert_shapes/ -n 1
                done
            done
        done
        for lm in 60 70 75 80 85 90 95 100 110 120 130 150 170 190 250 300 350 400 450 500 550 600 650 700 750 800 850
        do 
            #echo "${era}-${ch}-${lm}"
            bash shapes/do_estimations.sh ${era} output/${TAG}/uncert_shapes/${lm}/${era}-${ch}.root 0
            #rm output/${TAG}/uncert_shapes/${lm}/htt_${ch}.inputs-nmssm-${era}-${ch}_max_score_1000_3.root
            python shapes/convert_to_synced_shapes_org.py --era ${era} --input output/${TAG}/uncert_shapes/${lm}/${era}-${ch}.root --output output/${TAG}/uncert_shapes/${lm}/ -n 12
            hadd output/${TAG}/uncert_shapes/${lm}/htt_${ch}.inputs-nmssm-${era}-${ch}_max_score_1000_0.root output/${TAG}/uncert_shapes/${lm}/htt_${ch}.inputs-nmssm-${era}-${ch}_max_score_1000_0*
        done
    done
done 

# for batch in 1 2 3 4 5 6 7
# do
#     for ERA in  2016 2017 2018
#     do
#         for CHANNEL in  et mt tt
#         do         
#             # #rm -rf output/${TAG}/uncert_shapes/${batch}/${ERA}-${CHANNEL}
#             # mkdir -p output/${TAG}/uncert_shapes/${batch}/${ERA}-${CHANNEL}
#             # for sample in backgrounds1 backgrounds2 backgrounds3 backgrounds4 sm_signals nmssm_mH1000
#             # #data emb ggh qqh vh tth ztt zl zj ttt ttl ttj vvt vvl vvj w NMSSM_1000_125_60 NMSSM_1000_125_70 NMSSM_1000_125_75 NMSSM_1000_125_80 NMSSM_1000_125_85 NMSSM_1000_125_90 NMSSM_1000_125_95 NMSSM_1000_125_100 NMSSM_1000_125_110 NMSSM_1000_125_120 NMSSM_1000_125_130 NMSSM_1000_125_150 NMSSM_1000_125_170 NMSSM_1000_125_190 NMSSM_1000_125_250 NMSSM_1000_125_300 NMSSM_1000_125_350 NMSSM_1000_125_400 NMSSM_1000_125_450 NMSSM_1000_125_500 NMSSM_1000_125_550 NMSSM_1000_125_600 NMSSM_1000_125_650 NMSSM_1000_125_700 NMSSM_1000_125_750 NMSSM_1000_125_800 NMSSM_1000_125_850
#             # do        
#             #     echo "${TAG}-${ERA}-${CHANNEL}-${sample}-${batch}"
#             #     cp -r output/shapes/analysis_unit_graphs-${TAG}-${ERA}-${CHANNEL}-${sample}-${batch}/* output/${TAG}/uncert_shapes/${batch}/${ERA}-${CHANNEL}     
#             # done
#             # ls output/${TAG}/uncert_shapes/${batch}
#             # hadd output/${TAG}/uncert_shapes/${batch}/${ERA}-${CHANNEL}.root output/${TAG}/uncert_shapes/${batch}/${ERA}-${CHANNEL}/*
            
#             # bash shapes/do_estimations.sh ${ERA} output/${TAG}/uncert_shapes/${batch}/${ERA}-${CHANNEL}.root 0
#             # python shapes/convert_to_synced_shapes_org.py --era ${ERA} --input output/${TAG}/uncert_shapes/${batch}/${ERA}-${CHANNEL}.root --output output/${TAG}/uncert_shapes/${batch}/ -n 12
#             # hadd output/${TAG}/uncert_shapes/${batch}/htt_${CHANNEL}.inputs-nmssm-${ERA}-${CHANNEL}_max_score_1000_3.root output/${TAG}/uncert_shapes/${batch}/htt_${CHANNEL}.inputs-nmssm-${ERA}-${CHANNEL}_max_score_1000_0*
#             mv output/janek_nottclass_inttchannel/uncert_shapes/${batch}/htt_${CHANNEL}.inputs-nmssm-${ERA}-${CHANNEL}_max_score_1000_3.root output/janek_nottclass_inttchannel/uncert_shapes/${batch}/htt_${CHANNEL}.inputs-nmssm-${ERA}-${CHANNEL}_max_score_1000_${batch}.root 
#         done 
#     done
#     # for ERA in 2016 2017
#     # do 
#     # for CHANNEL in tt
#     # do
#     # python shapes/convert_to_synced_shapes_org.py --era ${ERA} --input output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}.root --output output/${TAG}/uncert_shapes/synced_shapes/ -n 12
#     # hadd output/${TAG}/uncert_shapes/synced_shapes/htt_${CHANNEL}.inputs-nmssm-${ERA}-${CHANNEL}_max_score_1000_3.root output/${TAG}/uncert_shapes/synced_shapes/${ERA}-${CHANNEL}-synced-NMSSM*
#     # done
#     # done
# done