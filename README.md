# Photophoretic force python module

This repository is the implementation of the asymmetryfactor module that calculates the behavior of the photophoretic force for a given particle and an optical beam that was the result of the master's thesis titled Algorithm in Python for calculating photophoretic forces by optical beams in on-axis configuration. The text is available for reading [here](https://).

Currently the force calculation implemented in this module is assuming a particle with the following properties:

And the following bundles are already available for use:

## How to use

You can calculate the asymmetry factor by calling the j1 function and passing the particle object and the beam object as in the following example

If you want to generate a graph, just use a for passing through the value referring to the x axis as in the following example


## How to contribute

You can create a pull request with changes if you wish to make them public, but if it is personal changes aimed at your research you can change the code as follows

The function that calculates the asymmetry factor uses two input parameters, a particle and a beam. Both are defined and modifiable classes.

If you need to use a beam other than those available, you can create a subclass of class X and implement the necessary functions to calculate the gn of that beam.

NOTE: If using the Frozen Wave beam, the total time calculated on a personal computer with the following characteristics took approximately 5 to 7 hours using 300 points.
This time can be drastically reduced if you have already calculated the gn of your beam or just reduced the complex integration into a defined equation, if you do this the total time for generating the graph can be reduced to minutes.


## Installation
To use the module correctly, download the repository and then run

$ pip install -r requirements.txt

The packages used will be installed and the code will be ready to be used. If you want to make sure everything went well, you can run the implemented tests by running the following command:

$ pytest


## Support
If you have any questions or suggestions for improvements, you can open an issue in the repository.


## License
For open source projects, say how it is licensed.

## Project status
This project is currently completed as the objective of the master's degree has been achieved. But it could enter development again with the next steps of research, which would be:
