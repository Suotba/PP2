"""
m = 0.04
m2 = 0.06
ro = 0.035
g = 9.82
h = 0.3
t40 = 1.86
t60 = 0.996
tt40 = 1.878
tt60 = 0.906

k = (2*h )/(t40**2)
k2 = (2*h)/(t60**2) 
k3 = (2*h)/(tt40**2) 
k4 = (2*h)/(tt60**2) 
w = g - k 
w2 = g - k2 
w3 = g - k3
w4= g - k4 

#момент силы создано нити
M = m * ro * w
M2= m2 * ro * w2
M3 = m * ro * w3
M4 = m2 * ro * w4

#угловое ускорение платформы 
E = k / ro 
E2 = k2 / ro 
E3 = k3 / ro 
E4 = k4 / ro 

#Инерция
I = M/E
I2 = M2/E2
I3 = M3 / E3
I4 = M4 / E4

#Теоритическая инерция 
d = 1/6
q = 1/3
l = 0.02
R = 0.015
r1 = 0.08
r2 = 0.14
Ir  = (d * m * (l**2)) + (4*m*r1) + (m * R)
Ir2 = (d * m2 * (l**2)) + (4*m2*r1) + (m2 * R)
Ir3 = (d * m * (l**2)) + (4*m*r2) + (m * R)
Ir4 = (d * m2 * (l**2)) + (4*m2*r2) + (m2 * R)




print("Moment created by Tension:",M, M2, M3, M4)
print("Angle accelaration:",E, E2, E3, E4)
print("Inertia:",I,I2,I3,I4)
print("Theoretic Inertia: ",Ir,Ir2,Ir3,Ir4)
"""
"""
h = float(input("radious:"))

n = h / 1000

w = float(input("speed:"))

R = 0.2
# v = w if we need to find velocity
d = 6580
g = 2.4*(n/R)
f = g + 1

k =(n**2)/w
m = (2/9)*9.8*k*d

t = m


print(t)
"""
"""
#Remond num

v = float(input("Velocity:"))

r = float(input("Radius of ball:"))
u = r / 1000

j = float(input("Viscosity of liquid:"))

p = 1260

Re = 2 * v * u * p / j

print("Remond num:",Re)
"""