'''
Created on Nov 6, 2015

@author: Ezequiel Luis Nicolazzi
'''

import os,sys,time
from PyQt4 import QtGui
from SNPConvert_gui import Ui_MainWindow

class Main(QtGui.QMainWindow):    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ###############################################
        ###### TAB1 - Illumina MATRIX Format ##########
        ###############################################
        #Setting log screen as readonly
        self.ui.Log_wdg_tab1.setReadOnly(True)
        #Setting action of buttons opening to Open file
        self.inputFinRepFile_tab1='';self.inputSnpMapFile_tab1=''
        self.ui.FinRep_tab1.clicked.connect(self.FinRep_open_tab1)
        self.ui.SnpMap_tab1.clicked.connect(self.SnpMap_open_tab1)
        #Setting linedit read (breed code)
        self.BrdCode_tab1='UNKN_BRD'
        self.ui.BrdCode_tab1.setPlaceholderText(self.BrdCode_tab1)  #default (example) value
        self.ui.BrdCode_tab1.cursorPositionChanged.connect(self.BrdCodeChange_tab1)
        #Setting linedit read (output name)
        self.OutName_tab1='Output_name'
        self.ui.OutName_tab1.setPlaceholderText(self.OutName_tab1)  #default (example) name
        self.ui.OutName_tab1.cursorPositionChanged.connect(self.OutNameChange_tab1)    
        #Setting action of buttons RUN
        self.ui.ConvertFile_tab1.clicked.connect(self.ConvertFile_run_tab1)

        ###############################################
        ###### TAB2 - Illumina ROW Format ##########
        ###############################################
        #Setting log screen as readonly
        self.ui.Log_wdg_tab2.setReadOnly(True)
        #Setting action of buttons opening to Open file
        self.inputFinRepFile_tab2='';self.inputSnpMap_tab2=''
        self.ui.FinRep_tab2.clicked.connect(self.FinRep_open_tab2)
        self.ui.SnpMap_tab2.clicked.connect(self.SnpMap_open_tab2)
        #Setting the combo box
        self.Chosen_allele='Forward'
        self.items = ('Forward','Top','AB')
        self.ui.AlleleCod_box_tab2.addItems(self.items)
        self.ui.AlleleCod_box_tab2.currentIndexChanged.connect(self.OutAlleleCoding_tab2)
        #Setting linedit read (breed code)
        self.BrdCode_tab2='UNKN_BRD'
        self.ui.BrdCode_tab2.setPlaceholderText(self.BrdCode_tab2)  #default (example) value
        self.ui.BrdCode_tab2.cursorPositionChanged.connect(self.BrdCodeChange_tab2)
        #Setting linedit read (output name)
        self.OutName_tab2='Output_name'
        self.ui.OutName_tab2.setPlaceholderText(self.OutName_tab2)  #default (example) name
        self.ui.OutName_tab2.cursorPositionChanged.connect(self.OutNameChange_tab2)    
        #Setting action of buttons RUN
        self.ui.ConvertFile_tab2.clicked.connect(self.ConvertFile_run_tab2)


        ################################
        ###### TAB3 - iConvert #########
        ################################
        #Setting log screen as readonly
        self.ui.Log_wdg_tab3.setReadOnly(True)
        #Setting action of buttons opening to Open file
        self.inputPedFile_tab3='';self.inputMapFile_tab3='';self.inputSnpChimpFile_tab3=''
        self.ui.PedFile_tab3.clicked.connect(self.PedFile_open_tab3)
        self.ui.MapFile_tab3.clicked.connect(self.MapFile_open_tab3)
        self.ui.SnpChimp_tab3.clicked.connect(self.SnpChimp_open_tab3)
        #Setting the combo box
        self.items1=['ILMN_Forward','ILMN_Top','ILMN_AB','AFFY_Forward','AFFY_AB','NO_allele_conv']
        self.INChosen_allele='ILMN_Forward'
        self.ui.AlleleCodIn_box_tab3.addItems(self.items1)
        self.ui.AlleleCodIn_box_tab3.currentIndexChanged.connect(self.InAlleleCoding_tab3)

        self.items2=['ILMN_Top','ILMN_Forward','ILMN_AB','AFFY_Forward','AFFY_AB','NO_allele_conv']
        self.OUTChosen_allele='ILMN_Top'
        self.ui.AlleleCodOut_box_tab3.addItems(self.items2)
        self.ui.AlleleCodOut_box_tab3.currentIndexChanged.connect(self.OutAlleleCoding_tab3)
        
        #Setting radio buttons
        self.UpdateMap = True
        self.ui.YesRadioButton_tab3.clicked.connect(self.YesRadio_clicked)
        self.ui.NoRadioButton_tab3.clicked.connect(self.NoRadio_clicked)
                
        #Setting linedit read (output name)
        self.OutName_tab3='Output_name'
        self.ui.OutName_tab3.setPlaceholderText(self.OutName_tab3)  #default (example) name
        self.ui.OutName_tab3.cursorPositionChanged.connect(self.OutNameChange_tab3)    
        #Setting action of buttons RUN
        self.ui.ConvertFile_tab3.clicked.connect(self.ConvertFile_run_tab3)



