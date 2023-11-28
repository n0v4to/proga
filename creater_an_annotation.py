import os
import csv

def create_annotation():
    '''
    Создает аннотацию
    '''
    dataset_path = os.path.abspath("dataset")

    with open('annotations.csv', 'w') as file:
        writer = csv.writer(file)
        for root, dirs, files in os.walk(dataset_path):
            for filename in files:
                abs_path = os.path.abspath(os.path.join(root, filename))
                rel_path = os.path.relpath(abs_path)
                class_name = os.path.basename(os.path.dirname(abs_path))
                if class_name in ["polar bear", "brown bear"]:
                    writer.writerow([abs_path, rel_path, class_name])
    
def main():
    create_annotation()

if __name__ == "__main__":
    main()