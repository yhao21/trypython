from haversine import inverse_haversine, Direction
from math import pi
paris = (48.8567, 2.3508) # (lat, lon)
# Finding 32 km west of Paris
new_point = inverse_haversine(paris, 32, Direction.WEST)
print(new_point)

## returns tuple (49.1444, 2.3508)
## Finding 32 km southwest of Paris
#inverse_haversine(paris, 32, pi * 1.25)
## returns tuple (48.5377, 1.8705)
## Finding 50 miles north of Paris
#inverse_haversine(paris, 50, Direction.NORTH, unit=Unit.MILES)
## returns tuple (49.5803, 2.3508)
## Finding 10 nautical miles south of Paris
#inverse_haversine(paris, 10, Direction.SOUTH, unit=Unit.NAUTICAL_MILES)
## returns tuple (48.6901, 2.3508)
