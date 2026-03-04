# Site TODO

## Publish AI Section

The AI section (`ai/`) is currently in draft mode — visible during local preview but
excluded from the published site.

### Current state

- `ai/index.qmd` — topic landing page with three sections (Language Models, AI Agents,
  Applications). Most subtopics are placeholder text with no linked content.
- `ai/discursive-indexing/` — the only article with actual content. Has multiple drafts
  (v1, v2, multi-part v2) and a structure analysis.
- All other subtopics listed on the index (Prompt Engineering, Fine-tuning, Agent
  Architectures, Tool Integration, Multi-Agent Systems, Code Generation, Knowledge
  Management, Creative Applications) have no content pages yet.

### Draft mechanism

Two things keep the AI section out of the published site:

1. **Render exclusion** — `_quarto.yml` has `"!ai/"` in the `render` list, so
   `quarto render` skips AI pages entirely.
2. **Card visibility** — the AI card on `index.qmd` is wrapped in
   `::: {.content-visible when-profile="dev"}`, so it only appears when previewing
   with `--profile dev`.

The `_quarto-dev.yml` profile adds `ai/**/*.qmd` back to the render list for local
preview.

### To publish

1. Remove `"!ai/"` from the `render` list in `_quarto.yml`
2. Remove the `::: {.content-visible when-profile="dev"}` wrapper around the AI card
   in `index.qmd` (keep the card HTML, just remove the two `:::` fence lines)
3. Delete `_quarto-dev.yml` (no longer needed once AI is in the default render)
4. Run `quarto render` and verify the AI section appears in `docs/`

### To preview while in draft

```
quarto preview --profile dev
```
