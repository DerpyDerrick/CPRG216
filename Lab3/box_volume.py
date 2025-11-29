def volume(length, width, height):
    return (length*width*height)

def main():
    l = float(input("Box #1 length (cm): "))
    w = float(input("Box #1 width (cm): "))
    h = float(input("Box #1 height (cm): "))
    print("Box #1 volume is", volume(l,w,h),"cm")

    l = float(input("Box #2 length (cm): "))
    w = float(input("Box #2 width (cm): "))
    h = float(input("Box #2 height (cm): "))
    print("Box #2 volume is", volume(l,w,h),"cm")

main()