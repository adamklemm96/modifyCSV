#!/bin/bash
echo "ALWAYS RUN THIS SCRIPT WITH ARGUMENT (PATH TO THE FILE)" 
path=$1 
gcloud compute scp import-passwords:"$path" ./