#####################################################################################################################
###### DEFS FOR TAB1 - Illumina MATRIX Format 
#####################################################################################################################
    def FinRep_open_tab1(self):
        self.inputFinRepFile_tab1 = QtGui.QFileDialog.getOpenFileName(self,"Open FinalReport file", "Open FinalReport file", self.tr("TXT Files (*.txt);;CSV Files (*.csv);;All Files (*)"))
        if self.inputFinRepFile_tab1.isEmpty():self.ui.Log_wdg_tab1.append("<font color=red><b>WARNING:</b>FinalReport file not selected!</font>")
        else:self.ui.Log_wdg_tab1.append("FinalReport file selected <font color=green><b>OK</b></font>")
    
    def SnpMap_open_tab1(self):
        self.inputSnpMapFile_tab1 = QtGui.QFileDialog.getOpenFileName(self,"Open SNP map file", "Open SNP map file", self.tr("TXT Files (*.txt);;CSV Files (*.csv);;All Files (*)"))
        if self.inputSnpMapFile_tab1.isEmpty():self.ui.Log_wdg_tab1.append("<font color=red><b>WARNING:</b>SNP map file not selected!</font>")
        else:self.ui.Log_wdg_tab1.append("SNP map file selected <font color=green><b>OK</b></font>")
        
    def BrdCodeChange_tab1(self):
        self.BrdCode_tab1 = self.ui.BrdCode_tab1.text()

    def OutNameChange_tab1(self):
        self.OutName_tab1 = self.ui.OutName_tab1.text()

    def ConvertFile_run_tab1(self):
        ### Check that parameters are not void and replace values when possible (if not return an error message!)
        self.ui.Log_wdg_tab1.clear()
        if not self.inputFinRepFile_tab1 or self.inputFinRepFile_tab1.isEmpty():return self.ui.Log_wdg_tab1.append("<font color=red><b>ERROR: Please select a FinalReport file!</b></font>")
        if not self.inputSnpMapFile_tab1 or self.inputSnpMapFile_tab1.isEmpty():return self.ui.Log_wdg_tab1.append("<font color=red><b>ERROR: Please select a SNP map file!</b></font>")
        if not self.BrdCode_tab1:self.BrdCode_tab1 = 'UNKN_BRD'
        if not self.OutName_tab1:self.OutName_tab1 = 'Output_name'
        ### Print the options used
        self.ui.Log_wdg_tab1.append("<b><i>PEDDA MATRIX software - ILMN Matrix --> PLINK</i></b>")
        self.ui.Log_wdg_tab1.append("<i>Conversion and GUI coded by E.L.Nicolazzi (PTP)</i><br>")
        self.ui.Log_wdg_tab1.append("<b>PARAMETERS USED</i></b>")
        self.ui.Log_wdg_tab1.append(time.strftime("- Analysis run on %d/%m/%y at %H:%M:%S", time.localtime()))
        self.ui.Log_wdg_tab1.append(" - FinalReport: <b>%s</b>" % self.inputFinRepFile_tab1)
        self.ui.Log_wdg_tab1.append(" - SNP map: <b>%s</b>" % self.inputSnpMapFile_tab1)
        self.ui.Log_wdg_tab1.append(" - Pop code: <b>%s</b>" % self.BrdCode_tab1)
        self.ui.Log_wdg_tab1.append(" - Output name: <b>%s</b><br>" % self.OutName_tab1)
        
        ### Start processing the Map file first
        self.ui.Log_wdg_tab1.append("<b>A) Processing SnpMap file</b>")
        conv={};chroms={}
        for a in open(self.inputSnpMapFile_tab1):
            if 'chromosome' in a.lower():continue  #.lower is used to avoid problems with capital letters
            # Automatic identifier of the separator (at least 4 fields should be enough)
            try: 
                if len(a.strip().split(','))>4:   
                    line=a.strip().split(',')[:4]
                    nn,snpid,cro,pos=line
                elif len(a.strip().split('\t'))>4:
                    line=a.strip().split('\t')[:4]
                    nn,snpid,cro,pos=line
                else:
                    line=a.strip().split()[:4]
                    nn,snpid,cro,pos=line
            except ValueError:return self.ui.Log_wdg_tab1.append("<font color=red><b>ERROR: Bad/Corrupt SNP map file! Please check the file!</b></font>")
            conv[snpid]=(cro,pos)   #This dictionary keeps map info related to the SNP name
            chroms[cro]=0           #This dictionary is useful only to inform the user
        self.ui.Log_wdg_tab1.append("====> Total number of SNPs processed: <b>%s</b>" % len(conv))    
        self.ui.Log_wdg_tab1.append("====> Total number of chromosomes found: <b>%s</b>" % len(chroms))
        self.ui.Log_wdg_tab1.append("====> List of chromosomes found: <b>%s</b><br>" % ','.join(sorted(chroms.keys())))
        
        #Adapt slashes to unix/mac or Windows
        direct_name=os.path.abspath(os.path.dirname(str(self.inputFinRepFile_tab1)))
        if '/' in direct_name:slsh='/'
        else:slsh='\\'
        #Rebuild the (full) path of the original inputFinRepFile_tab1 - for compatibility with Windows
        #Open the output files
        outnam = direct_name+slsh+self.OutName_tab1
        outgen = open(outnam+'.ped','w')
        outmap = open(outnam+'.map','w')
        
        ### Start processing the genotypes
        self.ui.Log_wdg_tab1.append("<b>B) Processing FinalReport file</b>")
        readfrom=False
        genos=[];anims=[];n=0
        for en,a in enumerate(open(self.inputFinRepFile_tab1)):
            if '[data]' in a.lower():  #.lower is used to avoid problems with capital letters
                readfrom=True
                continue
            if not readfrom:continue   # Skip the header of the illumina file
            n+=1 # Start counting SNPs
            # Automatic identifier of the file separator
            if len(a.strip().split(','))>=2:
                line=a.strip().split(',');sep=','
            elif len(a.strip().split('\t'))>=2:
                line=a.strip().split('\t');sep='\t'
            else:
                line=a.strip().split();sep=' '
            # This is the first line containing the IDs of individuals
            if n==1: 
                for x in range(len(line)):
                    if x==0:continue
                    anims.append(line[x]) # keep trace of individual IDs
                    genos.append([])      # create a list n.individuals long 
                continue              # Jump to the genotypes
            #If it is a , or \t separator, do it easy, otherise 
            snp,geno=a.strip().split(sep,1)
            geno.strip()
            #Write the Map file as soon as it is read (to maintain the order)
            try:outmap.write('%s %s 0 %s\n' % (conv[snp][0],snp,conv[snp][1]))
            except:return self.ui.Log_wdg_tab1.append("<font color=red><b>ERROR: Map file writing failed at row"+str(en+1)+". Missing snp in Map?? </b></font>")
            #read the genotype line as long string separated by...
            if sep==',' or sep=='\t':geno=geno.replace('-','0').strip().split(sep)
            else:geno=geno.replace('-','0').strip().split()
            # Keep genos in memory (in order)
            for x in range(len(geno)):genos[x].append(geno[x])
        #check if reading of the file went ok.    
        if not n:return self.ui.Log_wdg_tab1.append("<font color=red><b>ERROR: Bad/Corrupt FinalReport file! Please check the file!</b></font>")    
        self.ui.Log_wdg_tab1.append("====> Total number of INDIVIDUALS processed: <b>%s</b><br>" % len(geno))    
        self.ui.Log_wdg_tab1.append("<b>C) Writing output files</b>")
        
        for x in range(len(anims)):
            gty=[genos[x][i][0]+' '+genos[x][i][1] for i in range(len(genos[x]))]
            outgen.write('%s %s 0 0 0 0 %s\n' % (self.BrdCode_tab1,anims[x],' '.join(gty)))
        self.ui.Log_wdg_tab1.append("<br><br>====> Bazinga! <font color=green><b><i>Conversion run OK!</i></b></font>")
        self.ui.Log_wdg_tab1.append("<font color=blue>PED file available: <b>"+outnam+'.ped</b></font>')
        self.ui.Log_wdg_tab1.append("<font color=blue>MAP file available: <b>"+outnam+'.map</b></font>')



