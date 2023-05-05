def daily_calorie_needs(rmr, activity_level):
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }

    if activity_level not in activity_multipliers:
        raise ValueError("Invalid activity level. Accepted values: 'sedentary', 'light', 'moderate', 'active', 'very_active'")

    return rmr * activity_multipliers[activity_level]
