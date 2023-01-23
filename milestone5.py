import math


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
    file = open('output5.txt', 'w')
    file.write(header)
    for i in polygons:
        temp = 'boundary\n'+i['layer']+'\ndatatype 0\nxy  '+str(i['n'])
        for j in range(len(i['xy'])):
            temp += '  '+str(i['xy'][j][0])+' '+str(i['xy'][j][1])
        temp += '\nendel\n'
        file.write(temp)
    file.write(footer)


def polygonArea(poly):
    area = 0.0
    for i in range(0, poly['n']-1):
        area += (poly['xy'][i][0] + poly['xy'][i+1][0]) * \
            (poly['xy'][i][1] - poly['xy'][i+1][1])
    return float(abs(area / 2.0))


def findPoly(p1, p2):
    newpoly = []
    area = polygonArea(p1[0])
    # for i in p2:
    #     if p1[0]['n'] == i['n']:
    #         newpoly.append(i)
    #         s1 = math.dist(p1[0]['xy'][0], p1[0]['xy'][1])
    #         s2 = math.dist(i['xy'][0], i['xy'][1])
    #         try:
    #             mul = s1/s2
    #             a = polygonArea(i)
    #             if (a*mul*mul != area):
    #                 newpoly.pop()
    #                 continue
    #         except:
    #             newpoly.pop()
    #             continue
    #         j = 0
    #         for j in range(len(p1[0]['xy'])-1):
    #             s1 = math.dist(p1[0]['xy'][j], p1[0]['xy'][j+1])
    #             s2 = math.dist(i['xy'][j], i['xy'][j+1])
    #             try:
    #                 m = s1/s2
    #             except:
    #                 newpoly.pop()
    #                 break
    #             if m != mul:
    #                 newpoly.pop()
    #                 break
    for i in p2:
        a = polygonArea(i)
        if a == area:
            newpoly.append(i)

    return newpoly


headerpoi, p1, footerpoi = readInputs('POI.txt')
headerS, p2, footerS = readInputs('Source.txt')

polygons = findPoly(p1, p2)
writeOutput(headerS, polygons, footerS)
