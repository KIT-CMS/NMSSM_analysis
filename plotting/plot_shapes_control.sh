source utils/setup_cvmfs_sft.sh
source utils/setup_python.sh

ERA=$1
INPUT=$1

# #TAG=pNN_balanced_lm_mH1000_data
# PREPOST=prefit
# for TAG in pNN_all_bkgtrue_mH1000
# do
# for lm in 350 # 60 70 75 80 85 90 95 100 110 120 130 150 170 190 250 300 350 400 450 500 550 600 650 700 750 800 850
# do
#     for ch in mt #et mt tt
#     do
#         for era in 2017 # 2016 2017 2018
#         do
#             INPUT="fit_output/${TAG}/${lm}/output_combined_all_1000_3_nmssm_1000_${lm}/combined/cmb/prefitshape.root"
#             for cat in 5 #1 2 3 4 5 #emb tt ff misc NMSSM
#             do
#             #python plotting/plot_shapes_control.py -l --era Run${ERA} --input $INPUT --variables et_max_score --channels ${ch} --embedding --fake-factor --category-postfix ${cat} --tag ${TAG} --blinded
#             python plotting/pre_postfit.py -l --era ${era} --input $INPUT --variables ${ch}_max_score --channels ${ch} --embedding --fake-factor --category-postfix ${cat} --tag ${TAG}/${lm} --prepost ${PREPOST} --blinded --light_mass ${lm}
#             done 
#         done
#     done
# done
# done
for era in 2018 # 2016 2017 2018
do
for ch in tt # et mt tt
do
for var in mjj,pt_1,pt_2,m_vis,ptvis,m_sv_puppi,jpt_1,njets,jdeta,mjj,dijetpt,bpt_bReg_1,bpt_bReg_2,jpt_2,mbb_highCSV_bReg,pt_bb_highCSV_bReg,m_ttvisbb_highCSV_bReg,kinfit_mH,kinfit_mh2,kinfit_chi2,nbtag
do
python plotting/plot_shapes_control.py --era ${era} --input output/pNN_balanced_lm_mH1000_data/${era}-${ch}-control-shapes.root --variables ${var} --channels ${ch} --embedding --fake-factor --tag pNN_balanced_lm_mH1000_data --light_mass 300
done
done
done
