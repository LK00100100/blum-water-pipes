# blum-water-pipes

Given an array of PipeData, this program will calculate what sections will drain.

Check out the unit tests for more information.

note: finish todos and test more

## setup

```
conda create -n blum-water-pipes python=3.9
conda activate blum-water-pipes

# you should be in your conda environment
pip install matplotlib
```

Exact requirements used is in the requirements.txt. But you
really only need matplotlib.

```
# remember to activate conda
# to see what packages are used in your conda environment
pip list --format=freeze > requirements.txt

# to download all of the packages from a file
pip install -r requirements.txt
```

## algorithm

This will sort the points by x. It will then look from left to right.
This will look at every point once. At a point, it will be able to
make a can_drain decision based off of past information. The past information that
is stored is a point that is not blocked by another point. if a section of
pipe can drain, that "can drain" is carried upwards until it can't.

This will add more PipeData points as necessary. What causes another point to be added is related to a higher point

The code is written without too many optimizations since this will need to be ported to VBA.

Input size should be around 100 points.

I believe I can just go left/right from the drain. Try later
