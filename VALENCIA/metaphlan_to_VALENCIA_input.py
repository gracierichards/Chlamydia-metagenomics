import csv

output = open("metaphlan_input.csv", "w", newline='')
a = csv.writer(output)
column2 = {"107C":4273143, "107V":44126492, "121C":1917389, "121V":4033264, "192C":1593456, "192V":7937196, "30C":1143424,
           "30V":7431500, "319C":1305023, "319V":1542082, "35C":1069782, "35V":1570433, "362C":17988652, "362V":8102405,
           "57C":1808156, "57V":11897747, "72C":1510729, "72V":4644785, "98C":2239234, "98V":11508517}
lactobacillus = set()
gardnerella = set()
prevotella = set()
atopobium = set()
sneathia = set()
other = set()
for sample in column2:
    input0 = open("../../Downloads/Metaphlan/" + sample + ".txt", 'r')
    line = input0.readline()
    while line.startswith('#'):
        line = input0.readline()
    while line != "":
        column0 = line.split('\t')[0]
        taxa = column0.split('|')
        last = taxa[-1]
        if "s__" in last:
            if last.split('_')[2] == "Lactobacillus":
                lactobacillus.add(last[3:])
            elif last.split('_')[2] == "Gardnerella":
                gardnerella.add(last[3:])
            elif last.split('_')[2] == "Prevotella":
                prevotella.add(last[3:])
            elif last.split('_')[2] == "Atopobium":
                atopobium.add(last[3:])
            elif last.split('_')[2] == "Sneathia":
                sneathia.add(last[3:])
        else:
            remove_underscore = last[0:2] + last[3:]
            other.add(remove_underscore)
        line = input0.readline()
row1 = ["sampleID", "read_count"] + list(lactobacillus) + list(gardnerella) + list(prevotella) + list(atopobium) + list(sneathia) + list(other)
a.writerow(row1)

def find_abundance(sample, taxon):
    file = open("../../Downloads/Metaphlan/" + sample + ".txt", 'r')
    line = file.readline()    
    while line != "":
        column0 = line.split('\t')[0]
        taxa = column0.split('|')
        last = taxa[-1]
        taxon0 = last[3:]
        if taxon0 == taxon:
            return line.split()[2]
        line = file.readline()
    return 0

for sample in column2:
    row = [sample, column2[sample]]
    for taxon in row1:
        if taxon == "sampleID" or taxon == "read_count":
            x = 0
        else:
            if taxon[1] == "_":
                taxon = taxon[2:]
            abundance = find_abundance(sample, taxon)
            num_reads = float(abundance) * column2[sample] * 0.01
            row.append(num_reads)
    a.writerow(row)
    
