#!/bin/bash
set -e

# This script runs the nmssm analysis. The training of the neural network is performed using the condor cluster. 
# If the GPU of the cluster is used is decided by the image used in ml_condor/wite_condor_submission.sh
# This script can be called by multi_run_ml.sh
# 1. The training dataset is constructed from skimmed data
# 2. The training on the cluster is started
# 3. The trained modells are tested

ERA_NAME=$1 # Can be 2016, 2017, 2018 or "all_eras"
CHANNEL=$2 # Can be et, mt or tt
#MASS=$3 # only train on mH=500 GeV
#BATCH=$4 # only train on mh' in 85, 90, 95, 100 GeV (see ml/get_nBatches.py for assignment)
OPTIONS=$3 # recalculate certain stages of the programm: "1" datasets, "2" training, "3" testing,
# "c" for using cpu instead of gpu, "f" to run training on cluster even if training on same data is already running. Untitled-1
#Can be combined (13, 2c3). If no stage option is given, it is treated as "123" ( "c" becomes "c123" etc.)
CHANGE_USER=$4 # Use data of specifid USER on ceph

# Enable all stages if none were given
if [[ ! ${OPTIONS} =~ [1-3] ]]; then
  OPTIONS="${OPTIONS}123"
fi
# Change used USER if specified
if [[ ${CHANGE_USER} ]]; then
  USER=${CHANGE_USER}
fi
# Initialize
FOLDER=parametrized_nn_mh1000
SET=${ERA_NAME}_${CHANNEL}
OUTPUT_PATH=output/ml/${FOLDER}/${SET}
CEPH_PATH=/ceph/srv/${USER}/${FOLDER}/${SET}
if [[ ${ERA_NAME} == "all_eras" ]]; then
  ERAS="2016 2017 2018"
  ERAS_ALL="2016 2017 2018 all_eras"
else
  ERAS=${ERA_NAME}
  ERAS_ALL=${ERA_NAME}
fi
# Create log directory if needed
if [[ ! -d output/log/logandrun ]]; then
  echo create output/log/logandrun
  mkdir -p output/log/logandrun
fi
# Create ceph directory if needed
if [[ ! -d ${CEPH_PATH} ]]; then
  echo create ${CEPH_PATH}
  mkdir -p ${CEPH_PATH}
fi
# Create output directory if needed
if [[ ! -d ${OUTPUT_PATH} ]]; then
  echo create ${OUTPUT_PATH}
  mkdir -p ${OUTPUT_PATH}
fi

echo "ERA=${ERA_NAME}, CHANNEL=${CHANNEL}, OPTIONS=${OPTIONS}"

#---1---
# If dataset creation specified:
if ( [[ ${OPTIONS} == *"1"* ]] && [[ ! ${CHANGE_USER} ]] ); then
  # Run dataset creation
  echo "creating Datasets"
  for ERA in ${ERAS}; do
    ./ml/create_training_dataset_para.sh ${ERA} ${CHANNEL} ${FOLDER} &
  done
  wait
  if [[ ${ERA_NAME} == "all_eras" ]]; then
    ./ml/combine_configs_para.sh ${ERA_NAME} ${CHANNEL} ${FOLDER}
  fi
  for ERA in ${ERAS_ALL}; do
    echo "/ceph/srv/${USER}/${FOLDER}/${ERA}_${CHANNEL}"
    LOOP_CEPH_PATH=/ceph/srv/${USER}/${FOLDER}/${ERA}_${CHANNEL}
    LOOP_OUTPUT_PATH=output/ml/${FOLDER}/${ERA}_${CHANNEL}
    if [[ ! -d ${LOOP_CEPH_PATH} ]]; then
      # create directories if needed
      mkdir -p ${LOOP_CEPH_PATH}
    else
      # Remove data on ceph
      rm -f ${LOOP_CEPH_PATH}/*
    fi
    # Upload dataset and config file to ceph
    cp ${LOOP_OUTPUT_PATH}/dataset_config.yaml ${LOOP_CEPH_PATH}
    if [[ ! ${ERA} == "all_eras" ]]; then
      echo "Upload ${LOOP_OUTPUT_PATH}/foldx_training_dataset.root"
      cp ${LOOP_OUTPUT_PATH}/fold0_training_dataset.root ${LOOP_OUTPUT_PATH}/fold1_training_dataset.root ${LOOP_CEPH_PATH}
    fi
    #rm -rf ${LOOP_OUTPUT_PATH}/merge*
  done
else
  if [[ ${CHANGE_USER} ]]; then
    echo "Data of others can't be overwritten. The data of ${CHANGE_USER} will be used."
  fi
  echo "No new datasets needed"
fi

#---2---
# If training is specified:
if [[ ${OPTIONS} == *"2"* ]]; then
  # Setup and run the training on condor 
  echo "training modells"
  if [[ ${OPTIONS} == *"c"* ]]; then
    CALC=cpu
    echo "The training is using CPUs"
  else
    CALC=gpu
    echo "The training is using GPUs"
  fi
  if [[ ${OPTIONS} == *"f"* ]]; then
    FORCE=True
  else
    FORCE=False
  fi
  now=$(date +"%T")
  if [[ ! -d ${OUTPUT_PATH}/condor_logs_${CALC} ]]; then
    mkdir ${OUTPUT_PATH}/condor_logs_${CALC}
  fi
  echo "Timestamp job sent: ${now}" > ${OUTPUT_PATH}/condor_logs_${CALC}/times.txt
  ./ml_condor/setup_condor_training.sh ${ERA_NAME} ${CHANNEL} ${FORCE} ${CALC} ${OUTPUT_PATH} ${FOLDER}
  grep Timestamp ${OUTPUT_PATH}/condor_logs_${CALC}/out.txt >> ${OUTPUT_PATH}/condor_logs_${CALC}/times.txt
else
  echo "no new training needed"
fi

#---3---
# If testing is specified:
if [[ ${OPTIONS} == *"3"* ]]; then
  # Export for testing and test modells
  echo "testing new models"
  #xrdcp ${CEPH_PATH}/dataset_config.yaml ${OUTPUT_PATH}
  # for ERA in ${ERAS}; do
  #   LOOP_OUTPUT_PATH=output/ml/${FOLDER}/${ERA}_${CHANNEL}
  #   LOOP_CEPH_PATH=/ceph/srv/${USER}/${FOLDER}/${ERA}_${CHANNEL}
  #   cp ${LOOP_CEPH_PATH}/fold*.root ${LOOP_OUTPUT_PATH}/*.yaml ${LOOP_OUTPUT_PATH}
  # done
  ./ml/export_for_application.sh ${ERA_NAME} ${CHANNEL} ${FOLDER}
  for ERA in ${ERAS}; do
    if [[ ${ERA_NAME} = "all_eras" ]]; then
      ./ml/run_testing_all_eras.sh ${ERA} ${CHANNEL} ${FOLDER} $
    else
    ./ml/run_testing.sh ${ERA_NAME} ${CHANNEL} ${FOLDER}
    fi
    wait
    #rm ${LOOP_OUTPUT_PATH}/fold*.root
  done
  #rm ${OUTPUT_PATH}/dataset_config.yaml
else
  echo "no new testing needed"
fi