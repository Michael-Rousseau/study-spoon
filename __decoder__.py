#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from huffman import *
import pickle
import os

with open('fichier_pickle', "rb") as f:
    table_occ = pickle.load(f)
with open('fichier_encode.txt', "r") as f:
    data = f.read()

print("run decoding")
decoder(table_occ, data)

file_old = "fichier_encode.txt"
file_new_size = os.stat(file_old).st_size 
file_old_size = os.stat("Les_Miserables.txt").st_size 
ps = 1 - (((file_new_size)/8)/file_old_size)
print(file_old_size, "bytes compressed to: ",file_new_size," bytes", "with a rate of :", ps,"%")