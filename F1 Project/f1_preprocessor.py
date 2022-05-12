# -*- coding: utf-8 -*-
"""F1_preprocessor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tjDFH_z5Fd9fiCri3On25DW7f7_VTIyr
"""

def time_sec(s):
  if s.startswith('0 days 00:'):
    s = s[10:]
  (splitted_time,sec) = s.split(":")

  total = float(splitted_time) * 60 + float(sec)
  answer = round(total,3)
  return answer


def indexer(s):
  if s == 'SOFT':
    return 0
  if s == 'MEDIUM':
    return 1
  if s == 'HARD':
    return 2
  if s == 'INTERMEDIATE':
    return 3



def cleaning(df):
  # DROPS.
  df.drop('Unnamed: 0',axis=1,inplace=True)
  features = ['LapTime','LapNumber','Stint','Sector1Time','Sector2Time','Sector3Time','Compound','TyreLife','Driver','Team']
  df.dropna(subset = features ,inplace=True)

  # DATA TYPES.
  df = df.astype({"LapTime": str}, errors='raise') 
  df = df.astype({"Sector1Time": str}, errors='raise') 
  df = df.astype({"Sector2Time": str}, errors='raise') 
  df = df.astype({"Sector3Time": str}, errors='raise') 

  # TIMES IN TERMS OF SECONDS.
  df['LapTime'] = df['LapTime'].map(time_sec)
  df['Sector1Time'] = df['Sector1Time'].map(time_sec)
  df['Sector2Time'] = df['Sector2Time'].map(time_sec)
  df['Sector3Time'] = df['Sector3Time'].map(time_sec)

  df = df.astype({"Compound": str}, errors='raise')
  df['Compound'] = df['Compound'].map(indexer)

  df.drop(['Time','DriverNumber','SpeedST','FreshTyre','LapStartTime','TrackStatus','IsAccurate','LapStartDate'],axis=1,inplace=True)
  df.drop(['Sector1SessionTime','Sector2SessionTime','Sector3SessionTime','SpeedI1','SpeedI2','SpeedFL'],axis=1,inplace=True)

  df['PitOutTime'] = df['PitOutTime'].fillna(0)
  df['PitInTime'] = df['PitInTime'].fillna(0)

  df.loc[df.PitOutTime != 0, 'PitOutTime'] = 1
  df.loc[df.PitInTime != 0, 'PitInTime'] = 1


  return df
