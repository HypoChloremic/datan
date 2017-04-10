# Function for the Method of least squares
# by Justinas Smertinas
# Edited by Ali Rassolie

#What to import from numpy.
from numpy import array
from numpy import transpose
from numpy import dot
from numpy import linalg
from numpy import power

#We want to find the best fitting polynomial of any order (that you choose)
#between a set of point in the XY plane.
#For this we employ a Method of Least Squares.
#The following function returns a list of coefficients for a polynomial of
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
        list_of_XY_coordinates = [[x[i],y[i]] for i in range(0, len(x))]
        #We set up 3 list that later will be turned into numpy
        # A transposed
        # X values
        # Y values
        At = []
        X = []
        Y = []

        #From the list of coordinates we split Xs and Ys into their respective lists.
        #Do note that while X is just a list, Y is a list of lists
        #as we later want it to be a colmn vector.
        for i in range(lengthOfList):
            X.append(list_of_XY_coordinates[i][0])
            Y.append([list_of_XY_coordinates[i][1]])

        #We create A transposed list by appending list of X raised
        #to powers of descending order.
        for i in reversed(range(order+1)):
            At.append(power(X, i))
        #We turn At into a numpy array
        #And create its transversed version.
        At = array(At)
        A = At.transpose()

        #We solve a systen <At*A>=<At*Y>
        solutionArray = linalg.solve(dot(At, A), dot(At, Y))
        #However we obtain solution in form of an Array and since I dislike it's format
        #I turn it into a simple list with the folowing for loop.
        solution = []
        for i in range(len(solutionArray)):
            solution.append(solutionArray[i][0])
        return solution