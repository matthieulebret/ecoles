import streamlit as st
import pandas as pd
import numpy as np
import json
import urllib.parse
import requests

import plotly.graph_objects as go

import math
import re

import time
import random

import xlrd

import plotly.express as px


from bs4 import BeautifulSoup

st.set_page_config('Ecoles ingenieur comparatif',layout='wide')

st.title("Ecoles d'ingenieur en France")

col1,col2,col3 = st.beta_columns(3)

with col1:
    st.image('https://images.unsplash.com/photo-1581093803931-46e730e7622e?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8ZW5naW5lZXJpbmd8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60')
with col2:
    st.image('https://images.unsplash.com/photo-1581093806997-124204d9fa9d?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8ZW5naW5lZXJpbmd8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60')
with col3:
    st.image('https://images.unsplash.com/photo-1581090124420-bcab740faf94?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MjZ8fGVuZ2luZWVyaW5nfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60')

# base_url = 'https://etudiant.lefigaro.fr/etudes/ecoles-ingenieurs/classement/'

# df = pd.read_html(base_url)[0]
# st.write(df)


# response = requests.get(base_url)
# st.write(response.ok,response.status_code)
#
# html = response.content

# Make the soup

# soup = BeautifulSoup(html,'lxml')

# list of headers

# divs = soup.find('div',{'class':'content'})

## Tous les classements
#
# links = divs.find_all('a')
# alllinks = [link['href'] for link in links]
# alllinks.insert(0,base_url)


## Recuperer les noms des ecoles pour chaque classement

# allurls = []
# allnames = []
# allrankings = []
#
# for link in alllinks:
#
#     response = requests.get(link)
#     # st.write(response.ok,response.status_code)
#     html = response.content
#
#     soup = BeautifulSoup(html,'lxml')
#
#     divs = soup.find('div',{'class':'sections__ranking'})
#     schoolurls = divs.find_all('a')
#
#     ### List of school urls
#     schoollist = [school['href'] for school in schoolurls]
#     schoolnames = [school.string for school in schoolurls]
#     rankings = [(link,school.string) for school in schoolurls]
#     allurls.extend(schoollist)
#     allnames.extend(schoolnames)
#     allrankings.extend(rankings)
#
# allnames = pd.DataFrame([allurls,allnames]).transpose()
# allnames.columns = ['url Ecole','Ecole']
# allnames.to_csv('all_names.csv')
# st.write(allnames)
#
# bigdf = pd.DataFrame()
# for link in alllinks:
#     df = pd.read_html(link)[0]
#     df['Classement'] = link
#     bigdf = pd.concat([bigdf,df])



# bigdf.to_csv('tous_classements.csv')


# pd.DataFrame(allurls).to_csv('all_schools.csv')

# df = pd.read_csv('all_schools.csv').iloc[:,1]
# df = pd.DataFrame(df)
# df.columns = ['School']
#
# schoollist = df['School'].to_list()
#
#
# nbschools = len(schoollist)
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
#
# placeholder = st.empty()
# progholder = st.empty()
# mybar = st.progress(0)

colheaders = []
errors = []

