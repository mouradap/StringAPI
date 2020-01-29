import requests

def mapping(fileName):
        

    #Getting DE Genes List
    deGenesList = []
    lista = open('%s deGenesList.txt' % fileName, 'r')
    for line in lista:
        l = line.strip('\n')
        deGenesList.append(l)


    # Accessing the API
    stringApiUrl = 'https://string-db.org/api'
    outputFormat = 'tsv-no-header'
    method = 'get_string_ids'

    params = {
        "identifiers": "\r".join(deGenesList),
        "species": 9606, #Homo sapiens NCBI taxonomy ID
        "limit": 1, #Only the best match is returned.
        "echo_query": 1,
    }

    #Constructing a URL

    requestURL = "/".join([stringApiUrl, outputFormat, method])

    #Calling STRING

    results = requests.post(requestURL, data = params)


    #Reading and parsing results


    inputList = []

    for line in results.text.strip().split("\n"):
        l = line.split("\t")
        input_identifier, string_identifier = l[0], l[2]
        inputList.append(l[2])

        print("Input:", input_identifier, "STRING:", string_identifier, sep = '\t')

    with open("%s inputList.txt" % fileName, "w") as f:
        for geneId in inputList:
            f.write('%s\n' % geneId)