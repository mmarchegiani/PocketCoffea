from os import path

btagSF = {
    # DeepJet AK4 tagger shape SF
    '2016_PreVFP': "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/BTV/2016preVFP_UL/btagging.json.gz",
    '2016_PostVFP': "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/BTV/2016postVFP_UL/btagging.json.gz",
    '2017': "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/BTV/2017_UL/btagging.json.gz",
    '2018': "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz",
}

btagSF_calibration = {
    '2016_PreVFP': "",
    '2016_PostVFP': "",
    '2017': path.join(
        path.dirname(__file__),
        "btag_SF_calibration",
        "btagSF_calibrationSF_2017UL.json",
    ),
    '2018': path.join(
        path.dirname(__file__),
        "btag_SF_calibration",
        "btagSF_calibrationSF_2018UL.json",
    ),
}

jet_puId = {
    # Jet PU ID SF to be applied only on selected jets (pt<50) that are matched to GenJets
    '2016_PreVFP': "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/JME/2016preVFP_UL/jmar.json.gz",
    '2016_PostVFP': "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/JME/2016postVFP_UL/jmar.json.gz",
    '2017': "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/JME/2017_UL/jmar.json.gz",
    '2018': "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/JME/2018_UL/jmar.json.gz",
}

ptetatau21_reweighting = {
    'QCD_MuEnriched' : {
        '2016_PreVFP': path.join(
            path.dirname(__file__),
            "ptetatau21_reweighting",
            "QCD_MuEnriched",
            "FatJetGoodNMuon1_pt_eta_tau21_bintau05_2016_PreVFP_reweighting.json",
        ),
        '2016_PostVFP': path.join(
            path.dirname(__file__),
            "ptetatau21_reweighting",
            "QCD_MuEnriched",
            "FatJetGoodNMuon1_pt_eta_tau21_bintau05_2016_PostVFP_reweighting.json",
        ),
        '2017': path.join(
            path.dirname(__file__),
            "ptetatau21_reweighting",
            "QCD_MuEnriched",
            "FatJetGoodNMuon1_pt_eta_tau21_bintau05_2017_reweighting.json",
        ),
        '2018': path.join(
            path.dirname(__file__),
            "ptetatau21_reweighting",
            "QCD_MuEnriched",
            "FatJetGoodNMuon1_pt_eta_tau21_bintau05_2018_reweighting.json",
        ),
    },
    'QCD_HT' : {
        '2016_PreVFP': path.join(
            path.dirname(__file__),
            "ptetatau21_reweighting",
            "QCD_HT",
            "FatJetGoodNMuon1_pt_eta_tau21_bintau05_2016_PreVFP_reweighting.json",
        ),
        '2016_PostVFP': path.join(
            path.dirname(__file__),
            "ptetatau21_reweighting",
            "QCD_HT",
            "FatJetGoodNMuon1_pt_eta_tau21_bintau05_2016_PostVFP_reweighting.json",
        ),
        '2017': path.join(
            path.dirname(__file__),
            "ptetatau21_reweighting",
            "QCD_HT",
            "FatJetGoodNMuon1_pt_eta_tau21_bintau05_2017_reweighting.json",
        ),
        '2018': path.join(
            path.dirname(__file__),
            "ptetatau21_reweighting",
            "QCD_HT",
            "FatJetGoodNMuon1_pt_eta_tau21_bintau05_2018_reweighting.json",
        ),
    }
}