# df = pd.DataFrame()
#
# i=1
# for school in schoollist:
#     try:
#         response = requests.get(school,headers=headers)
#         html = response.content
#         soup = BeautifulSoup(html,'lxml')
#
#         div = soup.find('div',{'class':'mainside'})
#
#         all_sections = div.find_all('section')
#         sectionlist = [section['class'][0] for section in all_sections]
#         data = []
#         for section in all_sections:
#             divs = section.find_all('div')
#             text_list = [div.find_all('p') for div in divs]
#             items = [item[1].text for item in text_list]
#             data.extend(items)
#             # colheaders.extend([item[0].text for item in text_list])
#
#         data.insert(0,school)
#         pd.DataFrame(data).transpose().to_csv('school_data.csv',mode='a',header=False)
#     except:
#         errors.append(school)
#     with placeholder:
#         st.write(str(i)+' school out of '+str(nbschools)+' done, with '+str(len(errors))+' errors so far.')
#     with progholder:
#         pct_complete = '{:,.2%}'.format((i)/nbschools)
#         st.write(pct_complete,' complete.' )
#         mybar.progress(i/nbschools)
#     time.sleep(random.uniform(1,2))
#     i=i+1
#
# # headers.insert(0,'url Ecole')
# # pd.DataFrame(colheaders).to_csv('colheaders.csv')
#
# st.write('Errors:',errors)
#
# df = pd.read_csv('school_data.csv').iloc[:,1:35]
#
# colheaders = pd.read_csv('headers.csv').iloc[:,1].to_list()
#
# df.columns = colheaders
#
# df = df.drop_duplicates(subset='url Ecole')
#
# df['Excellence'] = df['Excellence'].apply(lambda x: x.replace('#',''))
# df['Excellence'] = pd.to_numeric(df['Excellence'],errors='raise')
#
nan = float('nan')
#
#
# def formatcol(string):
#     if '€' in str(string):
#         string = string.replace(' €','')
#     if ' ' in str(string):
#         string = string.replace(' ','')
#     if '%' in str(string):
#         string = string.replace('%','')
#     return float(string)
#
#
# df.iloc[:,12] = df.iloc[:,12].apply(formatcol)
# df.iloc[:,13] = df.iloc[:,13].apply(formatcol)
# df.iloc[:,14] = df.iloc[:,14].apply(formatcol)/100
# df.iloc[:,15] = df.iloc[:,15].apply(formatcol)/100
#
# df.iloc[:,18] = df.iloc[:,18].apply(formatcol)
# df.iloc[:,19] = df.iloc[:,19].apply(formatcol)
#
# df.iloc[:,21] = df.iloc[:,21].apply(formatcol)/100
# df.iloc[:,22] = df.iloc[:,22].apply(formatcol)/100
# df.iloc[:,23] = df.iloc[:,23].apply(formatcol)/100
# df.iloc[:,24] = df.iloc[:,24].apply(formatcol)/100
# df.iloc[:,26] = df.iloc[:,26].apply(formatcol)/100
#
# df.iloc[:,30] = df.iloc[:,30].apply(formatcol)/100
#
# def formatnotesbac(string):
#     if string == 'Non concerné':
#         string = nan
#     elif string == 'Non communiqué':
#         string = nan
#     return float(string)
#
# df["Moyenne au bac des nouveaux étudiants entrant à bac"] = df["Moyenne au bac des nouveaux étudiants entrant à bac"].apply(formatnotesbac)
#
# def extractnumbers(string):
#     return re.findall(r'\d+',string)
#
#
# df['Nombre admis'] = df['Nombre total d’étudiants recrutés en 2020 en première année de cycle ingénieur'].apply(extractnumbers)
# df['Prepa integree'] = df['Nombre admis'].str[0].apply(lambda x: float(x))
# df['CPGE'] = df['Nombre admis'].str[1].apply(lambda x: float(x))
# df['Admission parallele'] = df['Nombre admis'].str[2].apply(lambda x: float(x))
# df["Nombre total d'admis"] = df['Prepa integree']+df['CPGE']+df['Admission parallele']
#
# df['Prepa integree %'] = df['Prepa integree'] / df["Nombre total d'admis"]
# df['CPGE %'] = df['CPGE'] / df["Nombre total d'admis"]
# df['Admission parallele %'] = df['Admission parallele'] / df["Nombre total d'admis"]
#
#
# schools = pd.read_csv('all_names.csv').iloc[:,1:]
# schools = schools.drop_duplicates(subset='url Ecole')
#
# df = pd.merge(schools,df,on='url Ecole')
#
# adresses = pd.read_csv('adresses avec latlon.csv',engine='python')
#
# adresses.columns = ['Ecole','lat','lon']
#
# df = pd.merge(df,adresses, on='Ecole')
# df['Adresse'].to_excel('adresses.xlsx')



# all_names = df['Ecole'].to_list()
#
# def getname(string):
#     for name in all_names:
#         if name in string:
#             return name
#
# bigdf['Ecole'] = bigdf.iloc[:,1].apply(getname)

