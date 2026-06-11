---
name: excel-spreadsheet
description: Create, read, and edit Excel (.xlsx) spreadsheets. Use this when the user asks to build a spreadsheet, generate an Excel file, tabulate data into sheets, or read/inspect the contents of an existing .xlsx workbook.
metadata:
  author: LLM Bootcamp
  version: "1.0"
---

# Excel Spreadsheet skill

You can produce and read real `.xlsx` workbooks. All files live in the shared
workspace directory — created files are offered to the user as downloads, and
uploaded files are already in the workspace by their original filename.

## Tools available for this skill

- `create_excel(filename, sheets_json)` — write a new workbook.
- `read_spreadsheet(filename)` — preview the contents of an `.xlsx` or `.csv`.
- `analyze_data(filename)` — get statistics (use the `data-analysis` skill for deep work).

## Creating a workbook

Call `create_excel` with:

- `filename`: must end in `.xlsx` (e.g. `"budget.xlsx"`).
- `sheets_json`: a JSON **string** mapping each sheet name to its `columns`
  (a list of header strings) and `rows` (a list of rows, each row a list of
  cell values aligned to the columns).

Example `sheets_json`:

```json
{
  "Q1 Sales": {
    "columns": ["Region", "Units", "Revenue"],
    "rows": [
      ["North", 120, 24000],
      ["South", 90, 18000]
    ]
  },
  "Summary": {
    "columns": ["Metric", "Value"],
    "rows": [["Total Units", 210], ["Total Revenue", 42000]]
  }
}
```

Guidelines:

1. Plan the sheets and columns first (use `write_todos` for multi-sheet work).
2. Keep headers short and human-readable; put one logical table per sheet.
3. Numbers should be real numbers (not strings) so totals/formatting work.
4. After creating the file, tell the user the filename and briefly summarize
   what each sheet contains. The file becomes downloadable automatically.

## Reading a workbook

Call `read_spreadsheet(filename)` to get a markdown preview and the shape of
each sheet. Use this before editing or to answer questions about an uploaded
spreadsheet. For numeric analysis, prefer the `data-analysis` skill.
