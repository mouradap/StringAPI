import pandas as pd

def extractGenes(csvFile, fileName):
    deGenes = pd.read_csv(csvFile, header=None)
    with open("%s deGenesList.txt" % fileName, "w") as f:
        for gene in deGenes[0]:
            f.write('%s\n' % gene)