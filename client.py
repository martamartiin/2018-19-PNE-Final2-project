
import http.client

PORT = 8080
SERVER = 'localhost'

conn = http.client.HTTPConnection(SERVER, PORT)


endpoints = ['/listSpecies?json=true', '/listSpecies?limit=7;json=true', '/listSpecies?limit=0;json=true',
             '/listSpecies?limit=wrong;json=true', '/listSpecies?limit=-5;json=true',
             '/listSpecies?limit=;json=true', '/karyotype?specie=mouse;json=true',
             '/karyotype?specie=wrong;json=true', '/karyotype?specie=homo+sapiens;json=true',
             '/chromosomeLength?specie=mouse;chromo=18;json=true', '/chromosomeLength?specie=homo+sapiens;chromo=18;json=true',
             '/chromosomeLength?specie=wrong;chromo=18;json=true',
             '/chromosomeLength?specie=mouse;chromo=wrong;json=true',
             '/geneSeq?gene=FRAT1;json=true','/geneSeq?gene=wrong;json=true',
             '/geneInfo?gene=FRAT1;json=true', '/geneInfo?gene=wrong;json=true',
             '/geneCalc?gene=FRAT1;json=true', '/geneCalc?gene=wrong;json=true',
             '/geneList?chromo=1;start=0;end=30000;json=true', '/geneList?chromo=1;start=wrong;end=30000;json=true',
             '/geneList?chromo=1;start=0;end=wrong;json=true', '/geneList?chromo=wrong;start=0&end=wrong;json=true',
             '/wrong?json=true']

for request in endpoints:
    conn.request("GET", request)

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    # -- Print the received data
    print(data1)