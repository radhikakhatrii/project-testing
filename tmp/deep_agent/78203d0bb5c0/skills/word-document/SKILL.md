---
name: word-document
description: Create and read Microsoft Word (.docx) documents. Use this when the user asks to write a report, letter, memo, or any formatted document, to export prose to Word, or to read the text of an existing .docx file.
metadata:
  author: LLM Bootcamp
  version: "1.0"
---

# Word Document skill

You can produce and read real `.docx` documents. Created files are written to
the shared workspace and offered to the user as downloads.

## Tools available for this skill

- `create_word(filename, markdown_text)` — write a new Word document.
- `read_document(filename)` — read the text of a `.docx` or `.txt` file.

## Creating a document

Call `create_word` with:

- `filename`: must end in `.docx` (e.g. `"report.docx"`).
- `markdown_text`: the document body written in a small subset of Markdown.

Supported Markdown:

- `# Heading 1`, `## Heading 2`, `### Heading 3` — section titles.
- Blank-line-separated paragraphs — normal body text.
- `- item` or `* item` — bullet list items.
- `1. item` — numbered list items.

Example `markdown_text`:

```
# Quarterly Report

## Overview
This quarter showed steady growth across all regions.

## Highlights
- Revenue up 18% year over year
- Two new enterprise customers
- Churn reduced to 2%

## Next Steps
1. Expand the sales team
2. Launch the analytics dashboard
```

Guidelines:

1. For longer documents, outline the sections first with `write_todos`.
2. Write clear, complete prose — this is a deliverable, not notes.
3. After creating the file, tell the user the filename and summarize the
   structure. The document becomes downloadable automatically.

## Reading a document

Call `read_document(filename)` to extract the text of an uploaded `.docx` (or
`.txt`) so you can summarize, revise, or answer questions about it.
