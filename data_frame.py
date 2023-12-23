import pandas as pd
import cv2
import os

df = pd.read_csv("annotations.csv", delimiter=",", usecols = (0, 2), names = ("Absolute Path", "Name"))
# print(df.head(5))
# print(df.tail(5))

df["Label"] = df["Name"].apply(lambda x: 0 if x == "polar bear" else 1)
# print(df.head(5))
# print(df.tail(5))

df["Height"] = df["Absolute Path"].apply(lambda path: cv2.imread(path).shape[0])
df["Width"] = df["Absolute Path"].apply(lambda path: cv2.imread(path).shape[1])
df["Depth"] = df["Absolute Path"].apply(lambda path: cv2.imread(path).shape[2])
print(df.head(5))
print(df.tail(5))