import random

def generate_predictions():
    series = ["SK", "SS", "ST", "SU"]
    predictions = []

    for _ in range(5):
        s = random.choice(series)
        num = random.randint(100000, 999999)
        predictions.append(f"{s} {num}")

    return predictions

def hot_numbers():
    return [1, 7, 9, 4]

def cold_numbers():
    return [0, 2, 5]