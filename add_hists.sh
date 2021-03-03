ulimit -s unlimited
 
for era in 2016 2017 2018 
do
    for ch in  tt et mt 
    do
        # rm output/uncert_shapes/${era}-${ch}-control-shapes/shapes-analysis-${era}-${ch}_all_nmssm.root
        # rm output/uncert_shapes/correct_classdict_shapes/${era}-${ch}-analysis-shapes.root
        # hadd output/uncert_shapes/correct_classdict_shapes/${era}-${ch}-analysis-shapes.root output/shapes/analysis_unit_graphs-${era}-${ch}-backgrounds/* output/shapes/analysis_unit_graphs-${era}-${ch}-sm_signals/* output/shapes/analysis_unit_graphs-${era}-${ch}-nmssm_split1/* output/shapes/analysis_unit_graphs-${era}-${ch}-nmssm_split2/* output/shapes/analysis_unit_graphs-${era}-${ch}-nmssm_split3/* output/shapes/analysis_unit_graphs-${era}-${ch}-nmssm_split4/* output/shapes/analysis_unit_graphs-${era}-${ch}-nmssm_split5/*
        #hadd output/synced_shapes/htt_${ch}.inputs-nmssm-${era}-${ch}_max_score_500_3.root output/synced_shapes/htt_${ch}.inputs-nmssm-${era}-${ch}_max_score_500_3*
        #python shapes/convert_to_synced_shapes.py --era ${era} --input output/uncert_shapes/${era}-${ch}-control-shapes/shapes-analysis-${era}-${ch}_all_nmssm.root --output output/synced_shapes/
        hadd output/uncert_shapes/correct_classdict_shapes/synced_shapes/htt_${ch}.inputs-nmssm-${era}-${ch}_max_score_500_3.root output/uncert_shapes/correct_classdict_shapes/synced_shapes/htt_${ch}.inputs-nmssm-${era}-${ch}_max_score_500_3*
    done
done