class weight():
    weight = 100

    def to_pounds(self):  # method
        return 2.205 * self.weight


def to_pounds(kilos):  # funct
    return 2.205 * kilos


w = weight()  # calling a method
pounds = w.to_pounds()

kilos = 100  # calling a function
pounds = to_pounds(kilos)

print("Test")
