import csv
import argparse
import sys

def find_num_reads(sample, taxon):
    input0 = open(n.input, 'r')
    line = input0.readline()
    species = line.split()
    i = 0
    while i < len(species):
        if species[i] == taxon:
            break
        i += 1
    line = input0.readline()
    while line != "":
        sample2 = line.split()[0]
        if sample == sample2:
            return line.split()[i]
        line = input0.readline()

def add_up_genus(sample, genus):
    #cols contains the indices of the cells that are species of the given genus
    cols = []
    input0 = open(n.input, 'r')
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
    sum0 = 0
    line = input0.readline()
    while line != "":
        sample2 = line.split()[0]
        if sample == sample2:
            for col in cols:
                sum0 += int(line.split()[col])
        line = input0.readline()
    return sum0

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Please provide the path to the summary.Abundance.txt file.")
n = parser.parse_args()
try:
    input0 = open(n.input, "r")
except IOError:
    print("Error in provided input path.")
    sys.exit()

output = open("VALENCIAinputVIRGO.csv", "w", newline='')
a = csv.writer(output)
lactobacillus = []
gardnerella = []
prevotella = []
atopobium = []
sneathia = []
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

input0 = open(n.input, 'r')
line = input0.readline()
line = input0.readline()
while line != "":
    sample2 = line.split()[0]
    row_to_write = [sample2]
    for taxon in row1:
        if taxon == "sampleID" or taxon == "read_count":
            x = 0
        else:
            if taxon.startswith("g_"):
                num_reads = add_up_genus(sample2, taxon[2:])
            else:
                num_reads = find_num_reads(sample2, taxon)
            row_to_write.append(num_reads)
    #Calculate the read_count:
    row_to_write.insert(1, sum([int(x) for x in row_to_write[1:]]))
    a.writerow(row_to_write)
    line = input0.readline()