# bigdf.to_csv('tous_classements.csv')
#
# bigdf = pd.read_csv('tous_classements.csv').iloc[:,1:]
#
# bigdf = pd.DataFrame(bigdf[['Ecole','Classement','Rang']])
# bigdf.set_index('Classement',inplace=True)
#
# rankinglist = list(set(bigdf.index.to_list()))
#
# def getrank(ecole):
#     try:
#         return int(rankdf[rankdf['Ecole']==ecole]['Rang'][0].replace('#',''))
#     except:
#         return None
#
# for ranking in rankinglist:
#     rankdf = bigdf.loc[ranking]
#     bigdf[ranking] = bigdf['Ecole'].apply(getrank)
#
# bigdf.drop(['Rang'],axis='columns',inplace=True)
newcol = ['Ecole','Classement Generalistes pluri disciplinaires','Classement Materiaux','Classement BTP','Classement Genie industriel et mecanique','Classement Physique chimie','Classement Energie environnement','Classement Transport logistique','Classement Excellence','Classement Informatique mathematiques','Classement Agronomie biologie medical']
# bigdf.columns = newcol
#
# df.drop(['Excellence','Autre classement 1','Autre classement 2'],axis='columns',inplace=True)
# df.drop(['url Ecole','Nombre total d’étudiants recrutés en 2020 en première année de cycle ingénieur','Adresse','Nombre admis','Prepa integree','CPGE','Admission parallele'],axis='columns',inplace=True)
#
# df = pd.merge(df,bigdf,on='Ecole')
# df = df.drop_duplicates(subset='Ecole')

# df.to_excel('core_data.xlsx')


df = pd.read_excel('core_data.xlsx').iloc[:,1:]

rankinglist = newcol[1:]
rankinglist.insert(0,'All')

rankingfilter = st.selectbox('Choisissez une specialisation',rankinglist)

if rankingfilter != 'All':
    df = df[df[rankingfilter]>0]
    df = df.sort_values(by=rankingfilter,ascending=True)

fig = px.scatter_mapbox(df,lat='lat',lon='lon',hover_name='Ecole',color = 'Salaire à la sortie, hors prime',hover_data={'Note générale':True,'Salaire à la sortie, hors prime':True,'lat':False,'lon':False,'Moyenne au bac des nouveaux étudiants entrant à bac':':.2f','Moyenne au bac des nouveaux étudiants entrant à bac +2':':.2f','Pourcentage de mention TB au bac':':.2%',"Nombre total d'admis":':.2f','Prepa integree %':':.2%','CPGE %':':.2%','Admission parallele %':':.2%',"Nombre d'anciens sur Linkedin":True}
    ,zoom=9,center=dict(lat=48.86,lon=2.35),size='Note générale',size_max=15,height=800,category_orders={'Salaire à la sortie, hors prime':['+ de 41 000 €','de 38 000 à 41 000 €','de 35 000 à 38 000 €','de 32 000 à 35 000 €','- de 32 000 €']})
fig.update_layout(mapbox_style='open-street-map',title="Panorama des ecoles")
st.plotly_chart(fig,use_container_width=True)

df.set_index('Ecole',inplace=True)

