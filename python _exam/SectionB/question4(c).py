#Importing required modules
import math

def valueOfD():
    
    X1 = int(input('Enter the value of X1:\t')) # int() 
    X2 = int(input('Enter the value of X2:\t'))
    Y1 = float(input('Enter the value of Y1:\t')) #float()
    Y2 = float(input('Enter the value of Y2:\t')) 

    ExpressionToGetD = (X1-X2) + (Y1-Y2)
    d = math.sqrt(ExpressionToGetD)
    #return d
    print("The value of d is: %.2f " %d + " ")
   
#calling the function  
valueOfD()


