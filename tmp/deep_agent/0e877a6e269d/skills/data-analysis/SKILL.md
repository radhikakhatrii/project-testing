---
name: data-analysis
description: Analyze tabular data from CSV or Excel files — compute summary statistics, inspect columns and data types, find missing values, and surface trends. Use this when the user wants insights, descriptive statistics, or a data quality check on a dataset rather than just reading raw rows.
metadata:
  author: LLM Bootcamp
  version: "1.0"
---

# Data Analysis skill

You can analyze tabular datasets (`.csv` or `.xlsx`) that are in the workspace
(uploaded by the user or created earlier in this session).

## Tools available for this skill

- `analyze_data(filename)` — returns shape, column names and dtypes, missing
  value counts, descriptive statistics for numeric columns, and a small sample
  of rows.
- `read_spreadsheet(filename)` — raw preview of the data if you need to see
  actual values.
- `create_excel(filename, sheets_json)` — write results back to a workbook.

## Workflow

1. Identify the dataset filename (use `list_files` / `ls` if unsure).
2. Call `analyze_data(filename)` to get the statistical profile.
3. Interpret the numbers for the user in plain language:
   - Describe the dataset (rows, columns, what it appears to contain).
   - Call out notable statistics (ranges, averages, outliers, skew).
   - Flag data quality issues (missing values, suspicious types).
4. If the user asks for a deliverable, write the findings to a Word report
   (`word-document` skill) or a results workbook (`excel-spreadsheet` skill).

## Guidelines

- Be precise and quantitative — cite the actual numbers from `analyze_data`.
- Do not fabricate statistics. If a column is non-numeric, say so rather than
  inventing an average.
- For multi-step analysis, track the steps with `write_todos`.
