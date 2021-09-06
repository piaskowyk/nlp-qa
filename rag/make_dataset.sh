#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 2
#SBATCH --time=03:00:00
#SBATCH --partition=plgrid-gpu
#SBATCH --account=plglemkingpu3
#SBATCH --mem=25000
#SBATCH --gres=gpu:1

echo "START"
cd ..
. ./setup/setup.sh
cd rag
python use_own_knowledge_dataset.py \
    --csv_path ./wiki_csv/all_wiki.csv \
    --output_dir ./wiki_csv_parsed

echo "END"