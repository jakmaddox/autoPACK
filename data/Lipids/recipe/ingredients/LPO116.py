#include as follow : execfile('pathto/LPO116.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
LPO116= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/LPO116.sph',
radii = [[4.4100000000000001, 1.1499999999999999, 1.55, 3.7200000000000002, 1.51, 4.2199999999999998, 2.8900000000000001, 4.1299999999999999]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/LPO116.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'LPO116',
positions = [[(0.90000000000000002, 3.0099999999999998, 6.2699999999999996), (1.3500000000000001, 3.9199999999999999, 21.260000000000002), (0.10000000000000001, 3.2200000000000002, 23.449999999999999), (-2.2799999999999998, -5.7000000000000002, 17.82), (2.0800000000000001, 5.9100000000000001, 20.91), (1.5800000000000001, 2.3500000000000001, 15.35), (-1.1799999999999999, -0.81999999999999995, 21.469999999999999), (-0.97999999999999998, -5.6600000000000001, 9.3800000000000008)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(LPO116)