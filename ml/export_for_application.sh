#!/bin/bash

ERA=$1
CHANNEL=$2
FOLDER=$3


./ml/translate_models.sh $ERA $CHANNEL $FOLDER
./ml/export_lwtnn.sh $ERA $CHANNEL $FOLDER
