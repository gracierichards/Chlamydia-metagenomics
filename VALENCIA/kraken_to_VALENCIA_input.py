import csv

output = open("kraken_input.csv", "w", newline='')
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
    input0 = open("../../Downloads/kraken_reports/kraken_report_clean_" + sample + ".txt", 'r')
    line = input0.readline()
    while line != "":
        taxon = line.split('\t')[5]
        taxon = '_'.join(taxon.split())
        if line.split()[3] == 'S':
            if taxon.split('_')[0] == "Lactobacillus":
                lactobacillus.add(taxon)
            elif taxon.split('_')[0] == "Gardnerella":
                gardnerella.add(taxon)
            elif taxon.split('_')[0] == "Prevotella":
                prevotella.add(taxon)
            elif taxon.split('_')[0] == "Atopobium":
                atopobium.add(taxon)
            elif taxon.split('_')[0] == "Sneathia":
                sneathia.add(taxon)
        elif line.split()[3] == 'G':
            other.add("g_" + taxon)
        elif line.split()[3] == 'F':
            other.add("f_" + taxon)
        elif line.split()[3] == 'O':
            other.add("o_" + taxon)
        elif line.split()[3] == 'C':
            other.add("c_" + taxon)
        elif line.split()[3] == 'P':
            other.add("p_" + taxon)
        line = input0.readline()
row1 = ["sampleID", "read_count"] + list(lactobacillus) + list(gardnerella) + list(prevotella) + list(atopobium) + list(sneathia) + list(other)
a.writerow(row1)

def find_num_reads(sample, taxon):
    file = open("../../Downloads/kraken_reports/kraken_report_clean_" + sample + ".txt", 'r')
    line = file.readline()    
    while line != "":
        taxon0 = line.split('\t')[5]
        taxon0 = '_'.join(taxon0.split())
        if taxon0 == taxon:
            return line.split()[1]
        line = file.readline()

for sample in column2:
    row = [sample, column2[sample]]
    for taxon in row1:
        if taxon == "sampleID" or taxon == "read_count":
            x = 0
        else:
            if taxon[1] == "_":
                taxon = taxon[2:]
            num_reads = find_num_reads(sample, taxon)
            row.append(num_reads)
    a.writerow(row)


        
