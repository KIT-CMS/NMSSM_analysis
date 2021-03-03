ERA=$1
CHANNEL=$2
FOLDER=$3
source utils/setup_cvmfs_sft.sh
python ml/create_combined_config_para.py  --tag "" --channel $CHANNEL --output_dir output/ml/${FOLDER}/${ERA}_${CHANNEL} --folder ${FOLDER}