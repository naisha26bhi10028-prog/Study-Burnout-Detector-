# StudyWell — Student Study Pattern & Wellness Risk Analyzer

## Overview
StudyWell is an interactive Streamlit dashboard for reviewing selected study and wellness-related patterns. It accepts study hours, sleep hours, stress, breaks, and screen time, applies transparent project-defined rules, generates recommendations, stores assessment history, and visualises trends.

> **Disclaimer:** StudyWell is an educational self-assessment. Its scoring rules are project-defined and are not a medical or psychological diagnostic tool.

## Features
- Student assessment
- Rule-based risk scoring and classification
- Risk-factor and positive-habit identification
- Recommendation generation
- CSV assessment history
- Plotly trend visualisations
- Modular Streamlit interface
- Empty-state handling

## Technologies
Python, Streamlit, Pandas, Plotly, CSV, Git/GitHub.

## Project Structure
```text
Study-Burnout-Detector/
├── app.py
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
├── .streamlit/config.toml
├── modules/
│   ├── risk_analysis.py
│   ├── recommendations.py
│   ├── data_storage.py
│   └── visualisations.py
└── data/assessments.csv
```

## Installation
```bash
pip install -r requirements.txt
```

## Run
```bash
streamlit run app.py
```

## Disclaimer
The project-defined score is an educational indicator and is not clinically validated.
