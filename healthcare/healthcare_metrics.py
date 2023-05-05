def body_mass_index(weight, height):
    return weight / (height ** 2)

def resting_metabolic_rate(weight, height, age, gender):
    if gender == "male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "female":
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Accepted values: 'male', 'female'")
