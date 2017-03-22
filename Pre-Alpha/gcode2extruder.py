#//////////////////////////////////////
#Gcode Extruder Value Extract System
#/////////////////////////////////////
def main(filename):
    infile = open(filename)
    content = infile.read()
    infile.close()
    lines = content.split("\n")
    currentZ = 0
    currentE = "E0"
    points = []
    for line in lines:
        if ";" not in line:
            #This line is not a comment line
            if "Z" in line:
                currentZ = GetZ(line)
        if "X" in line and "Y" in line:
            #This is a coordinate define line
            x = GetX(line)
            y = GetY(line)
            if "E" not in line:
                points.append(str(x) + ' ' + str(y) + ' ' + str(currentZ) + ' ' + str(currentE))
            else:
                points.append(str(x) + ' ' + str(y) + ' ' + str(currentZ) + ' ' + str(GetE(line)))
                currentE = GetE(line)
            #print('(' + str(x) + ',' + str(y) + ',' + str(currentZ) + '):' + str(GetE(line)))
    Exportfile(points)
    
def Exportfile(array):
    extfile = open("extruderdata.ims","w")
    for item in array:
        extfile.write(item + "\n")
    extfile.close()
    print("[info] Extruderdata Exported")
    
def GetE(line):
    line = line.split()
    for item in line:
        if "E" in item:
            return item
    return "E0" #Usually the start of the gcode

def GetX(line):
    line = line.split()
    for item in line:
        if "X" in item:
            return float(item.replace("X",""))
def GetY(line):
    line = line.split()
    for item in line:
        if "Y" in item:
            return float(item.replace("Y",""))
def GetZ(line):
    line = line.split()
    for item in line:
        if "Z" in item:
            return float(item.replace("Z",""))

main("teapot.gcode")
