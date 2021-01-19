import pandas as pd 
import numpy as np 
import glob

""" Datas unidas"""
#Es la data madre que contiene todas las bases unidas, despues las separé para poder extraer el contenido

path =r'C:\Users\Usuario\Desktop\MY_GIT_HUB\data_science_student_nov_2020\data_science_student_nov_2020\PROYECTO\DATA'
filenames = glob.glob(path + "/*.csv")
data = pd.DataFrame()
for f in filenames:
 df = pd.read_csv(f, delimiter= ",", encoding="latin1", skiprows=11)
 data = data.append(df)

 
""" Data living openly and daily"""

living_data= pd.read_csv(r"C:\Users\Usuario\Desktop\MY_GIT_HUB\data_science_student_nov_2020\data_science_student_nov_2020\PROYECTO\DATA\Living_openly_and-daily.csv", delimiter= ",", encoding="latin1", skiprows=11)

"""Data socio demographics"""

socio_data = pd.read_csv(r"C:\Users\Usuario\Desktop\MY_GIT_HUB\data_science_student_nov_2020\data_science_student_nov_2020\PROYECTO\DATA\SOCIO_DEMOGRAPHICS.csv", delimiter= ",", encoding="latin1", skiprows=11)

""" Data discimination"""

discrimination_data = pd.read_csv(r"C:\Users\Usuario\Desktop\MY_GIT_HUB\data_science_student_nov_2020\data_science_student_nov_2020\PROYECTO\DATA\DISCRIMINATION.csv", delimiter= ",", encoding="latin1", skiprows=11)

"""Data Goverment, queria ver si existia algun dato interesante sobre el trabajo pero no encontré nada útil"""

goverment_data= pd.read_csv(r"C:\Users\Usuario\Desktop\MY_GIT_HUB\data_science_student_nov_2020\data_science_student_nov_2020\PROYECTO\DATA\goverment.csv", delimiter= ",", encoding="latin1", skiprows=11)


