__author__ = 'Martin'

fr = open("region.txt", "r")
fw = open("sqlregion.txt", "w")


try:
    while True:
        content = fr.readline()
        parts = content.split(',')
        if len(parts) < 3:
            break
        id = parts[0]
        num = parts[1]
        coord = parts[2:len(parts)]
        coordstr = ",".join(coord)
        coordstr.rstrip("\n")

        fw.writelines("INSERT INTO region VALUES(\r\n")
        fw.writelines("\t\'" + str(id) + "\',\r\n")
        fw.writelines("\tSDO_GEOMETRY(\r\n")
        fw.writelines("\t\t2003,\r\n")
        fw.writelines("\t\tNULL,\r\n")
        fw.writelines("\t\tNULL,\r\n")
        fw.writelines("\t\tSDO_ELEM_INFO_ARRAY(1,1003,1),\r\n")
        fw.writelines("\t\tSDO_ORDINATE_ARRAY(" + coordstr[0:len(coordstr)-1] + ")\r\n")
        fw.writelines("\t)\r\n")
        fw.writelines(");\r\n")
except EOFError:
    pass

fr.close()
fw.close()