SNPchimpRepo: _a suite of useful programs for SNPchiMp users_
===========
*ref: E.L. Nicolazzi (Fondazione Parco Tecnologico Padano) - Via Einstein, Loc. Cascina Codazza (26900) Lodi (Italy). Email: ezequiel [dot] nicolazzi [at] tecnoparco [dot] org*


The goal of this suite of programs is to help users doing some routine work without having to do any programming. 
I'll put all programs in this directory, source codes included, and will update this readme file accordingly.


### **1) Getting the programs and requirements**
The fastest and more clever way of getting all the programs is cloning this repository (you need 'git' installed, of course!).
Further information on how to install git can be found at: http://git-scm.com/book/en/Getting-Started-Installing-Git . An example of cloning command using command line is: 

    % git clone --recursive https://github.com/nicolazzie/SNPchimpRepo

This pipeline is mainly for linux/unix/mac users, but it should run on windows OSs too. Please note that I won't be able to give any support or troubleshooting for Windows users.
To run these programs you should only have Python (2.x) already installed on your computer, although 2.7 is adviced (Mac users have by default Python2.6. Although runtime will be slower, it should work anyway). 

### **2) Programs**

#### **iConvert.py**
_iConvert.py_ program converts genotype allele formats, using SNPchimp files and gentoypes in PLINK format. You need 3 input files: 2 PLINK (e.g. ped & map) files and 1 SNPchimp output file (coming from the download menu), containing the allele conversion information for the SNP chip you need to convert.
This program is able to handle conversion for all SNPchips of all species hosted in SNPchimp (both Illumina/Illumina-based and Affymetrix SNP chips).

To run this program (from command line), just type:

    % python iConvert.py

_iConvert.py_ program requires a parameter file, named "convert.param". You can choose your own parameter file name by indicating the new parameter file name after the "-p" option. For example, if the new parameter file is named "parameter_file" you should run the program using the following:

    % python iConvert.py -p parameter_file

The parameter file is self explaining. Please DO NOT change the variable names and follow the instructions embedded in the file.
_TIP_: If you don't know what allele format your data is, you have two options: 1) do some tests. The program will stop if your genotypes are not in the right input allelic format (not efficient, since genotypes are read at the end of the program!) or; 2) find a SNP with different FORWARD-TOP allele coding (e.g. SNP 'Hapmap42400-BTA-102731' is T/C in FORWARD and A/G in TOP allele formats. If your genotypes at that SNP are T/C, your input format is FORWARD, and TOP if A/G).

Genotypes with the converted allelic format will be written to a file named exactly as the input PED file + "\_updated"  (e.g. if input PED file is named "input.ped", then the converted genotypes file will be named 'input\_updated.ped')
In addition, if required,this program allows you to update the coordinates (chromosome and position) of your SNPs to a desired assembly, while updating your allele format. Just indicate "Y" in the "UPDATE\_map" variable.
If you desire only to update your map information, you need to specify "NO" for both the "IN\_format" and "OUT\_format" variables.

_Self advertisement_: If you're using the Affymetrix technology, you might be interested in the AffyPipe software, that you can find at: https://github.com/nicolazzie/AffyPipe.git



### **Disclaimer**
This repository is a set of free tools that uses proprietary software that is publicly available online: you can redistribute and/or modify these programs, but at your own risk. The programs above are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details: http://www.gnu.org/licenses/.this
These programs are intended for research and have not a commercial intent, but they can be used freely by any organization. The only goal is to help people.
For bug report, feedback and questions (PLEASE read the carefully this README file before sending your question) contact ezequiel [dot] nicolazzi [at] tecnoparco [dot] org.