#####################################################################################################################
###### DEFS FOR TAB2 - Illumina ROW Format 
#####################################################################################################################

    def FinRep_open_tab2(self):
        self.inputFinRepFile_tab2 = QtGui.QFileDialog.getOpenFileName(self,"Open FinalReport file", "Open FinalReport file", self.tr("TXT Files (*.txt);;CSV Files (*.csv);;All Files (*)"))
        if self.inputFinRepFile_tab2.isEmpty():self.ui.Log_wdg_tab2.append("<font color=red><b>WARNING:</b>FinalReport file not selected!</font>")
        else:self.ui.Log_wdg_tab2.append("FinalReport file selected <font color=green><b>OK</b></font>")
    
    def SnpMap_open_tab2(self):
        self.inputSnpMapFile_tab2 = QtGui.QFileDialog.getOpenFileName(self,"Open SNP map file", "Open SNP map file", self.tr("TXT Files (*.txt);;CSV Files (*.csv);;All Files (*)"))
        if self.inputSnpMapFile_tab2.isEmpty():self.ui.Log_wdg_tab2.append("<font color=red><b>WARNING:</b>SNP map file not selected!</font>")
        else:self.ui.Log_wdg_tab2.append("SNP map file selected <font color=green><b>OK</b></font>")
    
    def OutAlleleCoding_tab2(self,indice):
        self.Chosen_allele = self.items[indice]
        
    def BrdCodeChange_tab2(self):
        self.BrdCode_tab2 = self.ui.BrdCode_tab2.text()

    def OutNameChange_tab2(self):
        self.OutName_tab2 = self.ui.OutName_tab2.text()

    def ConvertFile_run_tab2(self):
        ### Check that parameters are not void and replace values when possible (if not return an error message!)
        self.ui.Log_wdg_tab2.clear()
        if not self.inputFinRepFile_tab2 or self.inputFinRepFile_tab2.isEmpty():return self.ui.Log_wdg_tab2.append("<font color=red><b>ERROR: Please select a FinalReport file!</b></font>")
        if not self.inputSnpMapFile_tab2 or self.inputSnpMapFile_tab2.isEmpty():return self.ui.Log_wdg_tab2.append("<font color=red><b>ERROR: Please select a SNP map file!</b></font>")
        if not self.BrdCode_tab2:self.BrdCode_tab2 = 'UNKN_BRD'
        if not self.OutName_tab2:self.OutName_tab2 = 'Output_name'
        ### Print the options used
        self.ui.Log_wdg_tab2.append("<b><i>Pedda ROW software - ILMN ROW --> PLINK</i></b>")
        self.ui.Log_wdg_tab2.append("<i>Conversion and GUI coded by E.L.Nicolazzi (PTP)</i><br>")
        self.ui.Log_wdg_tab2.append("<b>PARAMETERS USED</i></b>")
        self.ui.Log_wdg_tab2.append(time.strftime("- Analysis run on %d/%m/%y at %H:%M:%S", time.localtime()))
        self.ui.Log_wdg_tab2.append(" - FinalReport: <b>%s</b>" % self.inputFinRepFile_tab2)
        self.ui.Log_wdg_tab2.append(" - SNP map: <b>%s</b>" % self.inputSnpMapFile_tab2)
        self.ui.Log_wdg_tab2.append(" - Output allele coding: <b>%s</b>" % self.Chosen_allele)        
        self.ui.Log_wdg_tab2.append(" - Pop code: <b>%s</b>" % self.BrdCode_tab2)
        self.ui.Log_wdg_tab2.append(" - Output name: <b>%s</b><br>" % self.OutName_tab2)
        
        self.ui.Log_wdg_tab2.append("<b>A) Processing SNP map file file</b>")
        conv={};sep=''
        for a in open(self.inputSnpMapFile_tab2):
            if 'Chromosome' in a:continue
            if len(a.strip().split(','))>=3:sep=',';
            elif len(a.strip().split('\t'))>=3:sep='\t'
            else:sep=''
            if sep:
                nn,snpid,cro,pos,rest=a.strip().split(sep,4)
            else:
                line=a.strip().split()
                nn,snpid,cro,pos=line[:4]
            conv[snpid]=(cro,pos)
        if len(conv)==0:return self.ui.Log_wdg_tab2.append("<font color=red><b>ERROR:</b> The SNP map files seems to be empty!</font><br>")
        self.ui.Log_wdg_tab2.append("====> Total number of SNPs processed: "+str(len(conv))+'<br>')
        
        ### Start processing the Map file first
        self.ui.Log_wdg_tab2.append("<b>B) Processing FinRep file</b>")           
        direct_name=os.path.abspath(os.path.dirname(str(self.inputFinRepFile_tab2)))
        if '/' in direct_name:slsh='/'
        else:slsh='\\'
        #Rebuild the (full) path of the original inputFinRepFile_tab1 - for compatibility with Windows
        #Open the output files
        outnam = direct_name+slsh+self.OutName_tab2
        outgen = open(outnam+'.ped','w')
        outmap = open(outnam+'.map','w')
        readfrom=False
        SNPname=[]
        c=0;anim=-1;snp=0

        for en,a in enumerate(open(self.inputFinRepFile_tab2)):
            if 'allele1' in a.lower():
                readfrom=True
                if len(a.strip().split(','))>=3:
                    sep=',';
                    line=a.lower().strip().split(sep)
                elif len(a.strip().split('\t'))>=3:
                    sep='\t'
                    line=a.lower().strip().split(sep)
                else:   
                    sep=''
                    line=a.lower().strip().split()
                ### Seraching for 'SNP name' header
                if not 'snp name' in line and not 'snpname' in line:
                    return self.ui.Log_wdg_tab2.append("<font color=red><b>ERROR:</b> The header does not contain the required information: 'SNP name' or 'SNPname' (not case sensitive)<\font><br>")
                else:
                    try:
                        SNPid_pos = line.index('snp name')
                    except:
                        SNPid_pos = line.index('snpname')
                ### Searching for 'Sample ID' header
                if not 'sample id' in line and not 'sampleid' in line:
                    return self.ui.Log_wdg_tab2.append("<font color=red><b>ERROR:</b> The header does not contain the required information: 'Sample ID' or 'SampleId' (not case sensitive)<\font><br>")
                else:
                    try:
                        INDid_pos = line.index('sample id')
                    except:
                        INDid_pos = line.index('sampleid')
                ### Searching for the required allele coding format.
                if not 'allele1 - '+self.Chosen_allele.lower() in line:
                    self.ui.Log_wdg_tab2.append("<font color=red><b>ERROR:</b> The header does not contain the chosen allele coding: Allele1 - "+self.Chosen_allele+'<\font><br>')
                    self.ui.Log_wdg_tab2.append("<font color=red> Header read:'<b><i>"+a+"'</i></b></font><br>")
                    self.ui.Log_wdg_tab2.append("<font color=red> Possible causes: </font>")
                    self.ui.Log_wdg_tab2.append("<font color=red> - The requested allele format is not present in your header <i>[SOLUTION: choose an allele format that is available]</i></font>")
                    self.ui.Log_wdg_tab2.append("<font color=red> - The header in the Illumina header has changed (no 'Allele1 - "+self.Chosen_allele+"' field is present - not case sensitive) <i>[SOLUTION: Contact ezequiel.nicolazzi@ptp.it, or if you know how to code in python, change the if string related to this]</i></font>")
                    self.ui.Log_wdg_tab2.append("<font color=red> - The FinalReport file separator is not right <i>[SOLUTION: Contact ezequiel.nicolazzi@ptp.it, or if you know how to code in python, change the if string related to this]</i></font>")
                    self.ui.Log_wdg_tab2.append("<font color=red> - The FinalReport file is in Matrix format <i>[SOLUTION: Use the 'Illumina MATRIX format' tag instead]</i></font>")
                    self.ui.Log_wdg_tab2.append("<font color=red> - Other <i>[SOLUTION: Contact ezequiel.nicolazzi@ptp.it ... send me the header (e.g. first 10 rows) of the FinalReport file you're using]</i></font>")
                    return
                else:
                    alle_pos1=line.index('allele1 - '+self.Chosen_allele.lower())
                    alle_pos2=alle_pos1+1
                    continue
                           
            if not readfrom:continue
            if sep:line=a.strip().split(sep)
            else: line=a.strip().split()
            if alle_pos2 > len(line):
                return self.ui.Log_wdg_tab2.append("<font color=red><b>ERROR:</b> Probable error in the separator.. Position of Allele2 found in "+str(alle_pos2)+", but length of line in row "+str(en)+" is "+str(len(line))+" !!</font><br>"+\
                                                   "<font color=red>Please check your choice of separator is correct and that you don't have strange fields in you FinalReport file!</font>")
            snp_name=line[SNPid_pos]
            if not conv.has_key(snp_name):
                return self.ui.Log_wdg_tab2.append("<font color=red><b>ERROR:</b> SNP name: "+snp_name+" in FinalReport file not found in SNP map file!</font><br>")
            id_sample=line[INDid_pos]
            alle1=line[alle_pos1]
            alle2=line[alle_pos2]
            if alle1=='-':alle1='0'
            if alle2=='-':alle2='0'
            c+=1
            if c==1:
                snp=-1
                geno=[]
                name=[]
                name.append(id_sample)
            if id_sample in name:
                geno.append(alle1+' '+alle2)
                snp+=1
                if len(name)==1:
                    outmap.write('%s %s 0 %s\n' % (conv[snp_name][0],snp_name,conv[snp_name][1]))
                    SNPname.append(snp_name)
                else:
                    if snp_name!=SNPname[snp]:
                        return self.ui.Log_wdg_tab2.append("The order of the SNPs in the different individuals is consistent. Check "+snp_name+" and "+SNPname[snp])
            else:
                snp=0
                anim+=1
                outgen.write('%s %s 0 0 0 -9 %s\n' % (self.BrdCode_tab2,name[anim],' '.join(geno)))
                self.ui.Log_wdg_tab2.append('Finshed processing individual: '+name[anim]+' - Total SNPs: '+str(len(geno)))
                geno=[]
                geno.append(alle1+' '+alle2)
                name.append(id_sample)

        outgen.write('%s %s 0 0 0 -9 %s\n' % (self.BrdCode_tab2,id_sample,' '.join(geno)))
        anim+=2
        self.ui.Log_wdg_tab2.append('Finshed processing individual: '+id_sample+' - Total SNPs: '+str(len(geno)))
        self.ui.Log_wdg_tab2.append('<br><b>====> Total number of INDIVIDUALS processed: '+str(anim)+'</b><br><br>')    
        self.ui.Log_wdg_tab2.append("====> Bazinga! <font color=green><b><i>Conversion run OK!</i></b></font>")
        self.ui.Log_wdg_tab2.append("<font color=blue>PED file available: <b>"+outnam+'.ped</b></font>')
        self.ui.Log_wdg_tab2.append("<font color=blue>MAP file available: <b>"+outnam+'.map</b></font>')  

    def PedFile_open_tab3(self):
        self.inputPedFile_tab3 = QtGui.QFileDialog.getOpenFileName(self,"Open PED file", "Open PED file", self.tr("PED files (*.ped);;All files (*)"))
        if self.inputPedFile_tab3.isEmpty():self.ui.Log_wdg_tab3.append("<font color=red><b>WARNING:</b>PED file not selected!</font>")
        else:self.ui.Log_wdg_tab3.append("PED file selected <font color=green><b>OK</b></font>")
    
    def MapFile_open_tab3(self):
        self.inputMapFile_tab3 = QtGui.QFileDialog.getOpenFileName(self,"Open MAP file", "Open MAP file", self.tr("MAP files (*.map);;All files (*)"))
        if self.inputMapFile_tab3.isEmpty():self.ui.Log_wdg_tab3.append("<font color=red><b>WARNING:</b>MAP file not selected!</font>")
        else:self.ui.Log_wdg_tab3.append("MAP file selected <font color=green><b>OK</b></font>")
        
    def SnpChimp_open_tab3(self):
        self.inputSnpChimpFile_tab3 = QtGui.QFileDialog.getOpenFileName(self,"Open SNPchimp_v3 file", "Open SNPchimp_v3 file", self.tr("CSV files (*.csv);; TSV files (*.tsv);; All Files (*)"))
        if self.inputSnpChimpFile_tab3.isEmpty():self.ui.Log_wdg_tab3.append("<font color=red><b>WARNING:</b>SNPchimp_v3 file not selected!</font>")
        else:self.ui.Log_wdg_tab3.append("SNPchimp_v3 file selected <font color=green><b>OK</b></font>")
    
    def InAlleleCoding_tab3(self,indice):
        self.INChosen_allele = self.items1[indice]

    def YesRadio_clicked(self):
            self.UpdateMap = True
            
    def NoRadio_clicked(self):
            self.UpdateMap = False
                            
    def OutAlleleCoding_tab3(self,indice):
        self.OUTChosen_allele = self.items2[indice]
            
    def OutNameChange_tab3(self):
        self.OutName_tab3 = self.ui.OutName_tab3.text()

    def ConvertFile_run_tab3(self):
        #Clear screen
        self.ui.Log_wdg_tab3.clear()
        #Only update map info (do not ask for ped file                  
        if self.INChosen_allele == 'NO_allele_conv' and self.OUTChosen_allele == 'NO_allele_conv': onlymap=True 
        else:onlymap=False
        if not onlymap:
            if not self.inputPedFile_tab3 or self.inputPedFile_tab3.isEmpty():return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Please select a PED file!</b></font>")
        if not self.inputMapFile_tab3 or self.inputMapFile_tab3.isEmpty():return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Please select a MAP file!</b></font>")
        if not self.inputSnpChimpFile_tab3 or self.inputSnpChimpFile_tab3.isEmpty():return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Please select a SNPchimp_v3 file! (visit http://bioinformatics.tecnoparco.org/SNPchimp/)</b></font>")
        if not str(self.inputSnpChimpFile_tab3[-3:]).lower() in ['csv','tsv']:return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Original SNPchimp v.3 files are csv (comma separated) or tsv (tab separated).</b></font>")
        if not self.OutName_tab3:self.OutName_tab3 = 'Output_name'
        if not onlymap:
            if self.INChosen_allele==self.OUTChosen_allele:return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Input and Output allele coding MUST be different!</b></font>")
        if self.INChosen_allele[:4]=='ILMN' and self.OUTChosen_allele[:4]!='ILMN':return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Input and Output allele coding MUST be compatible (ILMN-ILMN, AFFY-AFFY or NO-NO)!</b></font>")
        if self.INChosen_allele[:4]=='AFFY' and self.OUTChosen_allele[:4]!='AFFY':return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Input and Output allele coding MUST be compatible (ILMN-ILMN, AFFY-AFFY or NO-NO)!</b></font>")
        if self.INChosen_allele[:2]=='NO' and self.OUTChosen_allele[:2]!='NO':return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Input and Output allele coding MUST be compatible (ILMN-ILMN, AFFY-AFFY or NO-NO)!</b></font>")
        
        ### Print the options used
        answer={True:'Yes',False:'No'}
        self.ui.Log_wdg_tab3.append("<b><i>iConvert software - Allele conversion and map update <i></b>")
        self.ui.Log_wdg_tab3.append("<i>Software and GUI coded by E.L.Nicolazzi (PTP)</i><br>")
        self.ui.Log_wdg_tab3.append("<b>PARAMETERS USED</i></b>")
        self.ui.Log_wdg_tab3.append(time.strftime("- Analysis run on %d/%m/%y at %H:%M:%S", time.localtime()))
        self.ui.Log_wdg_tab3.append(" - PLINK fmt - Ped file: <b>%s</b>" % self.inputPedFile_tab3)
        self.ui.Log_wdg_tab3.append(" - PLINK fmt - Map file: <b>%s</b>" % self.inputMapFile_tab3)
        self.ui.Log_wdg_tab3.append(" - SNPchimp v.3 file   : <b>%s</b>" % self.inputSnpChimpFile_tab3)
        self.ui.Log_wdg_tab3.append(" - Input allele coding : <b>%s</b><br>" % self.INChosen_allele)
        self.ui.Log_wdg_tab3.append(" - Map update requested: <b>%s</b><br>" % answer[self.UpdateMap])
        self.ui.Log_wdg_tab3.append(" - Output allele coding: <b>%s</b>" % self.OUTChosen_allele)        
        self.ui.Log_wdg_tab3.append(" - Output name         : <b>%s</b><br>" % self.OutName_tab3)
   
        self.ui.Log_wdg_tab3.append("<br><b>A) Processing SNPchimp v.3 file file</b><br>")
        othinfo = []
        chips = {};SNPdata = {}
        formats = [0,0]
        SEP = ','
        if self.UpdateMap: mapupd = {}

        readfrom=False
        for en,line in enumerate(open(self.inputSnpChimpFile_tab3)):
            if str(self.inputSnpChimpFile_tab3[-3:]).lower()=='csv':SEP=','
            elif str(self.inputSnpChimpFile_tab3[-3:]).lower()=='tsv':SEP='\t'
            if 'chip_name' in line.lower():
                readfrom=True
                hlin=line.lower().strip().split(SEP)
                ####### FILE header and stuff checks
                #Check SEPARATOR is right
                if len(hlin)<3:
                    return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: SNPchimp v.3 separator is not comma or tab, as assumed by the extension name - Download original SNPchimp v.3 files and try again</b></font>")
                # Check if user choices are coherent with the infor in SNPchimp v.3
                if self.INChosen_allele=='ILMN_Top' or self.OUTChosen_allele=='ILMN_Top':
                    try: 
                        head_finder=hlin.index('alleles_a_b_top')
                        if self.INChosen_allele=='ILMN_Top':formats[0]=head_finder
                        else:formats[1]=head_finder
                    except ValueError:return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: SNPchimp v.3 file does not contain the required Illumina TOP allele coding</b></font>")                  
                if self.INChosen_allele=='ILMN_Forward' or self.OUTChosen_allele=='ILMN_Forward':
                    try: 
                        head_finder=hlin.index('alleles_a_b_forward')
                        if self.INChosen_allele=='ILMN_Forward':formats[0]=head_finder
                        else:formats[1]=head_finder
                    except ValueError:return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: SNPchimp v.3 file does not contain the required Illumina FORWARD allele coding</b></font>")                  
                if self.INChosen_allele=='AFFY_Forward' or self.OUTChosen_allele=='AFFY_Forward':
                    try: 
                        head_finder=hlin.index('alleles_a_b_affymetrix')
                        if self.INChosen_allele=='AFFY_Forward':formats[0]=head_finder
                        else:formats[1]=head_finder
                    except ValueError:return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: SNPchimp v.3 file does not contain the required Affymetrix FORWARD allele coding</b></font>")
                # Check accessory information is there, otherwise stop
                try:
                    othinfo.append(hlin.index('chip_name'))
                    othinfo.append(hlin.index('chromosome'))
                    othinfo.append(hlin.index('position'))
                    othinfo.append(hlin.index('snp_name'))
                    continue
                except ValueError:
                    return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR:'chip name', 'chromosome', 'position' and 'SNP_name' header variables not found. These are always present in SNPchiMp downloaded files!</b></font>")
            if not readfrom:continue
            lista = line.strip().split(SEP)
            # Keep only useful info (skip other not wanted chips)
            if not chips.has_key(lista[othinfo[0]]): chips[lista[othinfo[0]]] = 0
            if 'AFFY' in self.INChosen_allele:
                if not 'Bov_AffyHD' in lista[0]:continue
            if 'ILMN' in self.INChosen_allele:
                if 'Bov_AffyHD' in lista[0]:continue
            # Keep SNPchimp map information only if required by the user.
            if self.UpdateMap: mapupd[lista[othinfo[3]]] = [lista[othinfo[1]],lista[othinfo[2]]]
            # If INPUT allele format is AB, use AB as IN and custom allele format as OUT
            if self.INChosen_allele == 'ILMN_AB' or self.INChosen_allele == 'AFFY_AB':
                SNPdata[lista[othinfo[3]]] = {'A':lista[formats[1]][0], 'B':lista[formats[1]][2]}
            # If OUTPUT allele format is AB, use AB as OUT and custom allele in format as IN 
            elif self.OUTChosen_allele == 'ILMN_AB' or self.OUTChosen_allele == 'AFFY_AB':
                SNPdata[lista[othinfo[3]]] = {lista[formats[0]][0]:'A', lista[formats[0]][2]:'B'}
            else:
                SNPdata[lista[othinfo[3]]] = {lista[formats[0]][0]:lista[formats[1]][0],
                                          lista[formats[0]][2]:lista[formats[1]][2]}

        if len(SNPdata) == 0:
            return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Problem reading SNPchimp file! Probably conversion info not available or headers are incorrect</b></font>")
        if len(chips)>1: 
            self.ui.Log_wdg_tab3.append("<font color=orange><b>WARNING: More than 1 chip in SNPchimp file. This might result in incorrect allele conversion!</b></font>")
        self.ui.Log_wdg_tab3.append("- Rows read in SNP chimp file :<b>%s</b>" % str(en+1))
        self.ui.Log_wdg_tab3.append("- SNPs with allele conversion information available :<b>%s</b>" % str(len(SNPdata)))

        ###### Process Map file
        self.ui.Log_wdg_tab3.append("<br><b>B) Processing PLINK MAP file and converting map information (if required)</b><br>")
        maporder = [];convert = []
        tab = False
        # Create new file if new remapping is needed
        if self.UpdateMap: 
            #Adapt slashes to unix/mac or Windows
            direct_name=os.path.abspath(os.path.dirname(str(self.inputMapFile_tab3)))
            if '/' in direct_name:slsh='/'
            else:slsh='\\'
            #Rebuild the (full) path of the original inputMapFile_tab3 - for compatibility with Windows
            outnammap = direct_name+slsh+self.OutName_tab3+'.map'
            remap=open(outnammap,'w')

        for enmap,line in enumerate(open(self.inputMapFile_tab3)):
            #Check for tab or blank space spearator (only these 2 are accepted here)       
            if enmap == 0: 
                test = line.strip().split('\t')
            if len(test) == 4:   # Warning: this only accepts "normal" MAP files (no --map3 or other options are allowed) 
                linea = line.strip().split('\t')
                tab = True
            else: linea = line.strip().split()
            snp = linea[1]
            maporder.append(snp)
            if not SNPdata.has_key(linea[1]):return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: SNP: "+ snp +" not found in SNPchimp file. Probable causes: you downloaded the wrong SNPchip or modified SNP names </b></font>") 
            else:convert.append(SNPdata[linea[1]])
            if self.UpdateMap:remap.write('%s %s %s %s\n' % (mapupd[snp][0],snp,linea[2],mapupd[snp][1]))
        self.ui.Log_wdg_tab3.append("- Rows read in PLINK MAP file (number of SNPs) : <b>%s</b>" % str(enmap+1))
        if self.UpdateMap: self.ui.Log_wdg_tab3.append("<font color=blue>- MAP file updated: <b>%s</b></font>" % outnammap)

        # Process PED file (if required)
        if not onlymap: 
            self.ui.Log_wdg_tab3.append("<br><b>C) Processing PLINK PED file and converting allele format</b><br>") 
            tab = False
            #Get full path of PED file
            #Adapt slashes to unix/mac or Windows
            direct_name=os.path.abspath(os.path.dirname(str(self.inputMapFile_tab3)))
            if '/' in direct_name:slsh='/'
            else:slsh='\\'
            #Rebuild the (full) path of the original inputMapFile_tab3 - for compatibility with Windows
            outnamped = direct_name+slsh+self.OutName_tab3+'.ped'

            reped=open(outnamped,'w')
            #Read ped file
            for enped,line in enumerate(open(self.inputPedFile_tab3)):
                if enped == 0:
                    test = line.strip().split('\t')
                    if len(test) == (6 + (enmap + 1) * 2): tab = True
                if tab: pedline = line.strip().split('\t')
                else: pedline = line.strip().split()
                if ((enmap+1)*2+6) != len(pedline):
                    return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Number of SNPs in PLINK MAP (" +str(enmap+1)+") should result in "+str((enmap+1)*2+6)+" columns PLINK PED but found "+str(len(pedline))+"<br>Check your .ped and .map files. Usually the problem is in the first line(s)...</font><br>")
                genotypes = [pedline[6 + x] + pedline[7 + x] for x in range(0, ((enmap+1)*2)-1, 2)]
                seq = -1
                genout = []
                nfailed = 0
                for alle in genotypes:
                    seq += 1
                    alle1 = alle[0];alle2 = alle[1]
                    if alle1 == '0' or alle1 =='?':
                        genout.append('0');genout.append('0')
                        continue
                    try:
                        genout.append(convert[seq][alle1])
                        genout.append(convert[seq][alle2])
                    except KeyError:
                        nfailed += 1
                if nfailed:
                    return self.ui.Log_wdg_tab3.append("<font color=red><b>ERROR: Individual " + pedline[1] + " failed conversion for " + str(nfailed) + \
                                                       " SNPs. Probably their IN format is not as specified (or you specified a wrong missing value)</font>")
                reped.write('%s %s\n' % (' '.join(pedline[:6]),' '.join(genout)))
            self.ui.Log_wdg_tab3.append("- Rows read in PLINK PED file (number of animals) : <b>%s</b>" % str(enped + 1))
            self.ui.Log_wdg_tab3.append("<font color=blue>- PED file updated: <b>%s</b></font><br><br>" % outnamped)
        self.ui.Log_wdg_tab3.append('<br><font color=green><b> PROGRAM ENDS OK! </b></font>')

        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    window.raise_()
    sys.exit(app.exec_())
