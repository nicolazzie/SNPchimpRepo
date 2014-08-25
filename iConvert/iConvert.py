from optparse import OptionParser
import sys,os, time

################################################
### Useful defs
################################################
### This stops the pipeline when something BAD happens
def bomb(msg):
    print('\n\n[BAD NEWS]: '+msg+'\n')
    print "*"*60
    print "Program stopped because of an error. Please read .log file"
    print "*"*60
    sys.exit()

### Prints (if required) and writes the log 
def logit(msg):
    print(msg)
    log.write(msg+'\n')
####################################################################

### Open log file + read param file
log = open(sys.argv[0].strip().split('.')[0]+'.log','w')
logit('\n' + '*' * 81 + '\n==> PROGRAM STARTS: ' + time.strftime("%B %d, %Y - %l:%M%p %Z") + '\n' + '*' * 81)

### Option to change the name of the param file (default: convert.param)
usage = "usage: %prog convert.param [option: -p/--par if other param filename]"
parser = OptionParser(usage = usage)

parser.add_option("-p","--par", dest = "PARAM_FILE", default = './convert.param',
                  help = "name of the param file (default: convert.param)", metavar = "<FILE>")
(opt, args) = parser.parse_args()

### Read parameter file and check all is ok.
if not os.path.exists(opt.PARAM_FILE):
    bomb("Param file not found. I looked for the following:",opt.PARAM_FILE)
else:
    PED = 0;MAP = 0;CHIMP = 0;SEP = 0;outFMT = 0
    for line in open(opt.PARAM_FILE):
        if '#' in line[0]: continue
        if '#' in line: line = line.strip().split('#')[0] 
        if 'PEDfile' in line:
            PED   = line.strip().split('=')[1]
            if not PED: bomb('PED file not provided in parameter file')
            else: PED = PED.strip().split('#')[0]
            if not os.path.exists(PED): bomb('Looking for ' + PED + ' file... FAILED! Please check PARAM file!')
        elif 'MAPfile' in line:
            MAP = line.strip().split('=')[1]
            if not MAP: bomb('MAP file not provided in parameter file')
            else: MAP = MAP.strip().split('#')[0]
            if not os.path.exists(MAP): bomb('Looking for ' + MAP + ' file... FAILED! Please check PARAM file!')
        elif 'MISSING' in line:
            MISS = line.strip().split('=')[1]
            if not MISS: bomb('MISSING information not provided in parameter file')
            else: MISS = MISS.strip().split('#')[0].strip()
        elif 'IN_format' in line:
            inFMT = line.strip().split('=')[1].lower()
            if not inFMT: bomb('Input allele format not provided in parameter file')
            else:inFMT = inFMT.strip().split('#')[0]
            if not any([match == inFMT for match in ['ill_ab','ill_forward','ill_top','aff_ab','aff_forward','no']]):
                bomb('Wrong option for "IN_format" variable in param file!')
        elif 'UPDATE_map' in line:
            tupd = line.strip().split('=')[1].lower()
            if not tupd: bomb('Option to update map info (UPDATE_map) not provided in parameter file')
            else: tupd = tupd.strip().split('#')[0]
            if not any([match == tupd for match in ['y','n']]):
                bomb('Wrong option for "UPDATE_map" variable in param file!')
            else:
                if tupd == 'y': upd = True
                else: upd = False
        elif 'SNPchimp_file' in line:
            CHIMP = line.strip().split('=')[1]
            if not CHIMP: bomb('SNPchimp file not provided in parameter file')
            else: CHIMP = CHIMP.strip().split('#')[0]
            if not os.path.exists(CHIMP): bomb('Looking for ' + CHIMP + ' file... FAILED! Please check PARAM file!')
        elif 'OUT_format' in line:
            outFMT = line.strip().split('=')[1].lower()
            if not outFMT: bomb('Out format not provided in parameter file')
            else: outFMT = outFMT.strip().split('#')[0]
            if not any([match == outFMT for match in ['ill_ab','ill_forward','ill_top','aff_ab','aff_forward','no']]):
                bomb('Wrong option for "OUT_format" variable in param file!')
            else:
                if 'aff' in inFMT and 'ill' in outFMT:
                    bomb("WHAT?!? I (you) can't convert alleles from Affymetrix to Illumina!!!")
                if 'aff' in outFMT and 'ill' in inFMT:
                    bomb("WHAT?!? I (you) can't convert alleles from Illumina to Affymetrix!!!")

