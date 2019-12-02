import os,argparse,glob

def makedirs(dir):
    if not os.path.exists(dir):
        os.makedirs(os.path.abspath(dir))

inputDir = "/cms/data/store/user/klo/ZZGNTuple/94X_MCProd_190925/"
outputDir = "/cms/data/store/user/t2/users/klo/Higgs/ZZGNTuple/94X_MCProd_190925/"

pdNames = glob.glob(inputDir+"/")

for pdDir in pdNames:
    pdName = pdDir.split("/")[-2]
    makedirs(os.path.join(outputDir,pdName))
    for crabDir in glob.glob(pdDir+"*/"):
        dataset_name = crabDir.split("/")[-2].replace("crab_","")
        cmd = "hadd -f "+os.path.join(outputDir,pdName,dataset_name+".root")+" "+crabDir+"*/*/*/*.root"
        print "="*50
        print cmd
        os.system(cmd)
