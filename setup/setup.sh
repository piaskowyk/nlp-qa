module load plgrid/tools/python-intel/3.6.2
module load plgrid/apps/cuda/10.1
source ./venv/bin/activate
pip install mpi4py
pip install -r setup/requirements.txt
# pip install tensorflow
# pip3 install torch torchvision torchaudio
# pip install pytorch-lightning