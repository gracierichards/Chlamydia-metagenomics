from Bio import SeqIO
import argparse
import os
import sys

"""Save this program in an empty directory that will contain the reads for a single sample. Also run this program from the directory
it is in."""

species_set = {}
clost = []
zoonotic = ["Anaplasma phagocytophilum", "Bacillus anthracis", "Bacillus paranthracis", "Borreliella burgdorferi", "Brucella abortus",
            "Brucella melitensis", "Brucella sp. 10RB9215", "Brucella suis", "Campylobacter avium", "Campylobacter coli",
            "Campylobacter jejuni", "Campylobacter ureolyticus", "Lumpy skin disease virus", "Enterococcus avium",
            "Erysipelothrix rhusiopathiae", "Francisella tularensis", "Haemophilus influenzae", "Haemophilus parahaemolyticus",
            "Haemophilus parainfluenzae", "Mycobacterium avium", "Mycobacterium chimaera", "Mycobacterium colombiense",
            "Mycobacterium intracellulare", "Mycobacterium lepraemurium", "Mycobacterium mantenii", "Mycobacterium marseillense",
            "Mycobacterium paraintracellulare", "Streptococcus suis",  "Yersinia enterocolitica", "Yersinia pestis", "Yersinia pseudotuberculosis"]
bv = ["Anaerococcus", "Atopobium", "Bifidobacterium", "Corynebacterium", "Enterobacter", "Finegoldia", "Gemella", "Megasphaera",
      "Mobiluncus", "Peptoniphilus", "Prevotella", "Staphylococcus", "Streptococcus"]
std = ["Human alphaherpesvirus 2", "Mycoplasma genitalium", "Neisseria gonorrhoeae"]
gut = ["Bacteroides fragilis", "Clostridioides difficile", "Enterococcus faecalis", "Enterococcus faecium", "Helicobacter pylori",
       "Rotavirus C", "Rotavirus D", "Salmonella enterica", "Vibrio cholerae", "Vibrio parahaemolyticus", "Yersinia similis"]
burkholderia = ["mallei", "oklahomensis", "pseudomallei", "sp. BDU6", "sp. BDU8", "sp. MSMB0266", "sp. MSMB0852", "sp. MSMB1588",
                "sp. MSMB617WGS", "thailandensis"]
skin = ["Lymphocystis disease virus 1", "Mycobacterium haemophilum", "Mycobacterium ulcerans", "Canid alphaherpesvirus 1",
        "Equid alphaherpesvirus 9", "Suid alphaherpesvirus 1"]
bacillus = ["albus", "bombysepticus", "cereus", "cytotoxicus", "luti", "mobilis", "mycoides", "pacificus", "pseudomycoides",
            "sp. ABP14", "sp. FDAARGOS_235", "sp. HBCD-sjtu", "sp. JAS24-2", "thuringiensis", "toyonensis", "tropicus", "wiedmannii"]
respiratory = ["Influenza A virus", "Bordetella parapertussis", "Bordetella pertussis", "Dialister pneumosintes",
               "Elizabethkingia anophelis", "Haemophilus haemolyticus", "Haemophilus pittmaniae", "Haemophilus sp. oral taxon 036",
               "Klebsiella aerogenes", "Klebsiella pneumoniae", "Legionella pneumophila", "Mycobacterium haemophilum",
               "Mycobacterium leprae", "Mycobacterium canettii", "Mycobacterium tuberculosis", "Mycoplasma pneumoniae"]
acinetobacter = ["baumannii", "calcoaceticus", "junii", "nosocomialis", "pittii"]
    
