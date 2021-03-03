#!/usr/bin/env python

import ROOT
from ROOT import gRandom
ROOT.PyConfig.IgnoreCommandLineOptions = True  # disable ROOT internal argument parser
#  ROOT.ROOT.EnableImplicitMT(12); # Tell ROOT you want to go parallel
import argparse
import yaml
import os
import subprocess
from array import array
from multiprocessing import Pool
import numpy as np
from root_numpy import array2tree,tree2array,list_trees
import logging

logger = logging.getLogger("create_training_dataset")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def parse_arguments():
    logger.debug("Parse arguments.")
    parser = argparse.ArgumentParser(description="Create training dataset")
    parser.add_argument(
        "--config", 
        help="Datasets config file"
    )
    parser.add_argument(
        "--era",
        required=True,
        type=str,
        help="Experiment era."
    )
    parser.add_argument(
        "--channel",
        required=True,
        type=str,
        help="Channel"
    )
    return parser.parse_args()


def parse_config(filename):
    logger.debug("Load YAML config: {}".format(filename))
    return yaml.load(open(filename, "r"))

ROOT.gInterpreter.Declare("""
            float pickMass(std::vector<int> masses, int length, std::vector<double> scales) {
            int idx = int(gRandom->Uniform(length));
            while (gRandom->Uniform(0,1) > scales.at(idx)) {
                idx = int(gRandom->Uniform(length));
            }
            return masses.at(idx);
            }
        """)
