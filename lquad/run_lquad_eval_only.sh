python run_lquad.py  \
    --model_type bert   \
    --model_name_or_path output  \
    --predict_file lquad/dev.json   \
    --do_eval   \
    --do_lower_case  \
    --per_gpu_eval_batch_size 12   \
    --max_seq_length 384   \
    --doc_stride 128  \
    --output_dir output
