import numpy as np

def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

X = np.array([[-2, -1],
              [25, 6],
              [17, 4],
              [-15, -6]])

Y = np.array([[1, 0, 0, 1]]).T

np.random.seed(1)

syn0 = 2 * np.random.random((2, 3)) - 1
syn1 = 2 * np.random.random((3, 1)) - 1

for iter in range(60000):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
        
    l2_error = Y - l2
    
    if (iter % 5000 == 0):
        print("Error: " + str(np.mean(np.abs(l2_error))))
    
    l2_delta = l2_error * nonlin(l2, deriv=True)
    
    l1_error = l2_delta.dot(syn1.T)
    
    l1_delta = l1_error * nonlin(l1, deriv=True)
    
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
    
print(syn1)
print(syn0)
print(l2)

emily = np.array([-7, -3]) # 128 pounds, 63 inches
l1 = nonlin(np.dot(emily, syn0))
l2 = nonlin(np.dot(l1, syn1))
print("Emily: " + str(l2))

frank = np.array([20, 2])  # 155 pounds, 68 inches
l1 = nonlin(np.dot(frank, syn0))
l2 = nonlin(np.dot(l1, syn1))
print("Frank: " + str(l2))
