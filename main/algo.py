# Function for the Method of least squares
# by Justinas Smertinas
# Edited by Ali Rassolie
# Edited again by Justinas Smertinas

#What to import from numpy.
from numpy import array, transpose, dot, linalg, power

#We want to find the best fitting polynomial of any order (that you choose)
#between a set of point in the XY plane.
#For this we employ a Method of Least Squares.
#The following function returns a list of coefficients for a polynomial
#of order chosen by the user.
#Exanple of the return [a, b, c, d] where a is coefficient of the largest
#degree term (in this case 3).

#This will give you whatever order polynomial you want, babe.
class Algo:
    def __init__(self):
        pass
        

    def leastSquares(self, x=None, y=None, order=1):
        #We note the length of the input list so that we do not have to compute it again
        lengthOfList = len(x)
        #We set up 3 list that later will be turned into numpy
        # A transposed

        At = []

        #We create A transposed list by appending list of X raised
        #to powers of descending order.
        for i in reversed(range(order+1)):
            At.append(power(x, i))
        #We turn At into a numpy array
        #And create its transversed version.
        At = array(At)
        A = At.transpose()

        #We solve a systen <At*A>=<At*Y>
        solutionArray = linalg.solve(dot(At, A), dot(At, y))
        #However we obtain solution in form of an Array and since I dislike it's format
        #I turn it into a simple list with the folowing for loop.
        solution = []
        for i in range(len(solutionArray)):
            solution.append(solutionArray[i])
        return solution


    #Returns a list of Y approximations from known X and Y for wanted x.
    #We need a list of known X and Y values to find polynomial approximations
    #and we also need a list of X values, for which we want approximated values.
    def leastSquaresApproximationResults(self, xKnown = None, xWanted = None, yKnown=None, order = 1):
        #We calculate the polynomial coefficients
        coefficients = self.leastSquares(xKnown, yKnown, order)
        #We reverse the list for later convenience when calculating approximated Y values
        coefficients.reverse()
        #We create a list that we will alter return
        yApproxList = []
        #We iterate through the list of wanted X Values
        for i in xWanted:
            #We calculate approximation of Y values for wanted X and append it to the list
            yApprox = 0
            for j in range(len(coefficients)):
                yApprox += coefficients[j]*(i**j)
            yApproxList.append(yApprox)
        #We return the list of approximated Y values
        return yApproxList


