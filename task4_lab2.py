import os

def get_next_instances(class_name: str) -> list:
    path = os.path.join('dataset', class_name)
    class_names = os.listdir(path)
    instances = [os.path.join(path, instance_name) for instance_name in class_names]
    return instances


def main(): 
    instances = get_next_instances('polar bear')
    if instances is not None:
        for instance in instances:
            print(instance)
        
if __name__ == "__main__":
    main()