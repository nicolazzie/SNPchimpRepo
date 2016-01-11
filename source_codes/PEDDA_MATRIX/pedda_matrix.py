import sys,os

''' This program converts Illumina matrix format into PLINK ped and map formats.
    It was NOT originally coded for release to the public, so coding and standards are not followed strictly.
    I release this following several requests from users.
    NOTE: If you ask your Genotyping lab, they are able to give you an "official" PLINK file format for your gentoypes. There is a specific plugin in GenomeStudio that does that!

    See ZANARDI PIPELINE to discover an easy solution to perform genomic analyses using the PLINK file formats!
    https://github.com/bioinformatics-ptp/Zanardi

    Coded originally by: Ezequiel L. Nicolazzi (Fondazione Parco Tecnologico Padano, Lodi, Italy)
    For bug report, comments and contributions: ezequiel.nicolazzi@ptp.it

    DISCLAIMER: See the usual GNU public disclaimer. Although I use this software quite on a regular basis,
             this is released under NO WARRANTY AT ALL (use at your own risk!).
'''
#### HEADER
print "#"*60
print "###                                                      ### "
print "###               PEDDA MATRIX software                  ### "
print "###      Converts Illumina row fmt into PLINK fmt        ### "
print "###                                                      ### "
print "###                              Coded by: E.L.Nicolazzi ### "
print "#"*60

#### USEFUL DEFs
def bomb(message):
    print "ERROR: "+message
    sys.exit()

def check_file(value,name):
    try:os.path.exists(value)
    except:bomb("FinalReport file provided in parameter '"+name+"' was not found")

def check_sep(value):
    if not value in ['\t',' ',',']:bomb("Separator provided in parameter 'sep' ( "+value+" ) not valid [options: ',',' ','\t']")


#### READ PARAMETERS
PARAMFILE_OPEN=open('peddam.param','r').readlines()
PARAMETERS=[ind.strip().replace("'","").replace('"','').replace(';',',') for ind in PARAMFILE_OPEN
if not '#' in ind[0]]
PARAM=[]
for i in PARAMETERS:
    if not i: continue
    PARAM.append(i.strip().split('=')[1].strip())
if PARAM[-1]=='\\t':PARAM[-1]='\t'

if len(PARAM)!=5:bomb('Wrong number of parameters found in peddam.param. Please check it!')
else:finrep,snpmap,outname,brdcode,sep=PARAM

print "### Rough check of parameters"
check_file(finrep,'finrep')
check_file(snpmap,'snpmap')
check_sep(sep)
print "====> Parameters check: OK"
print

print "### Processing SNPmap file"
conv={}
for a in open(snpmap):
    if 'Chromosome' in a:continue
    nn,snpid,cro,pos,rest=a.strip().split(sep,4)
    conv[snpid]=(cro,pos)
print "====> Total number of SNPs processed:",len(conv)
print

print "### Processing MATRIX FinalReport file:"
readfrom=False
genos=[];anims=[]
n=0
outped=open(outname+'.ped','w')
outmap=open(outname+'.map','w')

for a in open(finrep):
    if '[Data]' in a:
        readfrom=True
        continue
    if not readfrom:continue
    n+=1
    if n==1:
        line=a.strip().split(sep)
        for x in range(len(line)):
            if x==0:continue
            anims.append(line[x])
            genos.append([])
        continue
    snp,geno=a.strip().split(sep,1)
    outmap.write('%s %s 0 %s\n' % (conv[snp][0],snp,conv[snp][1]))
    geno=geno.replace('-','0').strip().split(sep)
    for x in range(len(geno)):genos[x].append(geno[x])

print '====> Total number of INDIVIDUALS processed:',len(geno)
print
print "### Writing output ped file"
for x in range(len(anims)):
    gty=[genos[x][i][0]+' '+genos[x][i][1] for i in range(len(genos[x]))]
    outped.write('%s %s 0 0 0 0 %s\n' % (brdcode,anims[x],' '.join(gty)))
print "====> PED FILE PRODUCED: "+outname+'.ped'
print "====> MAP FILE PRODUCED: "+outname+'.map'
print
print "BAZINGA! I'm done!"
