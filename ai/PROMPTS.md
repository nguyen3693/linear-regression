# Cursor Prompt Log — Assignment 3 (AI-assisted)

Prompts used in this Cursor session to build and document the `ai/` folder on branch `assignment3`.

---

## Prompt 1 — Initial assignment setup

> I am a beginner coder taking an intro to data science in biomedical studies. So far, I learned how to set up a personal Git repo, create branches, and push my working repository to branches. I am working on a new class assignment, "Assignment 3" that builds off from my previous "Assignment 2" where I learned how to manually create an environment, create working project directory, make jupyter notebooks for Python and R, read simple dataset csv file, perform linear regression model, run basic statistics, and output a basic scatter plot with regression line and printed stats. I also learned how to export jupyter notebooks into HTML files and executable python and r scripts. For Assignment 3, the goal is to enhance my previous regression analysis with detailed diagnostics (including mean squared error) and annotated plots, and demonstrate GitHub workflow proficiency through pull requests and tagging. Using the current project conda environment "7030_class_1" and working within project directory "linear-regression", I need you to create a new "ai" folder. Inside ai folder, generate new python and r notebooks in jupyter that reads dataset file "regression_data.csv", generates scatter plot with linear regression line overlay and relevant statistics including mean squared error and saves plot as .png file. Then, export notebooks into HTML file and executable python and r scripts. Finally, make sure all updates are on branch assignment3, and push to git hub repo: https://github.com/nguyen3693/linear-regression on branch "assignment3", NOT MAIN BRANCH.
> Ignore all contents in "manual" folder.
> Do not execute any changes without asking for permissions first.
> Confirm with me first before committing to git repo.

**Outcome:** Explored the repo and proposed a step-by-step plan. No changes made until approval.

---

## Prompt 2 — Revise plan without Assignment 2 context

> pretend you did not read Assignment 2, update your proposed plan.

**Outcome:** Rewrote the plan using only Assignment 3 requirements and current repo state.

---

## Prompt 3 — File naming and PROMPTS.md preference

> name files "linear_model...", do not make PROMPTS.md (I will do this myself manually). update proposed plan.

**Outcome:** Updated plan to use `linear_model_*` naming. Excluded `PROMPTS.md` from automated deliverables.

---

## Prompt 4 — Implement notebooks and exports

> only implement step 1: create ai/ folder and generate/run these files.

**Outcome:** Created `ai/` with Python and R notebooks, HTML exports, CLI scripts, and PNG outputs. Ran notebooks in `7030_class_1`. R used base R graphics (ggplot2 not installable in current env).

---

## Prompt 5 — Commit and push

> yes, execute step 2

**Outcome:** Committed and pushed `linear_model_*` files to `origin/assignment3` (commit `f289675`). Did not push to `main`.

---

## Prompt 6 — Code review request

> Now I want you to review assignment3 branch, comparing contents in manual versus ai folders. Highlight main similarities and differences in basic plan english. Save your review as "ai/CODE_REVIEW.md". Show preview before making CODE_REVIEW.md.

**Outcome:** Compared both folders and showed a preview of `CODE_REVIEW.md` before saving.

---

## Prompt 7 — Save review with edits

> save with edits

**Outcome:** Saved `ai/CODE_REVIEW.md` with verified Python script comparison results and clearer differences.

---

## Prompt 8 — AI README request

> generate a fresh README from ai code. Save it as `ai/README_AI.md` (don't overwrite your manual README). Show preview before creating file.

**Outcome:** Drafted README preview based on `ai/` code only.

---

## Prompt 9 — Save README

> yes, save

**Outcome:** Saved `ai/README_AI.md`.

---

## Prompt 10 — Commit documentation

> I want you to add updates to git on assignment3

**Outcome:** Committed and pushed `CODE_REVIEW.md` and `README_AI.md` to `origin/assignment3` (commit `830cd2a`). Left unrelated `manual/regression_plot_python.png` change unstaged.

---

## Prompt 11 — This prompt log

> put together prompt log in ai/PROMPTS.md of all prompts from this session. Show me preview before saving,

**Outcome:** This file.

---

## Summary of AI-assisted deliverables

| Deliverable | Status |
|-------------|--------|
| `ai/linear_model_python.ipynb` | Created and executed |
| `ai/linear_model_r.ipynb` | Created and executed |
| `ai/linear_model_python.html` | Exported |
| `ai/linear_model_r.html` | Exported |
| `ai/linear_model_python.py` | Created with CLI args |
| `ai/linear_model_r.r` | Created with CLI args |
| `ai/linear_model_python_output.png` | Generated |
| `ai/linear_model_r_output.png` | Generated |
| `ai/CODE_REVIEW.md` | Created |
| `ai/README_AI.md` | Created |
| `ai/PROMPTS.md` | This file |
