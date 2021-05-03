ulimit -s unlimited
 
for era in 2016 2017 2018
do
    for channel in  et mt tt
    do
        mkdir /ceph/rschmieder/nmssm/friends/${era}/${channel}/SVFit/pseudodata_${era}_${channel}_0_1pb_mH1000_mL300/
        mkdir /ceph/rschmieder/nmssm/friends/${era}/${channel}/FakeFactors_nmssm/pseudodata_${era}_${channel}_0_1pb_mH1000_mL300/
        mkdir /ceph/rschmieder/nmssm/friends/${era}/${channel}/HHKinFit/pseudodata_${era}_${channel}_0_1pb_mH1000_mL300/
        python create_empty_tree.py --era ${era} --channel ${channel} --friend SVFit
        python create_empty_tree.py --era ${era} --channel ${channel} --friend FakeFactors_nmssm
        python create_empty_tree.py --era ${era} --channel ${channel} --friend HHKinFit
        # echo $era $channel
        # mkdir output/uncert_shapes/${era}-${channel}-control-shapes
        # python shapes/produce_shapes.py --channels ${channel} --output-file output/uncert_shapes/${era}-${channel}-control-shapes/shapes-analysis-${era}-${channel} --directory /ceph/jbechtel/nmssm/ntuples/${era}/${channel}/ --${channel}-friend-directory /ceph/jbechtel/nmssm/friends/${era}/${channel}/SVFit/ /ceph/rschmieder/nmssm/friends/${era}/${channel}/FakeFactors_nmssm/ /ceph/jbechtel/nmssm/friends/${era}/${channel}/HHKinFit/ /ceph/jbechtel/nmssm/friends/${era}/${channel}/NNScore_train_all/NNScore_workdir/500_3/NNScore_workdir/NNScore_collected/ --era ${era} --num-processes 5 --num-threads 4 --optimization-level 1 --control-plot-set ${channel}_max_score 

        # bash shapes/do_estimations.sh ${era} output/uncert_shapes/${era}-${channel}-control-shapes/shapes-analysis-${era}-${channel}.root 0

        # python shapes/convert_to_synced_shapes.py --era ${era} --input output/uncert_shapes/${era}-${channel}-control-shapes/shapes-analysis-${era}-${channel}.root --output output/uncert_shapes/synced_shapes
        
        # hadd output/uncert_shapes/synced_shapes/${era}-${channel}-synced-NMSSM.root output/uncert_shapes/synced_shapes/${era}-${channel}-synced-NMSSM*
    done
done
