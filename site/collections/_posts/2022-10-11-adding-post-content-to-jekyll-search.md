---
title: "Adding Post content to Jekyll search"
layout: post
date:   2022-10-11 10:55:00 -0500
categories:
  - web
  - jekyll
---

I used [this tutorial at webjeda.com](https://blog.webjeda.com/instant-jekyll-search/){:target="_blank"}
to add simple search capabilities to my Jekyll site.

The article recommends against including the full content in the search config, stating:

> You can also add post.content to this. But I recommend not to. Adding content will result in a huge JSON file and also inaccurate search result.

Since I am just getting started, I am not too concerned about the search json getting
too large (yet) -- I want to see how far this simple approach will take me before I
need to change tack.

The "inaccurate search result" is not really explained, and is not intuitive to me. I
suspect it is more this, which I found: using the following seems to break the search
entirely (although I am not sure why):

⚠️ Probably don't do this:

```
{% raw %}"content"  : "{{ post.content | strip_html | strip_newlines }}"{% endraw %}
```

Instead, I've found that using cgi_escape, which replaces spaces with `+` signs, instead
of `strip_newlines` seems to do the trick without breaking the search:

✅ Do this instead:

```
{% raw %}"content"  : "{{ post.content | strip_html | cgi_escape }}"{% endraw %}
```

