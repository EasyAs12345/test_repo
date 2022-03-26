#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:03:43 2021

@author: john
"""

import numpy as np
import pandas as pd

filename = '/home/john/DataScience/SpyderProjects/dogs.csv'

dogs = pd.read_csv(filename)

print(dogs)

print(dogs.columns)
print(dogs.index)

dogs_ind = dogs.set_index("name")
print(dogs_ind)

print(dogs_ind.reset_index())

#  name was set as index, dropped and it is no longer displayed
print(dogs_ind.reset_index(drop=True))

print(dogs[dogs["name"].isin(["Bella", "Stella"])])
print(dogs_ind.loc[["Bella", "Stella"]])

dogs_ind2 = dogs.set_index("breed")
print(dogs_ind2)

print(dogs_ind2.loc["Labrador"])

dogs_ind3 = dogs.set_index(["breed", "color"])
print(dogs_ind3)

print(dogs_ind3.loc[["Labrador", "Chihuahua"]])

print(dogs_ind3.loc[[("Labrador", "Brown"), ("Chihuahua", "Tan")]])

print(dogs_ind3.sort_index())
print(dogs_ind3.sort_index(level=["color", "breed"], ascending=[True, False]))


breeds = ["Labrador", "Poodle",
          "Chow Chow", "Schnauzer",
          "Labrador", "Chihuahua",
          "St. Bernard"]

print(breeds)
print(breeds[2:5])

dogs_srt = dogs.set_index(["breed", "color"]).sort_index()
print(dogs_srt)

#   strange, but final value 'Poodle' is included
print(dogs_srt.loc["Chow Chow":"Poodle"])

print(dogs)
print(dogs_srt.loc[("Labrador", "Brown"):("Schnauzer", "Grey")])

print(dogs_srt.loc[:, "name":"height_cm"])
print(dogs_srt.loc[("Labrador", "Brown"):("Schnauzer", "Grey"), "name":"height_cm"])

dogs = dogs.set_index("date_of_birth").sort_index()
print(dogs)

print(dogs.loc["2014-08-25":"2016-09-16"])

