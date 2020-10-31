import sys

def get_pixels(filename):
    try:
        inf = open(filename, 'r')
    except FileNotFoundError:
        print("Unable to open {}".format(filename))
    except IndexError:
        print("Usage:")
    outf = open('faded.ppm', 'w')
    line1 = inf.readline()
    outf.write(line1)
    line2 = inf.readline()
    outf.write(line2)
    line3 = inf.readline()
    outf.write(line3)
    pixel = []
    c = 0
    for line in inf.readlines():
        lines = line.split()
        for obj in lines:
            pixel.append(int(obj))
            if len(pixel) == 3:
                line3 = line2.split()
                width = int(line3[0])
                x = c % width
                y = (c - x) // width
                c += 1
                dist = distance_from_radius(x, y, int(sys.argv[3]), int(sys.argv[2]))
                fade = scale(int(sys.argv[4]), dist, pixel)
                outf.write(str(fade[0]) + '\n' + str(fade[1]) + '\n' + str(fade[2]) + '\n')
                pixel = []


def scale(radius, distance, pixel):
    scale = (radius - distance) / radius
    if scale < 0.2:
        scale = 0.2
    pixel[0] = int(pixel[0] * scale)
    pixel[1] = int(pixel[1] * scale)
    pixel[2] = int(pixel[2] * scale)
    return pixel


def distance_from_radius(x1, y1, x2, y2):
    return((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


def main():
    pix = get_pixels(sys.argv[1])

if __name__ == '__main__':
    main()
