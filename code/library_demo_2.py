import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('mytextfile.txt', 'r', encod="utf8")as rf:
    my_string = rf.read()

my_string.replace(".", "").replace(",", "")