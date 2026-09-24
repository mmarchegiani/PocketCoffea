import awkward as ak
from pocket_coffea.workflows.delphes_base import DelphesBaseProcessorABC


def delphes_leptons(coll, pdgId):
    '''Delphes Electron/Muon -> PtEtaPhiMCandidate with a common field set, so that electrons and
    muons can be concatenated (the raw records differ in fields and spell the charge `Charge`).
    Only the listed fields are read from the file.'''
    return ak.zip(
        {
            "pt": coll.pt,
            "eta": coll.eta,
            "phi": coll.phi,
            "mass": coll.mass,
            "charge": coll.Charge,
            "pdgId": -pdgId * coll.Charge,
            "IsolationVar": coll.IsolationVar,
        },
        with_name="PtEtaPhiMCandidate",
        behavior=coll.behavior,
    )


class DelphesProcessor(DelphesBaseProcessorABC):

    def apply_object_preselection(self, variation):
        cuts = self.params.object_preselection

        # Leptons: pt, eta and Delphes relative isolation
        mu = self.events.Muon
        mu = mu[(mu.pt > cuts.Muon.pt) & (abs(mu.eta) < cuts.Muon.eta) & (mu.IsolationVar < cuts.Muon.iso)]
        el = self.events.Electron
        el = el[(el.pt > cuts.Electron.pt) & (abs(el.eta) < cuts.Electron.eta) & (el.IsolationVar < cuts.Electron.iso)]
        self.events["MuonGood"] = delphes_leptons(mu, 13)
        self.events["ElectronGood"] = delphes_leptons(el, 11)
        leptons = ak.concatenate((self.events.MuonGood, self.events.ElectronGood), axis=1)
        self.events["LeptonGood"] = leptons[ak.argsort(leptons.pt, ascending=False)]

        # Jets: pt, eta and deltaR cleaning against the good leptons
        # (same idiom used inside lib/jets.py::jet_selection; True when there are no leptons)
        jets = self.events.Jet
        clean = ak.all(jets.metric_table(self.events.LeptonGood) > cuts.Jet.dr_lepton, axis=2)
        self.events["JetGood"] = jets[(jets.pt > cuts.Jet.pt) & (abs(jets.eta) < cuts.Jet.eta) & clean]
        # b-tagging: Delphes stores the working points as bits of the BTag field
        jg = self.events.JetGood
        self.events["BJetGood"] = jg[((jg.BTag >> cuts.Jet.btag_bit) & 1) == 1]

    def count_objects(self, variation):
        # `n<coll>` is the naming used by the cut functions (e.g. get_nObj_min)
        for coll in ["MuonGood", "ElectronGood", "LeptonGood", "JetGood", "BJetGood"]:
            self.events[f"n{coll}"] = ak.num(self.events[coll])
