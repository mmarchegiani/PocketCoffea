import awkward as ak

from .base import BaseProcessorABC


class DelphesBaseProcessorABC(BaseProcessorABC):
    '''
    Base processor for Delphes ROOT files read with coffea's DelphesSchema (tree "Delphes").
    Run with `schema: DelphesSchema` in the run options.

    Only the source of the generator weight differs from NanoAOD: the rest of the processing
    (skim, preselection, categories, weights, histograms) is inherited from BaseProcessorABC.
    Object selection and counting are still defined by the user workflow, as for NanoAOD.
    '''

    def get_genweight(self):
        # Delphes stores the generator weight(s) in the `Weight` collection; the first entry is the
        # nominal one. `fill_none` turns the option type from `ak.firsts` into a plain float array.
        return ak.fill_none(ak.firsts(self.events.Weight.Weight), 1.0)

    def export_skimmed_chunk(self):
        # coffea's uproot_writeable does not support DelphesSchema: fail early with a clear message
        raise NotImplementedError("Skimmed-file export is not supported for DelphesSchema inputs.")
