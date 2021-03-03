# #!/bin/bash
set -e

source utils/setup_cvmfs_sft.sh
source utils/setup_python.sh
source utils/bashFunctionCollection.sh

ERA=$1
CHANNEL=$2
tauEstimation=emb
jetEstimation=ff
FOLDER=$3
outdir=output/ml/${FOLDER}/${ERA}_${CHANNEL}

TRAIN_STAGE_ARG="--nmssm"

source utils/setup_samples.sh $ERA 

[[ -d $outdir ]] ||  mkdir -p $outdir
echo $FF_Friends
if [ ${CHANNEL} != 'em' ]
then
  FRIENDS="${SVFit_Friends} ${HHKinFit_Friends} ${FF_Friends}"
else
  FRIENDS="${SVFit_Friends} ${HHKinFit_Friends}"
fi


# Write dataset config
logandrun python ml/write_dataset_config_para.py \
  --era ${ERA} \
  --channel ${CHANNEL} \
  --base-path $ARTUS_OUTPUTS \
  --friend-paths $FRIENDS \
  --database $KAPPA_DATABASE \
  --output-path $outdir \
  --output-filename training_dataset.root \
  --tree-path ${CHANNEL}_nominal/ntuple \
  --event-branch event \
  --training-weight-branch training_weight \
  --training-z-estimation-method $tauEstimation \
  --training-jetfakes-estimation-method $jetEstimation \
  --output-config $outdir/dataset_config.yaml \
  $TRAIN_STAGE_ARG

# # Create dataset files from config
logandrun ./htt-ml/dataset/create_training_dataset_para.py --config $outdir/dataset_config.yaml --era ${ERA} --channel ${CHANNEL}

# #split the dataset
logandrun hadd -f $outdir/combined_training_dataset.root \
    $outdir/fold0_training_dataset.root \
    $outdir/fold1_training_dataset.root

logandrun python ./ml/sum_training_weights.py \
  --era ${ERA} \
  --channel ${CHANNEL} \
  --dataset $outdir/combined_training_dataset.root \
  --dataset-config-file "$outdir/dataset_config.yaml" \
  --training-template "ml/templates/${ERA}_${CHANNEL}_training.yaml" \
  --write-weights True
