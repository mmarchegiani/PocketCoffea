import awkward as ak

import copy

from .base import BaseProcessorABC
from ..utils.configurator import Configurator
from ..parameters.lumi import goldenJSON
from ..parameters.btag import btag

class genWeightsProcessor(BaseProcessorABC):
    def __init__(self, cfg: Configurator) -> None:
        super().__init__(cfg)
        self.output_format = {
            "sum_genweights": {},
            "cutflow": {
                "initial": {s: 0 for s in self.cfg.datasets},
                "skim": {s: 0 for s in self.cfg.samples}
            }
        }

    def load_metadata(self):
        self._dataset = self.events.metadata["dataset"]
        self._sample = self.events.metadata["sample"]
        self._year = self.events.metadata["year"]
        self._btag = btag[self._year]
        self._isMC = self.events.metadata["isMC"] == "True"

        if self._isMC:
            self._era = "MC"
            self._xsec = self.events.metadata["xsec"]
        else:
            self._era = self.events.metadata["era"]
            self._goldenJSON = goldenJSON[self._year]

    def apply_object_preselection(self, variation):
        pass

    def count_objects(self, variation):
        pass

    def process(self, events: ak.Array):
        self.events = events

        self.load_metadata()
        self.output = copy.deepcopy(self.output_format)

        self.nEvents_initial = self.nevents
        self.output['cutflow']['initial'][self._dataset] += self.nEvents_initial
        if self._isMC:
            self.output['sum_genweights'][self._dataset] = ak.sum(self.events.genWeight)

        self.skim_events()
        if not self.has_events:
            return self.output

        if self.cfg.save_skimmed_files:
            self.export_skimmed_chunk()
            return self.output

        return self.output
