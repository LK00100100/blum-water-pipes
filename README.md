# blum-water-pipes

Given an array of PipeData, this program will calculate what sections will drain.

Check out the unit tests for more information.

## Algorithm

This will sort the points by x. It will then look from left to right.
This will look at every point once. At a point, it will be able to
make a decision based off of past information. The past information that
is stored is a point that is not blocked by another point.

This will add more PipeData points as necessary. What causes another point to be added is related to a peak.

The code is written without too many optimizations since this will need to be ported to VBA.

Input size should be around 100 points.
