class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # assume O(N * Log N) time and O(N) space
        POSITION = 0
        SPEED = 1
        carMovement = zip(position, speed)
        # Sort by the second element (index 1) of each tuple
        sortedCars = sorted(carMovement, key=lambda x: x[0], reverse = True)
        print(sortedCars)
        # car fleet can only be formed by cars ahead of it. Doing it in ascending order
        # makes it ambiguous in determining the final speed. 
        # an example 
        # pos: [1, 2, 3] speed [5, 4, 1] target = 8
        # after the first iteration, all cars are moving at 1 as  
        curCarfleet = set()
        carfleetStack = []

        # bucket sort or hash set
        # use equation to determine timesteps to destination: (target - position) / speed
        for index in range(len(sortedCars)):
            hopsToTarget = (target - sortedCars[index][POSITION]) / sortedCars[index][SPEED]
            if len(carfleetStack) == 0: 
                # holds time needed to reach target
                carfleetStack.append(hopsToTarget)
            elif hopsToTarget <= carfleetStack[-1]:
                continue
            else: 
                carfleetStack.append(hopsToTarget)
        return len(carfleetStack)

        