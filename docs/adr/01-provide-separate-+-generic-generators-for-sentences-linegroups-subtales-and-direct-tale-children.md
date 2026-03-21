# Provide separate + generic generators for sentences, linegroups, subtales and direct tale children

**Status:** accepted
**Date:** 2026-03


## Summary

In the context of heterogeneous tale content (sub-tales, prose, verse), facing the need for both flat sentence extraction and structured rendering, we decided to offer type-specific + generic children iterators with polymorphic rendering, to accept increased API surface in return for flexible and composable rendering logic.



## Context

In a tale (`<div n="1">`), there may be headings (`<head>`), sub-tales (`<div n="2">`), paragraphs (`<p>`), and line groups (`<lg>`, used for verses, poems).
Sub-tales have their own headings, paragraphs, line groups.
Sentences are inside headings, paragraphs or line groups.
See TEI P5 element reference about [div][div], [head][head], [p][p], [lg][lg], [s][s].

[div]: https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-div.html
[head]: https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-head.html
[p]: https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-p.html
[lg]: https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-lg.html
[s]: https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-s.html

When working with a tale, we are interested either in a tale's number, tale's heading, or the tale's content.
Each of these is accessible through a dedicated API.

When iterating over the member items of a tale, what should we yield?
Should there be a generic iterator over the items of a tale, no matter what they may be (i.e. yielding either sub-tales, paragraphs, or line groups)?

## Decision

We provide **four generators** on `Tale` / `Subtale`:

- `.sentences` → Sentence objects
- `.linegroups` → LineGroup objects
- `.subtales` → SubTale objects
- `.children` → generic iterator over direct children (Subtale | Paragraph | LineGroup | …)


## Considered Options

**A. Flat sentence-only iterator (most TEI → plain text pipelines do this)**
- Simplest for NLP/analysis use cases
- Loses all structure information (headings, poems, sub-tales)
- Rejected: project aims to support structured rendering + analysis

**B. Only type-specific iterators (sentences, linegroups, subtales)**
- Clean, explicit API
- Forces caller to know in advance what content exists
- Rejected: makes generic tale rendering awkward / requires lots of if/else

**C. Generic children iterator + type-dispatch rendering (chosen)**
- Flexible for all use-cases (bare text, poems-only, full structured render)
- Renderer objects become polymorphic / composable
- Small price: slightly more complex Tale API surface


## Consequences

**Positive**
- Supports all important usage pattern with one consistent mental model
- Renderers become reusable and composable
- Easy to add new content types later (e.g. tables, lists)

**Negative**
- Larger public API surface on Tale/SubTale classes
- Caller must understand the type hierarchy to use `.children()` effectively
- Slightly more complex implementation (type dispatching in renderers)


### Extracting Bare Sentences

To render just the bare Sentences without higher-level structure, the user will use the sentence renderer and feed it the items from the sentences generator.

### Extracting Poems and Verses

To render just the poems and verses, the user will use the line group renderer and feed it the items from the linegroups generator.

### Extracting Sub-Tales

To render a specific sub-tale, the user will use the sub-tale renderer and pass it one specific sub-tale and instructions whether to ignore or render headings content. It will then iterate over the direct children of the sub-tale and delegate the further rendering work to a renderer suitable for the type of object yielded (a paragraph renderer for a Paragraph object, a line group renderer for a LineGroup object, etc.)

### Rendering Tales

To render a specific tale, the user will use the tale renderer and feed it the items as yielded from the Tale's generic generator. Given instructions how to deal with the heading contents, the tale renderer delegate the further rendering work to a renderer suitable for the type of object yielded (e.g. a sub-tale renderer, a paragraph renderer, a line group renderer, etc.)
