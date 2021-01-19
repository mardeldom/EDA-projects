import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

""" Tiempo de realización del proyecto"""
def proyect_steps():
    time= [16,20, 25, 30, 20, 10, 5]
    action= ["Localización del tema y los datos","Definir la hipótesis","Limpiar y organizar los dataset", "Visualización","Presentación","Conclusiones", "RoadMap"]
    dt_steps= pd.DataFrame({"Time":time, "Activities":action})
    colors = ['#ff9999','#66b3ff','#ffcc99', "#ff6666", '#c2c2f0','#ffb3e6', '#99ff99'] 
    fig = px.pie(dt_steps, values='Time',names="Activities", color_discrete_sequence=colors, title='The Project Steps Section', width= 700, height=400)
    fig.update_traces(textposition='inside', hole= .6)
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    return fig.show()
    
""" Circunferencia del working status del total de personas que han respondido al cuestionario"""
def visualization_status(data):
    fig1 = px.pie(data, values= "percentage",names="answer", color="answer", width= 1200, height=600)
    fig1.update_traces(textposition='outside',textinfo="percent+label")
    fig1.update_layout(legend=dict(
        orientation="v",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
        ),uniformtext_minsize=13, uniformtext_mode='hide')
    return fig1.show()

""" Visualización de paises_avoid donde se representan todos los paises de la pregunta "Where do you avoid being open about yourself as LGBTI for fear of being assaulted, threatened or harassed by others?"
Como no se puede visualizar muy bien por ser demasiados paises, los he dividido por los que más y los que menos porcentages tienen en la respuesta Workplace.
"""
def visualization_avoid(dt=None):
    fig2, ax= plt.subplots(figsize=(30, 10))
    dt["Where do you avoid being open about yourself as LGBTI for fear of being assaulted, threatened or harassed by others?"].plot(kind="bar", legend="reverse", ax = ax, fontsize=20)
    return fig2.show()

""" Visualización de la pregunta "Where do you avoid being open about yourself as LGBTI for fear of being assaulted, threatened or harassed by others?" que esta dentro de la base de living_data
Divida por los 7 primeros paises con mas representación de Workplace y los que menos representación tienen
"""
def visualization_rank_avoid(dt=None):
    fig3, ax= plt.subplots(figsize=(17, 3))
    dt.plot(kind="bar",legend= "reverse", ax = ax, fontsize=14)
    ax.set_xlabel(None, fontsize=17)
    plt.xticks(rotation=0)
    ax.legend(bbox_to_anchor= (0., 1.02, 1., .102),loc='lower left',mode="expand", borderaxespad=0.,fontsize=11,markerfirst= False,ncol=3)
    return fig3.show()

""" Visualización de un gráfico circular sobre la pregunta Openness about being LGTBI at work de manera generalizada"""
def visualization_openness(dt=None):
    fig4 = px.pie(dt, values='percentage', names='answer', title='Openness about being LGBTI at work', width= 700, height=500, color_discrete_sequence=["#316395","rgb(255,217,47)", "#AA0DFE"])
    fig4.update_traces(textposition='inside', textinfo='percent+label', hole= .3)
    fig4.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    return fig4.show()

""" Visualización de la pregunta anterior dividida tambien por los 7 primeros paises con mas incidencia en la respuesta hide y los 7 que menos incidencia tienen"""
def visualization_rank_being(dt=None):
    fig5, ax= plt.subplots(figsize=(17, 3))
    m= ["#F6F926", "#3366CC", "#AA0DFE"]
    dt.plot(kind="bar",legend= "reverse", ax = ax, fontsize=14, color= m)
    ax.set_xlabel(None, fontsize=17)
    plt.xticks(rotation=0)
    ax.legend(bbox_to_anchor= (0., 1.02, 1., .102),loc='lower left',mode="expand", borderaxespad=0.,fontsize=13,markerfirst= False,ncol=3)
    return fig5.show()

""" Gráfico que representa la base de datos de lw() con las 4 preguntas sobre como se sienten al abrirse en el trabajo, con sus compañeros o superiores
lw() es el filtrado de palabras claves relacionadas con el trabajo en la data total de living, y cambiado la columna percentage a int
"""
def visualization_living(dt=None):
    fig6 = px.bar(dt, x="CountryCode", y="percentage", color="answer", barmode="group",
                facet_row="question_label",
                #category_orders ={"question_label":"Work colleagues"},{"question_label":"Inmediate superiors"},{"question_label":"Customers,clients"},{"question_label":"Openness"},
                width= 1050, height= 600)
    fig6.update_xaxes(title_text = None)
    fig6.update_yaxes(title_text = "Percentage")
    fig6.update_layout(title_text = "Living openly and daily life at work", legend_title_text='Answer')
    fig6.write_html("fig.html")
    return fig6.show()


""" - Matrix de correlación entre las preguntas Openness about being LGBTI at work y In the past 5 years have you heard or seen anyone at work support, protect or promote the rights of LGBTI people at work?
    - Con esta matrix se puede afirmar que cuanto mas abierto es en el trabajo mas ha escuchado a los compañeros proteger o apoyar los derechos en el trabajo y viceversa
"""

def matrix(dt=None):
    fig7= plt.figure(figsize=(10,5))
    c = dt.corr()
    sns.heatmap(c,
                annot=True, 
                cmap=sns.diverging_palette(20, 220, n=200),
                annot_kws={"size":15},
                linewidths=.5,)
    return fig7.show()


