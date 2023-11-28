import os
import shutil
import csv
import random

rand_num = random.sample(range(0,10001), 2005)
new_name = [f'{num}.jpg' for num in rand_num]

def remove_directory(path):
    if os.path.isdir(path):
        shutil.rmtree(path)

def get_old_rel_path():
    old_path = os.path.relpath('dataset2')
    old_name = os.listdir(old_path)
    old_rel_paths = [os.path.join(old_path, name) for name in old_name]
    return old_rel_paths

def get_new_rel_path():
    new_path = os.path.relpath('dataset_random')
    new_rel_paths = [os.path.join(new_path, name) for name in new_name]    
    return new_rel_paths

def create_dataset_random():
    if os.path.isdir('dataset_random'):
        shutil.rmtree('dataset_random')
    os.mkdir('dataset_random')
    old_rel_paths = get_old_rel_path()
    new_rel_paths = get_new_rel_path()
    for old_name, new_name in zip(old_rel_paths, new_rel_paths):
       shutil.copyfile(old_name, new_name)


def create_annotation_random():
    old_rel_paths = get_old_rel_path()
    abs_path = os.path.abspath('dataset_random')
    new_full_paths = [os.path.join(abs_path, name) for name in new_name]
    new_rel_paths = get_new_rel_path()
    with open('paths_random.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for full_path, rel_path, old_rel_path in zip(new_full_paths, new_rel_paths, old_rel_paths):
            if 'polar bear' in old_rel_path:
                class_name ='polar_bear'
            else:
                class_name= 'brown_bear'  
            writer.writerow([full_path, rel_path, class_name])

def main():
    create_dataset_random()
    create_annotation_random()

if __name__ == "__main__":
    main()
  