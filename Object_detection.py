import os
import torch
import torchvision
# from object_detection.utils import label_map_util
# from object_detection.utils import visualization_utils as viz_utils
# from object_detection.builders import model_builder


## Load pipeline config and build detection model
#configs = config_util.get_configs_from_pipeline_file(files['PIPELINE_CONFIG'])
#detection_model = model_builder.build(model_config=configs['model'], is_traininge=False)
MODEL_PATH = '/home/tessa/Programmi/Digital_twin_model/best_chkpt.pth.tar'

# restore checkpoint
checkpoint = tf.compat.v2.train.Checkpoint(model=detection_model)
checkpoint.restore(os.path(paths['MODEL_PATH']))
print(checkpoint)

checkpoint = torch.load()


# from roboflow

TEST_IMAGE_PATH = '/home/tessa/original_data_jpg/11222021_154618_1.jpg'

# checkpoint = torch.load(MODEL_PATH)
# model.load_state_dict(checkpoint['state_dict'])
# optimizer.load_state_dict(checkpoint['optimizer'])

#
#python /home/tessa/Programmi/YOLOX/tools/demo.py image -n /home/tessa/Programmi/YOLOX/exps/example/yolox_voc/yolox_voc_s.py
# -c /home/tessa/Programmi/Digital_twin_model/best_chkpt.pth.tar --path /home/tessa/original_data_jpg/11222021_154618_1.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device cpu
#    
#def detect_objects(image):
#    return (position_ring, boundingbox)