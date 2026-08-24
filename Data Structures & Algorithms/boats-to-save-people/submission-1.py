class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sortedWeights = sorted(people)
        # weights are now in ascending order
        l = len(people) - 1
        r = 0
        numboats = 0

        while r < l:
            if sortedWeights[l] == limit or (sortedWeights[l] + sortedWeights[r] > limit):
                # loop until l is below limit in that it can add weights
                l -= 1
                numboats += 1
                continue
            if (sortedWeights[l] + sortedWeights[r] == limit):
                l -= 1
                r += 1
                numboats += 1
                continue
            val = sortedWeights[l] + sortedWeights[r]
            while val < limit:
                r += 1
                val += sortedWeights[r]
            if val > limit:
                r -= 1
            else:
                r += 1
            l -= 1
            numboats += 1
        if r == l:
            numboats += 1
            # wasn't accounted for

        return numboats

                


        