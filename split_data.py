from os import listdir, makedirs
from os.path import isfile, join
from shutil import copy
from xml.dom.minidom import parse
import bs4
import xml.etree.ElementTree as et

# to split lists in a ratio
def list_splitter(list_to_split, ratio):
    elements = len(list_to_split)
    middle = int(elements * ratio)
    return [list_to_split[:middle], list_to_split[middle:]]


# for RoadSign
# annotations and images folder
rs_data_original_path = 'DataOriginal/RoadSign/'
rs_ao_path = rs_data_original_path + 'annotations/'
rs_io_path = rs_data_original_path + 'images/'
rs_ao = [rs_ao_path + f for f in listdir(rs_ao_path) if isfile(join(rs_ao_path, f))]
rs_io = [rs_io_path + f for f in listdir(rs_io_path) if isfile(join(rs_io_path, f))]

# create train and test folders

equal = len(rs_ao) == len(rs_io)
if equal:
    print("Annotations and images files match" )
else:
    print("Annotations and images files do not match")

# 80:20 split = TrainingData:TestingData
    
rs_a_train, rs_a_test = list_splitter(rs_ao, 0.8)
rs_i_train, rs_i_test = list_splitter(rs_io, 0.8)

# create ids for each object name in RoadSign
classes = dict()
for file_path in rs_ao:
    root = et.parse(file_path)
    width = float(root.find('width').text)
    height = float(root.find('height').text)
    objs = []
    for child in root.iter('name'):
        if child.text not in classes.keys():
            classes[child.text] = len(classes)  
            xmin = float(child.find('xmin').text)
            xmin = xmin/width
            xmax = float(child.find('xmax').text) 
            xmax = xmax/width
            ymin = float(child.find('ymin').text) 
            ymin = ymin/height
            ymax = float(child.find('ymax').text)
            ymax = ymax/height

            of = file_path[:len(file_path)-3] + 'txt'
            f = open(of, 'w')
            
            li = f'{classes[child.text]} {xmin} {ymin} {xmax} {ymax}\n'
            f.write(li)
            f.close()

# training
makedirs('Data/RoadSign/train/annotations', exist_ok=True)
makedirs('Data/RoadSign/train/images', exist_ok=True)
for file in rs_a_train:
    copy(file, 'Data/RoadSign/train/annotations')
for file in rs_i_train:
    copy(file, 'Data/RoadSign/train/images')



# for testing
makedirs('Data/RoadSign/validation/annotations', exist_ok=True)
makedirs('Data/RoadSign/validation/images', exist_ok=True)
for file in rs_a_test:
    copy(file, 'Data/RoadSign/validation/annotations')
for file in rs_i_test:
    copy(file, 'Data/RoadSign/validation/images')





