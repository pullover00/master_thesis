#import Measurements
import Object_detection
#import Segmentation
import Images

image_path = Images.import_image(random=True)
bbox, scores, classes = Object_detection.detect_rings(image_path)


# structure_segment, structure_type = segment_structure(image)
