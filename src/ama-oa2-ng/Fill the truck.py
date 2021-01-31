class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]], namely, [ numberOfBoxes, numberOfUnitsPerBox]
        :type truckSize: int ,namely the maximum number of boxes
        :rtype: int the totally maximum units on the turck
        """
        # Sorting the box accoring to the units it could contain in descend order
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        
        
        for box, units in boxTypes: # example [1,3] namely [ 1 box ,  each box could contain 3 units]
            if truckSize > box:
                truckSize -= box
                ans += box * units
            else:
                ans += truckSize * units # greedy Algorithm all the box should be the largest box could contain the most amount of units
                break
            
        return ans
        
        
#Time: O(nlogn)
#Space: O(logn)
        
'''
from typing import List

def fillTheTruck(num: int, boxes: List[int], unitSize: int, unitsPerBox: List[int], truckSize: int) -> int:
    ans = 0
    #boxes_left = truckSize
    for unit, i in sorted([(unit, i) for i, unit in enumerate(unitsPerBox)], reverse=True):
        if truckSize > boxes[i]:
            ans += boxes[i] * unit
            truckSize -= boxes[i]
            
        else:
            ans += truckSize * unit
            break
            
    return ans
        
'''

