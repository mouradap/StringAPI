import sys
from extractingDEGenes import extractGenes
from mappingGenes import mapping
from functionalEnrichment import funcEnrich
from gettingNetwork import createNet

def createReport(csvFile, fileName):
    extractGenes(csvFile, fileName)
    mapping(fileName)
    funcEnrich(fileName)
    createNet(fileName)

    print('Report of %s created successfully.' % csvFile)


if __name__ == '__main__':
    csvFile = sys.argv[1]
    fileName = sys.argv[2]
    createReport(csvFile, fileName)