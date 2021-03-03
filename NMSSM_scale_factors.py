import ROOT 
import numpy as np
import matplotlib.pyplot as plt
channels=["et","mt","tt"]
eras=["2016","2017","2018"]
light_mass=np.array([60, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 150, 170, 190, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850])
light_masses=light_mass.astype('str')
scale_factors={ "2016":   {"et" : [],
                       "mt" : [],
                        "tt" : []
                },
                "2017":   { "et" : [],
                       "mt" : [],
                        "tt" : []

                },
                "2018": {"et" : [],
                       "mt" : [],
                        "tt" : []
                }
            }
i=0
fold_factors={}
for era in eras:
    for ch in channels:        
        shapefile=ROOT.TFile("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/parametrized_nn_mh1000/{era}_{ch}/fold0_training_dataset.root".format(era=era,ch=ch),"READ")
        tree=shapefile.Get("NMSSM")
        nmssm_masses=np.zeros(tree.GetEntries())
        i=0
        for event in tree:
            nmssm_masses[i]=event.NMSSM_light_mass
            i+=1
        fold_factors["{ch}_{era}".format(ch=ch,era=era)]=np.histogram(nmssm_masses, bins=160, range=(57.5,857.5),density=True)


def random(input, probability):
 
    n = len(input)
    if n != len(probability):
        return -1                   # error
 
    # construct a sum list from given probabilities
    prob_sum = [None] * n
 
    # prob_sum[i] holds sum of all probability[j] for 0 <= j <=i
    prob_sum[0] = probability[0]
    for i in range(1, n):
        prob_sum[i] = prob_sum[i - 1] + probability[i]
 
    # generate a random integer from 1 to 100
    # and check where it lies in prob_sum
    r = np.random.uniform()
 
    # based on the comparison result, return corresponding
    # element from the input list
    #print(prob_sum)
    if r <= prob_sum[0]:  # handle 0'th index separately
        return input[0]
 
    for i in range(1, n):
        if prob_sum[i - 1] < r <= prob_sum[i]:
            return input[i]
#print(fold_factors)  



# prob=np.zeros(np.size(light_mass)) 
# hist,bins=fold_factors["tt_2018"]
# #print(hist,hist[1]-hist[0])
# i=0
# for j in range(len(hist)):
#     if hist[j]>0.00001:
#         prob[i]=(bins[1]-bins[0])*hist[j]
#         i+=1
# print(bins)
# print(prob) 
j=0
for i in range(len(scale_factor_dict["2016"]["tt"])):
    j+=scale_factor_dict["2016"]["tt"][i]
    print(j)
print(j)      
count=10000
masses=np.zeros(count)
for i in range(count):
    masses[i]=random(light_mass, scale_factor_dict["2016"]["tt"])

# hist,bins=np.histogram(nmssm_masses, bins=85,density=True)
plt.hist(masses, bins=80)
plt.savefig("hist.png")
# print (hist*(bins[1]-bins[0]))
# print(np.sum(hist)*(bins[1]-bins[0]))
# print(scale_factor_dict["2016"]["tt"])
# print(bins)

# plt.plot(light_mass,scale_factor_dict["2016"]["tt"])
# plt.savefig("scale16tt.png")

#scale factors from fold0 NMSSM mH=1000

