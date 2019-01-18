# What is the longest walk you can take and still be close enough to home to walk back at least 50% of the time
# The person returns home at least 50 % of the time if they walk 15 blocks from home.
import math
import sys
import random
n = int(sys.argv[1])
walks = int (sys.argv[2])
transport = 0
for i in range(walks):
	place = [0,0]
	for i in range (n):
		direction = random.randint(1,4)
		if direction == 1:
			place[0] = place[0] + 1
		if direction == 2:
			place[0] = place[0] - 1
		if direction == 3:
			place[1] = place[1] + 1
		if direction == 4:
			place[1] = place[1] - 1
	distance = abs(place[0]) + abs(place[1])
	if distance > 4:
		transport = transport + 1
percent = transport / walks
print(percent*100 , "%")
