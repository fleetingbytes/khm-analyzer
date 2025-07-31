# Rendering Notes

## Tags

- `head` Heading
- `p` Paragraph
- `s` Sentence
- `w` Word
- `lg` Line Group
- `l` Line
- `<lb/>` Line Break
- `<pb/>` Page Break
- `hi` Highlight
- `fw` Forme Work
- `choice` editorial change
- `sic` incorrect form in the original
- `corr` correct form, corrected by the editor of the digitized text

### hi

- `rendition="#g"`: increased kerning (gapped?)
- `rendition="#aq"`: latin script (not Fraktur), used in enumeration (e.g. "a)", "b)", "c)"), or used in roman numerals ("I", "II", "III", ...)
- `rendition="#et"`: indented (eingerückter Text?)
- `rendition="#in"`: initial (big initial letter of a paragraph)

### s

- `next`: this sentence is just the beginning of a longer sentence. The content continues in the sentenceID given here (usually the next sibling)
- `prev`: this sentence is just a part of a longer sentence. The previous content is in the sentenceID given here (usually the previous sibling)
- `xml:id`: if this is a continuation of a split sentence, it has the regex format `#s[0-9a-f]+_[0-9a-f]+`, else `#s[0-9a-f]+`

## Sources

- [DTA Basisformat][dta-basisformat]
- [TEI P5 Elements][tei-elements]

[dta-basisformat]: https://www.deutschestextarchiv.de/doku/basisformat/uebersichtText.html
[tei-elements]: https://guidelines.teipublisher.com/p5.xml/?id=REF-ELEMENTS
