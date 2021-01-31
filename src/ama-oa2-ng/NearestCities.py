from typing import List

#BSearch and Map
#Each query asks for the nearest city that shares either the x or y coordinates of the target city. 
#We can use maps to store coordinate: [city]. 
#Then for each query, we collect the list of candidate cities and find the closest city. 
#We can cache the results in case the same query is asked more than once.
#To apply binary search, we had to sort the list by coordinates and that incurred "n log n" cost.



def findNearestCities(numOfCities: int, cities : List[str], xCoordinates : List[int], yCoordinates : List[int], numOfQueries : int, queries : List[str]) -> List[str]:
    
    class City:
        def __init__(self, name, x, y):
            self.name = name
            self.x = x
            self.y = y
        def dist(self, other_city):
            return (self.x - other_city.x) ** 2 + (self.y - other_city.y) ** 2
            
            
            
    from collections import defaultdict
    xs = defaultdict(list) # x_coordinate: [city]
    ys = defaultdict(list)
    city_by_name = {}
    
    
    
    for i in range(numOfCities):
        name = cities[i]
        city = City(name, xCoordinates[i], yCoordinates[i])
        xs[city.x].append(city)
        ys[city.y].append(city)
        city_by_name[name] = city
    ans = []
    cache = {}
    
    for name in queries:
        if name in cache:
            ans.append(cache[name])
            continue
        city = city_by_name[name]
        search_cities = xs[city.x] + ys[city.y]
        if len(search_cities) == 2: # the target city itself is always in xs and ys, so if there are only two elements, no other city is in the list, we add NONE to the final result
            ans.append('NONE')
            continue
        search_cities.sort(key=lambda x: x.dist(city))
        closest = search_cities[2].name
        ans.append(closest)
        cache[city.name] = closest
        cache[closest] = city.name
        
        
    return ans
    
#Time Complexity: O(n.log n), where n refers number of cities.

#Space Complexity:  O(m), where m refers to the number of queries.
    
