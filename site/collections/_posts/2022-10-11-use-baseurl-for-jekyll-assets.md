---
title: "Use baseurl to specify the location of assets in Jekyll"
layout: post
date:   2022-10-11 10:45:00 -0500
categories:
  - web
  - jekyll
---

Jekyll's `baseurl` parameter is a path prefix (i.e. the subpath of your site) which is
specified in the `_config.yml` file. Specify this parameter, for example, for GitHub
project pages where the path prefix is the name of the repository.

In your content then, specify static assets by this path so that in the future you
can easily change the prefix without breaking your site.

E.g., an image location in a Markdown post might look like this:

```
{% raw %}![My Image]({{ site.baseurl }}/assets/images/my-image.png){% endraw %}
```
