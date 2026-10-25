# Boundary and echo scope fix

Task: horizons-boundary-fix. Owner: codex-horizons-boundary.
Date: 2026-10-25. User authorized a concrete bug fix in the active paper.

## Changes

- main.tex: replaced the three-diamond sandwich with exact equality to the
  closed union, supplying the missing relative-closedness argument.
- Included the late fixed-region onset boundary in the theorem and comoving
  prose (eta >= 2*pi-eta_b). The instant immediately before onset remains
  unfixed for this solution class.
- Named the rescaled field psi=a*phi in the antipodal sign-flip sentence.
- Restricted the unreal/spacelike-or-null echo interpretation to eta_b<=pi.
  After maximum expansion, an echo event can already lie in b's past.
- Removed an unjustified positive-time-separation assertion from the general
  echo proof; the distance inequality alone excludes the timelike future.
- horizons.pdf: rebuilt from the corrected source. Supporting verification
  and file hashes are recorded in this directory.

## Verification

Two successful local pdflatex passes, with all citations and cross-references
resolved on the final pass; no overfull boxes. One pre-existing underfull
bibliography line remains, with no visual clipping. Nine PDF pages rendered
and inspected as a contact sheet; affected pages 5 and 6 inspected separately
at higher size. No overlap or unreadable layout found.

Exact rational controls (times in units of pi) check a target just before,
at, and after the late onset; they also check a post-maximum echo that is
already in b's past, demonstrating why the epoch qualifier is required.
These bounded controls corroborate the analytical closure argument; they do
not prove the underlying general PDE theorem. No dependency installation.

## Scope and limits

The source repair relies on the existing three-diamond lower/upper proof and
continuity of the stated smooth solution class. It does not import the GLM
four-inequality formula rejected in GLM_FIRST_REVIEW.md. It does not complete
all source/priority checks or claim circulation clearance. Prior reviewer
reports remain historical and were not rewritten. All unrelated working
files were preserved.
