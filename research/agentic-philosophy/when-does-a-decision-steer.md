# When does a decision steer what happens?

*Coordinator note, 17 November 2026. This is a finite causal comparison and a conditional application to a field model. Its interpretation awaits independent review.*

Imagine a driver receiving a route recommendation and deciding whether to follow it. Every time we have looked, the driver has announced a decision and the vehicle has gone that way. Even a flawless record of successful trips can leave a precise question unanswered. Did the vehicle take the route because the driver selected it?

## Two routes and two mechanisms

Represent the routes by 0 and 1. Before the trip, the public sign recommends $R$. A private inspection supplies $S$, with 0 confirming the recommendation and 1 reporting that the recommended route is closed. At the next step a controller computes the verdict $V=R\mathbin{\mathrm{xor}}S$. A separate actuator then sends the vehicle down route $A=M(R,V)$. Both initial bits can be prepared in either state. In this finite system the controller is the candidate agent, and the verdict is its internal output. The complete initial state and the fixed update rules determine the whole run. The comparison changes no verdict or action by fiat.

Consider an actuator that follows the verdict, $M(R,V)=V$, and an automatic one that follows the sign, $M(R,V)=R$. Each entry below is a lawful run of each apparatus.

| Sign $R$ | Inspection $S$ | Verdict $V$ | Route with steering | Route with automatic routing |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |

If ordinary trials have $S=0$, their entire logged sequences $(R,S,V,A)$ agree point by point between the apparatuses. This remains true if we manipulate the sign, randomize its value, or run arbitrarily many ordinary trials with any distribution over signs. Both routes occur. Both verdicts track the recommendation. Every verdict matches the route. Nevertheless the verdict has no effect on automatic routing at either value of $R$.

**Exactly what do the data identify?** For a fixed sign $r$, define verdict influence by $M(r,0)\ne M(r,1)$. Among the sixteen deterministic Boolean actuators, exactly four fit every ordinary trial. The two diagonal entries are fixed; the two off-diagonal entries are free bits. The four surviving rules are verdict, sign, AND and OR. Their influence holds, respectively, at both signs, neither sign, only sign 1, and only sign 0. One disagreement trial distinguishes verdict from sign *if those are the only candidates*. To identify influence at both signs among all sixteen actuators requires both off-diagonal entries. Each omitted entry can be flipped independently without changing any data already gathered.

**What gives this causal force?** The trial holds the route recommendation and actuator mechanism fixed. It varies what the inspection reports and measures the resulting internal verdict and route. A necessary modeling premise for this identification is that $S$ has no separate route to the actuator and no other changing input jointly determines the verdict and route in these trials. This can be supported in the apparatus by inspecting the wiring or isolating the channel. Without that warrant the bypass $A=R\mathbin{\mathrm{xor}}S$, computed independently of $V$, reproduces even the four disagreement/ordinary records of genuine steering. A physically independent test of the verdict-to-actuator connection would then be needed. The choice of the controller boundary also matters. The wider vehicle may steer effectively when the driver's verdict is bypassed.

## Which past can be the same?

Three ordinary claims have different truth conditions in this example.

1. **“With exactly the same complete initial state and laws, I could have turned the other way.”** False of either deterministic apparatus. Running the same update functions on the same inputs returns the same outputs.
2. **“With the same road recommendation and mechanism, a different inspection result could have led me to select and take the other route.”** True with steering, false with automatic routing for the route actually taken. There is a real difference in an earlier physical bit. These trials test the efficacy of judgment across reasons. They do not test the ability to choose otherwise with all one's reasons and physical state fixed.
3. **“My judgment made a difference on this trip.”** In the steering model, holding $R=r$ fixed while varying $V$ through the inspection channel changes $A$ at both signs. That warrants a specific counterfactual dependence. Whether this mode of judgment belongs to the person, whether the person endorses it, and whether it grounds moral responsibility require features a two-bit controller lacks.

Which facts should be held fixed depends on the claim under test. For a capacity to respond to evidence, preserving the mechanism and varying the evidence gives the claim an independently testable consequence. For a claim of different lawful continuations from an identical complete past, a change in an earlier input defeats the comparison. Passing the first test cannot substitute for passing the second.

## Grant the incompatibilist an open physical future

