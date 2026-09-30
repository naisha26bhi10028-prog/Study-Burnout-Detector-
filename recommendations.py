def generate_recommendation(factors):
    recommendations = []

    recommendation_map = {
        "Long study duration":
            "Break long study sessions into focused blocks with regular breaks. If studying on a screen, use the "
            "20-20-20 rule to reduce eye strain.",

        "Low study duration":
            "Consider increasing focused study time gradually, prioritizing difficult or high-friction topics and using"
            " active recall and spaced repetition.",

        "Low sleep duration":
            "Morning light exposure: Get 10-15 minutes of natural sunlight within an hour of waking up to set your "
            "circadian clock and improve night-time sleep drive."
            " Switch to grayscale mode or use blue light filtering warm tones 2 hours before target sleep time.",
        
        "Moderate reported stress":
            "Active recovery breaks: Instead of checking your phone during a 10-minute study break, step outside, "
            "drink water, or stretch. Casual screen scrolling prevents cognitive recovery and increases overall "
            "stress.",

        "High reported stress":
            "Physiological sigh: Two quick inhales through the nose followed by a slow, long exhale through the mouth."
            " Performing 3-5 cycles rapidly lowers heart rate during high-stress study moments.",

        "Few study breaks":
            "Try the Pomodoro work style: 25-50 minute intervals of focused study followed by a 5-10 minute break."
            " This provides strategic, high-quality rests without losing productivity.",

        "High screen time":
            "Put hard timers on non-essential, high friction social media apps."
            " Charge devices in a separate room or out of reach overnight to eliminate screen use during the first and "
            "last 30 minutes of the day."
    }

    for x in factors:
        if x in recommendation_map:
            recommendations.append(recommendation_map[x])

    return recommendations

