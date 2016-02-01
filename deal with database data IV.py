__author__ = 'Martin'

fr = open("ambulancearea.txt", "r")
fw = open("sqlambulancearea.txt", "w")


try:
    while True:
        content = fr.readline()
        parts = content.split(',')
        if len(parts) < 4:
            break
        id = parts[0]
        x = parts[1]
        y = parts[2]
        r = parts[3]
        coordstr = str(int(x)-int(r)) + "," + y + ", " + x + "," + str(int(y)+int(r)) + ", " + str(int(x)+int(r)) + "," + y

        fw.writelines("INSERT INTO ambulancearea VALUES(\r\n")
        fw.writelines("\t\'" + str(id) + "\',\r\n")
        fw.writelines("\tSDO_GEOMETRY(\r\n")
        fw.writelines("\t\t2003,\r\n")
        fw.writelines("\t\tNULL,\r\n")
        fw.writelines("\t\tNULL,\r\n")
        fw.writelines("\t\tSDO_ELEM_INFO_ARRAY(1,1003,4),\r\n")
        fw.writelines("\t\tSDO_ORDINATE_ARRAY(" + coordstr + ")\r\n")
        fw.writelines("\t)\r\n")
        fw.writelines(");\r\n")
except EOFError:
    pass

fr.close()
fw.close()