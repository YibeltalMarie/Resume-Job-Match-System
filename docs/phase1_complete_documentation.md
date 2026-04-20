# Phase 1 Complete Documentation
## Resume Parser — Regex-Based Strategy

**Date:** April 20, 2026  
**Status:** ✅ Complete  
**Strategy:** Regex-based extraction  
**Competition Phase:** Phase 1 — Must Have (Core Requirements)

---

## Table of Contents

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Files Created](#files-created)
4. [What is Normalization?](#what-is-normalization)
5. [Do We Need Normalization Only for Regex?](#do-we-need-normalization-only-for-regex)
6. [Test Results](#test-results)
7. [What Works Well](#what-works-well)
8. [Limitations](#limitations)
9. [Key Concepts](#key-concepts)
10. [Commands to Remember](#commands-to-remember)
11. [Next Steps](#next-steps)

---

## Overview

Phase 1 implements a **rule-based resume parser** using Regular Expressions (regex). It extracts structured data from unstructured resume text (PDF, DOCX, TXT) and outputs JSON matching the competition schema.

### What We Built

| Component | Description |
|-----------|-------------|
| **Text Extraction** | Extract raw text from PDF, DOCX, TXT files |
| **Regex Extraction** | Find name, email, skills, experience, education using patterns |
| **Field Mapping** | Convert extracted data to standard schema names |
| **Normalization** | Standardize skills, companies, degrees, dates |
| **Validation** | Check schema compliance and calculate confidence |
| **JSON Output** | Generate competition-ready JSON with metadata |

---

## System Architecture
┌─────────────────────────────────────────────────────────────────┐
│ INPUT (PDF/DOCX/TXT) │
└─────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 1: TEXT EXTRACTION │
│ ├── PDFExtractor (PyPDF2) — handles .pdf files │
│ ├── DOCXExtractor (python-docx) — handles .docx files │
│ ├── TXTExtractor (native) — handles .txt files │
│ └── ExtractorFactory — automatically selects correct one │
└─────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 2: FIELD EXTRACTION (RegexStrategy) │
│ ├── Email: r'[\w.-]+@[\w.-]+.\w+' │
│ ├── Name: First two capitalized words in first 500 chars │
│ ├── Skills: Match against 50+ common skills dictionary │
│ ├── Experience: Pipe-separated patterns (Role | Company | Years)│
│ └── Education: Pipe-separated patterns (Degree | Institution | Year)│
└─────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 3: FIELD MAPPING (FieldMapper) │
│ └── Converts extracted fields to standard schema names │
└─────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 4: NORMALIZATION │
│ ├── SkillNormalizer: "sql" → "SQL", "js" → "JavaScript" │
│ ├── CompanyNormalizer: "Google Inc" → "Google" │
│ ├── DegreeNormalizer: "BSc" → "Bachelor of Science" │
│ └── DateParser: "2020-2023" → 3 years │
└─────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 5: VALIDATION │
│ ├── SchemaValidator: Checks all required fields exist │
│ ├── ConfidenceScorer: Calculates extraction confidence (0-1) │
│ └── MissingFieldHandler: Adds defaults for missing fields │
└─────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 6: OUTPUT (JSONGenerator) │
│ ├── Generates JSON matching competition schema │
│ └── Adds metadata (confidence, warnings, processing time) │
└─────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ OUTPUT JSON │
└─────────────────────────────────────────────────────────────────┘


---

## Files Created

### Total: 22 Python Files

### 1. Models (Data Structures) — 4 files

| File | Purpose |
|------|---------|
| `models/education.py` | Education dataclass (degree, institution, year) |
| `models/experience.py` | Experience dataclass (role, company, years) |
| `models/resume.py` | Resume dataclass with all fields + to_dict() |
| `models/parsing_result.py` | Wrapper with metadata (confidence, warnings) |

### 2. Text Extraction — 5 files

| File | Purpose |
|------|---------|
| `text_extraction/base.py` | Abstract base class defining extract() interface |
| `text_extraction/pdf_extractor.py` | PDF parsing with PyPDF2, handles bytes via BytesIO |
| `text_extraction/docx_extractor.py` | DOCX parsing with python-docx |
| `text_extraction/txt_extractor.py` | TXT parsing with UTF-8 fallback to latin-1 |
| `text_extraction/extractor_factory.py` | Factory pattern — returns correct extractor by extension |

### 3. Field Extraction — 3 files

| File | Purpose |
|------|---------|
| `field_extraction/base.py` | Strategy interface for pluggable extractors |
| `field_extraction/strategies/regex_strategy.py` | All regex patterns for email, name, skills, experience, education |
| `field_extraction/field_mapper.py` | Maps extracted fields to standard schema names |

### 4. Normalization — 5 files

| File | Purpose |
|------|---------|
| `normalization/skill_normalizer.py` | Maps skill variations (JS → JavaScript, sql → SQL) |
| `normalization/company_normalizer.py` | Maps company variations (Google Inc → Google) |
| `normalization/degree_normalizer.py` | Maps degree variations (BSc → Bachelor of Science) |
| `normalization/date_parser.py` | Parses date ranges (2020-2023 → 3 years) |
| `normalization/normalizer_pipeline.py` | Runs all normalizers in sequence |

### 5. Validation — 3 files

| File | Purpose |
|------|---------|
| `validation/schema_validator.py` | Checks all required fields exist with correct types |
| `validation/confidence_scorer.py` | Calculates confidence score (0-1) based on field completeness |
| `validation/missing_field_handler.py` | Adds default values for missing fields |

### 6. Output — 1 file

| File | Purpose |
|------|---------|
| `output/json_generator.py` | Creates competition-schema JSON with metadata |

### 7. Orchestration — 1 file

| File | Purpose |
|------|---------|
| `__init__.py` | Main ResumeParser class tying all modules together |

### 8. Utilities — 1 file

| File | Purpose |
|------|---------|
| `utils/constants.py` | COMMON_SKILLS list (50+ skills), section mappings |

---

## What is Normalization?

### Simple Definition

**Normalization = Making data consistent**

It's the process of converting variations of the same thing into a standard format.

### Real-World Examples

#### Example 1: Skills

| Raw Extracted | After Normalization |
|---------------|---------------------|
| `"Python"` | `"Python"` |
| `"python"` | `"Python"` |
| `"py"` | `"Python"` |
| `"Python3"` | `"Python"` |
| `"PYTHON"` | `"Python"` |

#### Example 2: Companies

| Raw Extracted | After Normalization |
|---------------|---------------------|
| `"Google Inc"` | `"Google"` |
| `"google"` | `"Google"` |
| `"Alphabet"` | `"Google"` |
| `"GOOG"` | `"Google"` |

#### Example 3: Degrees

| Raw Extracted | After Normalization |
|---------------|---------------------|
| `"BSc"` | `"Bachelor of Science"` |
| `"B.S."` | `"Bachelor of Science"` |
| `"Bachelor of Science"` | `"Bachelor of Science"` |
| `"B.Sc."` | `"Bachelor of Science"` |

#### Example 4: Dates

| Raw Extracted | After Normalization |
|---------------|---------------------|
| `"2020-2023"` | `3 years` |
| `"2020-Present"` | `current_year - 2020` |
| `"2020"` | `1 year` (assumption) |

---

## Do We Need Normalization Only for Regex?

### Short Answer: **NO**

Normalization is needed **regardless** of extraction method.

| Extraction Method | Does it need normalization? | Why? |
|-------------------|----------------------------|------|
| **Regex** | ✅ Yes | Extracts raw text as-is, which has variations |
| **spaCy NER** | ✅ Yes | Extracts entities, but still has case/spelling variations |
| **BERT/Transformers** | ✅ Yes | Even best model extracts "Google Inc" vs "Google" |
| **Any method** | ✅ Yes | Because humans write the same thing differently |

### Why Normalization Is Universal


---

## Test Results

### Input File

| Property | Value |
|----------|-------|
| Format | PDF |
| Size | 46KB |
| Content | Sample resume with pipe-separated format |

### Output JSON

```json
{
  "candidate_id": "c7fa301d",
  "name": "John Doe",
  "email": "john.doe@email.com",
  "skills": [
    "AWS",
    "Docker",
    "Kubernetes",
    "Python",
    "SQL"
  ],
  "education": [
    {
      "degree": "Master of Science",
      "institution": "Stanford",
      "year": "2020"
    },
    {
      "degree": "Bachelor of Science",
      "institution": "UC Berkeley",
      "year": "2018"
    }
  ],
  "experience": [
    {
      "role": "Senior Software Engineer",
      "company": "Google",
      "years": 5.0
    },
    {
      "role": "Software Engineer",
      "company": "Amazon",
      "years": 3.0
    }
  ],
  "total_experience_years": 8.0,
  "_metadata": {
    "confidence": 1.0,
    "warnings": [],
    "processing_time_ms": 227.53,
    "parser_version": "phase1_regex",
    "timestamp": "2026-04-20T10:45:19.536834"
  }
}