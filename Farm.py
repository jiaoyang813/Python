# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:38:09 2017
Farm
@author: Oscar
"""
from gurobipy import *

years = ["year1", "year2","year3","year4", "year5"]
herdtype = ["cow","heifer"]
landtype = ["grain","sugar"]

totalLand = 200
initialCow = 100
initialHeifer = 20

#variables
model = Model("Farm")
#model.Params.UpdateMode = 1

herds = model.addVars(years, herdtype, name="herd")

lands = model.addVars(years, landtype, name= "land")

#constraints

#land capacity each year
model.addConstrs((herds[years[years.index(year)-1],herdtype[0]] 
        + herds[years[years.index(year)-1],herdtype[1]]*2/3 <= totalLand
        for year in years), "LandCapa")

##initial herds
model.addConstr(herds[years[0], herdtype[0]] == initialCow, "InitialCow")
model.addConstr(herds[years[0], herdtype[1]] == initialHeifer,"InitialHeifer")


#new heifer
#model.addConstrs()