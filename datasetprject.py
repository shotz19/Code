#On my honor, I have neither given nor recieved unauthorized aid. 
#Stephanie Hotz 1-18-19
#Here I made three different presentations of precipitation per year in inches by state. I chose o do this because I live somwhere with very little rain and so it interests me how much rain other places get.
import matplotlib.pyplot as plt
#rainfall per state per year in inches
#https://www.currentresults.com/Weather/US/average-annual-state-precipitation.php
rainfall = [58.3,22.5,13.6,50.6,22.2,15.9,50.3,45.7,54.5,50.7,63.7,18.9,39.2,41.7,34.0,28.9,48.9,60.1,42.2,44.5,47.7,32.8,27.3,59.0,42.2,15.3,23.6,9.5,43.4,47.1,14.6,41.8,50.3,17.8,39.1,36.5,27.4,42.9,47.9,49.8,20.1,54.2,28.9,12.2,42.7,44.3,38.4,45.2,32.6,12.9]
#list of states
state = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
  #list of state abbreviations
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA","HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]




#simple bar chart
plt.bar(states,rainfall,color=(.5,.0,.5,1.0))

plt.xlabel("State")
plt.ylabel("Rain")

plt.show()




#3D histogram
#This imports the 3D bars
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()

#This sets up the bar
bar = fig.add_subplot(111, projection='3d')
#This loops through all of the states
for i in range (len(rainfall)):
	#This functionadds a 3d bar
	bar.bar3d(i, i, 0, 1, 1, rainfall[i], color='b', zsort='average')
plt.show()




# scatter plot
x = rainfall
y = state
# makes a scatter plot of the data using the marker 'o'
plt.scatter(x, y, 3, marker='o')

plt.xlabel("State")
plt.ylabel("Rain")

plt.show()