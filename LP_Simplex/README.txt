How to Run:
    1. environment: python 3.7 with standard libraries
    2. how to run:
        In the directory named lp, run this command(without the brackets []):
            python lp.py [filename]
        The parameter filename means the name of the input file of the lp problem, and if no filename is given, the default value is 'input'
        Notice: please ensure the input file is in the directory named lp with the lp.py

The Solver Architecture:
    Use Simplex Method to solve the lp problem, and the main step is as below:
        1. Read the input file and store the object coefficient to a list and s.t. coefficient into a matrix
        2. Get initial basic variables (always take the slack variables as initial ones)
        3. Calculate the test number σ to find the leaving basic variable, if no σ value is larger than 0, get the
            solution, and if the basic variables are all slack variables, the lp problem is infeasible
        4. Calculate the gradient of the nonbasic variables θ to find the entering basic variable, if no θ is larger than 0, the lp problem is unbounded
        5. Swap the leaving basic variable and the entering basic variable, and reduce the s.t. coefficient matrix by Gaussian elimination method
        6. Loop the step 3-5 until find the solution of the lp (or end with unbounded or infeasible)

Extra Features:
    Linear Algebraic Simplex Method