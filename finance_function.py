def future_value(present_value, rate, years):
    return round(present_value * (1 + rate) ** years, 2)

print(future_value(1000, .1, 5))