Change the model so that a genuinely stochastic bit $U$ is drawn after the complete pre-decision state, with $P(U=1)=1/4$ independently of $R,S$. Set $V=R$ xor $S$ xor $U$. A connected actuator takes $A=V$. A bypass receives the same draw $U$ and computes $A=R$ xor $U$ without receiving the verdict. For each fixed initial state both routes now have positive probability in **both** models. On every ordinary trial ($S=0$), the joint distribution of verdict and route is identical, even conditional on the complete pre-decision state. In each model the route follows the public recommendation with probability $3/4$.

With $R$ fixed and $S$ changed from 0 to 1, the probability of taking the publicly recommended route changes from $3/4$ to $1/4$ under steering and stays $3/4$ under bypass. This comparison uses observable conditional probabilities across preparations and needs no pairing of individual random draws across possible worlds. The verdict channel assumption still matters. Thus granting two genuinely lawful futures after the identical past leaves the question of guidance unresolved. Conversely, guidance can coexist with residual chance: the connected controller changes the outcome probabilities without choosing the random draw.

## Influence and the ability to secure an outcome

Even genuine influence at every setting can fall short of a usable ability. Suppose an intact actuator implements $A=V\mathbin{\mathrm{xor}}H$, where $H$ describes an ordinary or reversed steering linkage. Grant the controller access to either command. Holding either linkage fixed, changing the command changes the route. If the controller has no information about $H$, must issue a single command, and gets no feedback before arrival, it cannot guarantee route 0. For each $h$ there exists a successful command $v=h$, but no single $v$ succeeds for every $h$. Giving the controller an accurate pre-action observation of $H$ makes the policy $V(H)=H$ successful in both cases. Under a uniformly random independent $H$, even a randomized command independent of $H$ succeeds with probability exactly one half.

Thus an agent's records can matter to what it can *secure*, even when those records change neither the mechanism's causal power nor the possible routes. A guarantee is a demanding conception of ability. An agent can have partial skill, make a reasonable choice, or take responsibility for an uncertain outcome without being able to guarantee success.

## Connection to the field and to temporal ontology

In the [massive-field comparison](../horizons/finite-records-and-possible-futures.md) a change of source was a free input. It can instead be computed inside this example. Let $L=\partial_t^2-\Delta+m^2$. Choose a real smooth spacetime bump $b$ localized just after the decision, overlapping a later field reading with $F(b)\ne0$. Start the field from zero before the bump and prescribe the coupling $J=A\,Lb$. The unique response is $\phi=A b$. Once $R,S$ and the apparatus are specified, the registers, source and field all follow by the same rules in every run. With the same $R$ and differing $S$, the steering apparatus can give distinct later readings with identical field histories before the decision. The automatic apparatus cannot. The combined physical pasts differ in the inspection register. This is a one-way coupling with a prescribed source profile, an illustration of mediation rather than a model of human deliberation or an energetically closed vehicle.

A stepwise execution and a table of all complete runs agree on every comparison above if the table retains the preparation labels, mechanism, and admissible variations. A table of the single actual run discards precisely the comparisons needed to test steering. Writing complete runs down assumes a mathematical representation; attributing existence to all future events requires a philosophical bridge. Conversely, adding an undetermined outcome would establish alternatives without identifying who controls them. The model grants causal direction through its wiring and update order. It supplies no derivation of the direction of time.

## What this adds to the existing argument

List distinguishes physical and agential possibilities and explicitly considers adding a success-if-tried condition to deal with outcomes outside an agent's control. Fischer and Ravizza distinguish responsiveness of the operative mechanism from ownership of that mechanism; their Frankfurt discussion also explains why failure of a simple alternative-action test need not defeat responsibility. Pearl explains which mechanism-invariance assumptions make an intervention interpretable. These are substantive predecessors. The four-entry test makes a narrow use of them: it exhibits the precise observational ambiguity, the missing comparisons, and the bypass that defeats even those comparisons if their channel is misidentified. Read depth for this note is full text at the cited passages, with no priority claim for the example or the underlying principles. [List, modal account of abilities and footnote 32](https://philpapers.org/archive/LISFWD.pdf) · [Fischer and Ravizza, chapter 2, printed pp. 37–39](https://www.filosoficas.unam.mx/docs/942/files/Fischer%20Guidance%20control%20and%20RR.pdf) · [Pearl, §§3.2–3.2.1](https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf) · [Project reading on agency and the open future](../../knowledge/reading/agency-fatalism-open-future/READING.md)

The remaining philosophical dispute is specific. Someone who regards the steering comparison as an account of freedom must defend why this controller and these variations capture the agent's own capacity. Someone who requires alternatives with the identical total past must explain how an additional branching event supplies control over which branch occurs. Neither side settles that dispute by counting the available futures.
