import KratosMultiphysics as km
import KratosStructuralMechanicsApplication as sma
import KratosMultiphysics.LinearSolversApplication as esa
import numpy as np
import time

# Properties 
el = 1000
b = 100
h = 10
E = 210e3
nu = 0.3
rho = 7.9e-9
nElement = 50
nMode = 15

# Calculate cross-sectional parameters
A = h * b
Ix = b * h / 12 * ( h ** 2 + b ** 2) # Iy+Iz
Iy = b * h ** 3 / 12
Iz = b *h ** 3 / 12

# Initialize Kratos Model 
model = km.Model()
mp = model.CreateModelPart('Structure')

# Add solution variables
mp.AddNodalSolutionStepVariable(km.DISPLACEMENT)
mp.AddNodalSolutionStepVariable(km.REACTION)
mp.AddNodalSolutionStepVariable(km.REACTION_MOMENT)
mp.AddNodalSolutionStepVariable(km.ROTATION)

# Element property set - Geometric and material values
PropertySet = mp.CreateNewProperties(0)
PropertySet[sma.CROSS_AREA] = A
PropertySet[sma.TORSIONAL_INERTIA] = Ix
PropertySet[sma.I22] = Iy
PropertySet[sma.I33] = Iz
PropertySet[km.YOUNG_MODULUS] = E
PropertySet[km.DENSITY] = rho
PropertySet[km.POISSON_RATIO] = nu
PropertySet[km.COMPUTE_LUMPED_MASS_MATRIX] = False
PropertySet[km.CONSTITUTIVE_LAW] = sma.LinearElastic3DLaw()

# Create mesh
xNode = np.linspace(0, el, nElement + 1)
for i, xi in enumerate(xNode):
    mp.CreateNewNode(i + 1, xi, 0.0, 0.0)
elementType = 'CrLinearBeamElement3D2N'
for i in range(nElement):
    mp.CreateNewElement(elementType, i + 1, [ i + 1, i + 2], PropertySet)
    
# Add degrees of freedom and their reactions
km.VariableUtils().AddDof(km.DISPLACEMENT_X, km.REACTION_X, mp)
km.VariableUtils().AddDof(km.DISPLACEMENT_Y, km.REACTION_Y, mp)
km.VariableUtils().AddDof(km.DISPLACEMENT_Z, km.REACTION_Z, mp)
km.VariableUtils().AddDof(km.ROTATION_X, km.REACTION_MOMENT_X, mp)
km.VariableUtils().AddDof(km.ROTATION_Y, km.REACTION_MOMENT_Y, mp)
km.VariableUtils().AddDof(km.ROTATION_Z, km.REACTION_MOMENT_Z, mp)

# Boundary conditions
boundaryGroup = mp.CreateSubModelPart('BoundaryConditionsDirichelt')
boundaryGroup.AddNodes([1])
km.VariableUtils().ApplyFixity(km.DISPLACEMENT_X, True, boundaryGroup.Nodes)
km.VariableUtils().ApplyFixity(km.DISPLACEMENT_Y, True, boundaryGroup.Nodes)
km.VariableUtils().ApplyFixity(km.DISPLACEMENT_Z, True, boundaryGroup.Nodes)
km.VariableUtils().ApplyFixity(km.ROTATION_Z, True, boundaryGroup.Nodes)
km.VariableUtils().ApplyFixity(km.ROTATION_X, True, boundaryGroup.Nodes)
km.VariableUtils().ApplyFixity(km.ROTATION_Y, True, boundaryGroup.Nodes)

# Solver settings
settings = km.Parameters(
        """{
            "max_iteration":        5000,
            "tolerance":            1e-6,
            "number_of_eigenvalues": """
        + str(nMode)
        + """,
            "echo_level":             0,
            "normalize_eigenvectors":true
        }""")
    
Solver = esa.EigensystemSolver(settings)
BuilderSolver = km.ResidualBasedBlockBuilderAndSolver(Solver)
Scheme =sma.EigensolverDynamicScheme()
ModalDecomposition = False
MassMatrixDiagonalValue = 1.0
StiffnessMatrixDiagonalValue = -1.0
echo = 0
Strategy = sma.EigensolverStrategy(
        mp,
        Scheme,
        BuilderSolver,
        MassMatrixDiagonalValue,
        StiffnessMatrixDiagonalValue ,
        ModalDecomposition,
        )
Strategy.SetEchoLevel(echo)

# Solve 
Strategy.Solve()

# Extract values and print
eigenvalues = np.zeros(nMode)
for i in range(nMode):
    eigenvalues[i] = mp.ProcessInfo[sma.EIGENVALUE_VECTOR][i]
omegan = np.sqrt(eigenvalues) / 2 / np.pi
time.sleep(0.01)
print('-' * 25)
print('Natural frequencies:')
for i in omegan:
    print(round(i, 4))


