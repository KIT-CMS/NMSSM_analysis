ulimit -s unlimited
 
for era in 2018 #2016 2017 2018
do
    for channel in  et mt tt
    do

        python shapes/produce_shapes.py --channels ${channel} --output-file output/janek_500_3_kinfit_mh2/${era}_${channel} --directory /ceph/jbechtel/nmssm/ntuples/${era}/${channel}/ --${channel}-friend-directory /ceph/rschmieder/nmssm/friends/${era}/${channel}/SVFit/ /ceph/rschmieder/nmssm/friends/${era}/${channel}/FakeFactors_nmssm/ /ceph/rschmieder/nmssm/friends/${era}/${channel}/HHKinFit/ /ceph/jbechtel/nmssm/friends/${era}/${channel}/NNScore_train_all/NNScore_workdir/500_3/NNScore_workdir/NNScore_collected/ --era ${era} --num-processes 4 --num-threads 3 --optimization-level 1 --skip-systematic-variations --control-plots --control-plot-set kinfit_mh2 --process-selection data,emb,ggh,qqh,vh,tth,zl,ttl,vvl,ttt,NMSSM_500_125_110,NMSSM_500_125_120,NMSSM_500_125_130,NMSSM_500_125_150
        bash shapes/do_estimations.sh ${era} output/janek_500_3_kinfit_mh2/${era}_${channel}.root 0
    done
done
