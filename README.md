SNPchimpRepo: _a suite of useful programs for SNPchiMp users_
===========
*ref: E.L. Nicolazzi (Fondazione Parco Tecnologico Padano) - Via Einstein, Loc. Cascina Codazza (26900) Lodi (Italy). Email: ezequiel [dot] nicolazzi [at] tecnoparco [dot] org*


The goal of this suite of programs is to help users doing some routine work without doing any actual programming. 
This directory includes a GUI for Windows and Mac users (64bit) and source codes, so you're able to see what it is doing step by step (please see "Disclaimer" section).


### **1) Getting the programs and requirements**
The fastest and more clever way of getting the GUI and all the source codes is cloning this repository (you need 'git' installed, of course!).
Further information on how to install git can be found at: http://git-scm.com/book/en/Getting-Started-Installing-Git . An example of cloning command using command line is: 

    % git clone --recursive https://github.com/nicolazzie/SNPchimpRepo

The GUI was tested on Windows10 and Mac computers (64bits). Running the GUI has no requirements (just decompress and double click on the executable).
Source codes were fully tested on Linux/Unix/Mac. To run these programs you need Python (2.6+, although 2.7+ or latest is highly recommended for better performances) installed on your computer. 


### ** 2) >> BETA >> SNPConvert v1.0
SNPConvert is a all-in-one user-friendly GUI for Windows and Mac 64bit users. 
Linux users are required to use the source codes from command line (See section 3). SNPConvert is a simple GUI built from three programs you'll find in the "source_codes" folders. In fact, SNPConvert is able to convert any Illumina SNP-array raw format (ROW and MATRIX formats) to PLINK (PED & MAP), modify the allele coding of the file and the map information for any PLINK file (using SNPchimp output files). This GUI was built using PyQT project (full code provided). SNPConvert has 3 functionallities:
  - Illumina ROW format: this option converts formats from Illumina ROW to PLINK (PED & MAP). It requires 2 input files: a "FinalReport" file in **ROW** format and a SNP map file (both provided by the genotyping lab). Please see the _ExampleData_ folder to see what a (fake) FinalReport in ROW format looks like. The user is then free of choosing the output allele coding, the population ID used (e.g. first column in PLINK PED file), and the output filename. The resulting file will be placed in the same folder of the input FinalReport file. A runtime log window will guide the user on the process and outcomes of the program.
  - Illumina MATRIX format: this option converts formats from Illumina MATRIX to PLINK (PED & MAP). It requires 2 input files: a "FinalReport" file in **MATRIX** format and a SNP map file (both provided by the genotyping lab). Please see the _ExampleData_ folder to see what a (fake) FinalReport in MATRIX format looks like. The user is then free of choosing the population ID used (e.g. first column in PLINK ped file) and the output filename. The resulting file will be placed in the same folder of the input FinalReport file. A runtime log window will guide the user on the process and outcomes of the program.
  - iConvert software: this option maintains PLINK format, but converts allele coding and map information (if required). It requires 3 input files: one PLINK file couple (e.g. PED & MAP) and one SNPchimp (http://bioinformatics.tecnoparco.org/SNPchimp) "Download" menu output file (including both IN and OUT allele codings). Please see the _ExampleData_ folder to see how all these files look like. iConvert handles all SNPchips of all species hosted in SNPchimp (both Illumina/Illumina-based and Affymetrix SNP chips). A runtime log window will guide the user on the process and outcomes of the program.

#### How to run:
Once downloaded, unzip the executable and simply run by double-clicking on it. Note that since these are app/exe files, security warnings might pop up.
**NOTE TO MAC users**: you might need to temporarily allow third party apps to run ( System preferences --> Security & Privacy --> General --> Set "Allow apps downloaded from:" to Anywhere. Once the app is run the first time, this security feature can be restored to its original value.

#### Temporary beta-disclaimer
Although it still has to be improved from the graphical point of view, this BETA version is released as a preview to facilitate usage of these tools for non-linux/mac users. For feedback (HIGHLY appreciated) and bug report, please contact: ezequiel.nicolazzi@ptp.it


### **3) Source Codes**

Linux users should run the programs contained in this folder from command line, as no GUI is available for Linux users.

#### **PEDDA_ROW**
_pedda_row.py_ program converts Illumina ROW files into PLINK format. You need 2 input files: one Illumina FinalReport file (in ROW format) and one SNP_Map (original from Illumina). There is a specific parameter file to modify (peddar.param), the user is expected to modify according to the file(s) available: 
   - Variable **finrep** is the path to the FinalReport file (can be absolute or relative).
   - Variable **snpmap** is the path to the SNP map file, the one provided with any FinalReport (can be absolute or relative)
   - Variable **allele** is the allele strand you want to extract from the FinalReport file (options: "top","forward" or "ab")
   - Variable **SNPid_pos** is the position of the SNPids in the FinalReport file (usually they are in the first column. Accepted values: 1 to N)
   - Variable **INDid_pos** is the position of the individuals ids in the FinalReport file (usually they are in the second column. Accepted values: 1 to N)
   - Variable **outname** is the name of the output file (you'll find 2 files named as the name given + .ped and .map)
   - Variable **brdcode** is the name of the breed analysed. This info will be used on the "FID" field on the ped file (e.g. first column).
   - Variable **sep** is the separator of the input files. Options available: '\t' and  ','  and ' '

To run the program (from command line), just type:

    % python pedda_row.py

After a quick parameter and quality check, the program should tell you the names of the output files. No fancy options available. Sorry.
For any question, feedback or bug report, please contact: ezequiel.nicolazzi@ptp.it



#### **PEDDA_MATRIX**
_pedda_matrix.py_ program converts Illumina MATRIX files into PLINK format. You need 2 input files: one Illumina FinalReport file (in ROW format) and one SNP_Map (original from Illumina). There is a specific parameter file to modify (peddar.param), the user is expected to modify according to the file(s) available:
   - Variable **finrep** is the path to the FinalReport file (can be absolute or relative).
   - Variable **snpmap** is the path to the SNP map file, the one provided with any FinalReport (can be absolute or relative)
   - Variable **outname** is the name of the output file (you'll find 2 files named as the name given + .ped and .map)
   - Variable **brdcode** is the name of the breed analysed. This info will be used on the "FID" field on the ped file (e.g. first column).
   - Variable **sep** is the separator of the input files. Options available: '\t' and  ','  and ' '

To run the program (from command line), just type:

    % python pedda_matrix.py

After a quick parameter and quality check, the program should tell you the names of the output files. No fancy options available. Sorry.
For any question, feedback or bug report, please contact: ezequiel.nicolazzi@ptp.it




#### **iConvert.py**
_iConvert.py_ program converts genotype allele formats, using SNPchimp files and gentoypes in PLINK format. You need 4 input files: 2 PLINK files (e.g. ped & map), 1 SNPchimp output file (coming from the download menu with both input and output allele codings) and a parameter file. This program is able to handle conversion for all SNPchips of all species hosted in SNPchimp (both Illumina/Illumina-based and Affymetrix SNP chips).

To run this program (from command line), just type:

    % python iConvert.py

If you need help with PLINK and PLINK formats, please see: http://pngu.mgh.harvard.edu/~purcell/plink/
If you need help with SNPchiMp, please see: http://bioinformatics.tecnoparco.org/SNPchimp/index.php/faqs or contact me.
As previoulsy stated, _iConvert.py_ requires a parameter file, named _"convert.param"_. You can choose your own parameter filename by indicating the new parameter file name after the "-p" option. For example, if your parameter file is named _"parameter_file"_ you should run the program using the following:

    % python iConvert.py -p parameter_file

The parameter file is self explaining: DO NOT change the variable names and follow the instructions embedded in the file.

Genotypes with the converted allelic format will be written to a file named exactly as the input PED file + "\_updated"  (e.g. if input PED file is named _"input.ped"_, then the converted genotypes file will be named _"input\_updated.ped"_).
In addition, if required, this program allows you to update your map coordinates (chromosome and position) to a desired assembly. All you need to do is indicate "Y" in the "UPDATE\_map" variable (the program will use SNPchimp information and update the user map accordingly).

_NOTE_:
 - If you don't know what allele format your data is, you have two options: 1) do some tests. The program will stop if your genotypes are not in the right input allelic format (not an efficient choice -genotypes are read at the end of the program!- but the most simple) or; 2) find a SNP with different FORWARD-TOP allele coding (e.g. SNP 'Hapmap42400-BTA-102731' is T/C in FORWARD and A/G in TOP allele formats. If your genotypes at that SNP are T/C, your input format is FORWARD, and TOP if A/G).
 - If you __only__ wish to update your map information with the coordinates provided by SNPchiMp, you need to specify "NO" for both the _"IN\_format"_ and _"OUT\_format"_ variables in the parameter file

**_Self advertisement_: If you're using the Affymetrix technology, you might be interested in the AffyPipe software, that you can find at: https://github.com/nicolazzie/AffyPipe.git**


### **4) Disclaimer**
_This repository is a set of free tools that uses proprietary software that is publicly available online: you can redistribute and/or modify these programs, but at your own risk. The programs above are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details: http://www.gnu.org/licenses/.this
These programs are intended for research and have not a commercial intent, but they can be used freely by any organization. The only goal is to help people._
_For bug report, feedback and questions (PLEASE read the carefully this README file before sending your question) contact ezequiel [dot] nicolazzi [at] tecnoparco [dot] org._
