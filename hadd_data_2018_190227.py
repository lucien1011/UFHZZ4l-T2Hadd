import os,argparse,glob

def makedirs(dir):
    if not os.path.exists(dir):
        os.makedirs(os.path.abspath(dir))

#inputDir = "/cms/data/store/user/dsperka/UFHZZAnalysisRun2/Data2018_M19_Feb25_CJSLTEvents_RunABC_bestCandMela_v2/"
#outputDir = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/Data2018_M19_Feb25_CJSLTEvents_RunABC_bestCandMela_v2/"

#inputDir = "/cms/data/store/user/dsperka/UFHZZAnalysisRun2/Data2018_M19_Feb25_CJSLTEvents_RunD_bestCandMela_v2/"
#outputDir = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/Data2018_M19_Feb25_CJSLTEvents_RunD_bestCandMela_v2/"

inputDir = "/cms/data/store/user/klo/HZZ4l/Data2018_102X_M19_3l_2018jets/"
outputDir = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/Data2018_102X_M19_3l_2018jets/"

pdNames = glob.glob(inputDir+"/")

makedirs(os.path.join(outputDir,))
for crabDir in glob.glob(inputDir+"*/"):
    for datasetDir in glob.glob(crabDir+"*/"):
        outFileName = datasetDir.split("/")[-2].replace("crab_","")
        cmd = "hadd -f "+os.path.join(outputDir,outFileName+".root")+" "+datasetDir+"*/*/*.root"
        print "="*50
        print cmd
        os.system(cmd)
