ulimit -s unlimited


for era in 2016 2017 2018
do
for channel in et mt tt
do

echo $era $channel
#rm -r output/NMSSM_scale_factors_para_training/${era}-${channel}-control-shapes
# python shapes/produce_shapes.py --channels ${channel} --output-file output/NMSSM_scale_factors_para_training/${era}-${channel}-control-shapes --directory /ceph/jbechtel/nmssm/ntuples/${era}/${channel}/ --${channel}-friend-directory /ceph/jbechtel/nmssm/friends/${era}/${channel}/SVFit/ /ceph/rschmieder/nmssm/friends/${era}/${channel}/FakeFactors_nmssm/ /ceph/jbechtel/nmssm/friends/${era}/${channel}/HHKinFit/ /ceph/jbechtel/nmssm/friends/${era}/${channel}/NNScore_train_all/NNScore_workdir/500_3/NNScore_workdir/NNScore_collected/ --era ${era} --skip-systematic-variations --num-processes 4 --num-threads 3 --optimization-level 1 --control-plot-set pt_1 --control-plots --process-selection nmssm 
done
done 
