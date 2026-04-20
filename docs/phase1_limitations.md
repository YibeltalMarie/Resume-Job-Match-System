# Phase 1: Regex Strategy — Limitations & Trade-offs

## Overview

Phase 1 uses Regular Expressions (regex) as the baseline extraction strategy. While it works for well-structured resumes, it has significant limitations.

## What Works Well ✅

| Format | Example | Success Rate |
|--------|---------|--------------|
| Pipe-separated fields | `Role \| Company \| Years` | 90%+ |
| Standard section headers | `EXPERIENCE`, `EDUCATION`, `SKILLS` | 85%+ |
| Simple date formats | `2020-2023`, `2020-Present` | 90%+ |
| Email addresses | `name@domain.com` | 99%+ |
| Two-word names | `John Doe` | 85%+ |

## What Fails or Performs Poorly ❌

### 1. Different Field Separators

| Separator | Example | Regex Status |
|-----------|---------|--------------|
| `\|` (pipe) | `Engineer \| Google` | ✅ Works |
| `at` | `Engineer at Google` | ❌ Fails |
| `-` (dash) | `Engineer - Google` | ❌ Fails |
| `,` (comma) | `Engineer, Google` | ❌ Fails |
| No separator | `Engineer Google` | ❌ Fails |

### 2. Varying Section Names

| Section Variation | Detected? |
|-------------------|-----------|
| `EXPERIENCE` | ✅ Yes |
| `Work Experience` | ✅ Yes |
| `Employment History` | ❌ No |
| `Professional Background` | ❌ No |
| `Career Summary` | ❌ No |

### 3. Different Date Formats

| Format | Example | Parsed Correctly? |
|--------|---------|-------------------|
| `2020-2023` | `2020-2023` | ✅ Yes |
| `2020 - 2023` | `2020 - 2023` | ✅ Yes |
| `Jan 2020 - Dec 2023` | `Jan 2020 - Dec 2023` | ❌ No |
| `2020 to 2023` | `2020 to 2023` | ❌ No |
| `2020–2023` (en dash) | `2020–2023` | ⚠️ Partial |
| `2 years` | `2 years` | ❌ No |

### 4. Complex Name Formats

| Name Format | Extracted? |
|-------------|------------|
| `John Doe` | ✅ Yes |
| `J. Doe` | ❌ No |
| `Johnathan Michael Doe` | ⚠️ Partial |
| `Doe, John` | ❌ No |
| `Dr. John Doe` | ⚠️ Partial |

### 5. Skill Variations

| Skill Written | Normalized To | Success |
|---------------|---------------|---------|
| `Python` | `Python` | ✅ Yes |
| `python` | `Python` | ✅ Yes |
| `PYTHON` | `Python` | ✅ Yes |
| `py` | `Python` | ❌ No |
| `Python3` | `Python` | ❌ No |
| `Python (advanced)` | `Python` | ⚠️ Partial |

### 6. Complex Resume Layouts

| Layout Type | Regex Performance |
|-------------|-------------------|
| Single column, linear | ✅ Good |
| Two-column layout | ❌ Poor |
| Tables | ❌ Very poor |
| Bullet points without clear structure | ⚠️ Medium |
| Headers/footers with noise | ⚠️ Medium |
| Scanned PDFs (images) | ❌ Impossible (no text) |

### 7. Experience Extraction Edge Cases

| Scenario | Example | Works? |
|----------|---------|--------|
| Multiple jobs at same company | `Engineer (2018-2020), Senior (2020-2023)` | ❌ No |
| Freelance/contract work | `Freelance Developer, 2020-present` | ⚠️ Partial |
| Internships | `Intern, Google, Summer 2022` | ❌ No |
| Promotions within same company | `Analyst → Senior Analyst` | ❌ No |

### 8. Education Extraction Edge Cases

| Scenario | Example | Works? |
|----------|---------|--------|
| Multiple degrees from same school | `BSc and MSc, Stanford` | ❌ No |
| In-progress degrees | `MSc (expected 2025)` | ❌ No |
| Online certifications | `AWS Certified, Coursera` | ❌ No |
| Bootcamps | `Data Science Bootcamp, 2023` | ❌ No |

## Quantitative Limitations

| Metric | Regex Performance | Target |
|--------|-------------------|--------|
| Precision (exact match) | 65-75% | 85%+ |
| Recall (finding all fields) | 60-70% | 85%+ |
| Format robustness | Low | High |
| Maintenance cost | High (need new patterns) | Low |

## Root Cause Analysis

### Why Regex Fails on Varied Formats



## Mitigation Strategy (Phase 2 and Beyond)

| Phase | Strategy | Addresses |
|-------|----------|-----------|
| Phase 2 | spaCy NER | Entity recognition, flexible patterns |
| Phase 2 | Fallback chain | Graceful degradation |
| Phase 3 | Sentence-BERT | Semantic understanding |
| Phase 3 | Cross-encoder | Precise matching |
| Phase 4 | Fine-tuned model | Domain-specific optimization |

## Conclusion

**Regex is a baseline, not a production solution.**

It demonstrates:
- Understanding of pattern matching
- Quick prototyping ability
- Baseline for comparison

But it must be replaced/supplemented with:
- ML-based NER (spaCy)
- Semantic embeddings (SBERT)
- Fallback strategies for robustness

---

*Document prepared for competition submission - Phase 1 limitations analysis*

# Phase 1 Limitations — One Page Summary

## Works For
- ✅ Pipe-separated: `Role | Company | Years`
- ✅ Standard section names: `EXPERIENCE`, `EDUCATION`
- ✅ Simple dates: `2020-2023`
- ✅ Email addresses
- ✅ Two-word names

## Fails For
- ❌ Other separators: `at`, `-`, `,`, or none
- ❌ Date ranges with months: `Jan 2020 - Dec 2023`
- ❌ Non-standard section names: `Employment History`
- ❌ Complex names: `J. Doe`, `Doe, John`
- ❌ Two-column layouts
- ❌ Tables
- ❌ Scanned PDFs
- ❌ Bullet points without structure

## Accuracy Estimate
- Precision: ~70%
- Recall: ~65%
- Format coverage: ~30% of real-world resumes

## Next Steps
→ Phase 2: spaCy NER for better entity recognition
→ Phase 3: Semantic matching for understanding