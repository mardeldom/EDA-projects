from UTILS.folders_tb import living_data, discrimination_data, socio_data, data #a veces tengo que poner UTILS. y otras no, porque si no no me lo importa
import pandas as pd 
import numpy as np
"""Limpiamos los valores Nan de la columna question_label porque estaban vacios"""
data = data.loc[data["question_label"].notna()]

#Los siguientes pasos se han realizado en todos las dataset 

"""Accedemos a los valores de la columna question_label para ver lo que podemos extraer"""
def question(dt=None):
    q= list(pd.unique(dt["question_label"]))
    return q
"""Accedemos a los valores de la columna respuesta para saber como podemos agruparlo"""
def answer(dt=None):
    aw = list(pd.unique(dt["answer"]))
    return aw

"""Funciones que serán mis nuevos dataset filtrados y limpios con la información que quiero analizar"""
def sw():
    socio_w = socio_data.loc[socio_data["question_label"]=="Working status"]
    socio_w['percentage'] = socio_w['percentage'].astype(int)
    socio_w= socio_w.drop(socio_w[socio_w["CountryCode"] == "EU-28"].index)
    socio_w= socio_w.drop(['question_code', 'target_group', 'subset', 'notes'], axis=1)
    return socio_w

def lw():
    living_work = living_data.loc[(living_data["question_label"].str.contains("work")) | (living_data["question_label"].str.contains("job")) | (living_data["question_label"].str.contains("immediate"))]
    living_work['percentage'] = living_work['percentage'].astype(int)
    living_work= living_work.drop(living_work[living_work["CountryCode"] == "EU-28"].index)
    living_work= living_work.drop(['question_code', 'target_group', 'subset', 'notes'], axis=1)
    return living_work

def dw():
    discrimination_work = discrimination_data.loc[(discrimination_data["question_label"].str.contains("work")) | (discrimination_data["question_label"].str.contains("job"))]
    discrimination_work['percentage'] = discrimination_work['percentage'].astype(int)
    discrimination_work= discrimination_work.drop(discrimination_work[discrimination_work["CountryCode"] == "EU-28"].index)
    discrimination_work= discrimination_work.drop(['question_code', 'target_group', 'subset', 'notes'], axis=1)
    return discrimination_work


""" Filtrado de living_data la pregunta Where do you avoid being open about yourself as LGBTI for fear of being assaulted, threatened or harassed by others?"""
def data_avoid():
    avoid= living_data.loc[(living_data["question_label"].str.contains("yourself"))] 
    avoid['percentage'] = avoid['percentage'].astype(int)
    avoid= avoid.drop(avoid[avoid["CountryCode"] == "EU-28"].index)
    return avoid

"""Cambiar a int la columna percentage
def int_percentage(dt=None):
    dt['percentage'] = dt['percentage'].astype(int)
    return dt.info()
"""


""" Obtenemos el total de los paises y de las preguntas"""
def total(dt=None):
    table_total = dt.pivot_table("percentage", index= ["question_label","answer"])
    return table_total


""" Obtenemos los porcentages de todos los paises"""
def total_paises(dt=None):
    table_paises= dt.groupby(["question_label","answer", "CountryCode"])["percentage"].mean().unstack().T
    # En la data de data_socio al ser la misma pregunta la funcion puede ser la siguiente
    # dt.groupby(["answer", "CountryCode"])["percentage"].mean().unstack().T
    return table_paises

# Top 7 head ordenado por orden ascendente 
def rank_head(dt=None,sort=None):
    rank7_head= dt.groupby(["answer", "CountryCode"])["percentage"].mean().unstack().T.sort_values(sort, ascending=True).head(7)
    return rank7_head
    #rank7_head= data_avoid().groupby(["answer", "CountryCode"])["percentage"].mean().unstack().T.sort_values('Workplace ', ascending=True).head(7)

#Top 7 tail
def rank_tail(dt=None,sort=None):
    rank7_tail= dt.groupby(["answer", "CountryCode"])["percentage"].mean().unstack().T.sort_values(sort, ascending=True).tail(7)
    return rank7_tail