# scale_factor_dict = {'2016': {  'et': [0.04083731, 0.04214769 ,0.0400909, 0.04080414, 0.04138469, 0.04247943 ,0.04305998 ,0.04219745, 0.04320926, 0.04305998, 0.04369029, 0.04037288
#  ,0.04571391 ,0.04614517 ,0.04460257 ,0.04415472 ,0.04428742 ,0.04216428
#  ,0.0404724  ,0.03863124 ,0.03619294 ,0.03149881 ,0.0270203  ,0.02265791
#  ,0.01522691 ,0.01078158 ,0.00711584],  
#                                     'mt': [0.04003836 ,0.03983493 ,0.03804274 ,0.03924399 ,0.04025149 ,0.0424893
#  ,0.04097805 ,0.04266367 ,0.04277023 ,0.04357429 ,0.04404898 ,0.0420243
#  ,0.04268304 ,0.04321586 ,0.04460117 ,0.04491117 ,0.04445585 ,0.04253773
#  ,0.04113305 ,0.03785868 ,0.03595025 ,0.03255963 ,0.02789026 ,0.02427683
#  ,0.01923934 ,0.01308779 ,0.00963904],                       
#                                     'tt': [0.0407869  ,0.04275881 ,0.03831272 ,0.04083341 ,0.04239606 ,0.04288903
#  ,0.04257278 ,0.04370756 ,0.04314947 ,0.04494466 ,0.04509348 ,0.04541903
#  ,0.04595852 ,0.04610734 ,0.0465073  ,0.04730723 ,0.04602363 ,0.04438657
#  ,0.04148451 ,0.03938238 ,0.0356618  ,0.02909497 ,0.0248628  ,0.01877965
#  ,0.01292903 ,0.00581341 ,0.00283695]},                   
#                         '2017': {   'et': [0.03831795,0.03879693,0.0385997 ,0.03968444,0.04137494,0.03924773
# ,0.04110728,0.03341551,0.04324857,0.04227654,0.06909911,0.03964218
# ,0.04331901,0.04464323,0.04338945,0.04313587,0.04236106,0.04260055
# ,0.04050151,0.03796577,0.03490878,0.03144326,0.02837219,0.02327252
# ,0.01780658,0.01298866,0.00848066],                             
#                                     'mt': [0.03655853,0.03859896,0.03822473,0.04098689,0.03919594,0.0407285
# ,0.04030081,0.03965927,0.04158388,0.04162843,0.06662152,0.04299169
# ,0.04362431,0.04186009,0.04257291,0.04433713,0.04219868,0.04173535
# ,0.03827819,0.03756538,0.03555167,0.03143516,0.0281473 ,0.0232467
# ,0.01857775,0.01431868,0.00947154],                             
#                                     'tt': [0.03802169,0.03824488,0.03996786,0.03943222,0.04079811,0.04069098
# ,0.04111949,0.04140517,0.04327099,0.04324421,0.070437  ,0.04433335
# ,0.04472615,0.04581529,0.04670803,0.04503861,0.0448065 ,0.0436995
# ,0.04176226,0.03780744,0.03372763,0.03009418,0.02374682,0.01903317
# ,0.01249833,0.00645449,0.00311565]},                   
#                         '2018': {   'et': [0.03918467,0.04060224,0.04119912,0.0404381 ,0.04040826,0.04031873
# ,0.04191536,0.04257192,0.04427301,0.04436254,0.0439895 ,0.04436254
# ,0.04378059,0.04504894,0.04410887,0.04578011,0.04278083,0.04310911
# ,0.04116927,0.03905038,0.03567805,0.02970932,0.02711293,0.0227856
# ,0.01684672,0.01177331,0.00763997],                       
#                                     'mt': [0.03896092,0.04043341,0.04064642,0.0411002 ,0.04115577,0.0392017
# ,0.04037785,0.04267457,0.04315614,0.04262826,0.04256344,0.04376736
# ,0.04400815,0.04373958,0.04346175,0.0448972 ,0.04335988,0.04227635
# ,0.04082237,0.03821078,0.03477496,0.03251528,0.02884793,0.02365253
# ,0.01889239,0.01416003,0.00971476],                       
#                                     'tt': [0.03994206,0.04163802,0.0413355 ,0.04174803,0.04244474,0.04252725
# ,0.04328814,0.0441957 ,0.04469074,0.04476408,0.04511244,0.04569915
# ,0.04656088,0.0455158 ,0.04713842,0.04767929,0.04573582,0.04457156
# ,0.04109715,0.03857613,0.03371744,0.02921628,0.02397257,0.0179313
# ,0.01213755,0.0059496 ,0.00281437]}}


##########################

