# Red-team method

25 October 2026. How the multi-school red team of local fragmentalism was run,
so it can be audited, repeated or extended.

## Design

- **Target:** `../STRONGEST_VIEW.md` (the view) and `../../stein-gr/main.tex`
  (the theorem it rests on), with `../PRIOR_WORK.md` as known prior work.
- **Coverage:** positions grouped by school; one independent worker per group,
  run in parallel without sight of each other's output, so the groups cannot
  converge on a shared reading.
- **Per position:** steelman in its own terms; strongest attack aimed at a
  labelled claim (P#, R#, O#) or at the framing; whether the existing replies
  answer *this* version; severity (fatal / serious / manageable / misfire);
  best reply and what it concedes; any prior anticipation; sources with read
  depth (discovery / abstract / full-text / from-memory).
- **Rules:** no invented quotations, pages or citations; attacks must say which
  temporal notion they concern (ontology, passage, open future, causal order,
  clock time, thermodynamic arrow, time-consciousness); no votes or scores
  across positions. Workers write only their own file.
- **Synthesis (coordinator):** the attacks are merged by the claim they hit,
  not by school. Incompatible objections stay separate, and a claim counts as
  answered only if the reply survives the strongest version raised. Prior
  anticipations go to `../PRIOR_WORK.md` for checking against primary texts
  before any novelty claim changes.

## Groups

| # | Group | Positions | Status |
|---|---|---|---|
| 01 | Analytic A-theories | presentism (standard, ersatzer, thisness), growing block, shrinking tree, moving spotlight, Prior, preferred-foliation presentism (Craig, Zimmerman) | run |
| 02 | B-theory and deflationists | Smart, Mellor, Sider, Putnam–Rietdijk–Maxwell, Callender, Price, Ismael, Paul, Deng; presses O2 ("eternalism with tensed vocabulary") | run |
| 03 | Fragmentalist and relational | Fine, Hofweber–Lange, Lipman, Iaquinto–Torrengo, Dieks, Rovelli, Savitt, Arthur, Rakić, Müller | run |
| 04 | Philosophy of physics | branching space-times, causal-set becoming (Dowker, Sorkin), Earman 2008, Maudlin, quantum nonlocality and foliations, problem of time, Gödel–Yourgrau, Past Hypothesis, Malament, timelike tube theorem | run |
| 05 | Logic and metametaphysics | verbal-dispute deflation, Williamson permanentism, truthmakers and grounding, temporary intrinsics, open future (Thomason, Barnes–Cameron, MacFarlane), Dummett, coherence of the standpoint frame, McTaggart | run |
| 06 | Phenomenology and continental I | Husserl, Heidegger, Bergson (and the Einstein debate), Merleau-Ponty, Derrida, Levinas, Ricoeur | run |
| 07 | Process and speculative | Whitehead, Hartshorne, Čapek, Shimony/Stapp, Deleuze, Meillassoux, Stengers–Prigogine, Nietzsche (briefly); highest prior-anticipation risk | run |
| 08 | Historical and non-Western | Aristotle, Augustine, Kant, McTaggart, Sarvāstivāda vs Sautrāntika, Vasubandhu, Dharmakīrti, Nāgārjuna, Dōgen, kalām atomism, Mbiti and critics, Indigenous time, Zhuangzi/Mohists | **not run** (stopped to save usage) |
| 09 | Experience, theology, social time | specious present, Prosser, shared-present conversation, deliberation and the open future, temporal biases, divine eternity and Craig, open theism, Kristeva, Hägglund, Hartog, Fabian's coevalness, Benjamin | **not run** (stopped to save usage) |

To run a missing group, give one worker the brief below plus the group's row.

## Worker brief (verbatim)

### Red-team brief (shared by all red-team workers)

You are red-teaming a philosophical position on behalf of its author, who wants it attacked as hard as possible from every school of thought about time.

## Targets (read both in full first)
1. /Users/andrew/eternalism/research/local-fragmentalism/STRONGEST_VIEW.md  — "local fragmentalism": each event b has its own reality (its fragment) F(b) = J^-(b), its causal past; no shared present; tensed facts are standpoint-relative; tenseless facts are standpoint-invariant; principles P1–P7, results R1–R9, objections O1–O13 with replies.
2. /Users/andrew/eternalism/research/stein-gr/main.tex — the mathematical paper the view rests on (Stein/Clifton–Hogarth becoming theorem extended to general relativity under local covariance). Read at least the abstract, introduction, framework, results statements, and the philosophical discussion section.
Also skim /Users/andrew/eternalism/research/local-fragmentalism/PRIOR_WORK.md (what prior work is already known).

## Your job
For EACH position in your assigned list:
1. **Steelman** the position in 3–6 sentences, in its own terms (not as a foil).
2. **Strongest attack(s)** a sharp defender of that position would make on local fragmentalism (and, where relevant, on the bridge from the Stein-GR theorem to the metaphysics). Target specific labelled claims (P#, R#, O#, a premise, a definition). Prefer attacks on premises and on the bridge from mathematics to metaphysics over attacks on the theorem itself. Include attacks that say the whole framing is confused, if that is what the school would say.
3. **Already answered?** Say whether STRONGEST_VIEW already answers it (cite O#/R#) and whether that answer actually works against THIS version of the objection. Be candid; do not defend the view out of politeness.
4. **Severity:** fatal / serious / manageable / misfire, with one line of justification.
5. **Best available reply** (if any) in 2–4 sentences, and what concession it would cost.
6. **Prior anticipation:** flag any case where the school ALREADY holds something close to local fragmentalism (e.g. "an occasion's world is its causal past"), since that bears on novelty. Be specific about work and claim.
7. **Sources** for the position: author, title, year, and a locator if you have one. Label read depth honestly: discovery / abstract / full-text / from-memory. Use web search to confirm bibliographic details where you can.

## Rules
- Never invent quotations, page numbers, theorem numbers or citations. Paraphrase unless you have the exact text in front of you (from a fetched page), and then give the locator. "From memory" is acceptable for a well-known view but must be labelled.
- Distinguish: temporal ontology, objective passage, determinism/open future, causal order, clock time, the thermodynamic arrow, and time-consciousness. Say which one each attack concerns.
- Agent votes and citation counts are not arguments. Do not average or score positions.
- Write ONLY your assigned output file. Do not edit any other file. Do not commit. Do not install anything. Do not launch subagents.
- Length: thorough but dense; about 250–600 words per position, more for the most dangerous ones.

## Output format (markdown)
- Title line: `# Red team: <group name>`
- Date line: 25 October 2026; list of positions covered.
- One section per position, with the 7 headings above (bold labels fine).
- A final section **"Top threats from this group"**: rank the 3 most dangerous attacks, and say which single repair to the view would do the most good.
- A final section **"Prior anticipations found"** (may be "none").

When done, reply with a summary under 200 words: the top 3 threats and any prior anticipations.
