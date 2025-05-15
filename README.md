## Python
This repository holds analysis done in BIOL668 such as: Python (Object Orient Programming notebooks and other code)


## Features:
* Contreras_OOP_FinalProj_2025.py
* Contreras_PythonProject_2025.ipynb (jupyter notebook)
* Contreras_04A_Biopython_Tutorial_LSH-1.ipynb
* Contreras_PythonRefresher (1).py
* Contreras_make_person.py
* Contreras_person.py
* Contreras_wizard_class_HW.py
* Contreras_OOP_FinalProj_2025 (2).py

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
2. open jupyter notebook file and ensure this line of code is ran before running the rest of the code chunks in the jupyternotebook: exec(open("Contreras_OOP_FinalProj_2025.py").read())
3. All code chunks should run with no problem

   
<img width="1205" alt="Screenshot 2025-05-13 at 11 04 23 PM" src="https://github.com/user-attachments/assets/b126fad0-2a5e-4297-838f-76272e67adac" />

## OOP Project Part 2

Contains Biopython tutorial code found here: https://biopython.org/wiki/Seq
This project demonstrates similar usage to the classes and functions created in project part 1. 
It requires the following files: KRAS.fast, KRAS_genbank.gb, opuntia.dnd

Example of tutorial:
creates a phylogenetic tree using biopython module and opuntia.dnd

<img width="814" alt="Screenshot 2025-05-14 at 12 22 20 AM" src="https://github.com/user-attachments/assets/549cc09c-7b64-4ba5-a745-d179310a2ede" />

## Python Refresher
This project contains python code.
Function 1:
calculates the weight matrix for a given float value. The first float value is the toal count of a base at a postion (Nij). The second float value is the totoal number of sequences in an alignment (N). lastly, the third float value is the probability index (Pi) of a base being at a postiion. 

Weight Matrix Equation:    
   [  (Nij + Pi) / (N + 1)  ]                                       
Ln |------------------------|
   [           Pi           ]  

Function 2:
Finds motifs from a sequence dictionary. It then returns a dictionary that only contains matching motif sequences. 

Function 3:
Takes a sequence dictionary and returns a different dictionary with key value pairs that have sequences beginning with start codons "ATG" or "AUG". 

Function 4:
Calculates bray-curtis distance. 

Example usage:

<img width="384" alt="Screenshot 2025-05-14 at 7 21 53 PM" src="https://github.com/user-attachments/assets/20b82cce-ab1e-463f-848a-39e3c3ce7421" />


## OOP Wizard Game
This project utilized: Contreras_person.py, Contreras_wizard_class_HW.py, Contreras_make_person.py

Contreras_person.py -
Creates a Person class that holds first and last name. Employee class inherits Person class and adds date of birth and ssn information. 

Example usage:

<img width="494" alt="Screenshot 2025-05-14 at 7 39 48 PM" src="https://github.com/user-attachments/assets/555126c4-c583-4676-89e9-4e117046d873" />


Contreras_wizard_class_HW.py -
Creates a Character class that modifies the method Attack and subtracts from a second character. It also contains a Wizard class that inherits Character class's methods to adds heal and fireball methods. 

Example usage:

<img width="501" alt="Screenshot 2025-05-14 at 7 39 29 PM" src="https://github.com/user-attachments/assets/8499df0e-76ef-49d2-a680-bba51e624144" />

Contreras_make_person.py - 
Imports "Contreras_person.py" and ensures that file is working properly

Example usage:

<img width="249" alt="Screenshot 2025-05-14 at 7 41 42 PM" src="https://github.com/user-attachments/assets/df4764d4-8582-444d-9fe8-da37aa72e8aa" />


## Docstring Test
Applies doctest function to Contreras_OOP_FinalProj_2025 (2).py to ensure that all code runs as expected. 

Example usage:

<img width="411" alt="Screenshot 2025-05-14 at 7 47 30 PM" src="https://github.com/user-attachments/assets/8c7b44d6-c1e7-4dbd-868a-f7eec1a4a35f" />



