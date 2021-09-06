#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 2
#SBATCH --time=01:00:00
#SBATCH --partition=plgrid-gpu
#SBATCH --account=plglemkingpu3
#SBATCH --mem=25000
#SBATCH --gres=gpu:2

echo "START"
cd ..
. ./setup/setup.sh
cd rag

python finetune_rag.py \
    --data_dir ./trainingSet \
    --output_dir ./ragOutput \
    --model_name_or_path facebook/rag-sequence-base \
    --model_type rag_sequence \
    --gpus 2 \
    --index_name custom \
    --passages_path ./wiki_csv_parsed/my_knowledge_dataset \
    --index_path ./wiki_csv_parsed/my_knowledge_dataset_hnsw_index.faiss \
    --do_train \
    --do_predict \
    --n_val -1 \
    --val_check_interval 1.0 \
    --train_batch_size 1 \
    --eval_batch_size 1 \
    --max_source_length 2 \
    --max_target_length 2 \
    --val_max_target_length 2 \
    --test_max_target_length 2 \
    --label_smoothing 0.1 \
    --dropout 0.1 \
    --attention_dropout 0.1 \
    --weight_decay 0.001 \
    --adam_epsilon 1e-08 \
    --max_grad_norm 0.1 \
    --lr_scheduler polynomial \
    --learning_rate 3e-04 \
    --num_train_epochs 1 \
    --warmup_steps 1 \
    --gradient_accumulation_steps 1 \
    --use_dummy_dataset 1

echo "END"