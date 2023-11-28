import os


class Iterator:
    def __init__(self, class_name, name_of_dataset):
        self.name_of_dataset=name_of_dataset
        self.class_name = class_name
        self.data = os.listdir(os.path.join(name_of_dataset, self.class_name))
        self.counter=0
        self.limit=len(self.data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            next_path = os.path.join(self.name_of_dataset, self.class_name, self.data[self.counter])
            self.counter += 1
            return next_path
        else:
            return None
    
if __name__ == "__main__":
    polar_bear=Iterator('polar bear', 'dataset')
    brown_bear=Iterator('brown bear', 'dataset')
    
    print(next(polar_bear))
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))