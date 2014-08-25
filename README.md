SNPchimpRepo: _a suite of useful programs for SNPchiMp users_
===========
*ref: E.L. Nicolazzi (Fondazione Parco Tecnologico Padano) - Via Einstein, Loc. Cascina Codazza (26900) Lodi (Italy). Email: ezequiel [dot] nicolazzi [at] tecnoparco [dot] org*


The goal of this suite of programs is to help users doing some routine work without doing any actual programming. 
This directory includes source codes, so you're able to see what it is doing step by step (please see "Disclaimer" section).


### **1) Getting the programs and requirements**
The fastest and more clever way of getting all the programs is cloning this repository (you need 'git' installed, of course!).
Further information on how to install git can be found at: http://git-scm.com/book/en/Getting-Started-Installing-Git . An example of cloning command using command line is: 

    % git clone --recursive https://github.com/nicolazzie/SNPchimpRepo

These programs are fully tested on Linux/Unix/Mac, but they should run on Windows OSs too. Please note that no support or troubleshooting for Windows-specific issues will be provided.
To run these programs you need Python (2.x) installed on your computer. Python 2.7 is adviced (note that Mac users have Python 2.6 installed by defaul; runtime will be slower but it should do the work anyway!). 

### **2) Programs**

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



### **Disclaimer**
_This repository is a set of free tools that uses proprietary software that is publicly available online: you can redistribute and/or modify these programs, but at your own risk. The programs above are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details: http://www.gnu.org/licenses/.this
These programs are intended for research and have not a commercial intent, but they can be used freely by any organization. The only goal is to help people._
_For bug report, feedback and questions (PLEASE read the carefully this README file before sending your question) contact ezequiel [dot] nicolazzi [at] tecnoparco [dot] org._
