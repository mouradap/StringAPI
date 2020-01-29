import requests

def createNet(fileName):

    string_api_url = "https://string-db.org/api"
    output_format = "image"
    method = "network"

    inputList = []

    lista = open('%s inputList.txt' % fileName, 'r')
    for line in lista:
        l = line.strip('\n')
        inputList.append(l)

    ##
    ## Construct URL
    ##


    request_url = "/".join([string_api_url, output_format, method])

    ## For each gene call STRING

    params = {

        "identifiers": "\r".join(inputList),
        "species": 9606, #Homo sapiens NCBI taxonomy ID
        "add_white_nodes": 0, # add 15 white nodes to my protein 
        "network_flavor": "confidence", # show confidence links
        "required_score": 750,
        "hide_disconnected_nodes": 1
    }


    ##
    ## Call STRING
    ##

    response = requests.post(request_url, data=params)

    ##
    ## Save the network to file
    ##


    with open("%s network.png" % fileName, 'wb') as fh:
        fh.write(response.content)