### Print options read from the parameter file
logit('Parameters read from: ' + opt.PARAM_FILE)
logit('    - PLINK PED file         : %s' % PED)
logit('    - PLINK MAP file         : %s' % MAP)
if inFMT=='NO': logit('    - Input allele format    : %s' % 'NOT REQUIRED')
else:logit('    - Input allele format    : %s' % inFMT)
logit('    - Update map information : %s' % tupd)
logit('    - SNPchimp file          : %s' % CHIMP)
if outFMT=='NO': logit('    - Output allele format   : %s' % 'NOT REQUIRED')
else:logit('    - Output allele format   : %s' % outFMT)

### Check consistency of options
onlymap = False
if inFMT == 'NO' and outFMT != 'NO': bomb('If only map update is required, both IN_format and OUT_format must be = NO')
elif inFMT != 'NO' and outFMT == 'NO': bomb('If only map update is required, both IN_format and OUT_format must be = NO')
elif inFMT =='NO' and outFMT == 'NO': 
    onlymap = True
    if not upd: bomb('Nothing will be done (no conversion or map update required!')
elif inFMT == outFMT: bomb('Input and output allele formats are equal! This is a CONVERSION tool!\n'+
               '            (if you want to remap only, please set IN_format and OUT_format to NO')


### Now read the SNPchimp file, and check everything's ok
logit('\nReading SNPchimp file and checking available options')
othinfo = []
chips = {};SNPdata = {}
formats = [0,0]
SEP = ','
if upd: mapupd = {}
for en,line in enumerate(open(CHIMP)):
    if en == 0:
        test = line.strip().split(SEP)
        if len(test) == 1: SEP = '\t'
        head = line.strip().split(SEP)
        if inFMT == 'ill_forward' or outFMT == 'ill_forward':
            try:
                form = head.index('Alleles_A_B_FORWARD')
                if inFMT == 'ill_forward': formats[0] = form
                elif outFMT == 'ill_forward': formats[1] = form
            except ValueError:
                bomb('Input or output Illumina FORWARD allele coding required,' + \
                         'but "Alleles_A_B_FORWARD" not found in SNPchimp file!')
        if inFMT == 'ill_TOP' or outFMT == 'ill_TOP':
            try:
                form = head.index('Alleles_A_B_TOP')
                if inFMT == 'ill_top': formats[0] = form
                elif outFMT == 'ill_top': formats[1] = form
            except ValueError:
                bomb('Input or output Illumina TOP allele coding required,' + \
                         'but "Alleles_A_B_TOP" not found in SNPchimp file!')
        if inFMT == 'aff_forward' or outFMT == 'aff_forward':
            try:
                form = head.index('Alleles_A_B_Affymetrix')
                if inFMT == 'aff_forward': formats[0] = form
                elif outFMT == 'aff_forward': formats[1] = form              
            except ValueError:
                bomb('Input or output Affymetrix FORWARD allele coding required,' + \
                         'but "Alleles_A_B_Affymetrix" not found in SNPchimp file!')
        try:
            othinfo.append(head.index('chip_name'))
            othinfo.append(head.index('chromosome'))
            othinfo.append(head.index('position'))
            othinfo.append(head.index('SNP_name'))
        except ValueError:
            bomb('chip name, chromosome, position and SNP_name should always be present in SNPchiMp download files!')
    else:
        lista = line.strip().split(SEP)
        if not chips.has_key(lista[othinfo[0]]): chips[lista[othinfo[0]]] = 0
        if 'aff' in inFMT:
            if not 'AffyHD' in lista[0]:continue
        if 'ill' in inFMT:
            if 'AffyHD' in lista[0]:continue
        if upd: mapupd[lista[othinfo[3]]] = [lista[othinfo[1]],lista[othinfo[2]]]
        if inFMT == 'ill_ab' or inFMT == 'aff_ab':
            SNPdata[lista[othinfo[3]]] = {'A':lista[formats[1]][0], 'B':lista[formats[1]][2]}
        elif outFMT == 'ill_ab' or outFMT == 'aff_ab':
            SNPdata[lista[othinfo[3]]] = {lista[formats[0]][0]:'A', lista[formats[0]][2]:'B'}
        else:
            SNPdata[lista[othinfo[3]]] = {lista[formats[0]][0]:lista[formats[1]][0],
                                          lista[formats[0]][2]:lista[formats[1]][2]}

