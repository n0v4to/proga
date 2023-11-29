import os
import shutil
import csv
import random
import re

def create_random_dataset_and_annotations():
    '''
    Копирует набор данных
    Проходит папку dataset, генерирует новое имя файла с использованием имени класса и случайно сгенерированного числа
    После чего копирует файл с новым именем в созданную папку random_dataset
    Параллельно записывает в csv файл путь и метку класса
    '''
    dataset_path = os.path.abspath("dataset")

    if not os.path.exists("random_dataset"):
        os.makedirs("random_dataset")
    dataset2_path = os.path.abspath("random_dataset")

    with open('annotations3.csv', 'w') as file:
        writer = csv.writer(file)

        for root, dirs, files in os.walk(dataset_path):
            for filename in files:
                class_name = os.path.basename(root)
                class_name = class_name.replace(" ", "_")
                rand_num = random.randint(0, 10000)
                random_filename = f"{rand_num}.jpg"
                new_filename = f"{class_name}_{random_filename}"
                original_path = os.path.join(root, filename)
                new_filename = re.sub("\D{5}_\D{4}_", '', new_filename)
                new_path = os.path.join(dataset2_path, new_filename)
                shutil.copy(original_path, new_path)

                rel_path = os.path.relpath(new_path)
                writer.writerow([new_path, rel_path, class_name])

def main():
    create_random_dataset_and_annotations()

if __name__ == "__main__":
    main()