def generateRootFiles(jobconfig):
    
    process, num_fold, config = jobconfig
  #  if "ggH" in process:
    logger.debug("Collect events of process {} for fold {}.".format(process, num_fold))

    # Create output file
    output_filename = os.path.join(
        config["output_path"], "merge_fold{}_{}.root".format(num_fold, process)
    )

    # Collect all files for this process in a chain. Create also chains for friend files
    chain = ROOT.TChain(config["tree_path"])  ## "mt_nominal/ntuple"
    friendchains = {}
    for friendPath in config["friend_paths"]:  ####/ceph/htautau/2017/nnscore_friends/
        friendTreeName = os.path.basename(os.path.normpath(friendPath))
        friendchains[friendTreeName] = ROOT.TChain(config["tree_path"])

    # for each file, add ntuple TTree to the chain and do the same for the the friendTrees
    for filename in config["processes"][process]["files"]:
        path = os.path.join(config["base_path"], filename)
        if not os.path.isfile(path):
            logger.fatal("File does not exist: {}".format(path))
            raise Exception
        chain.AddFile(path)
        # Make sure, that friend files are put in the same order together
        for friendPath in config["friend_paths"]:
            friendFileName = os.path.join(friendPath, filename)
            if not os.path.isfile(friendFileName):
                logger.fatal("File does not exist: {}".format(friendFileName))
                raise Exception
            friendTreeName = os.path.basename(os.path.normpath(friendPath))
            logger.debug(
                "Attaching friendtree for {}, filename{}".format(
                    friendTreeName, friendFileName
                )
            )
            friendchains[friendTreeName].AddFile(friendFileName)

    logger.debug("Joining TChains")
    for friendTreeName in friendchains.keys():
        logger.debug("Adding to mainchain: {}".format(friendTreeName))
        chain.AddFriend(friendchains[friendTreeName], friendTreeName)

    logger.debug("Calculationg number of events")
    rdf = ROOT.RDataFrame(chain)
    chain_numentries = rdf.Count().GetValue()
    if chain_numentries == 0:
        logger.fatal("Chain (before skimming) does not contain any events.")
        raise Exception
    logger.info("Found {} events for process {}.".format(chain_numentries, process))

    # Skim the events with the cut string
    cut_string = "({EVENT_BRANCH}%2=={NUM_FOLD})&&({CUT_STRING})".format(
        EVENT_BRANCH=config["event_branch"],
        NUM_FOLD=num_fold,
        CUT_STRING=config["processes"][process]["cut_string"],
    )
    logger.debug("Skim events with cut string: {}".format(cut_string))

    rdf = rdf.Filter(cut_string)

    chain_skimmed_numentries = rdf.Count().GetValue()
    if not chain_skimmed_numentries > 0:
        logger.fatal("Chain (after skimming) does not contain any events.")
        raise Exception
    logger.debug(
        "Found {} events for process {} after skimming.".format(
            chain_skimmed_numentries, process
        )
    )

    # # Write training weight to new branch
    logger.debug(
        "Add training weights with weight string: {}".format(
            config["processes"][process]["weight_string"]
        )
    )
    #print(process)
    
    rdf = rdf.Define(
        config["training_weight_branch"],
        "(float)(" + config["processes"][process]["weight_string"] + ")",
    )
    
    mass_dict= {
                "heavy_mass": [1000],
                "light_mass_coarse": [60, 70, 80, 90, 100, 120, 150, 170, 190, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800],
                "light_mass_fine": [60, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 150, 170, 190, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850],
            }

    scale_factor_dict = {'2016': {'et': [0.03828, 0.03919, 0.03961, 0.03952, 0.03937, 0.03973, 0.04021, 0.03971, 0.03976, 0.04001, 0.03994, 0.03985, 0.03991, 0.04025, 0.03957, 0.0388, 0.03882, 0.0385, 0.03788, 0.03751, 0.03611, 0.03518, 0.03321, 0.0311, 0.02951, 0.02545, 0.02302],                             'mt': [0.04957, 0.04822, 0.04858, 0.04749, 0.04694, 0.04646, 0.04434, 0.04533, 0.04333, 0.04151, 0.04056, 0.03932, 0.03886, 0.03851, 0.03918, 0.03818, 0.03806, 0.03643, 0.03523, 0.03257, 0.03152, 0.02895, 0.02599, 0.02438, 0.02058, 0.01659, 0.0133],                        'tt': [0.03895, 0.03958, 0.03895, 0.03975, 0.04042, 0.04072, 0.04048, 0.04106, 0.04094, 0.04134, 0.04063, 0.04135, 0.0415, 0.04133, 0.04125, 0.04156, 0.04093, 0.04079, 0.0397, 0.03905, 0.03705, 0.03492, 0.03205, 0.02899, 0.02528, 0.01851, 0.01291]},                   '2017': {'et': [0.03819, 0.03931, 0.03976, 0.03911, 0.03983, 0.03941, 0.04101, 0.03997, 0.04025, 0.04053, 0.04022, 0.04002, 0.04016, 0.04042, 0.03951, 0.03949, 0.03952, 0.03888, 0.0375, 0.03667, 0.0356, 0.03526, 0.03325, 0.03067, 0.02873, 0.02519, 0.02154],                             'mt': [0.04844, 0.04821, 0.04661, 0.04712, 0.04638, 0.04606, 0.04562, 0.04494, 0.04339, 0.04221, 0.04076, 0.04081, 0.04037, 0.03927, 0.03909, 0.03863, 0.03748, 0.037, 0.03495, 0.0337, 0.03186, 0.02955, 0.02681, 0.02328, 0.01983, 0.01573, 0.0119],                             'tt': [0.03857, 0.03876, 0.03964, 0.0396, 0.0403, 0.04061, 0.04016, 0.04102, 0.04099, 0.04037, 0.04109, 0.04155, 0.0412, 0.04117, 0.04149, 0.04174, 0.04135, 0.04062, 0.0401, 0.03823, 0.03682, 0.03506, 0.03178, 0.02928, 0.02508, 0.01904, 0.01436]},                   '2018': {'et': [0.03883, 0.03984, 0.04031, 0.03902, 0.03986, 0.04056, 0.04034, 0.0403, 0.04112, 0.04089, 0.04107, 0.04025, 0.03995, 0.04086, 0.04024, 0.03971, 0.0393, 0.03884, 0.03821, 0.03709, 0.03649, 0.03393, 0.03261, 0.03075, 0.02697, 0.02333, 0.01931],                       'mt': [0.04919, 0.04819, 0.04805, 0.04713, 0.04666, 0.04656, 0.04455, 0.04516, 0.04386, 0.04192, 0.04105, 0.04056, 0.03985, 0.04007, 0.03936, 0.03898, 0.03741, 0.03656, 0.03538, 0.03329, 0.0311, 0.02928, 0.02631, 0.02305, 0.01957, 0.01524, 0.01169],                       'tt': [0.03912, 0.03964, 0.04035, 0.04061, 0.04033, 0.04031, 0.04089, 0.04144, 0.04148, 0.04164, 0.04208, 0.04189, 0.04147, 0.04161, 0.04238, 0.04147, 0.04144, 0.04114, 0.03958, 0.03834, 0.036, 0.03373, 0.03109, 0.02794, 0.02348, 0.01773, 0.01281]}}


    light_masses=[]
    scale_factors=scale_factor_dict["{era}".format(era=args.era)]["{channel}".format(channel=args.channel)]
    #print(scale_factors)
    for light_mass in mass_dict["light_mass_fine"]:
        if light_mass+125<mass_dict["heavy_mass"][0]:
            light_masses.append(light_mass)
    
    if "NMSSM" in process:
        masses=process.split("_")
        heavy_mass=float(masses[1])
        light_mass=float(masses[3])
        # rdf = rdf.Define(
        #     "NMSSM_heavy_mass",
        #     heavy_mass,
        # )
        rdf = rdf.Define(
            "NMSSM_light_mass",
            "(float)({light_mass})".format(light_mass=light_mass),
        )
    else:           
        rdf=rdf.Define("NMSSM_light_mass", "(float)(pickMass({{{masses}}}, {len},{{{scale_factors}}}))".format(masses=",".join(map(str, light_masses)), len=len(light_masses), scale_factors=",".join(map(str, scale_factors))))
        

    opt = ROOT.ROOT.RDF.RSnapshotOptions()
    opt.fMode = "RECREATE"
    rdf.Snapshot(config["processes"][process]["class"], output_filename, "^((?!nickname).)*$", opt)
    logger.info("snapshot created for process {}!".format(process))
    print(num_fold,output_filename)
    return (num_fold, output_filename)


def main(args, config):
    
    jobL = [
        (process, fold, config) for process in config["processes"] for fold in range(2)
    ]
    #print(jobL)
    pool = Pool(1)
    created_files = pool.map(generateRootFiles, jobL)
    for num_fold in range(2):
        logger.info("Merge input files for fold {}.".format(num_fold))
        foldfile = [fn for fold, fn in created_files if fold == num_fold]
        # Combine all skimmed files using `hadd`
        logger.debug(
            "Call `hadd` to combine files of processes for fold {}.".format(num_fold)
        )
        output_file = os.path.join(
            config["output_path"],
            "fold{}_{}".format(num_fold, config["output_filename"]),
        )
        subprocess.call(["hadd", "-f", output_file] + foldfile)
        logger.info("Created output file: {}".format(output_file))


if __name__ == "__main__":
    args = parse_arguments()
    config = parse_config(args.config)
    main(args, config)
