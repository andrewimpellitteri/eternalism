# Worker report: read-persistence

12 November 2026. Native reading lane, shared checkout, not committed. Submission for review, not a truth claim. No temporal ontology is selected.

## Files

- `knowledge/reading/persistence/READING.md`: the five required parts (positions, five arguments, five open problems, repository dependencies, ten ranked sources). Roughly 1,900 words, which may run slightly over three printed pages.
- `knowledge/reading/persistence/sources.jsonl`: 20 records, prefix `pers-`.
- This report (written here, not at the repository root, per the native-run rules).

## Read depth

- Full-text (6): Gibson and Pooley 2006 (partial: Secs. 1-2, parts of 3-6); Gilmore 2006 (Secs. 0-4.1 only); Balashov's persistence-and-multilocation chapter (Secs. 1-2 and D1-D13); Sider 1997 (Secs. 1-3); SEP Temporal Parts and SEP Identity Over Time (both secondary, partial; some sections via a summarising fetch tool, flagged in the records).
- Abstract (6): Haslanger 2003 (headings and opening of Sec. 2); Gilmore 2002; Balashov 2000, 2002, 2005; Parfit 1984 ch. 10 (search excerpts of a third-party copy).
- Discovery (8): SEP Personal Identity (Secs. 1-2 opening), SEP Location and Mereology (Secs. 1-2.2), IEP Persistence in Time (excerpts), NDPR review of Balashov, Haslanger's comments on Sider (excerpts), and three book/paper leads not accessed (Lewis 1986, Hawley 2001, Merricks 1999).

## Not accessed

Lewis 1986 and 1976; Hawley 2001; Sider 2001 and 1996; Merricks 1995 and 1999; Zimmerman 1996; Balashov's 2010 book; Hales and Johnson 2003; Saunders 2002; Parfit 1984 as a whole and Parfit 1971. Haslanger 2003 text extraction was broken, so only headings and an opening were used. PDF extraction of Gibson-Pooley and Gilmore dropped spaces in places; text was read by search. Descriptions of unread works are marked as secondary in READING.md and the records.

## Checks

`python3 scripts/check_sources.py`: 0 errors; the 4 warnings belong to other lanes. `python3 scripts/check_links.py`: 0 broken links.

## Limitations

- Sections 6-7 of SEP Temporal Parts and Sec. 2.4, 4.1 and 4.5 of SEP Identity Over Time were read through a summarising tool and not verbatim.
- The argument reconstructions for C (Balashov) and D (Hales-Johnson) come from Gibson and Pooley's own restatements, not from the originals.
- The fairness assessment of main.tex's Part IV rests on main.tex lines 450-470, 585-660, 723-770 and the abstract; the `parts/` files were not read.
- The claim that a persistence theory (worm, endurance, stage) gives different lower bounds R in the paper's framework is our conjecture and is labelled so.

## Unresolved questions

Whether Merricks 1999 or Zimmerman 1996 already contain the paper's lower-bound-only observation; whether Balashov's chapter is the same text as the 2010 book chapter; whether the "relativity rules out presentism" premise used by Gibson and Pooley is needed for their endurantist proposal.
