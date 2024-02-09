def v_sphere(r):
    p = 3.14
    t = 4/3
    w = r * r * r
    v = p * t * w
    return v

r = float(input("Give me radius: "))   
print(v_sphere(r))