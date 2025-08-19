# CI-CD-Challenge
# CI/CD with GitHub Actions — Dev → QA → Prod

![CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/<OWNER>/<REPO>/actions/workflows/cd.yml/badge.svg)

A minimal CI/CD pipeline using **GitHub Actions** that simulates deployments to **Dev**, **QA**, and **Prod** with environment approvals. Sample app is built with **Streamlit** and changes look & title by environment.

The sample app is a **Detective Language Translator** that calls Google's Gemini API. Provide `GEMINI_API_KEY` via environment secrets or `.env`.

## Features
- CI on PRs to `main`: lint + tests, uploads reports as artifacts.
- CD on pushes: `dev` → Dev, `qa` → QA, `main` → Prod (**requires approval**).
- Each deploy emits a log like: `🚀 Deployed to 'environment'` and uploads a zip artifact.
- Uses environment **secrets** (`GEMINI_API_KEY`) written into `.env` at build time.

# Quick, Ready-to-Ship Pack

Use this pack as-is. Copy the folder/file structure and contents into your repo, commit, and push.

# 10‑Minute Setup Checklist

10‑Minute Setup Checklist

Create branches: dev, qa, keep main.

Create GitHub Environments: dev, qa, prod (Repo → Settings → Environments).

In prod, enable Required reviewers (1+), save.

(Optional) Add an environment secret GEMINI_API_KEY for each env to see secrets step working.

Commit & push all files below to main.

Trigger CI: open a PR into main → CI runs.

Trigger CD: push to dev → deploy to dev; push to qa → deploy to qa; push to main → waits for prod approval, then deploys.

## Project Structure
app/            # Streamlit app
app.py        # callable: app(env)
main.py       # sets background based on APP_ENV and mounts app(env)

tests/          # Unit tests for CI
test_app.py

.github/workflows/
ci.yml         # Continuous Integration (PRs → main)
cd.yml         # Continuous Delivery (Dev/QA/Prod)
## Repository Tree

CI-CD-Challenge
├── README.md
├── requirements.txt
├── .flake8
├── app/
│   ├── __init__.py
│   ├── app.py
│   └── main.py
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        ├── ci.yml
        └── cd.yml




##  Local Run
```bash
python -m pip install -r requirements.txt
# Provide GEMINI_API_KEY (either in .env or as shell var)
# macOS/Linux
export GEMINI_API_KEY=sk-... && APP_ENV=dev streamlit run app/main.py
# Windows PowerShell
# $env:GEMINI_API_KEY = "sk-..."; $env:APP_ENV = "dev"; streamlit run app/main.py
```
# Environments:

dev → green background, title "Dev Environment"

qa → yellow background, title "QA Environment"

prod → red background, title "Production Environment"

## Setup

Create branches: dev, qa, keep main.

Create Environments: dev, qa, prod (Repo → Settings → Environments).

In prod, enable Required reviewers (at least 1). Save.

Add secret GEMINI_API_KEY per environment.

Commit these files to main and push.

## Triggering CI/CD

CI: open a Pull Request into main → runs ci.yml.

CD:

Push to dev → deploys to dev environment.

Push to qa → deploys to qa environment.

Push to main → waits for prod approval → deploys to prod.

# Example Logs

In the CD job logs (and in the uploaded artifact):

Deployed to 'dev'
Deployed to 'qa'
Deployed to 'prod'

## Branch Protections (recommended)

Protect main: require PRs, require passing checks (CI), require review before merge.

## Evaluation Mapping

Complete: CI on PRs; CD on dev/qa/main; prod requires approval.

Correct: Workflows pass; artifacts uploaded; secrets optional.

Great: This README explains usage with logs; linting + artifacts implemented.

---

##  Handy Git Commands (optional)
```bash
# initial push
git add .
git commit -m "Scaffold CI/CD challenge"
git push -u origin main

# create branches
git checkout -b dev && git push -u origin dev
git checkout -b qa  && git push -u origin qa

# sample change to trigger dev deploy
echo "# dev change" >> notes.md
git add notes.md && git commit -m "dev: trigger deploy" && git push
```
## What the Evaluator Will See

CI runs on PRs to main (lint + tests + artifacts).

CD runs on pushes to dev/qa/main.

Prod deployment is blocked until approval in Environments → prod.

Streamlit app present; environment-specific UI demonstrated via APP_ENV.