def pathogen_type(species):
    if species.split()[0] == "Lactobacillus":
        return "Lactobacillus"
    elif species.split()[0] == "Gardnerella":
        return "Gardnerella"
    elif species.split()[0] == "Rickettsia":
        return "Zoonotic_pathogens"
    elif species.split()[0] == "Chlamydia":
        return "Chlamydia"
    elif species.split()[0] == "Waddlia":
        return "Chlamydia_like"
    elif species.split()[0].endswith("chlamydia"):
        return "Chlamydia_like"
    elif species.split()[0] == "Simkania":
        return "Chlamydia_like"
    elif species.split()[0] == "Coxiella":
        return "Zoonotic_pathogens"
    elif species.split()[0] == "Leptospira":
        return "Zoonotic_pathogens"
    elif species.split()[0] == "Orientia":
        return "Zoonotic_pathogens"
    elif species.startswith("Streptococcus sp."):
        return "Zoonotic_pathogens"
    elif species == "Escherichia coli":
        return "BV_pathogens"
    elif species.startswith("Coriobacteri"):
        return "BV_pathogens"
    elif species == "Collinella aerofaciens":
        return "BV_pathogens"
    elif species == "Pseudomonas aeruginosa":
        return "STD_pathogens"
    elif species == "Ureaplasma urealyticum":
        return "UTI_pathogens"
    elif species.split()[0] == "Alphapapillomavirus":
        return "STD_pathogens"
    elif species.split()[0] == "Shigella":
        return "Gut_pathogens"
    elif species.split()[0] == "Burkholderia" and species.split()[1:] in burkholderia:
        return "Skin_pathogens"
    elif species == "Listeria monocytogenes":
        return "Foodborne_pathogens"
    elif species.split()[0] == "Bacillus" and species.split()[1:] in bacillus:
        return "Foodborne_pathogens"
    elif species.split()[0] == "Acinetobacter" and species.split()[1] in acinetobacter:
        return "ARB"
    elif species in zoonotic:
        return "Zoonotic_pathogens"
    elif species in clost:
        return "BV_pathogens"
    elif species.split()[0] in bv:
        return "BV_pathogens"
    elif species in std:
        return "STD_pathogens"
    elif species in gut:
        return "Gut_pathogens"
    elif species in skin:
        return "Skin_pathogens"
    elif species in respiratory:
        return "Respiratory_pathogens"
    else:
        return "Other"
    
"""Fills in the dictionary species_set with the keys being species and subspecies, and the values are tuples (taxon name,
parent species)"""
def subspecies():
    species_taxid = ""
    for line in report:
        columns = line.split("\t")
        taxon = " ".join(columns[5].split())
        if columns[3] == "S":
            species_taxid = columns[4]
            if columns[4] not in species_set:
                species_set[columns[4]] = (taxon, "")
        elif columns[3].startswith("S"):
            species_set[columns[4]] = (taxon, species_taxid)
    report.close()
    
"""Goes through the Kraken report and lists out the taxids of all species within the order Clostridiales."""
def make_list_clost_species():
    list1 = []
    found = False
    report = open("/home/sbomman/Kraken2/output/kraken_report_clean_" + n.sample + ".txt", "r")
    for line in report:
        columns = line.split("\t")
        if found:
            if columns[3] == "O":
                global clost
                clost = list1
                report.close()
                return
            elif columns[3] == "S":
                species = " ".join(columns[5].split())
                list1.append(species)
        else:
            if columns[4] == "186802":
                found = True
    print("Error: Did not find the end of Clostridiales in Kraken report")
    
def make_directories(pathogen):
    try:
        os.mkdir(os.getcwd() + "/" + pathogen)
    except FileExistsError:
        pass
    
parser = argparse.ArgumentParser()
parser.add_argument("sample")
n = parser.parse_args()
try:
    kraken_out = open("/home/sbomman/Kraken2/analysis_output/" + n.sample + "_kraken.out", "r")
    report = open("/home/sbomman/Kraken2/output/kraken_report_clean_" + n.sample + ".txt", "r")
    records = SeqIO.index("/home/sbomman/Kneaddata/knead_" + n.sample + "/kneaddata_output/" + n.sample + "_trimmed_grouped_kneaddata.fastq", "fastq")
except IOError:
    print("Not a valid sample name.")
    sys.exit()

subspecies()
make_list_clost_species()

for pathogen in ["Lactobacillus", "Gardnerella", "Chlamydia", "Chlamydia_like", "Zoonotic_pathogens", "BV_pathogens", "STD_pathogens",
                 "Gut_pathogens", "Skin_pathogens", "Foodborne_pathogens", "Respiratory_pathogens", "UTI_pathogens", "ARB", "Other"]:
    make_directories(pathogen)

line = kraken_out.readline()
while line != "":
    if line[0] != "U":
        read_id = line.split("\t")[1]
        taxid = line.split("\t")[2]
        if taxid != "0" and taxid != "1":
            if taxid in species_set:
                if species_set[taxid][1] == "":
                    species = species_set[taxid][0]
                else:
                    parent_species = species_set[taxid][1]
                    species = species_set[parent_species][0]
                record = records[read_id]
                target_dir = pathogen_type(species)
                species = species.replace(":", "")
                species = species.replace("(", "")
                species = species.replace(")", "")
                species = species.replace("[", "")
                species = species.replace("]", "")
                species = species.replace("/", "")
                species = species.replace(" ", "_")
                f = open(os.getcwd() + "/" + target_dir + "/" + species + ".fastq", "a")
                SeqIO.write(record, f, "fastq")
                f.close()
    line = kraken_out.readline()
    