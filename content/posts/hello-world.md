---
title: "Hello World"
date: 2026-08-31T00:00:00Z
draft: false
tags: ["meta", "hugo"]
summary: "Why this blog exists and how it's built."
---

This is the first post. The site is built with [Hugo](https://gohugo.io/) using the
[PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, and deploys to GitHub
Pages automatically on every push to `main`.

## Writing a new post

```bash
hugo new content posts/my-new-post.md
```

That creates a draft in `content/posts/`. Drafts are excluded from production builds, so
flip `draft: true` to `draft: false` when it's ready to publish.

## Previewing locally

```bash
hugo server -D
```

The `-D` flag includes drafts. The dev server live-reloads on save at
<http://localhost:1313>.

## Publishing

```bash
git add .
git commit -m "Add new post"
git push
```

The GitHub Actions workflow builds the site and publishes it. No `public/` directory is
ever committed.
