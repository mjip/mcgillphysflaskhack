# Equipotential Field Simulator

![screenshot](https://i.imgur.com/DYYjIDT.png "In action")
![screenshot](https://i.imgur.com/dfVFVfU.png "After generation")

With this project, we are attempting to simulate equipotential fields of charged particles. You can specify a maximum of three
particles and their charges (in the range of [-10,10]) as well as their x, y coordinates in a 2D plane, with the origin (0,0) being
in the centre and (100,100) and (-100,-100) defining the top right and bottom left corners respectively. You can also generate a
random set of 5 particles and their charges and the graph associated with them. The fields are computed using Python, the plot is 
generated using matplotlib, the final product is displayed with Javascript and the backend runs on Flask. 
