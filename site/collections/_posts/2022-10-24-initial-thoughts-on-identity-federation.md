---
title: "Initial thoughts on federating identity from the get-go"
layout: post
date:   2022-10-24 15:00:00 -0500
categories:
  - devops
  - identity-management
---

I've recently begun working my way through Juval Löwy's
[Righting Software](https://www.amazon.com/Righting-Software-Juval-L%C3%B6wy/dp/0136524036/){:target="_blank"}
which has so-far struck me as a really rare find on the architectural aspects of
software engineering. The basic foundation of Löwy's ideas seem to be this: Stop
decomposing systems along the lines of functionality, and instead start thinking in
terms of volatility.

It is a slightly provocative idea because, first of all, functional decomposition is
nearly ubiquitous, and secondly, how the heck do you identify volatility? I'm still
working my way through the book, so I'll refrain from further comment on that, but as I've
been reading and thinking about existing systems (or systems I've worked on in the past)
one aspect of systems development really stood out for me as being a major stumbling
block in the volatilty of growing enterprise systems -- user identity.

Here's the thing: a lot of popular application frameworks give you authentication built
right in, which can be really great if you're trying to get something up and running
quickly. Even frameworks that don't have builtin concepts of identity usually have a ton
of easily findable tutorials on how to build it yourself. In either case, as soon as
your organization goes from one application to more than one, how do you handle that?
Identity, authentication, and authorization pervade nearly every aspect of an application,
so you can almost guarantee that this won't be a simple refactoring job. The core
problems of factoring your auth system into something usable with growth is a key
example of enterprise volatility in a nutshell.

I am developing some thoughts on some potential principles for dealing identity system
rot as a fundamentally latent form of volatility, which will be forthcoming, but I
think it will essentially come down to this: If you can currently imagine how your
organization will likely grow into more than one application requiring identity
management, then you're probably better off not using your framework's builtin
authentication system. Call me crazy, but ripping out even just dozens of
foreign keys downstream to accomodate a newfangled identity system in your legacy
application that is live with active users just doesn't strike me as fun. Instead, I'm
leaning toward a policy of mitigating early on, at the very least using UUID user IDs
from the outset, but also, probably using an external identity management platform from
the get-go.
