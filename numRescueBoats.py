"""
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        i, j = 0, len(people) - 1
        numVisits = 0
        while i <= j:
            numVisits += 1
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1

        return numVisits
