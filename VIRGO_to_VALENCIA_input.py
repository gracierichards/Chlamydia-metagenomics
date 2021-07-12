import csv

def find_num_reads(sample, taxon):
    input0 = open("../../Downloads/VIRGO output/summary.Abundance.txt", 'r')
    line = input0.readline()
    species = line.split()
    i = 0
    while i < len(species):
        if species[i] == taxon:
            break
        i += 1
    row = 0
    while row < 30:
        line = input0.readline()
        sample2 = line.split()[0]
        if sample == sample2:
            return line.split()[i]
        row += 1

def add_up_genus(sample, genus):
    cols = []
    input0 = open("../../Downloads/VIRGO output/summary.Abundance.txt", 'r')
    line = input0.readline()
    species = line.split()
    i = 0
    while i < len(species):
        genus2 = species[i].split("_")[0]
        if genus2 == genus:
            while genus2 == genus:
                cols.append(i)
                i += 1
                if i < len(species):
                    genus2 = species[i].split("_")[0]
                else:
                    break
            break
        i += 1
    row = 0
    sum0 = 0
    while row < 30:
        line = input0.readline()
        sample2 = line.split()[0]
        if sample == sample2:
            for col in cols:
                sum0 += int(line.split()[col])
        row += 1
    return sum0

output = open("VALENCIAinputVIRGO.csv", "w", newline='')
a = csv.writer(output)
column2 = {"107C":4273143, "107V":44126492, "121C":1917389, "121V":4033264, "192C":1593456, "192V":7937196, "30C":1143424,
           "30V":7431500, "319C":1305023, "319V":1542082, "35C":1069782, "35V":1570433, "362C":17988652, "362V":8102405,
           "57C":1808156, "57V":11897747, "72C":1510729, "72V":4644785, "98C":2239234, "98V":11508517}
lactobacillus = []
gardnerella = []
prevotella = []
atopobium = []
sneathia = []
input0 = open("../../Downloads/VIRGO output/summary.Abundance.txt", 'r')
line = input0.readline()
species = line.split()[1:]
for s in species:
    if s.split("_")[0] == "Lactobacillus":
        lactobacillus.append(s)
    elif s.split("_")[0] == "Gardnerella":
        gardnerella.append(s)
    elif s.split("_")[0] == "Prevotella":
        prevotella.append(s)
    elif s.split("_")[0] == "Atopobium":
        atopobium.append(s)
    elif s.split("_")[0] == "Sneathia":
        sneathia.append(s)
genera = set()
for s in species:
    genus = s.split("_")[0]
    genera.add("g_" + genus)
genera.remove("g_Lactobacillus")
genera.remove("g_Gardnerella")
genera.remove("g_Prevotella")
genera.remove("g_Atopobium")
genera.remove("g_Sneathia")
genera.remove("g_BVAB1")
genera.add("BVAB1")

row1 = ["sampleID", "read_count"] + lactobacillus + gardnerella + prevotella + atopobium + sneathia + list(genera)
a.writerow(row1)
for sample in column2:
    row = [sample, column2[sample]]
    for taxon in row1:
        if taxon == "sampleID" or taxon == "read_count":
            x = 0
        else:
            if taxon.startswith("g_"):
                num_reads = add_up_genus(sample, taxon[2:])
            else:
                num_reads = find_num_reads(sample, taxon)
            row.append(num_reads)
    a.writerow(row)
    
