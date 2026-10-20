You are auditing bibliographic source records from a research knowledge base. The file below lists 17 records (R01–R17). Each has a title, authors, url and, for most, a version string giving the arXiv version and/or the journal, volume, pages and year.

For every record, check each field against primary landing pages:
- arXiv abstract pages (https://arxiv.org/abs/ID) for titles, author lists, version dates;
- the Crossref API (https://api.crossref.org/works/DOI) or the DOI resolver for journal metadata and author lists;
- the publisher page when needed.

Check every author name listed, including given names, and check that the url and any DOI point to this exact work. Some records may be fully correct and some may contain errors. Do not assume either way.

Rules:
- Mark `defect` only when a primary source you actually read contradicts a field. Name the field(s) and quote what the primary source says.
- Mark `unverifiable` if you could not reach a primary source for a field you needed. Do not guess from memory.
- Mark `ok` if every field you checked matches.
- Formatting differences (capitalization, "et al.", abbreviations of the journal name, a missing optional field) are not defects.

Output exactly one JSON object per line, one per record, in order R01..R17, and nothing else after the last line:
{"item": "R01", "verdict": "ok" | "defect" | "unverifiable", "fields": ["authors", ...], "evidence": "short quote or value from the primary source, with its URL"}

Records:
