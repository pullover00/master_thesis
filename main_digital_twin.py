import Measurement
import Object_detection
import Segmentation
import Images


image = import_image(random=True, test=True)

structure_segment, structure_type = segment_structure(image)
