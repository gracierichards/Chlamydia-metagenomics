cervical_columns = []
vaginal_columns = []
rectal_columns = []
f = open("/Users/gracie/Downloads/Thesis/Pathway Abundance/pathabundance_relab.tsv", "r")
first_line = f.readline()[:-1]
columns = first_line.split('\t')
for c in range(len(columns)):
    if 'C' in columns[c]:
        cervical_columns.append(c)
    elif 'V' in columns[c]:
        vaginal_columns.append(c)
    elif 'R' in columns[c]:
        rectal_columns.append(c)
        
def VcomparedtoR():
    print("Pathways that have a higher sum of abudances in vaginal samples than rectal samples")
    f2 = open("/Users/gracie/Downloads/unique_V_compared_to_R.tsv", "w")
    f2.write(first_line + "\tVaginal Sum\tRectal Sum\tDifference\n")
    line = f.readline()[:-1]
    while line != "":
        columns = line.split('\t')
        Vsum = 0
        for i in vaginal_columns:
            Vsum += float(columns[i])
        Rsum = 0
        for j in rectal_columns:
            Rsum += float(columns[j])
        if Vsum > Rsum:
            print(columns[0])
            f2.write(line + "\t" + str(Vsum) + "\t" + str(Rsum) + "\t" + str(Vsum-Rsum) + "\n")
        line = f.readline()[:-1]
    f2.close()
    
def pathways_in_all_V():
    print("Pathways found in all vaginal samples")
    f2 = open("/Users/gracie/Downloads/pathways_in_all_V.tsv", "w")
    f2.write(first_line + "\n")
    line = f.readline()[:-1]
    while line != "":
        columns = line.split('\t')
        found0 = False
        for i in vaginal_columns:
            if float(columns[i]) == 0:
                found0 = True
        if not found0:
            print(columns[0])
            f2.write(line + "\n")
        line = f.readline()[:-1]
    f2.close()
    
"""Searches for pathways that are only found in vaginal samples,
but could be just some of the vaginal samples, not all"""
def pathways_only_in_V():
    print("Pathways only found in vaginal samples")
    f2 = open("/Users/gracie/Downloads/pathways_only_in_V.tsv", "w")
    f2.write(first_line + "\n")
    line = f.readline()[:-1]
    while line != "":
        columns = line.split('\t')
        Vall0 = True
        for i in vaginal_columns:
            if float(columns[i]) != 0:
                Vall0 = False
        all0 = True
        for i in cervical_columns:
            if float(columns[i]) != 0:
                all0 = False
        for i in rectal_columns:
            if float(columns[i]) != 0:
                all0 = False
        if all0 and not Vall0:
            print(columns[0])
            f2.write(line + "\n")
        line = f.readline()[:-1]
    f2.close()
    
"""Searches for pathways that are only found in rectal samples,
but could be just some of the rectal samples, not all"""
def pathways_only_in_R():
    print("Pathways only found in rectal samples")
    f2 = open("/Users/gracie/Downloads/pathways_only_in_R.tsv", "w")
    f2.write(first_line + "\n")
    line = f.readline()[:-1]
    while line != "":
        columns = line.split('\t')
        Rall0 = True
        for i in rectal_columns:
            if float(columns[i]) != 0:
                Rall0 = False
        all0 = True
        for i in cervical_columns:
            if float(columns[i]) != 0:
                all0 = False
        for i in vaginal_columns:
            if float(columns[i]) != 0:
                all0 = False
        if all0 and not Rall0:
            print(columns[0])
            f2.write(line + "\n")
        line = f.readline()[:-1]
    f2.close()
    
"""Searches for pathways that are only found in cervical samples,
but could be just some of the cervical samples, not all"""
def pathways_only_in_C():
    print("Pathways only found in cervical samples")
    f2 = open("/Users/gracie/Downloads/pathways_only_in_C.tsv", "w")
    f2.write(first_line + "\n")
    line = f.readline()[:-1]
    while line != "":
        columns = line.split('\t')
        Call0 = True
        for i in cervical_columns:
            if float(columns[i]) != 0:
                Call0 = False
        all0 = True
        for i in rectal_columns:
            if float(columns[i]) != 0:
                all0 = False
        for i in vaginal_columns:
            if float(columns[i]) != 0:
                all0 = False
        if all0 and not Call0:
            print(columns[0])
            f2.write(line + "\n")
        line = f.readline()[:-1]
    f2.close()

