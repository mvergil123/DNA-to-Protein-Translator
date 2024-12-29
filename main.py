# DNA to RNA function
def dna_to_rna(sequence):
    #Take a DNA sequence
    #Return the transcribed RNA sequence string
    new_seq = ""
    for char in sequence:
        if char == "A":
            char = "U"
        elif char == "T":
            char = "A"
        elif char == "G":
            char = "C"
        elif char == "C":
            char = "G"
        new_seq += char

    return new_seq


def parse_file_into_acids(filename):
    nest_text = []
    with open(filename, "r") as text:
        for line in text:
            line = line.replace("\n", "")
            line = line.split()
            nest_text.append(line)
    return nest_text

def translating_rna(rna_seq):
    #read through the sequence until you detect "AUG"
    #start from AUG until you find one of the stopping codons
    stop_codon = ["UAA", "UGA", "UAG"]
    #find where AUG first is !!! don't use this function 


    sequence = rna_seq

    # Convert both the sequence and search pattern to lowercase
    sequence_lower = sequence.lower()
    search_pattern = "AUG".lower()

    # Find the index of "AUG" in the lowercase string
    ind = sequence_lower.find(search_pattern)

    rna_seq = rna_seq[ind:]

    cycle = len(rna_seq) // 3
    nucelos = []
    start = 0
    end = 3
    for i in range(cycle):
        #Splits by 3 letters
        word = rna_seq[start:end]
        nucelos.append(word)
        start += 3
        end += 3

    stop = 0
    #find the stop codon
    for codon in stop_codon:
        if codon in nucelos:
            stop = nucelos.index(codon)
            break

    nucleos = nucelos[:stop]
    return nucleos


def finding_protein(codon_list, parsed_list):
    #find the protein name of the codon
    #abbreviate it
    count = 0
    location_list = []
    for c in codon_list:
        for list in parsed_list:
            if c in list:
                location_list.append(count)
                count = 0
                break
            else:
                count += 1
            

    #I have the location of the list of where the thingy is
    #so now i gotta put find the actual name of it
    protein = ""
    for num in location_list:
        letter = parsed_list[num][2]
        protein += letter

    return protein


def test_my_functions():
    #Call other functions with test data
    #Assert it
    #After your program is finished, this function should be callable without throwing an error
    #Test at least 3 cases with the dna to rna function
    
    sequence = "A"
    expected = "U"
    assert dna_to_rna(sequence) == expected

    sequence = ""
    expected = ""
    assert dna_to_rna(sequence) == expected

    sequence = "T"
    expected = "A"
    assert dna_to_rna(sequence) == expected


# regular code
if __name__ == "__main__":
    #Inputs
    file = input("FILENAME> ")
    seq = input("SEQUENCE> ") 
    #results from the functions 
    rna = dna_to_rna(seq) 
    text = parse_file_into_acids(file)
    translated_rna = translating_rna(rna)
    protein = finding_protein(translated_rna, text)
    test_my_functions()
    print("OUTPUT",protein)
