# Integration_Calculator
Program that will perform numerical integration using Gaussian Quadrature

The Program can handle polynomial, Trigonometric Functions, Eulers number and Logarithmic Functions for Integration. As the Weights and Zeroes of Legendre Polynomials were allowed to be taken at the beginning of the Program, they were calculated using a library function; however, the manual method of calculating the weights is attached as comments at the end of the code, which is not used as it's not entirely accurate and adds to the errors.

The Program can take limits of similar functions and constants such as e, pi and Infinity.

Kindly use the following input formats:
1. First input for order of Gaussian Quadrature is taken as an integer
2. The Lower and Upper Limits are taken in separate inputs, respectively.
3. Enter the following keywords in limits for the corresponding function FOR e -> e, Inifinity -> inf , PI-> pi
4. Enter the Function to be Integrated into the form of variable x as the Program doesn't support any other variables
5. Enter any trigonometric or transcendental function with x in brackets. [ e.g sin(x),cos(x),sin(x)**2 ]
6. Use * for Multiplication and ** for the power of a function. Missing any * or using ^ will result in an error. e.g [x**3 +3*x**2 + 1]
7. The following python modules have been used sympy, NumPy, math and re.
Please use the above input formats.
