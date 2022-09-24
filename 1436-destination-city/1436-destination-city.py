class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        cities = {}
        for path in paths:
            city = path[0]
            destination = path[1]
            if city not in cities:
                cities[city] = destination
        
        for path in paths:
            destination = path[1]
            if destination not in cities:
                return destination
        return None