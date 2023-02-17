#KIRSTY ACHEAMPONG
6921721
"""
@author: KIRSTY 
#https://github.com/Kirsty2005
#Kirsty302005
"""
import numpy as np

L=12 #total length of beam in meters
W=10 #load intensity in kN/m
x=0
M=(W*(-6*x**2 + 6*L*x -L**2))/12
V=W*(L/2 - x)
#Shear force(V)and bending moment(M) at the fist end ,x=0
x=0
m='the bending moment at x=0 is'
n='the shear force at x=0 is'
print()
print('(a.1)' + m + str(M) + 'and', n + str(V))
#Bending moment(M) and shear force(V) at the first end,x=L=10
x=L
M=(W*(-6*x**2 + 6*L*x - L**2))/12
V=W*(L/2 - x)
a='The bending moment at x=L is'
b='the shear force at x=L is'
print()
print('(a.2)' + m + str(M) + 'and',n + str(V))

#Question b
"""
when the bending moment is zero, we get an expression x**2 - L*x + L**2/6 = 0
"""
#from the expression
a=1
b=-L
c=L**2/6
#using the Almighty formula,the two roots are;
discriminant= b**2 - 4*a*c
root_1b = (-b + np.sqrt(discriminant))/2*a
root_2b = (-b - np.sqrt(discriminant))/2*a
print()
print('(b)the points of contraflexure are {0} and {1}'.format(root_1b,root_2b))
   
#Question c
"""
when V is zero, x=L/2
"""
x=L/2
print()
print('(c) the point at which V=0 is{}'.format(x))

#Question d
i=0
j=0.01
k=L + j
x=np.arange(i,j,k)
M=(W*(-6*x**2 + 6*L*x - L**2))/12
print()
print('(d) using the initialized variable, the bending moment at each step in the array is {0}'.format(M))

#Question e
V=W*(L/2 - x)
print()
print('(e) the shear force for each step along the span is {}'.format(V))

#Question f
"""
Let the absolute value of the bending moment array be ABM
Also let the minimum ABM be m_ABM
"""
ABM= abs(M)
m_ABM= min(ABM)
"""
When the bending moment is m_ABM,we get an expression x**2 - L*x + (L**2/6) + (2*m_ABM)W=0
"""
#from the above expression
a=1
b=-L
c=(L**2/6) + (2*m_ABM)/W
#Using the Almighty formula the roots are;
discriminant=b**2 - 4*a*c
root_1f=(-b + np.sqrt(discriminant))/2*a
root_2f=(-b - np.sqrt(discriminant))/2*a
print()
print('(f) the points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(root_1f,root_2f))
  
#Question g
"""
Let the relative errors be q_r
"""
q_r1=((root_1b - root_1f)/root_1b*100) 
q_r2=((root_2f - root_2b)/root_2f*100) 
print()  
print('(g) the relative errors between estimated points of contraflexure are {0}% and {1}%'.format(q_r1,q_r2))

#Question h
"""
Let the maximum bending moment be max_M 
Let the minimum bending moment be min_M
"""
#for the maximum
max_M=max(M)
"""
When the bending moment is max_M,we get an expression x**2 - L*X + (L**2/6) + (2*max_M)/W=0
"""
a=1
b=-L
c=(L**2/6) + (2*max_M)/W
#Using the Almighty formula the roots are;
discriminant=b**2 - 4*a*c
root_1=(-b + np.sqrt(discriminant))/2*a
root_2=(-b - np.sqrt(discriminant))/2*a
print()
print('(h.1) the points at which the maximum bending moment occur are {0} and {1}'.format(root_1,root_2))

#for the minimum
min_M=min(M)
"""
When the bending moment is min_M,we get an expression x**2 - L*x + (L**2//6) + (2*min_M)/W=0
"""
a=1
b=-L
c=(L**2//6) + (2*min_M)/W
#Using the Almighty formula the two roots are;
discriminant=b**2 - 4*a*c
root_1=(-b - np.sqrt(discriminant))/2*a
root_2=(-b + np.sqrt(discriminant))/2*a
print()
print('(h.2) the points at which the minimum bending moment occur are {0} and {1}'.format(root_1,root_2))
      
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                            
     
    