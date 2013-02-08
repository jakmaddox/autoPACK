#include as follow : execfile('pathto/POP48.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP48= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP48.sph',
radii = [[3.5899999999999999, 2.79, 1.7, 2.0800000000000001, 3.54, 3.0099999999999998, 3.0099999999999998, 2.98]],
cutoff_boundary = 0,
Type = 'MultiSphere',
cutoff_surface = 0,
gradient = '',
jitterMax = [0.5, 0.5, 0.10000000000000001],
packingPriority = 0,
rotAxis = [0.0, 2.0, 1.0],
nbJitter = 5,
molarity = 1.0,
rotRange = 6.2831,
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP48.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP48',
positions = [[(2.48, 1.8, -5.4299999999999997), (0.16, -2.7599999999999998, -18.010000000000002), (-2.3700000000000001, 4.1299999999999999, -23.460000000000001), (-2.2000000000000002, 0.98999999999999999, -22.760000000000002), (-1.45, -4.9500000000000002, -4.3399999999999999), (3.5, 2.2599999999999998, -12.630000000000001), (-1.1200000000000001, -3.8999999999999999, -11.27), (0.68999999999999995, 2.9199999999999999, -18.620000000000001)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP48)