import sys
import decode

def get_pixels(filename):
    try:
        inf = open(filename, 'r')
    except IOError:
        print("Unable to open {}".format(filename))
        exit()
    except IndexError:
        print("Usage: python3 blur.py <image> [<reach>]")
        exit()
    outf = open('blurred.ppm', 'w')
    line1 = inf.readline()
    outf.write(line1)
    line2 = inf.readline()
    outf.write(line2)
    line3 = inf.readline()
    outf.write(line3)
    output = []
    complete = []
    for line in inf.readlines():
       lines = line.split()
       for num in lines:
           output.append(num)
    line4 = line2.split()
    width = int(line4[0])
    group = decode.groups_of_three(output, 3)
    blur = blur_image(group, width, sys.argv[2])
    for num in blur:
        outf.write(str(num) + '\n')
    inf.close()
    outf.close()
        

def blur_image(pixels, width, reach):
    new_pix = []
    for y in range(0, int(len(pixels) / width)):
        for x in range(0, width):
            r_total = 0
            g_total = 0
            b_total = 0
            count = 0
            for y2 in range(y - int(reach), y + int(reach) + 1):
                for x2 in range(x - int(reach), x + int(reach) + 1):
                    if x2 >= 0 and  x2 <= width and  y2 >= 0 and  y2 <= int(len(pixels) / width):
                        red = pixels[y2 * width + x2][0]
                        green = pixels[y2 * width + x2][1]
                        blue = pixels[y2 * width + x2][2]
                        count += 1
                        r_total += int(red)
                        g_total += int(green)
                        b_total += int(blue)
            if count != 0:
                r_avg= r_total / count
                g_avg = g_total / count
                b_avg = b_total / count
                new_pix.append(int(r_avg))
                new_pix.append(int(g_avg))
                new_pix.append(int(b_avg))
    return new_pix


def main():
    pixels = get_pixels(sys.argv[1]) 

if __name__ == '__main__':
    main()
