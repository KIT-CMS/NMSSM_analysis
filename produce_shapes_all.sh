ulimit -s unlimited
 
for era in 2017 # 2016 ${era} 2018
do
    for channel in  et mt tt
    do
        for batch in 1 4 6
        do
        # python shapes/produce_shapes.py --channels ${channel} --output-file output/mbb_shapes_${channel}_${batch} --directory /ceph/jbechtel/nmssm/ntuples/${era}/${channel}/ --${channel}-friend-directory /ceph/rschmieder/nmssm/friends/${era}/${channel}/SVFit/ /ceph/rschmieder/nmssm/friends/${era}/${channel}/FakeFactors_nmssm/ /ceph/rschmieder/nmssm/friends/${era}/${channel}/HHKinFit/ /ceph/jbechtel/nmssm/friends/${era}/${channel}/NNScore_train_all/NNScore_workdir/1000_${batch}/NNScore_workdir/NNScore_collected/ --era ${era} --num-processes 4 --num-threads 3 --optimization-level 1 --skip-systematic-variations --control-plots --control-plot-set kinfit_mh2
        bash shapes/do_estimations.sh ${era} output/mbb_shapes_${channel}_${batch}.root 0
        done
    done
done
