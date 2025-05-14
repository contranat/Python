## Python
This repository holds analysis done in BIOL668 such as: Python (Object Orient Programming notebooks and other code)


## Features:
* Contreras_OOP_FinalProj_2025.py
* Contreras_PythonProject_2025.ipynb (jupyter notebook)
* Contreras_04A_Biopython_Tutorial_LSH-1.ipynb

## Files Needed:
* KRAS.fasta
* KRAS_genbank.gb
* opuntia.dnd


## OOP Project Part 1
Builds on from a constructuro and adds methods of a parent class. 
Classes:

Seq -
cleans sequences, creates kmers, outputs fasta-like information.

DNA - 
inherits methods from the Seq class. 
Counts GC content, performs reverse complementary DNA, returns 6 frames (3 forward, 3 reverse complement frames).

RNA -
inherits methods from DNA class. 
Creates codons, translates and returns into protein.

Protein - 
inherits methods from Seq class. 
Calculates total hydrophobicity and molecular weight. 


Example usage:
Directions -
1. Run Contreras_OOP_FinalProj_2025.py
2. open ensure this line of code is ran before running the rest of the code chunks in the jupyternotebook: exec(open("Contreras_OOP_FinalProj_2025.py").read())
3. All code chunks should run with no problem

   
<img width="1205" alt="Screenshot 2025-05-13 at 11 04 23 PM" src="https://github.com/user-attachments/assets/b126fad0-2a5e-4297-838f-76272e67adac" />

## OOP Project Part 2

Contains Biopython tutorial code found here: https://biopython.org/wiki/Seq
This project demonstrates similar usage to the classes and functions created in project part 1. 
It requires the following files: KRAS.fast, KRAS_genbank.gb, opuntia.dnd

Example of tutorial:
creates a phylogenetic tree using biopython module and opuntia.dnd

<img width="814" alt="Screenshot 2025-05-14 at 12 22 20 AM" src="https://github.com/user-attachments/assets/549cc09c-7b64-4ba5-a745-d179310a2ede" />

