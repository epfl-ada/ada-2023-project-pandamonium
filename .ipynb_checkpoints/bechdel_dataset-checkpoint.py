import numpy as np
import pandas as pd
import time
from difflib import SequenceMatcher as SM
from rapidfuzz import fuzz, utils

#DATASET:
#https://www.kaggle.com/datasets/treelunar/bechdel-test-movies-as-of-feb-28-2023/

#Common movies with strict search: 5562
#Common movies: 6521
#Exact Matches: 5553
#Partial Matches 968
#Total Movies in CMU: 81740
#Total Movies in Bechdel Dataset: 9902
#Finished in 840.4943616390228

data_CMU = pd.read_csv('movie.metadata.tsv',sep='\t')
data_CMU_year = data_CMU.iloc[:,3]
data_CMU_name = data_CMU.iloc[:,2]

data_bechdel = pd.read_csv('bechdel_movies_2023_FEB.csv')
data_bechdel_year = data_bechdel["year"]
data_bechdel_name = data_bechdel["title"]

data_CMU_name = list(data_CMU_name.to_numpy())
data_bechdel_name = list(data_bechdel_name.to_numpy())

data_CMU_year = list(data_CMU_year.to_numpy())
data_bechdel_year = list(data_bechdel_year.to_numpy())

#print(data_bechdel)
#print(data_CMU)
print(len(data_CMU_name), len(data_CMU_year))
print(len(data_bechdel_name), len(data_bechdel_year))

start_time = time.time()
counter_complete = 0
counter_partial = 0
counter_progress = 0
for movie1 in range(len(data_CMU_name)):
    if movie1 % (len(data_CMU_name) // 10) == 0:
        print("------------------%",10*counter_progress ,"passed!-----------------")
        counter_progress += 1
    for movie2 in range(len(data_bechdel_name)):

        if data_CMU_name[movie1] == data_bechdel_name[movie2]:
            counter_complete += 1
            break
        #elif SM(isjunk = None, a = movie1.lower(), b = movie2.lower()).ratio() > 0.85:
        elif fuzz.QRatio(data_CMU_name[movie1].lower(), data_bechdel_name[movie2].lower(), processor=utils.default_process) > 80:
            year1 = str(data_CMU_year[movie1])
            year2 = str(data_bechdel_year[movie2])

            if "-" in year1:
                year1 = year1.split("-")[0]
            
            if year1 == year2:
                print(data_CMU_name[movie1], "---", data_bechdel_name[movie2])
                print(year1, "---", year2)
                counter_partial += 1
                break

print("Common movies:", counter_complete + counter_partial)
print("Exact Matches:", counter_complete)
print("Partial Matches", counter_partial)
print("Total Movies in CMU:", len(data_CMU_name))
print("Total Movies in Bechdel Dataset:", len(data_bechdel_name))
print("Finished in", time.time() - start_time)


#When 100x100 movies are compared,
#common = 7
#time = 0.09379