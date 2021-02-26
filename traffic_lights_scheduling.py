# Define the different objects of the city plan
class Intersection:
    def __init__(self, id, incomingStreets, outcomingStreets):
        """
        :param id: the id of the intersection
        """
        self.id = id
        self.incomingStreets = incomingStreets
        self.outcomingStreets = outcomingStreets

    def update_incoming_streets(self, street):
        self.incomingStreets.append(street)

    def update_outcoming_streets(self, street):
        self.outcomingStreets.append(street)

class Street:
    def __init__(self, name, duration, intStart, intEnd ):
        """
        :param name: the name of the street
        :param duration: the needed time to traverse the street
        :param intStart: the id of the intersection at the start of the street
        :param intEnd: the id of the intersection at the end of the street
        """
        self.name = name
        self.L = duration
        self.intStart = intStart
        self.intEnd  = intEnd

class Car:
    def __init__(self, id, numStreets, streets):
        """
        :param id: the id of the car
        :param numStreets: the number of streets that the car wants to travel
        :param streets: the streets traversed in order
        """
        self.id = id
        self.numStreets = numStreets
        self.streets = streets


def read_input_data(file_path ):
    file = open(file_path, 'r')
    numLine = 0
    for line in file.readlines():
        line = line.strip('\n')
        items = line.split(' ')
        if numLine == 0:
            D, I, S, V, F = ( int(i) for i in tuple(items))
        else:
            if numLine <= S:
                intStart , intEnd, streetName, L = tuple(items)
                streets[streetName] = Street(streetName, L, int(intStart), int(intEnd) )
                if intStart not in intersections:
                    intersections[intStart] = Intersection(intStart, [], [streetName])
                else:
                    intersections[intStart].update_outcoming_streets(streetName)
                if intEnd not in intersections:
                    intersections[intEnd] = Intersection(intEnd, [streetName], [])
                else:
                    intersections[intEnd].update_incoming_streets(streetName)
            else:
                P, carStreets = items[0], items[1:]
                cars[numLine - S] = Car(numLine - S, P, carStreets)

        numLine += 1
    return D, I, S, V, F

def write_output_data(file_path, output):
    f = open(file_path, "w")
    f.writelines(output)


def traffic_lights_scheduling(D, I, S, V, F, streets, cars):
    pass

if __name__ == '__main__':
    #test_files = [ "a", "b", "c", "d", "e", "f"]
    test_files = ["a"]
    for file in test_files:
        # D : the duration of the simulation
        # I : the number of intersections
        # S : the number of streets
        # V : the number of cars
        # F : the bonus points for each car that reaches the destination
        # the streets defined in the city
        streets = {}
        # the different cars running in the city
        cars = {}
        # the intersections in the city
        intersections = {}
        # read test file
        D, I, S, V, F  = read_input_data( "Data/" + file + ".txt")
        # define the traffic lights scheduling
        output = traffic_lights_scheduling()
        # write the output
        write_output_data("Data/output/" + file + ".txt")



