import glob, random

def import_image(random=True):
    if random:
        PATH = r"/home/tessa/original_data_jpg"
        # photos = glob.glob(random.choice(PATH))
    image = random.choice([
            x for x in os.listdir(path)
            if os.PATH.isfile(os.path.join(path,x))
            ])

    return image


# # # # # # # # # TESTING AREA # # # # # # # # # # # 
        
img = import_image(random=True)