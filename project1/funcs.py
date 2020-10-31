# Name:         Ethan Rohlf
# Course:       CPE 101
# Instructor:   Nupur Garg
# Assignment:   Project 1
# Term:         Spring 2017

import math

def pounds_to_kg(pounds):
    kilograms = pounds * 0.453592
    return kilograms

def get_mass_object(obj):
    if obj == ('t'):
        return 0.1
    elif obj == ('p'):
        return 1.0
    elif obj == ('r'):
        return 3.0
    elif obj == ('g'):
        return 5.3
    elif obj == ('l'):
        return 9.07
    else:
        return 0.0
     
def get_velocity_object(distance):
    distance = abs(distance)
    velocity = math.sqrt ((9.8 * distance) / 2)
    return velocity

def get_velocity_skater(mass_skater, mass_object, velocity_object):
    mass_object = abs(mass_object)
    mass_skater = abs(mass_skater)
    velocity_object = abs(velocity_object)
    return ((mass_object * velocity_object) / mass_skater)

