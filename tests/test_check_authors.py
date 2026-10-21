"""Offline tests for scripts/check_authors.py comparison rules, using real cases found
in the 2026-10-20 knowledge-base sweep. No network."""
import importlib.util
from pathlib import Path
import unittest

PROJECT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_authors", PROJECT / "scripts/check_authors.py")
ca = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ca)


def src(*names):
    return [ca.split_name(n) for n in names]


def levels(recorded, source):
    return [level for level, _ in ca.compare(recorded, source)]


class RealErrors(unittest.TestCase):
    def test_wrong_given_name_flagged(self):  # Loriani et al., ico-qrf records
        self.assertEqual(levels(["Sebastian Loriani"], src("Sina Loriani")), ["FLAG"])
        self.assertEqual(levels(["Alfred Grinbaum"], src("Alexei Grinbaum")), ["FLAG"])
        self.assertEqual(levels(["Costantino Branciard"], src("Cyril Branciard")), ["FLAG"])

    def test_wrong_author_flagged(self):  # Kostelecky-"Mewes", Martinetti-"Rovelli"
        self.assertEqual(levels(["V. Alan Kostelecký", "Matthew Mewes"],
                                src("V. Alan Kostelecký", "Arnaldo J. Vargas")), ["FLAG"])
        self.assertEqual(levels(["Pierre Martinetti", "Carlo Rovelli"], src("Pierre Martinetti")), ["FLAG"])

    def test_unsupported_expansion_flagged(self):  # "Nicolas" for printed "Nick"
        self.assertEqual(levels(["Nicolas Ormrod"], src("Nick Ormrod")), ["FLAG"])


class FalsePositivesAvoided(unittest.TestCase):
    def test_transliteration(self):
        self.assertEqual(levels(["Philipp A. Höhn"], src("Philipp A. Hoehn")), [])
        self.assertEqual(levels(["Markus P. Müller"], src("Markus P. Mueller")), [])

    def test_suffix_and_role(self):
        self.assertEqual(levels(["Hugh Everett III"], src("Hugh Everett")), [])
        self.assertEqual(levels(["Alain Aspect (introduction)"], src("Alain Aspect")), [])

    def test_initials(self):
        self.assertEqual(levels(["H. Poincaré"], [("poincare", ["m", "h"])]), [])
        self.assertEqual(levels(["V. Alan Kostelecky"], src("Alan Kostelecky")), [])

    def test_particles(self):
        self.assertEqual(levels(["Fabio Di Pumpo"], src("Fabio Di Pumpo")), [])
        self.assertEqual(levels(["Anne-Catherine de la Hamette"], src("Anne-Catherine de la Hamette")), [])

    def test_collaboration_and_et_al_skipped(self):
        self.assertEqual(levels(["J. P. Lees et al. (BABAR Collaboration)"], src("J. P. Lees")), [])

    def test_packed_entry_warns_not_flags(self):
        self.assertEqual(levels(["Richard Schmoetten, Jake E. Palmer, Jacques D. Fleuriot"],
                                src("Richard Schmoetten")), ["WARN"])


class Identifiers(unittest.TestCase):
    def test_doi_preferred_and_datacite_ignored(self):
        self.assertEqual(ca.identifiers({"url": "https://doi.org/10.1126/sciadv.aax8966"}),
                         ("10.1126/sciadv.aax8966", None))
        self.assertEqual(ca.identifiers({"url": "https://arxiv.org/abs/2604.00092v1",
                                         "version": "DOI 10.48550/arXiv.2604.00092"}), (None, "2604.00092"))

    def test_old_style_arxiv(self):
        self.assertEqual(ca.identifiers({"url": "https://arxiv.org/html/hep-th/0208013v3"}),
                         (None, "hep-th/0208013"))


if __name__ == "__main__":
    unittest.main()
