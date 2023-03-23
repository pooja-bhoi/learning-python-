
%matplotlib inline  #tells the IPython environment to draw the plots immediately after the current cell
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [20.0, 10.0] #set the default width and height


#reading data, these 3 types worked 

#data = pd.read_csv(r"C:\Users\.....headbrain.csv")
#data = pd.read_csv("C:/Users/...../headbrain.csv")
data = pd.read_csv("C:\\Users.....\\headbrain.csv")
print(data.shape)
data.head()



