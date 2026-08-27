class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position: list of positions towards a target point
        # as order matters when determining speed, need to sort it a certain way
        # The order is a car behind cannot overtake a car infront, therefore, sorting it
        # in a descending manner will make it clear how fast cars can go if moving faster than the cars in front of it 
        POSITION = 0
        SPEED = 1
        carPosSpeed = zip(position, speed)
        sortedCarRoad = sorted(carPosSpeed, reverse=True)

        carFleet = []
        
        # now we recognise, we have speed and position and a target spot. Can calculate distance required 
        # to reach target and then calculate how many iterations (time) it will take to reach the target
        # time = distance / speed. Distance = target - position
        
        # if time taken is less than or equal to the car infront, that it forms a carfleet as car behind cannot
        # overtake but only travel at the same speed as the car/s infront.

        # stack is used to keep track of the current car's time to get there. Only push onto the stack when time 
        # taken is more than what's currently on the stack as that indicates a potential new fleet. 
        # (ones currently on the stack that is less will reach target before this new fleet gets there)
        # that is why you push

        for car in sortedCarRoad:
            position = car[POSITION]
            timeToTarget = (target - position)/car[SPEED]
            if len(carFleet) == 0: 
                # push the car closest to target first, as if other cars move quicker than this and 
                # catch up, it can only drive as fast as this
                carFleet.append(timeToTarget)
            elif timeToTarget <= carFleet[-1]:
                # if car takes less time/equal time to get to target, it can only move as fast as the one infront
                # therefore just continue
                continue
            else: 
                # else a new fleet can be formed using this new car's speed as this
                # car never catches the one in front and so on...
                carFleet.append(timeToTarget)
        return len(carFleet) # length of stacks indicate how many car fleets it takes to reach target. 

        