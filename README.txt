The code provides the trajectories of the planets for 1 year and then switches the mass of the sun to the
mass of a black hole. The mass of the black hole can be edited under PARAMETERS. The variable for the mass
of the black hole is 'blackholemass'. The units are in AU.

The code will provide an array that shows the time at which the planets reach the closest point to the black hole. With
different masses for the black hole, the length of the trajectories may vary. Therefore, with each edit to the mass of the
black hole, change the time at which the trajectories are plotted until, starting from Venus. The default of 2000 solar
masses of a black hole has the following end times.

[1003.]
[1004.]
[1008.]
[1047.]
[1117.]
[1333.]
[1652.]

As you can see, those same numbers are in the code for plotting. If those numbers change when the code is ran, change them
in the plot code to have an accurate depiction of when the planets reach the black hole. If a smaller time step (dt)
is chosen, then you can change the point at which the planets reach the center. There may have to be more than one trial
required to find the "sweet spot" of the closest distance you can get to the center. The default value is 0.5, and it is
in the for loop that calculates the times for the 'stop' array.

The last piece of code provides the time it takes for each planet to reach the black hole. If a smaller time step is
chosen, convert the time step to hours (given that everything is in AU) and change the factor being multiplied to each
number. The default value is 9 for the time step of dt = 0.001.