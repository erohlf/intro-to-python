from urllib.request import urlopen
from json import loads
from datetime import datetime

# Name: Ethan Rohlf
# Course: CPE101
# Instructor: Nupur Garg
# Assignment: Project 5
# Term: Spring 2017

# GIVEN FUNCTIONS: Use these two as-is and do not change them
def get_json(url):
    """Function to get a JSON dictionary from a website.

    Args:
        url (str): The url from which to get the JSON

    Returns:
        A Python dictionary containing the information from the JSON object
    """
    with urlopen(url) as response:
        html = response.read()
    htmlstr = html.decode("utf-8")
    return loads(htmlstr)


def time_to_str(time):
    """Converts integer seconds since unix epoch to a string.

    Args:
        time (int): Unix time

    Returns:
        A nicely formated time string
    """
    return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

# TODO: Add Earthquake class definition here
class Earthquake(object):
    def __init__(self, place, mag, longitude, latitude, time):
        self.place = place
        self.mag = mag
        self.longitude = longitude
        self.latitude = latitude
        self.time = time

    def __eq__(self, other):
        return(self.place == other.place and self.mag == other.mag and self.longitude == other.longitude and self.latitude == other.latitude and self.time == other.time)

    def __str__(self):
        return ("({1:.2f}) {0:>40} at {4} ({2:>8.3f}, {3:.3f})").format(self.place, float(self.mag), float(self.longitude), float(self.latitude), time_to_str(float(self.time)))
    
    def __repr__(self):
        return


# TODO: Required function - implement me!
def read_quakes_from_file(filename):
    in_file = open(filename, 'r')
    output = []
    x = ' '
    for line in in_file.readlines():
        line2 = line.split()
        place = ' '.join(line2[4:-1])
        place += x
        place += ''.join(line2[-1])
        result = Earthquake(place, line2[0], line2[1], line2[2], line2[3])
        output.append(result)
    in_file.close()
    return output


# TODO: Required function - implement me!
def filter_by_mag(quakes, low, high):
    lst = []
    for obj in quakes:
        if obj.mag >= low and obj.mag <= high:
            lst.append(obj)
    return lst



def quakes_sort(quakes, letter):
    if letter == 'm' or letter == 'M':
        return sorted(quakes, key = lambda quakes:quakes.mag, reverse = True)
    elif letter == 't' or letter == 'T':
        return sorted(quakes, key = lambda quakes:quakes.time, reverse = True)
    elif letter == 'l' or letter == 'L':
        return sorted(quakes, key = lambda quakes:quakes.longitude, reverse = True)
    elif letter == 'a' or letter == 'A':
        return sorted(quakes, key = lambda quakes:quakes.latitude)
             
def read_back(quakes, filename):
    out_file = open(filename, 'w')
    for obj in quakes:
        obj = ("{0} {1} {2} {3} {4}\n").format(float(obj.mag), obj.longitude, obj.latitude, obj.time, obj.place)
        obj = str(obj)
        out_file.write(obj + '\n')

    out_file.close()


# TODO: Required function - implement me!
def filter_by_place(quakes, word):
    lst2 = []
    letter = word[0]
    wordup = word.upper()
    wordlow = word.lower()
    up = word.replace(letter, letter.upper())
    low = word.replace(letter, letter.lower())
    for obj in quakes:
        u = word.isupper()
        l = word.islower()
        if wordup in obj.place:
            lst2.append(obj)
        elif wordlow in obj.place:
            lst2.append(obj)
        elif up in obj.place:
            lst2.append(obj)
        elif low in obj.place:
            lst2.append(obj)
    return lst2


# TODO: Required function for final part - implement me too!
def quake_from_feature(feature):
        place = feature["properties"]["place"]
        mag = feature["properties"]["mag"]
        longitude = feature["geometry"]["coordinates"][0]
        latitude = feature["geometry"]["coordinates"][1]
        milliseconds = feature["properties"]["time"]
        time = int(milliseconds / 1000)
        quake =  Earthquake(place, mag, longitude, latitude, time) 
        return quake
    


# TODO: Required function - implement me!
def filter_by_place(quakes, word):
    lst2 = []
    letter = word[0]
    wordup = word.upper()
    wordlow = word.lower()
    up = word.replace(letter, letter.upper())
    low = word.replace(letter, letter.lower())
    for obj in quakes:
        u = word.isupper()
        l = word.islower()
        if wordup in obj.place:
            lst2.append(obj)
        elif wordlow in obj.place:
            lst2.append(obj)
        elif up in obj.place:
            lst2.append(obj)
        elif low in obj.place:
            lst2.append(obj)
    return lst2




# TODO: Required function for final part - implemen 
