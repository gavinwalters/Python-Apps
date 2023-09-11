

class Rectangle:
    #def object w/ attributes for height and width.
    def __init__(self, height, width):
        self.height = height
        self.width = width

    #method to calc perimieter
    def perimeter(self):
        return 2 * (self.width + self.height)

    #method to calc area
    def area(self):
        return self.width * self.height

    #method for rectangle string
    def string(self):
        w = []

        for i in range(self.height):
            l = []
            for j in range(self.width):
                l.append("  ")
            w.append(l)

        for i in range(self.height):
            for j in range(self.width):
                if i==0 or i==self.height-1:
                    w[i][j] = "* "
                if j==0 or j==self.width-1:
                    w[i][j] = "* "
        
        string = ""

        for i in w:
            for j in i:
                string = string+j
            string = string+"\n"
        
        return string

def main():
    print("Rectangle Calculator")

    #loop until user enters n
    while(True):
        print()
        height = int(input("Height: "))
        width = int(input("Width: "))
        rectangle = Rectangle (height,width)
        print("Perimeter: ", rectangle.perimeter())
        print("Area: ", rectangle.area())
        print(rectangle.string())
        cont = input("Continue? (y/n): ").lower()
        if cont == "n":
            print()
            break

    print("Bye!")

if(__name__ == "__main__"):
    main()