# master_thesis

1. Install YOLOX
git clone git@github.com:Megvii-BaseDetection/YOLOX.git
cd YOLOX
pip3 install -v -e .  # or  python3 setup.py develop

2. Install onnox
if error message for onnox shows up:
pip install onnox & comment onnox out requirements.txt

3. Install torch
pip install torch==1.10.2+cu102 torchvision==0.11.3+cu102 torchaudio===0.10.2+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html

4. Install apex 
git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./

5. Change classes
open YOLOX/yolox/data/datasets/voc_classes.py
change default classes to
  "mpu",
  "mpui",
  "mpli"


6. Change more classes
open YOLOX/yolox/data/datasets/coco_classes.py
change default classes to
  "mpu",
  "mpui",
  "mpli"

7. In terminal
NUM_CLASSES = 3
!sed -i -e 's/self.num_classes = 20/self.num_classes = {NUM_CLASSES}/g' "/content/YOLOX/exps/example/yolox_voc/yolox_voc_s.py"

8. Save demo_modified
Save "demo_modified" under:
YOLOX/tools/demo_modified.py
