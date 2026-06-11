---
name: pdf-extract
description: Read PDFs and create PDFs. Use this when the user uploads a PDF to summarize, answer questions about, or extract data from, OR when the user asks to generate, build, write, or export a PDF document or report.
metadata:
  author: LLM Bootcamp
  version: "1.0"
---

# PDF skill

You can both **read** the text of uploaded PDFs and **create** new PDF documents.

## Tools available for this skill

- `read_pdf(filename)` — extract the text content of a `.pdf`, page by page.
- `create_pdf(filename, markdown_text)` — write a new `.pdf` from Markdown
  (headings, **bold**/*italic*, links, ordered/unordered/nested lists, and tables).

## Reading a PDF

1. Confirm the PDF filename (uploaded files keep their original name; use `ls` if unsure).
2. Call `read_pdf(filename)` — the result is labeled per page so you can cite page numbers.
3. Do the requested task with the text:
   - **Summarize**: produce a concise, faithful summary; cite page numbers.
   - **Answer questions**: ground every answer in the extracted text; if the answer
     is not present, say so — do not invent content.
   - **Extract data**: pull the requested fields. Hand off to `create_excel` for a
     spreadsheet, or `create_word` / `create_pdf` for a written document.

## Creating a PDF

1. Plan the document first (use `write_todos` for multi-section work).
2. Write the body in the supported Markdown and call
   `create_pdf(filename, markdown_text)` with a filename ending in `.pdf`.
3. Tell the user the filename; the PDF becomes downloadable automatically.

## Notes

- PDF creation uses standard fonts, so unusual symbols or emoji may be simplified.
- PDF text extraction can be imperfect for scanned or image-only PDFs; if the
  extracted text is empty or garbled, tell the user the PDF appears to be scanned.
