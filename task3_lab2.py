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

def main():
    create_dataset_random()
    create_annotation_random()

if __name__ == "__main__":
    main()
  