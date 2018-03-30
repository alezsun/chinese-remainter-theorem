
# coding: utf-8

# In[202]:


def check_relative_prime(x, y):
    if(x < y):
        x, y = y, x
    
    z = x % y
    if(z != 0):
        print(x, " % ", y, " = ", z)
        return check_relative_prime(y, z)
    else:
        print(x, " % ", y, " = ", z)
        return (True if y==1 else False)
    
            
def list_equations(x, y, b1, b2, b1r1 = 1, b2r1 = 0, b1r2 = 0, b2r2 = 1):
    if(b1 < b2):
        b1, b2 = b2, b1
        x, y = y, x
    
    r = x % y
    times = x // y
    
    b1r1 = b1r1 - times * b1r2
    b2r1 = b2r1 - times * b2r2

    if(r != 0):
        print(r, " = ", b1r1, " * ", b1, " + ", b2r1, " * ", b2)
        return list_equations(y, r, b1, b2, b1r2, b2r2, b1r1, b2r1)
    else:
        return b1r2, b2r2
        
# x(mod n), y(mod m)
def find_mod(x, n, y, m):
    if(x == 0 or n == 0 or y == 0 or m == 0):
        print("invalid input")
        return 0,0
    elif(check_relative_prime(n, m)):
        if(n < m):
            x, y = y, x
            n, m = m, n
        
        x_base, y_base = list_equations(n, m, n, m)
        target = y - x
        
        final = n * target * x_base + x
        final = final if final > 0 else (final + n * m)
        while(final > n*m):
            final -= n*m
        
        print(final, "(mod", n * m, ")", sep='')
        return final, n*m
    else:
        print("invalid input")
        return 0,0


# In[206]:


a = 15
b = 4
check = check_relative_prime(a, b)
print()
if(check):
    x, y = list_equations(a, b, a, b)
    print(x, y)


# In[204]:


'''
example to show:
x ≡ 1(mod 5)
x ≡ 2(mod 7)
x ≡ 3(mod 9)
x ≡ 4(mod 11)
'''

n1, n2 = find_mod(1, 5, 2, 7)
print()
n1, n2 = find_mod(n1, n2, 3, 9)
print()
n1, n2 = find_mod(n1, n2, 4, 11)

