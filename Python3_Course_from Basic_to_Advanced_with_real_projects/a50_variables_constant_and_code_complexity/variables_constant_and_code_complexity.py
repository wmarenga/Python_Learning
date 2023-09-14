"""
CONSTANT = "Variables" that will not change
Too many conditions in the same if (bad) <- Complexity count (bad)
"""
speed = 62  # current speed of the car
cars_place = 103  # location where the car is on the road

# !Constant always use upper letters.
RADAR_1 = 60  # maximum radar speed 1
LOCAL_1 = 100  # location where radar 1 is
RADAR_RANGE = 1  # The distance where the radar picks up

# We can use \ to break codes in Python.
car_passed_radar_1 = cars_place >= (LOCAL_1 - RADAR_RANGE) and \
    cars_place <= (LOCAL_1 + RADAR_RANGE)
car_fined = speed > RADAR_1
car_before_radar1 = cars_place < (LOCAL_1 - RADAR_RANGE)
car_after_radar1 = cars_place >= (LOCAL_1 + RADAR_RANGE)

if car_passed_radar_1 or car_after_radar1:
    print('Car passed on radar 1')
    if car_fined:
        print('Car fined by radar 1')
    else:
        print('Car passed below the speed limit on radar 1')
if car_before_radar1:
    print('The car has not yet passed radar 1.')
