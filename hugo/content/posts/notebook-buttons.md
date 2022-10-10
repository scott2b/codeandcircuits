---
title: "Code Notebook Buttons in Hugo"
description: "My current approach to providing Colab and GitHub link buttons on my published notebooks in Hugo is crude but effective."
date: 2022-10-07T12:25:48-05:00
draft: true
---

My current approach to providing Colab and GitHub link buttons on my published notebooks
in Hugo is crude but effective. I have the following template snippet defined for Hugo at
`layouts/shortcodes/notebook-buttons.html`:


```
{{ $path := .Get 0 }}
<div>
  <a style="display: inline-block; height: 52px;" href="https://colab.research.google.com/github/{{ $path }}"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a>
  <a class="github-button" href="https://github.com/{{ $path }}" aria-label="View on GitHub">View on GitHub</a>
</div>
<script async defer src="https://buttons.github.io/buttons.js"></script>
```

The buttons can then be included with a shortcode like the following:

```
{{</* notebook-buttons "username/repo/path/to/ipynb/file.ipynb" */>}}
```

where the quoted path should match the ipynb file path in GitHub. There is some gross
styling here that I'd like to improve upon, but this is a good-enough-for-now solution.

## "Open in Colab" with Markdown

Note that if you just need the "Open in Colab" button, you can do this with Markdown:

```
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/username/repo/path/to/ipynb/file.ipynb)
```
