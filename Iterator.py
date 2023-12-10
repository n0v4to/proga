# import os
# class Iterator:
#     def __init__(self, class_name):
#         self.class_name = class_name
#         self.data = os.listdir(os.path.join('dataset', self.class_name))
#         self.limit = len(self.data)
#         self.counter = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return os.path.join(self.class_name, self.data[self.counter])
#         else:
#             raise StopIteration

# def main():
#     polar_bear=Iterator('polar bear')
#     brown_bear=Iterator('brown bear')

#     print(next(polar_bear))
#     print(next(brown_bear))
#     print(next(polar_bear))
#     print(next(brown_bear))
#     print(next(polar_bear))
#     print(next(brown_bear))

# if __name__ == "__main__":
#     main()

import os
import csv

class Iterator:
    def __init__(self,class_name, dataset_name):
        self.dataset_name=dataset_name
        self.class_name =class_name
        self.data = os.listdir(os.path.join(dataset_name, self.class_name))
        self.counter=0
        self.limit=len(self.data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            next_path = os.path.join(self.dataset_name,self.class_name, self.data[self.counter])
            self.counter += 1
            return next_path
        else:
            return None
    

if __name__ == "__main__":
    polar_bear=Iterator('polar bear','dataset')
    brown_bear=Iterator('brown bear', 'dataset')
    
    print(next(polar_bear))
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))