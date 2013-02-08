#include as follow : execfile('pathto/POP60.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP60= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP60.sph',
radii = [[2.54, 1.5800000000000001, 4.9699999999999998, 2.5, 1.8600000000000001, 5.0899999999999999, 2.8199999999999998, 1.99]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP60.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP60',
positions = [[(-1.4099999999999999, -2.4900000000000002, 4.4699999999999998), (0.83999999999999997, -1.0900000000000001, 22.440000000000001), (1.6799999999999999, 2.2599999999999998, 12.789999999999999), (-1.47, -3.3100000000000001, 10.619999999999999), (-2.3999999999999999, -0.46999999999999997, -0.070000000000000007), (2.29, 4.1200000000000001, 2.7200000000000002), (-1.6100000000000001, -2.4900000000000002, 16.18), (-1.72, -1.1200000000000001, 20.399999999999999)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP60)