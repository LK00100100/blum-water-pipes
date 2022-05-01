# blum-water-pipes

Given an array of PipeData, this program will calculate what sections will drain.

Check out the unit tests for more information.

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

## Notes

This will add more PipeData points as necessary. What causes another point to be added is related to a higher point.

The code is written without too many optimizations since this will need to be ported to VBA
:(

Input size should be around 100 points.
