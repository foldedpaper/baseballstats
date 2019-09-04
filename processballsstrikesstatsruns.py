#!/usr/bin/python3
import sys, re

lineRe = re.compile(r'^\((\d), \((\d), (\d), (\d)\), \((\d), (\d)\)\): \[(.*)\]\s*$')
def main(fileName):
    f = open(fileName, 'r')
    print('<situations>')
    for line in f.readlines():
        lineMatch = lineRe.match(line)
        if lineMatch:
            # Starting at one to make compliant with other file
            baseSum = 1
            if (lineMatch.group(2) == '1'):
                baseSum = baseSum + 1
            if (lineMatch.group(3) == '1'):
                baseSum = baseSum + 2
            if (lineMatch.group(4) == '1'):
                baseSum = baseSum + 4
            stringToPrint = "<situation outs=\"%s\" runners=\"%d\" balls=\"%s\" strikes=\"%s\">" % (lineMatch.group(1), baseSum, lineMatch.group(5), lineMatch.group(6))
            runsList = lineMatch.group(7).split(', ')
            runsList = [int(x) for x in runsList]
            totalRuns = sum(runsList)
            stringToPrint += "<total>%d</total>" % totalRuns
            curRuns = 0
            for numInstances in runsList:
                stringToPrint += '<count runs="%d">%d</count>' % (curRuns, numInstances)
                curRuns = curRuns + 1
            stringToPrint += '</situation>'
            #stringToPrint = stringToPrint + "%s,%s,%s,%s,%s,%s" % (lineMatch.group(1), lineMatch.group(3), baseSum, lineMatch.group(7), lineMatch.group(9), lineMatch.group(8))
            print(stringToPrint)
        else:
            print("ERROR - couldn't parse line %s" %line)
    print('</situations>')
    f.close()

if (__name__ == '__main__'):
    main(sys.argv[1])
