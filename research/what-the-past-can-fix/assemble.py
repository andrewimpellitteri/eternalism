"""Copy the proved sections of the two source manuscripts into parts/.

Run from anywhere with python3. main.tex inputs these fragments, so a repair
to either source reaches the unified paper by rerunning this script.
"""
import pathlib

here = pathlib.Path(__file__).resolve().parent
research = here.parent
stein = (research / "stein-gr" / "main.tex").read_text()
horizons = (research / "horizons" / "main.tex").read_text()
parts = here / "parts"
parts.mkdir(exist_ok=True)


def between(text, start, end):
    i = text.index(start)
    return text[i : text.index(end, i)]


def swap(text, old, new):
    if old not in text:
        raise SystemExit(f"expected passage not found: {old[:60]}")
    return text.replace(old, new)


def write(name, text):
    (parts / name).write_text(text.rstrip() + "\n")


write("becoming_framework.tex",
      between(stein, "\\begin{definition}\n$\\GH$", "\\section{Why one spacetime"))
write("becoming_single.tex",
      between(stein, "\\begin{proposition}\\label{prop:single}", "\\section{Results}"))
write("becoming_results.tex",
      between(stein, "\\begin{theorem}[Clifton--Hogarth]", "\\section{Proofs}"))

proofs = between(stein, "\\section{Proofs}", "\\section{Causal sets")
proofs = swap(proofs, "\\section{Proofs}\\label{sec:proofs}",
              "\\section{Proofs for Part I}\\label{sec:proofs}")
write("becoming_proofs.tex", proofs)

causets = between(stein, "\\section{Causal sets", "\\section{Energy conditions}")
causets = swap(causets, "\\section{Causal sets: an exact Stein theorem}\\label{sec:causets}",
               "\\subsection{Causal sets}\\label{sec:causets}")
causets = swap(causets, "\\section{Gödel universes are isolated}\\label{sec:godel}",
               "\\subsection{Gödel universes are isolated}\\label{sec:godel}")
write("becoming_causets.tex", causets)

energy = between(stein, "\\section{Energy conditions}", "\\section{What this shows about becoming}")
energy = swap(energy, "\\section{Energy conditions}\\label{sec:energy}",
              "\\subsection{Energy conditions}\\label{sec:energy}")
energy = swap(energy, "$M'$ above", "the spacetime $M'$ of Appendix~\\ref{sec:proofs}")
energy = swap(energy, "$\\Sigma$ as above", "$\\Sigma$ as in Lemma~\\ref{lem:D}")
energy = swap(energy, "near $w$, $v$ and the detour",
              "near the points $w$, $v$ and the detour of the proof of Theorem~\\ref{thm:main}")
write("becoming_energy.tex", energy)

phil = between(stein, "\\paragraph{The robust part of Stein's theorem.}", "\\section{Prior work}")
write("becoming_phil.tex", phil)

prior = between(stein, "Stein's theorem and its Clifton--Hogarth form are the direct predecessors",
                "\\paragraph{Note on method.}")
prior = swap(prior, "quoted in Section~\\ref{sec:intro}", "quoted after Corollary~\\ref{cor:worldline}")
write("becoming_prior.tex", prior)

write("fixing_guaranteed.tex",
      between(horizons, "\\begin{definition}\nAn event $x$ is", "\\section{The standard models}"))
models = between(horizons, "\\begin{lemma}\\label{lem:balls}", "\\section{Changing the law")
models = swap(models,
              "Whether in the closed models some local law fixes no more than\n$\\Det(b)\\cup J^-(b)$ we leave open.",
              "Theorem~\\ref{thm:massive} shows that on closed dust a local law can fix exactly\n"
              "$\\Det(b)\\cup J^-(b)$ for every $\\tau\\neq\\pi$. Whether some local law does so at\n"
              "$\\tau=\\pi$, or in other closed models, we leave open.")
write("fixing_models.tex", models)

mass = between(horizons, "The massless example is special.", "\\section{Unreality and openness}")
mass = swap(mass,
            "This proves neither that all extra fixing is lost nor a formula for $F_m$.\n"
            "The mass threshold can depend on the target and data. The result concerns a",
            "Theorem~\\ref{thm:massive} below gives the full formula; this proposition\n"
            "supplies an explicit first-order witness. The result concerns a")
head, tail = mass.split("\\subsection{A norm bound for hidden alternatives}")
write("fixing_mass.tex", head)
write("fixing_norm.tex", "\\subsection{A norm bound for hidden alternatives}" + tail)

write("logic_remark.tex",
      between(horizons, "Read $\\Box A$ at $b$", "\\section{Conclusion}"))
