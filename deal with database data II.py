__author__ = 'Martin'

fr = open("lion.txt", "r")
fw = open("sqllion.txt", "w")


try:
    while True:
        content = fr.readline()
        parts = content.split(',')
        if len(parts) < 3:
            break
        id = parts[0]
        coord = parts[1:len(parts)]
        coordstr = ",".join(coord)

        fw.writelines("INSERT INTO lion VALUES(\r\n")
        fw.writelines("\t\'" + str(id) + "\',\r\n")
        fw.writelines("\tSDO_GEOMETRY(\r\n")
        fw.writelines("\t\t2001,\r\n")
        fw.writelines("\t\tNULL,\r\n")
        fw.writelines("\t\tSDO_POINT_TYPE(" + coordstr[0:len(coordstr)-1] + ",NULL),\r\n")
        fw.writelines("\t\tNULL,\r\n")
        fw.writelines("\t\tNULL\r\n")
        fw.writelines("\t)\r\n")
        fw.writelines(");\r\n")
except EOFError:
    pass

fr.close()
fw.close()