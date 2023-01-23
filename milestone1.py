def readInputs(filename):
    polygons = []
    file = open(filename, "r")

    all = file.read().split('boundary')

    header = all.pop(0)
    # print(header)

    last = all.pop(-1)

    footer = last.split('endstr')[-1]
    footer = 'endstr'+footer
    # print(footer)

    last = last.split('endstr')[0]
    # print(last)
    all.append(last)

    for i in all:
        temp = i.split('\n')
        layer = temp.pop(1)
        temp = temp[-3]
        temp = temp.split('  ')
        temp.pop(0)
        pn = int(temp.pop(0))
        xy = {}
        for i in range(pn):
            xy[i] = []
            xy[i].append(int(temp[i].split(' ')[0]))
            xy[i].append(int(temp[i].split(' ')[1]))
        d1 = {'layer': layer, 'n': pn, 'xy': xy}
        polygons.append(d1)
    return header, polygons, footer


def writeOutput(header, polygons, footer):
    file = open('output1.txt', 'w')
    file.write(header)
    for i in polygons:
        temp = 'boundary\n'+i['layer']+'\ndatatype 0\nxy  '+str(i['n'])
        for j in range(len(i['xy'])):
            temp += '  '+str(i['xy'][j][0])+' '+str(i['xy'][j][1])
        temp += '\nendel\n'
        file.write(temp)
    file.write(footer)


def selectFirst2(polygons):
    newpoly = []
    for i in range(len(polygons)):
        if i < 2:
            newpoly.append(polygons[i])

    return newpoly


header, polygons, footer = readInputs("Format_Source.txt")
polygons = selectFirst2(polygons)
writeOutput(header, polygons, footer)
