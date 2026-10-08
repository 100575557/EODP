
# MAIN FUNCTION TO CALL THE L1C MODULE

from l1c.src.l1c import l1c

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:/Users/maria/OneDrive/Escritorio/master/Segundo/PrimerCuatri/procesado/EODP/auxiliary'
# GM dir + L1B dir
indir = r'C:/Users/maria/OneDrive/Escritorio/master/Segundo/PrimerCuatri/procesado/SHARED/EODP_TER_2021/EODP-TS-L1C/input/gm_alt100_act_150/,C:/Users/maria/OneDrive/Escritorio/master/Segundo/PrimerCuatri/procesado/SHARED/EODP_TER_2021/EODP-TS-L1C/input/l1b_output'
outdir = r'C:/Users/maria/OneDrive/Escritorio/master/Segundo/PrimerCuatri/procesado/SHARED/EODP_TER_2021/EODP-TS-L1C/myoutputs'



# Initialise the ISM
myL1c = l1c(auxdir, indir, outdir)
myL1c.processModule()
