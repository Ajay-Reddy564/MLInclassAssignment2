import numpy as np

#creating a random vector of size 15 with integers in the range 1-20 as given in the question
x = np.random.randint(1,20,15)
print("Original array:")
print(x)

#Here we are Reshaping the array using a method called reshape
y = x.reshape(3, 5)
print("Reshaped array:")
print(y)

#printing the Shape of an array
print('Shape of the array:',y.shape)

#replacing the max in each row with 0
for i in y:
    i[i == max(i)] = 0
    
print("Replacing the max in each row with Zero")
print(y)
   
   
   

       
   