####scale factors from ntuple
# scale_factor_dict = {'2016': {'et': [0.03828, 0.03919, 0.03961, 0.03952, 0.03937, 0.03973, 0.04021, 0.03971, 0.03976, 0.04001, 0.03994, 0.03985, 0.03991, 0.04025, 0.03957, 0.0388, 0.03882, 0.0385, 0.03788, 0.03751, 0.03611, 0.03518, 0.03321, 0.0311, 0.02951, 0.02545, 0.02302],                             'mt': [0.04957, 0.04822, 0.04858, 0.04749, 0.04694, 0.04646, 0.04434, 0.04533, 0.04333, 0.04151, 0.04056, 0.03932, 0.03886, 0.03851, 0.03918, 0.03818, 0.03806, 0.03643, 0.03523, 0.03257, 0.03152, 0.02895, 0.02599, 0.02438, 0.02058, 0.01659, 0.0133],                        'tt': [0.03895, 0.03958, 0.03895, 0.03975, 0.04042, 0.04072, 0.04048, 0.04106, 0.04094, 0.04134, 0.04063, 0.04135, 0.0415, 0.04133, 0.04125, 0.04156, 0.04093, 0.04079, 0.0397, 0.03905, 0.03705, 0.03492, 0.03205, 0.02899, 0.02528, 0.01851, 0.01291]},                   '2017': {'et': [0.03819, 0.03931, 0.03976, 0.03911, 0.03983, 0.03941, 0.04101, 0.03997, 0.04025, 0.04053, 0.04022, 0.04002, 0.04016, 0.04042, 0.03951, 0.03949, 0.03952, 0.03888, 0.0375, 0.03667, 0.0356, 0.03526, 0.03325, 0.03067, 0.02873, 0.02519, 0.02154],                             'mt': [0.04844, 0.04821, 0.04661, 0.04712, 0.04638, 0.04606, 0.04562, 0.04494, 0.04339, 0.04221, 0.04076, 0.04081, 0.04037, 0.03927, 0.03909, 0.03863, 0.03748, 0.037, 0.03495, 0.0337, 0.03186, 0.02955, 0.02681, 0.02328, 0.01983, 0.01573, 0.0119],                             'tt': [0.03857, 0.03876, 0.03964, 0.0396, 0.0403, 0.04061, 0.04016, 0.04102, 0.04099, 0.04037, 0.04109, 0.04155, 0.0412, 0.04117, 0.04149, 0.04174, 0.04135, 0.04062, 0.0401, 0.03823, 0.03682, 0.03506, 0.03178, 0.02928, 0.02508, 0.01904, 0.01436]},                   '2018': {'et': [0.03883, 0.03984, 0.04031, 0.03902, 0.03986, 0.04056, 0.04034, 0.0403, 0.04112, 0.04089, 0.04107, 0.04025, 0.03995, 0.04086, 0.04024, 0.03971, 0.0393, 0.03884, 0.03821, 0.03709, 0.03649, 0.03393, 0.03261, 0.03075, 0.02697, 0.02333, 0.01931],                       'mt': [0.04919, 0.04819, 0.04805, 0.04713, 0.04666, 0.04656, 0.04455, 0.04516, 0.04386, 0.04192, 0.04105, 0.04056, 0.03985, 0.04007, 0.03936, 0.03898, 0.03741, 0.03656, 0.03538, 0.03329, 0.0311, 0.02928, 0.02631, 0.02305, 0.01957, 0.01524, 0.01169],                       'tt': [0.03912, 0.03964, 0.04035, 0.04061, 0.04033, 0.04031, 0.04089, 0.04144, 0.04148, 0.04164, 0.04208, 0.04189, 0.04147, 0.04161, 0.04238, 0.04147, 0.04144, 0.04114, 0.03958, 0.03834, 0.036, 0.03373, 0.03109, 0.02794, 0.02348, 0.01773, 0.01281]}}


# for ch in channel:
#     for er in era:
#         for lm in light_masses:
#             shapefile=ROOT.TFile("output/NMSSM_scale_factors_para_training/{era}-{channel}-control-shapes.root".format(era=er, channel=ch),"READ") 
#             if "2016" in er:
#                 ntuplefile=ROOT.TFile("/ceph/jbechtel/nmssm/ntuples/{era}/{channel}/NMSSMM1000h1M125tautauh2M{lm}_RunIISummer16MiniAODv3_PUMoriond17_13TeV_MINIAOD_madgraph-pythia8_v1/NMSSMM1000h1M125tautauh2M{lm}_RunIISummer16MiniAODv3_PUMoriond17_13TeV_MINIAOD_madgraph-pythia8_v1.root".format(era=er, channel=ch,lm=lm),"READ")    
#             elif "2017" in er:
#                 ntuplefile=ROOT.TFile("/ceph/jbechtel/nmssm/ntuples/{era}/{channel}/NMSSMM1000h1M125tautauh2M{lm}_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1/NMSSMM1000h1M125tautauh2M{lm}_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1.root".format(era=er, channel=ch,lm=lm),"READ")  
#             else:
#                 ntuplefile=ROOT.TFile("/ceph/jbechtel/nmssm/ntuples/{era}/{channel}/NMSSMM1000h1M125tautauh2M{lm}_RunIIAutumn18MiniAOD_102X_13TeV_MINIAOD_madgraph-pythia8_v1/NMSSMM1000h1M125tautauh2M{lm}_RunIIAutumn18MiniAOD_102X_13TeV_MINIAOD_madgraph-pythia8_v1.root".format(era=er, channel=ch,lm=lm),"READ")
#             shapehist=shapefile.Get("NMSSM_1000_125_{lm}#{ch}-NMSSM#Nominal#pt_1".format(lm=lm,ch=ch))
#             ntuplehist=ntuplefile.Get("{ch}_nominal/ntuple".format(ch=ch))
#             shape_entries=shapehist.GetEntries()
#             ntuple_entries=ntuplehist.GetEntries()
#             #print(shape_entries,ntuple_entries)
#             scale_factors["{era}".format(era=er)]["{ch}".format(ch=ch)].append(shape_entries/float(ntuple_entries))
#            # print(i)
#             i+=1
# #normed_scale_factors["{era}".format(era=er)]["{ch}".format(ch=ch)]
# normed_scale_factors={"2016":{},"2017":{},"2018":{}}
# for er in era:
#     for ch in channel:

#         normed_scale_factors["{era}".format(era=er)]["{ch}".format(ch=ch)] = [round(i/sum(scale_factors["{era}".format(era=er)]["{ch}".format(ch=ch)]),5) for i in scale_factors["{era}".format(era=er)]["{ch}".format(ch=ch)]]
# print (normed_scale_factors)