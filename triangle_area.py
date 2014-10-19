import math

def add2(u, v):
    return (u[0] + v[0], u[1] + v[1])

def scale2(u, a):
    return (a*u[0], a*u[1])

def sub2(u, v):
    return (u[0] - v[0], u[1] - v[1])

def dot2(u, v):
    return u[0] * v[0] + u[1] * v[1]

def norm_sq2(u):
    return u[0]**2 + u[1]**2

def area2(a, b, c):
    """ 
    Calculate the area of the triangle with vertices a, b, c
    
    let z = b - a

    Then we want to find some point p such that p = a + kz for some 
    scalar k, such that z and (p - c) perpendicular.

    the above is enough information to find k. we need:

        z (dot) (p - c) = 0

    equivalently,
        
        z (dot) (a + kz - c) = 0

    or

    k |z|^2 = z (dot) (c - a)

    Once we have k we know p, and the base is the magnitude of z and 
    the height is the magnitude of (p - c)
    """
    z = sub2(b, a)

    c_min_a = sub2(c, a)

    normsq_z = norm_sq2(z)
    k = dot2(z, c_min_a) / normsq_z

    p = add2(a, scale2(z, k))

    return 0.5 * math.sqrt(normsq_z) * math.sqrt(norm_sq2(sub2(p, c)))

def orient2(a, b, c):
    """One way to check the orientation of an ordered triangle is to let
    z = b - a
    w = z rotated 90 degrees counterclockwise

    then check whether (c - b) (dot) w is positive or negative

    no idea if there's a better way"""
    z = sub2(b, a)
    w = (-z[1], z[0])
    return 1 if dot2(w, sub2(c, b)) > 0 else -1

a = (1, 1)
b = (3, 5)
c = (4, 2)
print(orient2(a, b, c) * area2(a, b, c))

a = (1, 2)
b = (5, -1)
c = (2, 1)
print(orient2(a, b, c) * area2(a, b, c))

a = (2, 1)
b = (-1, 3)
c = (1, 4)
print(orient2(a, b, c) * area2(a, b, c))
