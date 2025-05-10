
## Development

Obsolete:

```
cd site
bundle exec jekyll serve --livereload
```

New:

```
cd site2
quarto preview
```

## Deploy

Currently building locally because GitHub is being stupid.

```
cd site2
quarto render
```

Merge changes into pub and push

## Troubleshooting

To force re-rendering a file, e.g.:

```
quarto render posts/2025-05-09-obsidian-environment/index.qmd --execute
```
