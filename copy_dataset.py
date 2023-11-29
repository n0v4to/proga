import os
import shutil
import csv
import re

def copy_dataset():
    '''
    Копирует набор данных
    Проходит папку dataset, генерирует новое имя файла с использованием имени класса и порядкового номера
    После чего копирует файл с новым именем в созданную папку dataset 2
    '''
    dataset_path = os.path.abspath("dataset")

    if not os.path.exists("dataset2"):
        os.makedirs("dataset2")
    dataset2_path = os.path.abspath("dataset2")

    for root, dirs, files in os.walk(dataset_path):
        for filename in files:
            class_name = os.path.basename(root)
            class_name = class_name.replace(" ", "_")
            new_filename = f"{class_name}_{filename}"
            original_path = os.path.join(root, filename)
            new_path = os.path.join(dataset2_path, new_filename)
            shutil.copy(original_path, new_path)

def create_annotation_of_copy_dataset():
    '''
    Создает аннотацию для dataset2
    '''
    dataset_path = os.path.abspath("dataset2")

    with open('annotations2.csv', 'w') as file:
        writer = csv.writer(file)
        for root, dirs, files in os.walk(dataset_path):
            for filename in files:
                abs_path = os.path.abspath(os.path.join(root, filename))
                rel_path = os.path.relpath(abs_path)
                class_name = os.path.basename(abs_path)
                class_name = re.sub("_\d{4}.jpg", '', class_name)
                writer.writerow([abs_path, rel_path, class_name])

def main():
    copy_dataset()
    create_annotation_of_copy_dataset()

if __name__ == "__main__":
    main()