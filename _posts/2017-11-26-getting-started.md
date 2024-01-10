---
layout: post
title: salam
featured-img: sleek
mathjax: true
---

# Getting started

salam . bia bebin chekhabare
## Writing content

### Posts

Create a new Markdown file such as `2017-01-13-my-post.md` in `_post` folder. Configure YAML Front Matter (stuff between `---`):

```yaml

---
layout: post # needs to be post
title: salam # title of your post
featured-img: sleek #optional - if you want you can include hero image
---

```

#### Images

salam 

### Pages

chekhabar

### Images TODO

ina be nazar matn mohemmie . bekhan va biamooz

Introduce gulp optimization

Breakpoint | Image Type | Width | Retina
------------ | ------------ | ------------- | -------------
xs |Post Thumb | 535px | 1070px
sm |Post Thumb | 500px| 1000px
md |Post Thumb | 329.375px | 658.75px
lg |Post Thumb | 445.625px | 891.25px
xl |Post Thumb | 353.125px | 706.25px

Breakpoint | Image Type | Width | Retina
------------ | ------------ | ------------- | -------------
xs |Post Hero | 535px | 1070px
sm |Post Hero | 500px| 1000px
md |Post Hero | 329.375px | 658.75px
lg |Post Hero | 445.625px | 891.25px
xl |Post Hero | 353.125px | 706.25px

### MathJax

If you want to use [MathJax](https://www.mathjax.org/) in your posts, add `mathjax: true` in [YAML front matter](https://jekyllrb.com/docs/frontmatter/) of your post:

```yaml
---
layout: post
title: Blog Post with MathJax
featured-img: sleek # optional - if you want you can include name of hero image
mathjax: true # add this line in order to enable MathJax in the post
---
```

#### Example

In N-dimensional simplex noise, the squared kernel summation radius $r^2$ is $\frac 1 2$
for all values of N. This is because the edge length of the N-simplex $s = \sqrt {\frac {N} {N + 1}}$
divides out of the N-simplex height $h = s \sqrt {\frac {N + 1} {2N}}$.
The kerel summation radius $r$ is equal to the N-simplex height $h$.

$$ r = h = \sqrt{\frac {1} {2}} = \sqrt{\frac {N} {N+1}} \sqrt{\frac {N+1} {2N}} $$
Happy hacking!
