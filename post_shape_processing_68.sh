ulimit -s unlimited

TAG=10_onenet_summed_0_5
#source /cvmfs/sft.cern.ch/lcg/views/LCG_98python3/x86_64-centos7-gcc9-opt/setup.sh
#source /cvmfs/sft-nightlies.cern.ch/lcg/views/dev3/latest/x86_64-centos7-gcc10-opt/setup.sh
#export PYTHONPATH=$PWD:$PYTHONPATH

for ERA in  2016 2017 2018
do
    for CHANNEL in  et mt tt
    do         
       
        # rm -rf output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}/output-single_graph_job-analysis_unit_graphs-10_onenet-2016-et-NMSSM_360_125_190*
        mkdir -p output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}
        for sample in data emb ggh qqh vh tth zl ttl vvl ttt NMSSM_360_125_190 NMSSM_600_125_400 NMSSM_1000_125_150 NMSSM_1000_125_800 NMSSM_280_125_120 NMSSM_320_125_110 NMSSM_360_125_80 NMSSM_240_125_90 NMSSM_400_125_190 NMSSM_450_125_120 NMSSM_500_125_90 NMSSM_550_125_150 NMSSM_600_125_130  NMSSM_700_125_150 NMSSM_700_125_500 NMSSM_800_125_400 NMSSM_900_125_300 NMSSM_1600_125_600
        #NMSSM_360_125_190 NMSSM_600_125_400 data emb ggh qqh vh tth zl ttl vvl ttt NMSSM_1000_125_60 NMSSM_1000_125_70 NMSSM_1000_125_75 NMSSM_1000_125_80 NMSSM_1000_125_85 NMSSM_1000_125_90 NMSSM_1000_125_95 NMSSM_1000_125_100 NMSSM_1000_125_110 NMSSM_1000_125_120 NMSSM_1000_125_130 NMSSM_1000_125_150 NMSSM_1000_125_170 NMSSM_1000_125_190 NMSSM_1000_125_250 NMSSM_1000_125_300 NMSSM_1000_125_350 NMSSM_1000_125_400 NMSSM_1000_125_450 NMSSM_1000_125_500 NMSSM_1000_125_550 NMSSM_1000_125_600 NMSSM_1000_125_650 NMSSM_1000_125_700 NMSSM_1000_125_750 NMSSM_1000_125_800 NMSSM_1000_125_850 NMSSM_240_125_90 NMSSM_280_125_120 NMSSM_320_125_110 NMSSM_360_125_80 NMSSM_240_125_90 NMSSM_400_125_190 NMSSM_450_125_120 NMSSM_500_125_90 NMSSM_550_125_150 NMSSM_600_125_130  NMSSM_700_125_150 NMSSM_700_125_500 NMSSM_800_125_400 NMSSM_900_125_300 NMSSM_1600_125_600
        do        
            echo "${TAG}-${ERA}-${CHANNEL}-${sample}"
            cp -r output/shapes/analysis_unit_graphs-${TAG}-${ERA}-${CHANNEL}-${sample}-0/* output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}     
        done
        hadd output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}.root output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}/*
        
        bash shapes/do_estimations.sh ${ERA} output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}.root 0

        python shapes/convert_to_synced_shapes_org.py --era ${ERA} --input output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}.root --output output/${TAG}/uncert_shapes/ -n 12

        hadd output/${TAG}/uncert_shapes/htt_${CHANNEL}.inputs-nmssm-${ERA}-${CHANNEL}_max_score_1000_0.root output/${TAG}/uncert_shapes/htt_${CHANNEL}.inputs-nmssm-${ERA}-${CHANNEL}_max_score_1000_0*

    done 
done
