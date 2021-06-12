source utils/setup_cvmfs_sft.sh
source utils/setup_python.sh

# ERA=$1
# INPUT=$1

TAG=pNN_balanced_lm_mH1000_data_finebinning
PREPOST=prefit
echo "hi"
for lm in 550 #60 300 550 850
do
    for ch in et mt tt
    do
        for era in 2017 # 2016 2017 2018
        do
            INPUT="fit_output/${TAG}/${lm}/output_combined_all_1000_0_nmssm_1000_${lm}/combined/cmb/prefitshape.root"
            for cat in 1 2 3 4 5 #emb tt ff misc NMSSM
            do
            #python plotting/plot_shapes_control.py -l --era Run${ERA} --input $INPUT --variables et_max_score --channels ${ch} --embedding --fake-factor --category-postfix ${cat} --tag ${TAG} --blinded
            python plotting/pre_postfit.py -l --era ${era} --input $INPUT --variables ${ch}_max_score --channels ${ch} --embedding --fake-factor --category-postfix ${cat} --tag ${TAG}/${lm} --prepost ${PREPOST} --blinded --light_mass ${lm}
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
