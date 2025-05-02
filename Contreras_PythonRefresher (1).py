
#----------------------------------------------------------------------------------------------------
#== FUNCTION 1 ==
#Write a function called weight_matrix, that takes in three float values as its arguments.
#Calculate the weight matrix value for the given float values.
#The first float value will be the total count of a base at a particular position (Nij).
#The second float value will be the total number of sequences in the alignment (N).
#The third float value will be the probability index of a base being at a particular position (Pi).
#Weight Matrix Equation:    [  (Nij + Pi) / (N + 1)  ]
#                        Ln |------------------------|
#                           [           Pi           ]  
#The weight matrix value should be returned.  Note: Ln is the natural log.

#import libraries
import numpy 
import re

def weight_matrix(Nij, N, Pi):
    numerator = (Nij + Pi)/(N+1)
    wm = numpy.log((numerator/Pi))
    return f'Weight Matrix:\n{wm}'

#Test the function with these data as the arguments. (return => 0.167054084663)
float2a=3  #Nij
float2b=10 #N
float2c=0.25 #Pi
print(weight_matrix(float2a,float2b,float2c))

#----------------------------------------------------------------------------------------------------
#== FUNCTION 2 ==
#Write a function called find_motifs two argument:
#  1) a motif
#  2) a dictionary of sequences
#and returns a dictionary that only includes sequences that match the motif 

def find_motifs(motif, seq_dict):
    dictionary_seq = {}
    for key, seq in seq_dict.items():
        if re.search(motif, seq):
            dictionary_seq[key] = seq
        else:
            print(f'{motif} Motif does not match {seq}')
    
    return f'{motif} Motif FOUND in {dictionary_seq}'
          
m='C[CG]'
test_data={0:'AGAC',1:'AGTCCC',2:'GAA',3:'GGCGG',4:'ATTAGGA'}

#Test the function with the motif and test_data
#It should return: {1: 'AGTCCC', 3: 'GGCGG'}
print(find_motifs(m, test_data))
#----------------------------------------------------------------------------------------------------
#== FUNCTION 3 ==
#Write a function called extract_pept that takes a sequence dictionary as an argument
#and returns a dictionary with only the key value pairs that have sequence that 
#begin with a start codon "ATG" or "AUG". However, the returned dictionary needs to contain
#only RNA seqeunces. In other words, all the T's need to be changed to U's.

def extract_pept(data):
    dictionary_key = {}  #empty dictionary to store matches

    for key, seq in data.items():
        #convert DNA to RNA 
        rna_seq = seq.replace("T", "U")
        
        #search for "AUG"
        #i kept "rna_seq[:3] == "ATG":" to check anyways but I know that this would not be possible 
        #since the DNA sequences are converted into RNA regardless. A bit redundant. 
        if rna_seq[:3] == "AUG" or rna_seq[:3] == "ATG": #[:3] takes the first indexes from the rna_seq string 
            dictionary_key[key] = rna_seq #stores sequences containing AUG
                

    return f'Sequences with start codon:\n{dictionary_key}'

test_data={0:'AGTACG',1:'AUGCCC',2:'GAA',3:'GGCGG',4:'ATGAGGGCG',5:'AUGGGGGAA'}

#Test the function with sequence_names, sequence_data.
#It should return: {1: 'AUGCCC', 4: 'AUGAGGGCG', 5: 'AUGGGGGAA'}
print(extract_pept(test_data))

#----------------------------------------------------------------------------------------------------
#== FUNCTION 4 ==
#Write a function called bray curtis that takes in a two lists of samples counts
#and returns the bray-curtis distance. Make sure to check that the list lengths
#are equal before doing the calculation. If they are not equal, "The samples
#do not have the name number of features. and return 0

def bray_curtis(sampleA, sampleB):
    #makes sure both lists have the same length
    if len(sampleA) != len(sampleB):
        print("The samples do not have the same number of features.")
        
        return 0 #if lengths don't match it does not proceed and returns 0.
    
    #calculates Bray-curtis distance 
    num = 0 #initialized to add numerator values
    den = 0 #initialized to add denomenator values
        
    for A, B in zip(sampleA, sampleB): #zip combines different elements into tuples
        num += abs(A - B)  #calculates the difference between sampleA and sampleB
        den += (A + B)  #calculates the total number of counts between sampleA and sampleB
    bc = num / den #calculates the bray-curtis distance
    
    return f'Bray-Curtis Distance:\n{bc}'

sampleA=[10, 50, 100, 150]
sampleB=[150, 100, 50, 10]

#Test the function with sampleA and sampleB
#It should return: 0.6129032258064516
print(bray_curtis(sampleA, sampleB)) #moderately related