if len(SNPdata) == 0:
    bomb("Data in SNP chimp file is incorrect! Probably conversion info for your SNPs is not available")
if len(chips)>1: logit('\n!!! WARNING !!! >1 chip in SNPchimp file. This might cause incorrect allele conversion!\n')

if SEP == ',': logit('    - COMMAS used as separator for SNPchimp file')
else: logit('    - TABS used as separator for SNPchimp file')
logit('    - Rows read in SNP chimp file                       : ' + str(en))
logit('    - SNPs with allele conversion information available : ' + str(len(SNPdata)))


### Reading MAP file (and remapping if required)
logit('\nReading MAP file and converting map info (if required)')
maporder = []
convert = []
tab = False
if upd: remap=open(MAP.split('.')[0] + '_updated.map','w')

for enmap,line in enumerate(open(MAP)):
    if enmap == 0: test = line.strip().split('\t')
    if len(test) == 4: 
        linea = line.strip().split('\t')
        tab = True
    else: linea = line.strip().split()
    snp = linea[1]
    maporder.append(snp)
    if not SNPdata.has_key(linea[1]):
        bomb('SNP: ' + snp + ' not found in SNPchimp file. Probably you downloaded the wrong SNP chip?')
    else:
        convert.append(SNPdata[linea[1]])
    if upd:
        remap.write('%s %s 0 %s\n' % (mapupd[snp][0],snp,mapupd[snp][1]))

if tab: logit('    - TAB used as separator for PLINK MAP file')
else:  logit('    - SPACES used as separator for PLINK MAP file')
logit('    - Rows read in PLINK MAP file (number of SNPs)      : ' + str(enmap + 1))
if upd: logit('    - MAP file updated, please see file                 : ' + MAP.split('.')[0] + '_updated.map')


### Reading PED file (if required) and doing the magic here...
if not onlymap:
    logit('\nReading PED file and converting alleles as required')
    tab = False
    reped = open(PED.split('.')[0] + '_updated.ped','w')
    for enped,line in enumerate(open(PED)):
        if enped == 0:
            test = line.strip().split('\t')
            if len(test) == (6 + (enmap + 1) * 2): tab = True
        if tab: pedline = line.strip().split('\t')
        else: pedline = line.strip().split()
        genotypes = [pedline[6 + x] + pedline[7 + x] for x in range(0, ((enmap+1)*2)-1, 2)]
        seq = -1
        genout = []
        nfailed = 0
        for alle in genotypes:
            seq += 1
            alle1 = alle[0];alle2 = alle[1]
            if alle1 == MISS:
                genout.append(MISS);genout.append(MISS)
                continue
            try:
                genout.append(convert[seq][alle1])
                genout.append(convert[seq][alle2])
            except KeyError:
                nfailed += 1
        if nfailed:
            bomb('Individual ' + pedline[1] + ' failed conversion for ' + str(nfailed) + \
                 ' SNPs. Probably their IN format is not as specified (or you specified a wrong missing value)')
        reped.write('%s %s\n' % (' '.join(pedline[:6]),' '.join(genout)))

    if tab: logit('    - TAB used as separator for PLINK PED file')
    else:  logit('    - SPACES used as separator for PLINK PED file')
    logit('    - Rows read in PLINK PED file (number of animals)   : ' + str(enped + 1))
    if upd: logit('    - PED file updated, please see file                 : ' + PED.split('.')[0] + '_updated.map')

logit('\n' + '*' * 81 + '\n==> PROGRAM ENDS: ' + time.strftime("%B %d, %Y - %l:%M%p %Z") + '\n' + '*' * 81 + '\n')
