aminotable = [
['Ile' , 'AUU','AUC','AUA'],                            #0
['Leu' , 'CUU','CUC','CUA','CUG','UUA','UUG'],          #1
['Val' , 'GUU','GUC','GUA','GUG'],                      #2
['Phe' , 'UUU','UUC'],                                  #3
['Met' , 'AUG'],                                        #4
['Cys' , 'UGU','UGC'],                                  #5
['Ala' , 'GCU','GCC','GCA','GCG'],                      #6
['Gly', 'GGU', 'GGC', 'GGA', 'GGG'],                    #7
['Pro' , 'CCU', 'CCC', 'CCA', 'CCG'],                   #8
['Thr' , 'ACU', 'ACC', 'ACA', 'ACG'],                   #9
['Ser' , 'UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],     #10
['Tyr' , 'UAU', 'UAC'],                                 #11
['Trp' , 'UGG'],                                        #12
['Gln' , 'CAA', 'CAG'],                                 #13
['Asn' , 'AAU', 'AAC'],                                 #14
['His' , 'CAU', 'CAC'],                                 #15
['Glu' , 'GAA', 'GAG'],                                 #16
['Asp' , 'GAU', 'GAC'],                                 #17
['Lys', 'AAA', 'AAG'],                                  #18
['Arg' , 'CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],     #19
['Stop' , 'UAA', 'UAG', 'UGA'],                         #20
]

sequence = input("\nEnter RNA Sequence : ")

print('Original sequence: ',sequence,'\n')

n = 0
seqlength = len(sequence)

print('Amino Sequence: ')

while (n < seqlength):
    codon = sequence[n:n+3]
    for amino in aminotable:
        for i in range(len(amino) - 1):
            match = amino[i+1]
            if (codon == match) :
                print(amino[0], end = '-')
                break
    n += 3

print('\n\n\nEnd of program')
