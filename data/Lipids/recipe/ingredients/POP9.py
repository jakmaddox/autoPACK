#include as follow : execfile('pathto/POP9.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP9= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP9.sph',
radii = [[3.8399999999999999, 3.1899999999999999, 2.4399999999999999, 3.1600000000000001, 3.3300000000000001, 1.5900000000000001, 1.99, 2.2000000000000002]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP9.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP9',
positions = [[(-0.59999999999999998, 4.0300000000000002, -10.359999999999999), (2.0499999999999998, -1.22, -12.43), (1.8999999999999999, 0.45000000000000001, -18.989999999999998), (-3.5600000000000001, 4.5700000000000003, -17.699999999999999), (1.03, -4.4299999999999997, -5.9900000000000002), (1.23, -4.4100000000000001, -21.600000000000001), (0.54000000000000004, -1.6100000000000001, -23.43), (-2.5800000000000001, 1.8100000000000001, -21.84)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP9)