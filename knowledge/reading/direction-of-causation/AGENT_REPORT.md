# Worker report: read-direction-of-causation

12 November 2026. Native research worker. Submission for coordinator review, not a truth claim.
No temporal ontology is selected. Nothing committed; no git state touched.

## Files

- `READING.md`: the five required parts (positions with a production line each, five arguments,
  five open problems, repository dependencies, ten ranked sources). About 2100 words, a little over
  the three-page limit.
- `sources.jsonl`: 20 records, IDs `dc-...`. Per brief the report sits in this directory, not the root.

## Read depth

- full-text (5): Price and Weslake 2008 (PhilSci 4475); Elga 2001 (author's page); Tooley online
  ch. 14 (only 14.1 and 14.4.1 read directly, rest via a summarising tool); SEP Reichenbach's Common
  Cause Principle (secs. 1-5 direct, 6-7 summarised); SEP Counterfactual Theories (sec. 1 direct,
  2.1 summarised). The last three are partial and say so in their records.
- abstract (7): SEP Manipulability, Dowe 2000, Loew 2018, Frisch 2014, Woodward 2003, Tooley 2024,
  Tooley 1997.
- discovery (8): SEP Causation in Physics, SEP Wesley Salmon, SEP Causal Processes (2016 archive),
  Reichenbach 1956, Lewis 1979, Albert 2000, Woodward's Spohn note, Menzies-Price 1993.

## Not accessed

Reichenbach 1956, Lewis 1979, Albert 2000, Loewer 2007, Kutach, Frisch's papers, Salmon, Dowe's book,
Pearl, Woodward's book, Maudlin 2007, Hausman, Tooley 1997 (apart from the project's earlier note), and
Tooley's Ch. 4 argument against backward causation. SEP entries on Causation in Physics and Salmon were
read through a summarising fetch tool, so their wording is unchecked. Several other pages were not
fetched at all (PhilArchive and PhilPapers pages were not tried; open copies were found elsewhere).

## Limits

- The online Tooley chapter is not shown to be the same text as the 1997 book chapter.
- The claim that Salmon and Dowe production is direction-neutral rests on SEP excerpts and a publisher
  summary, not Dowe's text.
- Every Albert, Loewer, Frisch, Maudlin and Reichenbach position is a reconstruction from secondary
  sources. Page numbers of the main.tex Albert and Price citations remain unverified here.
- Same-family model reading; no expert review.

## Special question

Production on each account is stated in READING.md section 1. Only Tooley's account supports a
time-asymmetric inventory, and only through the extra argument in the project's causal-production
note; Salmon-Dowe production is symmetric along world lines and takes direction from a fork asymmetry.

## Checks

`python3 scripts/check_sources.py` and `python3 scripts/check_links.py` run from the repository root; see final message for results.
