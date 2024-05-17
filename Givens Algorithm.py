import numpy as np 
import math

def rotate(A, col, row, angle):#Create the rotaion matrix
    e = np.identity(len(A))
    e[col][col] = math.cos(angle)
    e[row][row] = math.cos(angle)
    e[col][row] = math.sin(angle)
    e[row][col] = -math.sin(angle)
    return e, e.transpose()

def givens(Matrix,threshold):# returns the similar tridiagonal matrix
    similar = Matrix.copy()
    counter=0
    while True:
        condition = 0 #Stop condition
        #checking one of the points which must convert to zero
        for i in range(len(similar)):
            for j in range(i+2, len(similar)):
                if not(abs(similar[i][j]) <= threshold):
                    point = (j, i)
                    condition = 1
                    break
        # If there are no points for making to the zero , quit the While.
        if condition == 0:
            break

        col, row = point
        q = row + 1
        val_pr = similar[col][row]
        val_qr = similar[q][row]
        #calculating the angle
        theta = math.atan(val_pr / val_qr)
        #calcualting the rotaion matrix and its transposed form
        e, e_tr = rotate(similar, col, q, theta)
        #calculating the similar matrix which is zero in the given point indices
        similar = np.dot(np.dot(e_tr, similar), e)
        counter+=1
    return similar,counter

# Example of the book
m1=[[4,4,2],[4,4,1],[2,1,8]]

# the 21th practice of the book 
m2=[
    [2, 1, 0, 1],
    [1, 3, 2, 0],
    [0, 2, 5, 4],
    [1, 0, 4, 1]
]
matrix=np.array(m2)
similar,iteraion=givens(matrix,0.005)
#filtering the similar matrix by threshold to enhance visual clarity
for i in range(len(similar)):
    for j in range(i+2, len(similar)):
        if similar[i][j] <= 0.005:
            similar[i][j]=0
            similar[j][i]=0

print("--------------------The similar tridiagonal matrix is :-------------------- \n",similar)
print("\n-----------The number of iteration : ",iteraion)