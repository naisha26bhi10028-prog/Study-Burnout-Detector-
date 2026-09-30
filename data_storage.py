import os
import pandas as pd
from datetime import datetime

DATA_FILE = "data/assessments.csv"

def initialise_storage():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATA_FILE):
        name = [
            "timestamp",
            "study_hours",
            "sleep_hours",
            "stress",
            "breaks",
            "screen_time",
            "risk_score",
            "risk_level"
        ]
        a = pd.DataFrame(columns=name)
        a.to_csv(DATA_FILE, index=False)


def save_assessment(study_hours, sleep_hours, stress, breaks, screen_time, risk_score, risk_level):
    initialise_storage()
    assessment = {
        "timestamp" : datetime.now(),
        "study_hours" : study_hours,
        "sleep_hours" : sleep_hours,
        "stress" : stress,
        "breaks" : breaks,
        "screen_time" : screen_time,
        "risk_score" : risk_score,
        "risk_level" : risk_level
    }
    new_data = pd.DataFrame([assessment])
    existing_data = pd.read_csv(DATA_FILE)
    updated_data = pd.concat(
        [existing_data, new_data],
        ignore_index=True
    )
    updated_data.to_csv(DATA_FILE, index=False)

def load_assessment():
    initialise_storage()
    return pd.read_csv(DATA_FILE)

