"""Assignment 4.

Calculates the number of hours & minutes & seconds needed for
traveling for a given distance (km) at a given velocity (km/h).

"""

distance = 500  # the amount to be travelled
velocity = 110  # the velocity of the car
timeHours = distance / velocity
timeMinutes = (timeHours * 60) % 60
timeSeconds = (timeMinutes * 60) % 60

if distance <= 0:
    print('That is not a valid distance. Distance must be greater than 0.')

if velocity <= 0:
    print('That is not a valid velocity. Velocity must be greater than 0.')

if timeHours >= 1:
    print(f'The amount of time required to travel {distance} kilometers at \
{velocity} km/h is {int(timeHours)} hours {int(timeMinutes)} minutes \
{int(timeSeconds)} seconds.')

else:
    print(f'The amount of time required to travel {distance} kilometers at \
{velocity} km/h is {int(timeMinutes)} minutes {int(timeSeconds)} seconds.')
