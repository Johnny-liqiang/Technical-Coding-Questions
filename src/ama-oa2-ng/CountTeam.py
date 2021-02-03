from typing import List

def countTeams(num: int, skills: List[int], minAssociates: int, minLevel: int, maxLevel: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    qualified = []
    possible_teams = [[]]
    
    for a in skills:
        if minLevel <= a <= maxLevel:
            qualified.append(a)

    num_teams = 0
    while qualified:
        person = qualified.pop()
        new_teams = []
        for team in possible_teams:
            new_team = [person] + team
            if len(new_team) >= minAssociates:
                num_teams += 1
            new_teams.append(new_team)
        possible_teams += new_teams

    return num_teams

'''

Brute force, recursion method. This goes through the entire list to count the
number of valid combinations. 
Time Complexity: O(n^n), where n is the size of the skills array. There are n
skills to go through.
Space complexity: O(n), max recursion stack size.
'''
              
if __name__ == "__main__":
      num = int(input())
      skills = [int(y) for y in input().split()]
      minAssociates = int(input())
      minLevel = int(input())
      maxLevel = int(input())
      result = countTeams(num, skills, minAssociates, minLevel, maxLevel)
      print(result)
   
