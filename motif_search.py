# Creates tuples from FASTA file containing (fasta identifier information, sequence)
from pprint import pprint
import re
input_file = 'UP000005640_9606.fasta'   # human proteome
pattern = 'MAA.RDN'
k = len(pattern)

def fasta_idseq(file_name):
    with open(file_name, 'r') as fhand:
        id = None
        seq = []

        for line in fhand:
            line = line.strip()
            joinedseq = ''.join(seq)
            if line.startswith('>'):
                if id is None:
                    id = line
                else:
                    yield (id, joinedseq)
                    id = line
                    seq = []
            else:
                seq.append(line)

# Finds all proteins containing the matching pattern and adding them to a list, as tuples with ID and seq ('found')
def find_proteins():
    count = 0
    found = []
    for item in fasta_idseq(input_file):
        if re.search(pattern, item[1]):
            count += 1
            for i in range(count):
                if item not in found:
                    found.append(item)
    return found

found = find_proteins()

# Counts number of times the pattern shows up in the found proteins containing the pattern.
def count_pattern():
    counter = {}
    regex = re.compile(pattern)
    for i in found:
        match_count = len(re.findall(regex, i[1]))
        counter[i[0]] = match_count
    return counter

print(count_pattern())








