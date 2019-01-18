import matplotlib.pyplot as plt
rainfall = [58.3,22.5,13.6,50.6,22.2,15.9,50.3,45.7,54.5,50.7,63.7,18.9,39.2,41.7,34.0,28.9,48.9,60.1,42.2,44.5,47.7,32.8,27.3,59.0,42.2,15.3,23.6,9.5,43.4,47.1,14.6,41.8,50.3,17.8,39.1,36.5,27.4,42.9,47.9,49.8,20.1,54.2,28.9,12.2,42.7,44.3,38.4,45.2,32.6,12.9]
state = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA","HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#simple bar chart
plt.bar(states,rainfall,color=(.5,.0,.5,1.0))
plt.show()

#3D histogram
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range (len(rainfall)):
	ax.bar3d(i, i, 0, 1, 1, rainfall[i], color='b', zsort='average')
plt.show()