import numpy as np

np.set_printoptions(precision=3, suppress=True)
# sigmoid function
def nonlin(x, deriv=False):
    if (deriv==True):
        return x * (1-x)
    return 1/(1+np.exp(-x))

# input dataset
X = np.array([[1, 0, 1], 
              [0, 1, 1],
              [1, 0, 0],
              [1, 1, 1], 
              [1, 1, 0]])

# output dataset
y = np.array([[0, 1, 0, 1, 0]]).T

#
#
np.random.seed(2)

#
syn0 = 2*np.random.random((3, 5)) - 1
syn1 = 2*np.random.random((5, 1)) - 1

for iter in range(2):
    
    # forward
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    print(l1)
    l2 = nonlin(np.dot(l1, syn1))
    print(l2)
    
    #
    l2_error = y - l2
    
    
    if (iter % 10000) == 0:
        print("Error: " + str(np.mean(np.abs(l2_error))))
    #
    #
    l2_delta = l2_error*nonlin(l2, deriv=True)
    
    l1_error = l2_delta.dot(syn1.T)
    
    l1_delta = l1_error * nonlin(l1, deriv=True)
    
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

# print(l2)

tests = np.array([[1, 0, 1],
                  [1, 1, 1],
                  [1, 0, 0],
                  [1, 1, 0],
                  [0, 0, 1],
                  [0, 1, 1],
                  [0, 0, 0],
                  [0, 1, 0]])
print(tests)
print(nonlin(np.dot(nonlin(np.dot(tests, syn0)), syn1)))