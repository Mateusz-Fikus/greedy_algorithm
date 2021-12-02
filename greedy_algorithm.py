from math import sqrt
import random

class GreedyAlgorithm():
    #Extract coordinates from the file
    def parse(file_path):
        with open(file_path, 'r+') as temp_file:
            lines = temp_file.readlines()
            cords = []
            for line in lines:
                if line[0].isdigit():
                    cords.append(line.split()[0:3])
            temp_file.close()

            #Return nested list of coordinates i.e [[12,34], [34,23]...]
            return cords

    #Calculate distance using greedy algorithm
    def calculate(cords_list):
        # Starting from random city
        start_city = cords_list[random.randint(0, len(cords_list)-1)]
        path = [start_city]
        cords_list.pop(int(start_city[0])-1)

        #Loop trough cities added to path, continous loop untill all cities are visited
        for city in path:
            print(f'we are now going from {city}')
            distances = {}

            #Check if there are cities left to visit
            if len(cords_list) == 0:
                break

            #Loop trough every city in cords list to find the shortest path
            for decision in cords_list:
                
                distance = sqrt((float(decision[1]) - float(city[1]))**2
                            + (float(decision[2]) - float(city[2]))**2)
                
                #Add distance to the city with its instance index
                distances[decision[0]] = distance

            #Get the shortest path from the dictionary
            closest_city = min(distances, key=distances.get)

            #Find the closest city in cords list, append it to path and remove from
            #cords
            for x in cords_list:
                if x[0] == closest_city:
                    path.append(x)
                    cords_list.remove(x)

            print(f'from point {city} \ndistances are: {distances}, \
                 \n closest city is: {closest_city} \n current path is {path}')

        return path

GreedyAlgorithm.calculate(GreedyAlgorithm.parse('coordinates_files/berlin52.tsp'))
GreedyAlgorithm.calculate(GreedyAlgorithm.parse('coordinates_files/berlin11_modified.tsp'))
GreedyAlgorithm.calculate(GreedyAlgorithm.parse('coordinates_files/kroA150.tsp'))