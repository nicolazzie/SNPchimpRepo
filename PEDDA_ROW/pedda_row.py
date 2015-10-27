import sys,os

''' This program converts Illumina row format into PLINK ped and map formats.
    It was NOT originally coded for release to the public, so coding and standards are not followed strictly.
    I release this following several requests from users. 
    NOTE: If you ask your Genotyping lab, they are able to give you an "official" PLINK file format for your gentoypes
          There is a specific plugin in GenomeStudio that does that!

    See ZANARDI PIPELINE to discover an easy solution to perform genomic analyses using the PLINK file formats!
    https://github.com/bioinformatics-ptp/Zanardi
    
    Coded originally by: Ezequiel L. Nicolazzi (Fondazione Parco Tecnologico Padano, Lodi, Italy)
    For bug report, comments and contributions: ezequiel.nicolazzi@ptp.it

    DISCLAIMER: See the usual GNU public disclaimer. Although I use this software quite on a regular basis, 
             this is released under NO WARRANTY AT ALL (use at your own risk!).
'''

### HEADER
print "#"*60
print "###                                                      ### "
print "###                  PEDDA software                      ### "
print "###      Converts Illumina row fmt into PLINK fmt        ### "
print "###                                                      ### "
print "###                              Coded by: E.L.Nicolazzi ### "
print "#"*60

### USEFUL DEFs
def bomb(message):
    print "ERROR: "+message
    sys.exit()

def check_file(value,name):
    try:os.path.exists(value)
    except:bomb("FinalReport file provided in parameter '"+name+"' was not found")

def check_strand(value):
    if not value in ['top','forward','ab']:bomb("Strand provided in parameter 'allele' ( "+allele+" ) not valid [options: 'top','forward','ab']")
        
def check_pos(value,name):
    try:
        int(value)
        if int(value)<=0:bomb("'"+name+"' parameter must be positive and greater than 0")
    except ValueError:bomb("'"+name+"' parameter provided is not a number")

def check_sep(value):
    if not value in ['\t',' ',',']:bomb("Separator provided in parameter 'sep' ( "+value+" ) not valid [options: ',',' ','\t']")

#### IMPORT parameter file
PARAMFILE_OPEN=open('peddar.param','r').readlines()
PARAMETERS=[ind.strip().replace("'","").replace('"','').replace(';',',') for ind in PARAMFILE_OPEN if not '#' in ind[0]]
PARAM=[]
for i in PARAMETERS:
    if not i: continue
    PARAM.append(i.strip().split('=')[1].strip())
if PARAM[-1]=='\\t':PARAM[-1]='\t'

if len(PARAM)!=8:bomb('Wrong number of parameters found in peddam.param. Please check it!')
else:finrep,snpmap,allele,SNPid_pos,INDid_pos,outname,brdcode,sep=PARAM

print "### Rough check of parameters"
### Run checks on the parameters (add-on for user release)
check_file(finrep,'finrep')
check_file(snpmap,'snpmap')
check_strand(allele)
check_pos(SNPid_pos,'SNPid_pos')
check_pos(INDid_pos,'INDid_pos')
check_sep(sep)
print "====> Parameters check: OK"
print 
print "### Processing FinalReport file:"
### Start doing stuff
readfrom=False
SNPname=[]
lagida=''
c=0;anim=-1;snp=0
outped=open(outname+'.ped','w')
outmap=open(outname+'.map','w')

for en,a in enumerate(open(finrep)):
    ## Header of the Illumina row format (line below the [Data] line)
    if 'Allele1' in a:  
        readfrom=True
        line=a.lower().strip().split(sep)
        if not 'allele1 - '+allele.lower() in line:
            print "ERROR: The header does not contain the required field: Allele1 - "+allele
            print 
            print "Header read:"
            print a
            print "Possible causes:"
            print "      - The requested allele format is not present in your header"
            print "        SOLUTION: choose an allele format that is available"
            print "      - The header in the Illumina header has changed (no 'Allele1 - '"+allele+" field is present - not case sensitive!)"
            print "        SOLUTION: Contact ezequiel.nicolazzi@ptp.it, or if you know how to code in python, change the if string related to this"
            print "      - The FinalReport file separator is not right (you provided "+sep+" )"
            print "        SOLUTION: Choose the right separator"
            print "      - The FinalReport file is in Matrix format"
            print "        SOLUTION: Use the software pedda_matrix.py, instead of this script!"
            print "      - Other"
            print "        SOLUTION: Contact ezequiel.nicolazzi@ptp.it ... send me the header (e.g. first 10 rows) of the FinalReport file you're using"
            print
            sys.exit()
        alle_pos1=line.index('allele1 - '+allele.lower())
        alle_pos2=alle_pos1+1
        continue
    if not readfrom:continue
    line=a.strip().split(sep)
    if alle_pos2 > len(line): 
        bomb("Probable error in the separator.. Position of Allele2 found in "+alle_pos2+", but length of line in row "+en+" is "+len(line)+" !!"+\
             "\n       Please check your choice of separator is correct and that you don't have strange fields in you FinalReport file!")
    snp_name=line[int(SNPid_pos)-1]
    id_sample=line[int(INDid_pos)-1]
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
            SNPname.append(snp_name)
        else:
            if snp_name!=SNPname[snp]:
                bomb("The order of the SNPs in the different individuals is consistent. Check "+snp_name+" and "+SNPname[snp])
                sys.exit()
    else:
        snp=0
        anim+=1
        outped.write('%s %s 0 0 0 -9 %s\n' % (brdcode,name[anim],' '.join(geno)))
        print 'Finshed processing individual:',name[anim],' - Total SNPs:',len(geno)
        geno=[]
        geno.append(alle1+' '+alle2)
        name.append(id_sample)

outped.write('%s %s 0 0 0 -9 %s\n' % (brdcode,id_sample,' '.join(geno)))
anim+=2
print 'Finshed processing individual:',id_sample,' - Total SNPs:',len(geno)
print '====> Total number of INDIVIDUALS processed:',anim 
print 
print "### Processing SNPmap file"

conv={}
for a in open(snpmap):
    if 'Chromosome' in a:continue
    nn,snpid,cro,pos,rest=a.strip().split(sep,4)
    conv[snpid]=(cro,pos)
print "====> Total number of SNPs processed:",len(conv)
print
print "### Writing output map file"
for x in SNPname:
    if not conv.has_key(x): bomb("SNP: "+x+" in FinalReport is not present in SNP map!!!")
    outmap.write('%s %s 0 %s\n' % (conv[x][0],x,conv[x][1]))
print "====> PED FILE PRODUCED: "+outname+'.ped'
print "====> MAP FILE PRODUCED: "+outname+'.map'
print
print "BAZINGA! I'm done!"
