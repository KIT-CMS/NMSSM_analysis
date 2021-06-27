source utils/setup_cvmfs_sft.sh
source utils/setup_python.sh

# ERA=$1
# INPUT=$1

TAG=10_onenet_summed_0_5
PREPOST=prefit

# for lm in 550 #60 300 550 850
# do
    for ch in et mt tt
    do
        for era in 2016 2017 2018
        do
            INPUT="output/10_onenet_summed_0_5/uncert_shapes/${era}-${ch}.root"
            for cat in NMSSM_MH321to500_boosted #1 2 3 4 5
            do
            python plotting/plot_shapes_control.py -l --era Run${era} --input $INPUT --variables ${ch}_summed_score --channels ${ch} --embedding --fake-factor  --tag ${TAG} --blinded --category-postfix ${cat}
            #python plotting/pre_postfit.py -l --era ${era} --input $INPUT --variables ${ch}_max_score --channels ${ch} --embedding --fake-factor --category-postfix ${cat} --tag ${TAG} --prepost ${PREPOST} --blinded --normalize-by-bin-width #--light_mass ${lm} --normalize-by-bin-width
            done 
        done
    done
#done

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
