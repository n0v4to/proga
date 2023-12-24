import pandas as pd
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("annotations.csv", delimiter=",", usecols = (0, 2), names = ("Absolute Path", "Name"))
# print(df.head(5))
# print(df.tail(5))

df["Label"] = df["Name"].apply(lambda x: 0 if x == "polar bear" else 1)
# print(df.head(5))
# print(df.tail(5))

df["Height"] = df["Absolute Path"].apply(lambda path: cv2.imread(path).shape[0])
df["Width"] = df["Absolute Path"].apply(lambda path: cv2.imread(path).shape[1])
df["Depth"] = df["Absolute Path"].apply(lambda path: cv2.imread(path).shape[2])
# print(df.head(5))
# print(df.tail(5))

stat_info0 = df[df["Label"] == 0]["Height"].describe()
# print(stat_info0)
stat_info1 = df[df["Label"] == 1]["Height"].describe()
# print(stat_info1)

def filter_class(df: pd.DataFrame, class_label: int):
    '''
    Возвращает dataframe путем фильтрации переданного dataframe по метке класса
    Parameters
        df : pd.DataFrame
        датафрейм
        class_label : int
        Метка класса
    '''
    return df[df["Label"] == class_label]

def size_filter(df: pd.DataFrame, class_label: int, max_height: int, max_width: int):
    '''
    Возвращает dataframe путем фильтрации переданного dataframe по метке класса, максимальной высоте и ширине
    Parameters
        df : pd.DataFrame
        датафрейм
        class_label : int
        Метка класса
        max_height : int
        Максимальная высота изображения
        max_width : int
        Максимальная ширина изображения
    '''
    return df[(df["Label"] == class_label) & (df["Height"] <= max_height) & (df["Width"] <= max_width)]

def df_group(df: pd.DataFrame, class_label: int):
    '''
    Возвращает dataframe группируя по метке класса, вычисляя максимальное, минимальное и среднее значения по количеству пикселей
    Parameters
        df : pd.DataFrame
        датафрейм
        class_label : int
        Метка класса
    '''
    filtered_df = filter_class(df, class_label)
    pixel_counts = []
    
    for path in filtered_df["Absolute Path"]:
        img = cv2.imread(path)
        pixel_counts.append(img.size)
    
    filtered_df["pixels"] = pixel_counts
    filtered_df.groupby("pixels").count()
    print(filtered_df["pixels"].describe())

def build_histogram(df: pd.DataFrame, class_label: int):
    '''
    Строит гистограмму
    Parameters
        df : pd.DataFrame
        датафрейм
        class_label : int
        Метка класса
    '''
    random_image = df[df["Label"] == class_label].sample(1)
    image_path = random_image["Absolute Path"].values[0]
    image = cv2.imread(image_path)
    b, g, r = cv2.split(image)
    arr = []
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
    arr.append(hist_b)
    arr.append(hist_g)
    arr.append(hist_r)
    return arr

def plot_histogram(df: pd.DataFrame, class_label: int):
    '''
    Отрисовывает гистограмму
    Parameters
        df : pd.DataFrame
        датафрейм
        class_label : int
        Метка класса
    '''
    hist = build_histogram(df, class_label)
    plt.figure(figsize=(12, 6))

    plt.subplot(131)
    plt.plot(hist[0], color='b')
    plt.title('Blue Channel')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.subplot(132)
    plt.plot(hist[1], color='g')
    plt.title('Green Channel')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.subplot(133)
    plt.plot(hist[2], color='r')
    plt.title('Red Channel')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.show()


if __name__ == '__main__':
    # print(df.head(5))
    # print(df.tail(5))
    # print(size_filter(df, 1, 400, 300))
    # print(size_filter(df, 0, 400, 300))
    # print(filter_class(df, 1))
    # print(filter_class(df, 0))
    # df_group(df, 1)
    # df_group(df, 0)
    plot_histogram(df, 1)