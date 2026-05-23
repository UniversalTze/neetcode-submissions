class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # assume O(N * Log N) time and O(N) space
        # formula: time = distance / speed

        # anytime when working with a positional list (position matters)
        # then always best to sort it
        POSITION = 0
        SPEED = 1
        carMovement = zip(position, speed)
        # created a tuple so that speed and position is not lost. 
        sortedCars = sorted(carMovement, key=lambda x: x[0], reverse = True)
        # car fleet can only be formed by cars ahead of it. Doing it in ascending order
        # makes it ambiguous in determining the final speed
        # an example 
        # pos: [1, 2, 3] speed [5, 4, 1] target = 8
        # after the first iteration, all cars are moving at 1 as they cannot overtake 3
        # (car can not pass another car ahead of it)
        carfleetStack = []

        # bucket sort or hash set
        # use equation to determine timesteps to destination: (target - position) / speed
        for index in range(len(sortedCars)):
            hopsToTarget = (target - sortedCars[index][POSITION]) / sortedCars[index][SPEED]
            if len(carfleetStack) == 0: 
                # holds time needed to reach target
                carfleetStack.append(hopsToTarget)
            elif hopsToTarget <= carfleetStack[-1]:
                # nothing needs to be done here
                # as car can only move as fast as the car in front of it
                continue
            else: 
                # car will reach there at a later time stamp, which becomes the 
                # new car fleet
                carfleetStack.append(hopsToTarget)

        # stack is used to represent different time points it takes vehicles to get there
        return len(carfleetStack)

        