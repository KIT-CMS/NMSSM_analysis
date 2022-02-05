source utils/setup_cvmfs_sft.sh
source utils/setup_python.sh

# ERA=$1
# INPUT=$1

TAG=pNN_balanced_lm_mH1000_data_finebinning
PREPOST=postfit

# for lm in 550 #60 300 550 850
# do
    for ch in mt #et mt tt
    do
        for era in 2017 #2016 2017 2018
        do
            for mp in 350
            do
            INPUT="/work/rschmieder/nmssm_newframework/nmssm_newframework_analysis/fit_output/pNN_balanced_lm_mH1000_data_finebinning/350/output_combined_all_1000_0_nmssm_1000_350/combined/cmb/postfitshape.root"
            for cat in 5 #NMSSM_MH321to500_boosted #1 2 3 4 5
            do
            # python plotting/plot_shapes_control.py -l --era Run${era} --input $INPUT --variables ${ch}_summed_score --channels ${ch} --embedding --fake-factor  --tag ${TAG} --blinded --category-postfix ${cat}
            python plotting/pre_postfit.py -l --era ${era} --input $INPUT --variables ${ch}_max_score --channels ${ch} --embedding --fake-factor --category-postfix ${cat} --tag ${TAG} --prepost ${PREPOST} --light_mass ${mp} --normalize-by-bin-width #--blinded 
            
             #--normalize-by-bin-width
            done 
        done
    done
done

# for era in 2017 # 2016 2017 2018
# do
# for ch in et mt tt
# do
# for var in kinfit_mh2 #mjj,pt_1,pt_2,m_vis,ptvis,m_sv_puppi,jpt_1,njets,jdeta,mjj,dijetpt,bpt_bReg_1,bpt_bReg_2,jpt_2,mbb_highCSV_bReg,pt_bb_highCSV_bReg,m_ttvisbb_highCSV_bReg,kinfit_mH,kinfit_mh2,kinfit_chi2,nbtag
# do
# for batch in 1 4 6
# do
# for lm in 60 250 700
# do
# python plotting/plot_shapes_control.py --era ${era} --input output/mbb_shapes_${ch}_${batch}.root --variables ${var} --channels ${ch} --embedding --fake-factor --tag kinfit_mh2_roger_${ch}_${batch}_${lm} --light_mass ${lm}
# done
# done
# done
# done
# done
