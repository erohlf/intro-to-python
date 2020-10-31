import sys

def groups_of_three(lst, num):
    result = [lst[x:x+num] for x in range(0, len(lst), num)]
    return result

def return_pixels(filename):
    try:
        in_file = open(filename, 'r')
    except FileNotFoundError:
        print("Unable to open {}".format(filename))
    out_file = open('decoded.ppm', 'w')
    line1 = in_file.readline()
    out_file.write(line1)
    line2 = in_file.readline()
    out_file.write(line2)
    line3  = in_file.readline()
    out_file.write(line3)
    output = []
    for line in in_file.readlines():
        lines = line.split()
        for obj in lines:
            output.append(int(obj)) 
            if len(output) == 3:
                deco = decode(output)    
                out_file.write(str(deco[0]) + '\n' +  str(deco[1]) + '\n' + str(deco[2]) + '\n')
                output = []        

def decode(pixel):
    red_pixel = pixel[0] * 10
    pixel[0] = red_pixel
    if red_pixel > 255:
        red_pixel = 255
    pixel[1] = red_pixel
    pixel[2] = red_pixel
    return pixel
    


def main():
    pixels = return_pixels(sys.argv[1])
    
if __name__ == '__main__':
    main()
      
