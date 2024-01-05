from os import listdir, makedirs
from os.path import isfile, join
from shutil import copy

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

# training
makedirs('Data/RoadSign/Train/annotations', exist_ok=True)
makedirs('Data/RoadSign/Train/images', exist_ok=True)
for file in rs_a_train:
    copy(file, 'Data/RoadSign/Train/annotations')
for file in rs_i_train:
    copy(file, 'Data/RoadSign/Train/images')



# for testing
makedirs('Data/RoadSign/Test/annotations', exist_ok=True)
makedirs('Data/RoadSign/Test/images', exist_ok=True)
for file in rs_a_test:
    copy(file, 'Data/RoadSign/Test/annotations')
for file in rs_i_test:
    copy(file, 'Data/RoadSign/Test/images')





