ulimit -s unlimited
TAG=pNN_interpol_signalrandom_mH1000
for ERA in 2016 2017 2018
do
    for CHANNEL in  et mt tt
    do         
        echo "${ERA}-${CHANNEL}"
        mkdir -p output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}
        for sample in nmssm_mH1000 backgrounds3 backgrounds4 sm_signals backgrounds1 backgrounds2 
       #nmssm_split1 nmssm_split2 nmssm_split3 nmssm_split4 nmssm_split5 nmssm_split6 nmssm_split7 nmssm_split8 nmssm_split9 nmssm_split_10 nmssm_split_11 nmssm_split_12 nmssm_split_13 nmssm_split_14 nmssm_split_15 nmssm_split_16 nmssm_split_17 nmssm_split_18 nmssm_split_19 nmssm_split_20
        do            
            cp -r output/shapes/analysis_unit_graphs-${TAG}-${ERA}-${CHANNEL}-${sample}/* output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}     
        done
        hadd output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}.root output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}/*
        bash shapes/do_estimations.sh ${ERA} output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}.root 0
        mkdir -p output/${TAG}/uncert_shapes/synced_shapes/
        python shapes/convert_to_synced_shapes.py --era ${ERA} --input output/${TAG}/uncert_shapes/${ERA}-${CHANNEL}.root --output output/${TAG}/uncert_shapes/synced_shapes/ -n 12
        hadd output/${TAG}/uncert_shapes/synced_shapes/htt_${CHANNEL}.inputs-nmssm-${ERA}-${CHANNEL}_max_score_1000_3.root output/${TAG}/uncert_shapes/synced_shapes/htt_${CHANNEL}.inputs-nmssm-${ERA}-${CHANNEL}_max_score_1000_3*
    done 
done
