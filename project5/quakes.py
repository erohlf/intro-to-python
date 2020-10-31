import quake_funcs

def main():
    print("Earthquakes:\n------------")
    quakes = quake_funcs.read_quakes_from_file('quakes.txt')
    for obj in quakes:
        print(obj)
    print('')
    letter = True
    while letter == True:
        user = input("Options:\n (s)ort\n (f)ilter\n (n)ew quakes\n (q)uit\n\nChoice: ")
        if user == 's' or user == 'S':
            lett = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? \n")
            sorting = quake_funcs.quakes_sort(quakes, lett)
            quakes = sorting
            print("Earthquakes:\n------------")
            for obj in sorting:
                print(obj)
            print('')
        elif user == 'f' or user == 'F':
            let = input("Filter by (m)agnitude or (p)lace? ")
            if let == 'p' or let == 'P':
                string = input("Search for what string? \n")
                filtering = quake_funcs.filter_by_place(quakes, string)
                print("Earthquakes:\n------------")
                for obj in filtering:
                    print(obj)
                print('')
            elif let == 'm' or let == 'M':
                low = input("Lower bound: ")
                high = input("Upper bound: \n")
                filtering = quake_funcs.filter_by_mag(quakes, low, high)
                print("Earthquakes:\n------------")
                for obj in filtering:
                    print(obj)
                print('')
        elif user == 'q' or user == 'Q':
            quit = quake_funcs.read_back(quakes,'quakes.txt')
            letter = False
        elif user == 'n' or user == 'N':
            quakes_dict = quake_funcs.get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
            x =  quakes_dict["features"]
            for obj in x:    
                quake = quake_funcs.quake_from_feature(obj)
                if quake not in quakes:
                    quakes.append(quake)
            print("New quakes found!!!\n")
            print("Earthquakes:\n------------")
            for j in quakes:
                print(j)
            print('')

if __name__ == '__main__':
    main()