"""Searches for pathways that are not found in rectal samples,
but must be present in at least one vaginal and cervical sample"""
def pathways_only_in_VC():
    print("Pathways only found in vaginal and cervical samples")
    f2 = open("/Users/gracie/Downloads/Thesis/Pathway Abundance/pathways_only_in_VC.tsv", "w")
    f2.write(first_line + "\n")
    line = f.readline()[:-1]
    while line != "":
        columns = line.split('\t')
        Vall0 = True
        for i in vaginal_columns:
            if float(columns[i]) != 0:
                Vall0 = False
        Call0 = True
        for i in cervical_columns:
            if float(columns[i]) != 0:
                Call0 = False
        Rall0 = True
        for i in rectal_columns:
            if float(columns[i]) != 0:
                Rall0 = False
        if Rall0 and not Vall0 and not Call0:
            print(columns[0])
            f2.write(line + "\n")
        line = f.readline()[:-1]
    f2.close()
    
"""Searches for pathways that are not found in vaginal samples,
but must be present in at least one cervical and rectal sample"""
def pathways_only_in_CR():
    print("Pathways only found in cervical and rectal samples")
    f2 = open("/Users/gracie/Downloads/Thesis/Pathway Abundance/pathways_only_in_CR.tsv", "w")
    f2.write(first_line + "\n")
    line = f.readline()[:-1]
    while line != "":
        columns = line.split('\t')
        Call0 = True
        for i in cervical_columns:
            if float(columns[i]) != 0:
                Call0 = False
        Rall0 = True
        for i in rectal_columns:
            if float(columns[i]) != 0:
                Rall0 = False
        Vall0 = True
        for i in vaginal_columns:
            if float(columns[i]) != 0:
                Vall0 = False
        if Vall0 and not Call0 and not Rall0:
            print(columns[0])
            f2.write(line + "\n")
        line = f.readline()[:-1]
    f2.close()
    
"""Searches for pathways that are not found in cervical samples,
but must be present in at least one vaginal and rectal sample"""
def pathways_only_in_VR():
    print("Pathways only found in vaginal and rectal samples")
    f2 = open("/Users/gracie/Downloads/Thesis/Pathway Abundance/pathways_only_in_VR.tsv", "w")
    f2.write(first_line + "\n")
    line = f.readline()[:-1]
    while line != "":
        columns = line.split('\t')
        Vall0 = True
        for i in vaginal_columns:
            if float(columns[i]) != 0:
                Vall0 = False
        Rall0 = True
        for i in rectal_columns:
            if float(columns[i]) != 0:
                Rall0 = False
        Call0 = True
        for i in cervical_columns:
            if float(columns[i]) != 0:
                Call0 = False
        if Call0 and not Vall0 and not Rall0:
            print(columns[0])
            f2.write(line + "\n")
        line = f.readline()[:-1]
    f2.close()
    
"""Searches for pathways that are found at least once in each site"""
def pathways_in_all():
    print("Pathways found in all sites")
    f2 = open("/Users/gracie/Downloads/Thesis/Pathway Abundance/pathways_only_in_CVR.tsv", "w")
    f2.write(first_line + "\n")
    line = f.readline()[:-1]
    while line != "":
        columns = line.split('\t')
        Call0 = True
        for i in cervical_columns:
            if float(columns[i]) != 0:
                Call0 = False
        Vall0 = True
        for i in vaginal_columns:
            if float(columns[i]) != 0:
                Vall0 = False
        Rall0 = True
        for i in rectal_columns:
            if float(columns[i]) != 0:
                Rall0 = False
        if not Call0 and not Vall0 and not Rall0:
            print(columns[0])
            f2.write(line + "\n")
        line = f.readline()[:-1]
    f2.close()

#Call all the functions you want here:
pathways_only_in_VC()
pathways_only_in_CR()
pathways_only_in_VR()
pathways_in_all()

f.close()
