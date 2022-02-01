import os

def detect_rings(image_path):
    
    os.system('ipython yolox_trained.ipy')
    
    file_path = r'C:\Users\988559\Digital_twin\Detection_output.csv'
    f = open(file_path, "r")
    content = (f.read())
    
    lines = f.readlines()
    print(lines)

    results = content.split('tensor', 3)
    bbox = results[1]
    scores = results[2]
    classes = results[3]
    
    bbox = 0
    scores = 0
    classes = 0
    
    return(bbox, scores, classes)

########################## TESTING #########################################

bbox, scores, classes = detect_rings(r'C:\Users\988559\Digital_twin\original_data_jpg\11222021_15716_1.jpg')
