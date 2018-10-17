# object oriented programming with Python
# Michael Wack 2015

class Fruit:
    def __init__(self, weight):
        self.weight = weight

    def __repr__(self):
        return( "fruit with weight {:.2e}".format( self.weight))


class Rock:
    # class variable
    rockcounter=0


    @classmethod
    def BlueRock(cls, weight, volume):
        return cls( color="blue", weight=weight, volume=volume)


    @staticmethod
    def density( weight, volume):
        return weight / volume

    def __init__(self, color, weight, volume=11e-6):
        self.color = color
        self.weight = weight  # SI: kg
        self.volume = volume  # SI: m^3

        Rock.rockcounter += 1
        self.no = Rock.rockcounter

        print("{}. rock created".format(Rock.rockcounter))

    def calculate_density(self):
        return Rock.density( self.weight, self.volume)  # SI: kg / m^3


    def __repr__(self):
        return( "{} rock (No {}) with a density of {:.2f}".format( self.color, self.no, self.calculate_density()))


class Sediment( Rock):
    def __init__(self, color, weight, volume=11e-6, grainsize=0):
        super().__init__(color, weight, volume)

        self.grainsize = grainsize


    def double_grainsize(self):
        self.grainsize *= 2

    def __repr__(self):
        return( "{} sediment (No {}) with a density of {:.2e} and a grainsize of {:.2e}".format( self.color, self.no, self.calculate_density(), self.grainsize))



class MagneticMatter(): # all volume normalized
    def __init__(self, magnetization=0, susceptibiltiy=0):
        self.magnetization = magnetization # Am^2 / m^3 = A/m
        self.susceptibility = susceptibiltiy # volume normailzed -> no units

    def induced_magnetization(self, external_field_H): # SI A/m
        return self.susceptibility * external_field_H

    def total_magnetization(self, external_field_H): # SI A/m
        return self.induced_magnetization(external_field_H) + self.magnetization



class MagneticSediment( MagneticMatter, Sediment):
    def __init__(self, color, weight, volume, grainsize=0, magnetization=0, susceptibility=0):
        MagneticMatter.__init__( self, magnetization, susceptibility)
        Sediment.__init__( self, color, weight, volume)

    def magnetic_moment(self):
        return self.magnetization * self.volume


# class to determine weight of other object instances
class Scale():
    def __init__(self, weight_limit=100):
        self.weight_limit = weight_limit
        self.instances = []

    def put_on(self, inst):
        if inst in self.instances:
            print("{} is already on scale.".format(inst))
        else:
            self.instances.append(inst)
            print("{} placed on scale.".format(inst))

    def take_off(self, inst):
        try:
            self.instances.remove(inst)
            print("{} removed.".format(inst))
        except KeyError:
            print("{} was not on scale.".format(inst))

    @property
    def weight(self):
        weight = 0
        for i in self.instances:
            weight += i.weight
        if weight > self.weight_limit:
            print("Scale overloaded.")

        return weight
