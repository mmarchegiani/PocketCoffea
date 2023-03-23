from pocket_coffea.parameters.cuts.preselection_cuts import *
from pocket_coffea.workflows.tthbb_base_processor import ttHbbBaseProcessor
from pocket_coffea.lib.cut_functions import get_nObj_min, get_nObj_eq, get_HLTsel
from pocket_coffea.lib.columns_manager import ColOut
from pocket_coffea.parameters.histograms import *
from config.datamc.plots import cfg_plot

samples = ["ttHTobb",
           "TTToSemiLeptonic",
           "TTTo2L2Nu",
           "SingleTop",
           "WJetsToLNu_HT",
           "DATA_SingleEle",
           "DATA_SingleMuon"]

subsamples = {'DATA_SingleEle'  : {'DATA_SingleEle' : [get_HLTsel("semileptonic", primaryDatasets=["SingleEle"])]},
              'DATA_SingleMuon' : {'DATA_SingleMuon' : [get_HLTsel("semileptonic", primaryDatasets=["SingleMuon"]),
                                                        get_HLTsel("semileptonic", primaryDatasets=["SingleEle"], invert=True)]}
             }

cfg =  {
    "dataset" : {
        "jsons": ["datasets/signal_ttHTobb_local.json",
                  "datasets/backgrounds_MC_ttbar_local.json",
                  "datasets/backgrounds_MC_local.json",
                  "datasets/DATA_SingleMuon_local.json",
                  "datasets/DATA_SingleEle_local.json",],
        "filter" : {
            "samples": samples,
            "samples_exclude" : ["ttHTobb",
                                "TTToSemiLeptonic",
                                "TTTo2L2Nu",
                                "SingleTop",
                                "WJetsToLNu_HT"],
            "year": ['2018']
        },
        "subsamples": subsamples
    },

    # Input and output files
    "workflow" : ttHbbBaseProcessor,
    "output"   : "output/particle_transformer/ntuples_2018_DATA",
    "worflow_options" : {},

    "run_options" : {
        "executor"       : "dask/slurm",
        "workers"        : 1,
        "scaleout"       : 300,
        "queue"          : "standard",
        "walltime"       : "12:00:00",
        "mem_per_worker" : "6GB", # GB
        "exclusive"      : False,
        "chunk"          : 400000,
        "retries"        : 50,
        "treereduction"  : 10,
        "max"            : None,
        "skipbadfiles"   : None,
        "voms"           : None,
        "limit"          : None,
        "adapt"          : False,
    },

    # Cuts and plots settings
    "finalstate" : "semileptonic",
    "skim": [get_nObj_min(4, 15., "Jet"),
             get_HLTsel("semileptonic", primaryDatasets=["SingleEle", "SingleMuon"]) ],
    "preselections" : [semileptonic_presel],
    "categories": {
        "inclusive": [get_nObj_eq(1, coll="LeptonGood")],
    },

    "weights": {
        "common": {
            "inclusive": ["genWeight","lumi","XS",
                          "pileup",
                          "sf_ele_reco", "sf_ele_id", "sf_ele_trigger",
                          "sf_mu_id","sf_mu_iso", "sf_mu_trigger",
                          "sf_btag", "sf_btag_calib",
                          "sf_jet_puId"
                          ],
            "bycategory" : {
            }
        },
        "bysample": {
        }
    },

    "variations": {
        "weights": {
            "common": {
                "inclusive": [ ],
                "bycategory" : {

                }
            },
            "bysample": {
            }    
        },
        "shape": {
            "common":{
                "inclusive": [ ]
            },
            "bysample": {
            }
        }
    },

   "variables": {},

    "columns": {
        "common": {
            "inclusive": [
                    ColOut(
                        "JetGood",
                        ["pt", "eta", "phi", "btagDeepFlavB"],
                    ),
                    ColOut("LeptonGood",
                            ["pt","eta","phi","pdgId"],
                            pos_end=1, store_size=False),
                    ColOut("MET", ["phi","pt","significance"]),
            ]
        },
    },

    "plot_options": cfg_plot
}
