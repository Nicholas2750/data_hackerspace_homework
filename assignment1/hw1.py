#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    #Stores CSV data into histogram_data.
    with open(filename) as histogram:
        csv_reader = csv.reader(histogram)
        histogram_data = list(csv_reader)

    #Creates a list for hour 0 - 23.
    eventHours = [0 for i in range (0, 24)]

    #Goes through histogram_data.
    for event in histogram_data[1: ]:
        #Access the time collumn and gets the first 2 character of the time/hour.
        tempHour = event[1][0 : 2]
        #Ignores datas that cannot be turned into integers.
        if not tempHour.isdigit():
            continue
        #Changes tempHour's data type to integers.
        tempHour = int(tempHour)
        #Adds every event to eventHours according to its occurence hour.
        eventHours[tempHour] += 1

    return eventHours


def weigh_pokemons(filename, weight):
    #Stores JSON file into pokemon_database.
    with open(filename) as f:
        pokemon_database = json.load(f)

    #Creates an empty list to store matching pokemon in.
    matchingPokemon = []

    #Goes through every pokemon in the database.
    for pokemon in pokemon_database['pokemon']:
        #Checks if the weight in the database (with the 'kg' removed) matches
        #with the inputted weight.
        if float(pokemon['weight'][ : -2]) == weight:
            #Adds matching pokemon to the list prepared.
            matchingPokemon.append(pokemon['name'])

    return matchingPokemon


def single_type_candy_count(filename):
    #Stores JSON file into pokemon_database.
    with open(filename) as f:
        pokemon_database = json.load(f)

    candySum = 0;

    #Goes through every pokemon in the database.
    for pokemon in pokemon_database['pokemon']:
        #Checks if the pokemon is a single type.
        if 'candy_count' in pokemon and len(pokemon['type']) == 1:
            #Adds the pokemon's candy count to candySum.
            candySum += pokemon['candy_count']

    return candySum


def reflections_and_projections(points):
    #Reflects points over y = 1.
    for i in range(len(points[1])):
        points[1][i] = 2 -(points[1][i])

    #Rotates points 90 degrees around the origin.
    points = np.matmul([[0, -1], [1, 0]], points)

    #Project the points onto the line y = 3x
    points = np.matmul([[1, 3], [3, 9]], points) / 10

    return points


def normalize(image):
    #Finds the maximum and minimum value in the 2 dimensional array (image).
    maximum = max(max(x) for x in image)
    minimum = min(min(x) for x in image)

    #Changes every element in the two dimensional array according to the formula.
    image =  255 / (maximum - minimum) * (np.array(image) - minimum)

    return image


def sigmoid_normalize(image, a):
    #Changes every element in the two dimensional array according to the formula.
    image = 255 * (1 + exp((-a ** -1) * (np.array(image) - 128))) ** (-1)
    return image
