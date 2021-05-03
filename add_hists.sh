
for era in 2016 2017 2018
do
    for ch in et mt tt
    do        
        for lm in 60 70 75 80 85 90 95 100 110 120 130 150 170 190 250 300 350 400 450 500 550 600 650 700 750 800 850
        do
            # cp -r output/pNN_balanced_lm_mH1000_data/uncert_shapes/${lm}/${era}-${ch}.root output/pNN_balanced_lm_mH1000_pseudodata_shapebasis/uncert_shapes/${lm}/${era}-${ch}.root
            # python shapes/convert_to_synced_shapes_org.py --era ${era} --input output/pNN_balanced_lm_mH1000_pseudodata_shapebasis/uncert_shapes/${lm}/${era}-${ch}.root --output output/pNN_balanced_lm_mH1000_pseudodata_shapebasis/uncert_shapes/${lm}/ -n 12
            hadd output/pNN_balanced_lm_mH1000_pseudodata_shapebasis/uncert_shapes/${lm}/htt_${ch}.inputs-nmssm-${era}-${ch}_max_score_1000_0.root output/pNN_balanced_lm_mH1000_pseudodata_shapebasis/uncert_shapes/${lm}/htt_${ch}.inputs-nmssm-${era}-${ch}_max_score_1000_0*
        done
    done 
done 
#python add_hists_pseudodata.py