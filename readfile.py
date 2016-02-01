__author__ = 'Martin'

f = open("ppot.p.tex.aa.ppm", "rb")
a = f.read()
j = 0
for i in a:
    print(i, end=" ")
    j += 1
    if j == 256:
        j = 0
        print()

f.close()