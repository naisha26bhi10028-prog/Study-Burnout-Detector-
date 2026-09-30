def calculate_risk(study_hours, sleep_hours, breaks, stress, screen_time):
    score = 0
    risk_factors = []
    positive_habits = []

    if study_hours > 8:
        score = score + 3
        risk_factors.append("Long study duration")
    elif study_hours >= 5:
        score = score + 1
        positive_habits.append("Moderate study duration")
    else:
        score = score + 2
        risk_factors.append("Low study duration")

    if sleep_hours < 6:
        score = score + 3
        risk_factors.append("Low sleep duration")
    elif sleep_hours < 8:
        score = score + 1
        positive_habits.append("Sufficient sleep duration")
    else:
        positive_habits.append("Good sleep")

    if stress >= 8:
        score = score + 3
        risk_factors.append("High reported stress")
    elif stress >= 5:
        score = score + 2
        risk_factors.append("Moderate reported stress")
    else:
        positive_habits.append("Low reported stress")

    if breaks <= 2:
        score = score + 2
        risk_factors.append("Few study breaks")
    else:
        positive_habits.append("Sufficient study breaks")

    if screen_time >= 6:
        score = score + 2
        risk_factors.append("High screen time")
    elif screen_time >= 3:
        score = score + 1
        positive_habits.append("Moderate screen time")
    else:
        positive_habits.append("Low screen time")

    if score <= 3:
        risk_level = "Low"
    elif score <= 7:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    return score, risk_level, risk_factors, positive_habits