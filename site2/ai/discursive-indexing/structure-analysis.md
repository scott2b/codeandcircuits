# Structure Analysis: Discursive Indexing Article

## Current Section Inventory

1. Opening paragraph (no heading) - defines concepts
2. **Introduction** - sets up question and thesis
3. **Why "Write Like Hemingway" Works** - hooks reader, previews article
4. **The core fact: LLMs don't "know" authors** - technical foundation
5. **What the model actually learns about "Hemingway"** - training signals
6. **Names as stylistic shortcuts** - cultural compression intro
7. **If models are "next-token predictors," why does this work?** - semantic conditioning
8. **Why this is different from "think step by step"** - distinguishes from procedural
9. **Why author names are especially powerful triggers** - reinforces thesis
10. **Why this does _not_ imply true stylistic understanding** - limitations
11. **The general rule** - first synthesis
12. **Why obscure authors don't work the same way** - counter-examples
13. **An experiment with a fictional author** - empirical demonstration
14. **What happens when style is defined explicitly** - shows solution
15. **Why Claude and ChatGPT behaved differently** - platform policies
16. **Why this matters** - summary
17. **Stylistic fidelity scales with discourse density** - deeper thesis restatement
18. **Why discourse beats corpus size** - three signal types
19. **What the model actually learns** - joint distribution
20. **Why "hundreds of novels" may still underperform** - explains failures
21. **Observable consequences** - predictions
22. **Practical implication** - brief advice
23. **Bottom line** - second synthesis
24. **The takeaway** - third synthesis
25. **Implications for authorship and authorial "voice"** - 17-item list
26. **Implications for writers** - practitioner advice
27. **Implications for Unknown or Emerging Writers** - 10 subsections
28. **Glossary of concepts** - technical background
29. **The missing unifying term** - conceptual framing
30. **Who is closest to "getting it"** - research landscape
31. **Why this is under-discussed** - meta-analysis
32. **Why this matters (big picture)** - final synthesis
33. **References**

---

## Structural Issues

### 1. Multiple summary/synthesis sections
The article has at least 5 "summary" moments:
- "The general rule" (section 11)
- "Why this matters" (section 16)
- "Bottom line" (section 23)
- "The takeaway" (section 24)
- "Why this matters (big picture)" (section 32)

These repeat similar points and fragment the argument.

### 2. Theory comes late
Semantic conditioning (section 7) appears AFTER examples. The mechanism should ground the examples, not follow them.

### 3. Two introductions
Both the opening paragraph and "Why Write Like Hemingway Works" function as introductions. The article starts twice.

### 4. Discourse thesis is split
The core argument about discourse > corpus appears in:
- Section 6 (Names as stylistic shortcuts)
- Section 17-23 (Stylistic fidelity scales with discourse density + subsections)

These should be unified.

### 5. Glossary buried at end
The glossary contains foundational concepts (feature superposition, distributional steering) that would help readers understand earlier sections. Consider moving key concepts earlier or integrating them.

### 6. Implications section sprawl
"Implications for authorship" is a 17-item bullet list. Could be grouped thematically.

---

## Proposed Restructure

### Part I: The Phenomenon
**Goal**: Hook reader, establish observable fact

- Introduction (merged: current intro + Hemingway section)
- The puzzle: Why Hemingway works but obscure authors don't

### Part II: The Mechanism
**Goal**: Explain HOW this works technically

- LLMs as next-token predictors (what they don't contain)
- Semantic conditioning: names as latent space selectors
  - **[INSERT Reynolds signifier concept here]**
  - **[INSERT mimetic proxy concept here]**
- Why this differs from "think step by step"
- Feature superposition (moved from glossary)

### Part III: The Role of Discourse
**Goal**: Explain WHY some names work better than others

- What models learn about "Hemingway" (training signals)
- Names as culturally compressed labels
- Discourse density > corpus size (unified section)
- Why obscure authors fail

### Part IV: Demonstration
**Goal**: Empirical evidence

- The Frank Calderon experiment
- Platform differences (Claude vs ChatGPT)

### Part V: Implications
**Goal**: So what?

- For understanding AI (consolidated list)
- For writers (practical)
  - **[INSERT cultural archetype / teacher-student advice here]**
- For emerging writers supplying samples

### Part VI: Context & References
**Goal**: Scholarly framing

- Research landscape (who is working on this)
- Why under-discussed
- References

---

## Reynolds & McDonell Content Placement

### Item 1: Signifiers supervening on infinite examples
> "Direct specifications [i.e. signifiers] can supervene on an infinity of implicit examples, like a closed-form expression on an infinite sequence, making them very powerful and compact." (p. 5)

**Placement**: Part II, within "Semantic conditioning" section

**Rationale**: This explains WHY a single token can do so much work. It's the theoretical foundation for the mechanism. Should appear right after explaining that "Hemingway" nudges toward a latent space region.

### Item 2: Mimetic proxy / specification by compressed index
> "Rather than indicative of an action or instruction, stylistic markers operate as compressed indexes to latent representations. This is specification by mimetic proxy which is mechanistically similar to direct [declarative] specification, except that the signifier keys behaviors from memespace/cultural consciousness instead of naming the behavior directly." (p. 5)

**Placement**: Part II, immediately following Item 1, or as part of the same passage

**Rationale**: This distinguishes mimetic proxy from direct specification. It connects to the "Why this is different from think step by step" point but is more fundamental—should come earlier in the theoretical exposition.

### Item 3: Practical advice - cultural archetypes (teacher/student)
> "Practical consideration for authors: take advantage of mimetic proxy + cultural archetypes. E.g. discussion between teacher & student"

**Placement**: Part V, within "For writers (practical)" section

**Rationale**: This is actionable advice for practitioners. Fits with the existing practical implication content. Could be expanded with examples of other cultural archetypes beyond teacher/student.

---

## Summary of Moves

1. **Merge** opening paragraph + Introduction + Hemingway section into one cohesive intro
2. **Move** theoretical mechanism (semantic conditioning) earlier
3. **Consolidate** discourse thesis into one section
4. **Move** key glossary concepts (feature superposition) into mechanism section
5. **Consolidate** multiple synthesis sections into one "Bottom line"
6. **Group** implications thematically
7. **Add** Reynolds content at identified insertion points
