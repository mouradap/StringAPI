import requests ## python -m pip install requests 
import json

def funcEnrich(fileName):
        

    string_api_url = "https://string-db.org/api"
    output_format = "json"
    method = "functional_annotation"


    ##
    ## Construct the request
    ##

    request_url = "/".join([string_api_url, output_format, method])

    ##
    ## Set parameters
    ##

    my_genes = []
    lista = open('%s inputList.txt' % fileName, 'r')
    for line in lista:
        l = line.strip('\n')
        my_genes.append(l)

    #my_genes = my_genes[0:5]


    params = {

        "identifiers" : "%0d".join(my_genes), # your protein
        "species" : 9606, # species NCBI identifier 

    }

    ##
    ## Call STRING
    ##

    response = requests.post(request_url, data=params)

    ##
    ## Read and parse the results
    ##

    data = json.loads(response.text)

    #print(data)

    functionsReport = []
    for row in data:

        term = row["term"]
        preferredNames = ",".join(row["preferredNames"])
        description = row["description"]
        category = row["category"]
        number_of_genes = row["number_of_genes"]
        ratio = row["ratio_in_set"]
        if (category == 'RCTM' and number_of_genes > 5) or (category == 'SMART' and number_of_genes > 5) or (category == 'Process' and ratio >= 0.5):
            report = (str(ratio), str(number_of_genes), term, description)
            functionsReport.append(report)        
            
            #print("\t".join([str(ratio), str(number_of_genes), term, description]))
            #print("\t".join([str(ratio), str(number_of_genes), preferredNames, category, term, description]))

    print(functionsReport)

    with open("%s functionalEnrichment.txt" % fileName, "w") as f:
        for report in functionsReport:
            ratio, numGenes, term, description = report

            f.write('%s %s %s %s\n' % (ratio, numGenes, term , description))