df = df.style.format(
    {'Note générale':'{:.2f}',
    'Relation entreprise':'{:.2f}',
    'International':'{:.2f}',
    'Excellence académique':'{:.2f}',
    'Frais et droits de scolarité':'Eur {:,.2f}',
    "Nombre d'étudiants dans le programme":'{:,.2f}',
    'Part de femmes':'{:,.2%}',
    "Part d'alternants dans le cycle ingénieur":'{:,.2%}',
    "Nombre d'anciens sur Linkedin":'{:,.2f}',
    "Chiffre d'affaire de la junior entreprise":'Eur {:,.2f}',
    'Part de diplômés étrangers':'{:,.2%}',
    "Part d'étudiants passant un semestre ou plus en échange académique":'{:,.2%}',
    "Part d'étudiants passant plus de six mois en stage à l'étranger":'{:,.2%}',
    "Part de diplômés en poste à l'étranger 1 an après la fin des études (moyenne sur 2 ans)":'{:,.2%}',
    'Part de poursuite en thèse sur 3 ans':'{:,.2%}',
    "Moyenne au bac des nouveaux étudiants entrant à bac":'{:,.2f}',
    "Moyenne au bac des nouveaux étudiants entrant à bac +2":'{:,.2f}',
    "Pourcentage de mention TB au bac":'{:,.2%}',
    'Prepa integree':'{:,.2f}',
    'CPGE':'{:,.2f}',
    'Admission parallele':'{:,.2f}',
    "Nombre total d'admis":'{:,.2f}',
    'Prepa integree %':'{:,.2%}',
    'CPGE %':'{:,.2%}',
    'Admission parallele %':'{:,.2%}',
    'Classement Generalistes pluri disciplinaires':'{:.0f}',
    'Classement Materiaux':'{:.0f}',
    'Classement BTP':'{:.0f}',
    'Classement Genie industriel et mecanique':'{:.0f}',
    'Classement Physique chimie':'{:.0f}',
    'Classement Energie environnement':'{:.0f}',
    'Classement Transport logistique':'{:.0f}',
    'Classement Excellence':'{:.0f}',
    'Classement Informatique mathematiques':'{:.0f}',
    'Classement Agronomie biologie medical':'{:.0f}'
    })


with st.beta_expander('Visualisez les donnees'):
    st.write(df)

# df.to_excel('ecoles.xlsx')

##########################################
##########################################
############ L'etudiant ##################
##########################################
##########################################

# base_url = r'https://www.letudiant.fr/palmares/liste-profils/palmares-des-ecoles-d-ingenieurs/palmares-general-des-ecoles-d-ingenieurs/home.html#indicateurs=900716,900717,900718,900719&criterias'
#
# response = requests.get(base_url)
# st.write(response.ok,response.status_code)
#
# html = response.content

# Make the soup

# soup = BeautifulSoup(html,'lxml')

# list of headers

# schoollinks = soup.find_all('a',{'class':'u-typo-strong'})
#
# alllinks = [(link['href'],link.text) for link in schoollinks]
# # alllinks
#
# placeholder = st.empty()
# progholder = st.empty()
# mybar = st.progress(0)
#
# errors=[]
# bigdf = pd.DataFrame()
# i=1
# nbschools = len(alllinks)
#
# for link in alllinks:
#     try:
#         response = requests.get(link[0])
#         html = response.content
#         soup = BeautifulSoup(html,'lxml')
#         catlist = soup.find_all('a',{'class':'c-pmd-flex__item'})
#         school = [link[1] for cat in catlist]
#         allcat = [cat.text for cat in catlist]
#         scorelist = soup.find_all('td',{'class':'c-pmd-table__value'})
#         allscores = [score.find('span',{'class':'u-typo-strong'}).text for score in scorelist]
#         df=pd.DataFrame([school,allcat,allscores]).transpose()
#         df.to_csv('letudiant.csv',mode='a')
#     except:
#         errors.append(link[1])
#
#     with placeholder:
#         st.write(str(i)+' school out of '+str(nbschools)+' done, with '+str(len(errors))+' errors so far.')
#     with progholder:
#         pct_complete = '{:,.2%}'.format((i)/nbschools)
#         st.write(pct_complete,' complete.' )
#         mybar.progress(i/nbschools)
#     time.sleep(random.uniform(2,4))
#     i=i+1

st.header("Classement l'Etudiant")

# bigdf = pd.read_csv('letudiant.csv').iloc[:,1:]
# bigdf.columns = ['Ecole','Critere','Note']
# bigdf = bigdf[bigdf['Ecole']!='0']
#
# schoollist = bigdf['Ecole'].unique().tolist()
# criterelist = bigdf['Critere'].unique().tolist()
#
# bigdf.set_index('Ecole',inplace=True)
#
# def getnote(critere):
#     try:
#         return df[df['Critere']==critere]['Note'][0]
#     except:
#         return None
#
# newdf = pd.DataFrame()
#
# for school in schoollist:
#     notes = [school]
#     for critere in criterelist:
#         df = bigdf.loc[school]
#         notes.append(getnote(critere))
#     newdf = newdf.append(pd.DataFrame(notes).transpose())
#
# criterelist.insert(0,'Ecole')
# newdf.columns=criterelist
#
# newdf.to_csv('letudiant_all_data.csv')

