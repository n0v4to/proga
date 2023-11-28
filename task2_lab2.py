import os
import csv
import shutil

def get_full_paths(class_name: str) -> list:
    full_path = os.path.abspath('dataset2')
    image_names = os.listdir(full_path)
    image_class_names = [name for name in image_names if class_name in name]
    image_full_paths = list(
        map(lambda name: os.path.join(full_path, name), image_class_names))
    return image_full_paths

def get_relative_paths(class_name: str) -> list:
    rel_path = os.path.abspath('dataset2')
    image_names = os.listdir(rel_path)
    image_class_names = [name for name in image_names if class_name in name]
    image_rel_paths = list(
        map(lambda name: os.path.join(rel_path, name), image_class_names))
    return image_rel_paths

def replace_images(class_name: str) -> list:
    rel_path = os.path.relpath('dataset2')
    class_path = os.path.join(rel_path, class_name)
    image_names = os.listdir(class_path)
    image_rel_paths = list(
        map(lambda name: os.path.join(class_path, name), image_names))
    new_rel_paths = list(
        map(lambda name: os.path.join(rel_path, f'{class_name}_{name}'), image_names))
    for old_name, new_name in zip(image_rel_paths, new_rel_paths):
        os.replace(old_name, new_name)

    os.chdir('dataset2')

    if os.path.isdir(class_name):
        os.rmdir(class_name)

    os.chdir('..')

def create_dataset2():
    class_polar_bear="polar bear"
    class_brown_bear="brown bear"
    
    if os.path.isdir('dataset2'):
        shutil.rmtree('dataset2')

    old = os.path.relpath('dataset')
    new = os.path.relpath('dataset2')
    shutil.copytree(old, new)
    
    replace_images(class_polar_bear)
    replace_images(class_brown_bear)
    
def create_annotation2():
    class_polar_bear="polar bear"
    class_brown_bear="brown bear"
    
    polar_bear_full_paths = get_full_paths(class_polar_bear)
    polar_bear_rel_paths = get_relative_paths(class_polar_bear)
    brown_bear_full_paths = get_full_paths(class_brown_bear)
    brown_bear_rel_paths = get_relative_paths(class_brown_bear)
    
    with open('paths2.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for full_path, rel_path in zip(polar_bear_full_paths, polar_bear_rel_paths):
            writer.writerow([full_path, rel_path, class_polar_bear])
        for full_path, rel_path in zip(brown_bear_full_paths, brown_bear_rel_paths):
            writer.writerow([full_path, rel_path, class_brown_bear])

def main():
    create_dataset2()
    create_annotation2()

if __name__ == "__main__":
    main()