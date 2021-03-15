source utils/setup_cvmfs_sft.sh
source utils/setup_python.sh

ERA=$1
INPUT=$2
TAG=$3
for ch in et #mt tt
do
for era in 2016 #2017 2018
do
for cat in ff # emb tt ff misc NMSSM
do
plotting/plot_shapes_control.py -l --era Run${ERA} --input $INPUT --variables et_max_score --channels ${ch} --embedding --fake-factor --category-postfix ${cat} --tag ${TAG} --blinded
done 
done
done