df = pd.read_csv('letudiant_all_data.csv').iloc[:,1:]


orientcol = df.columns[27:41].insert(0,'Ecole')

orientation = df[[col for col in orientcol]]

def formatcol(string):
    if '%' in str(string):
        string=string.replace('%','')
    if ',' in str(string):
        string=string.replace(',','.')
    if str(string) == 'NC':
        string = nan
    return float(string)/100

for col in orientcol[1:]:
    orientation[col] = orientation[col].apply(formatcol)


schoollist = orientation['Ecole'].unique().tolist()
schoollist.sort()

schoolselect = st.multiselect('Selectionnez les ecoles',schoollist,default=schoollist[:3])

orientation = orientation[orientation['Ecole'].isin(schoolselect)]
orientation.fillna(0,inplace=True)

##### Spider chart

categories = orientcol[1:].to_list()

# orientation[orientation['Ecole']==schoolselect[0]][categories[0]].values[0]


fig = go.Figure()

for school in schoolselect:
    fig.add_trace(go.Scatterpolar(
          r=[orientation[orientation['Ecole']==school][cat].values[0] for cat in categories],
          theta=categories,
          fill='toself',
          name=school
    ))

fig.update_layout(template='plotly_dark',
                polar=dict(
                    radialaxis=dict(tickformat='%')
                ))


st.plotly_chart(fig,use_container_width=True)

df.set_index('Ecole',inplace=True)


def formatnote(string):
    if ',' in str(string):
        string = string.replace(',','.')
    if ' semaines' in str(string):
        string = string.replace(' semaines','')
    if str(string) == 'NC':
        string = nan
    return float(string)


df.iloc[:,1] = df.iloc[:,1].apply(formatnote)
df.iloc[:,2] = df.iloc[:,2].apply(formatnote)
df.iloc[:,3] = df.iloc[:,3].apply(formatcol)
df.iloc[:,4] = df.iloc[:,4].apply(formatcol)
df.iloc[:,5] = df.iloc[:,5].apply(formatnote)
df.iloc[:,6] = df.iloc[:,6].apply(formatnote)
df.iloc[:,7] = df.iloc[:,7].apply(formatcol)
df.iloc[:,8] = df.iloc[:,8].apply(formatnote)
df.iloc[:,9] = df.iloc[:,9].apply(formatnote)

df.iloc[:,11] = df.iloc[:,11].apply(formatnote)
df.iloc[:,12] = df.iloc[:,12].apply(formatnote)
df.iloc[:,13] = df.iloc[:,13].apply(formatnote)

df.iloc[:,14] = df.iloc[:,14].apply(formatcol)

df.iloc[:,19] = df.iloc[:,19].apply(formatcol)
df.iloc[:,20] = df.iloc[:,20].apply(formatcol)

df.iloc[:,22] = df.iloc[:,22].apply(formatcol)

for i in range(25,40):
    df.iloc[:,i] = df.iloc[:,i].apply(formatcol)
    i=i+1

df.iloc[:,43] = df.iloc[:,43].apply(formatnote)
df.iloc[:,44] = df.iloc[:,44].apply(formatcol)

for i in range(45,51):
    df.iloc[:,i] = df.iloc[:,i].apply(formatnote)
    i=i+1

df.iloc[:,51] = df.iloc[:,51].apply(formatcol)
df.iloc[:,52] = df.iloc[:,52].apply(formatcol)
df.iloc[:,53] = df.iloc[:,53].apply(formatcol)

df.iloc[:,60] = df.iloc[:,60].apply(formatnote)
df.iloc[:,61] = df.iloc[:,61].apply(formatcol)
df.iloc[:,63] = df.iloc[:,63].apply(formatcol)

df.iloc[:,65] = df.iloc[:,65].apply(formatnote)

df.iloc[:,69] = df.iloc[:,69].apply(formatnote)
df.iloc[:,70] = df.iloc[:,70].apply(formatnote)
df.iloc[:,71] = df.iloc[:,71].apply(formatnote)

with st.beta_expander('Visualiser les donnees'):
    st.write(df)
