import random
import math

import numpy as np

def display_stats(data: list[list[int]]):
    """Displays statistics for each sublist in a formatted table."""
    if not data:
        print("No data to display.")
        return
    
    headers = ["Day", "Min", "Max", "Average", "Median", "Difference"]
    row_format = " ".join("{:<%s}"%(len(_)+2) for _ in headers)
    #row_format = "{:<6} {:<6} {:<6} {:<8} {:<8} {:<8}"
    print(row_format.format(*headers))
    print("-" * 50)
    
    for i, sublist in enumerate(data):
        if not sublist:
            stats = [0, 0, "-", "-", "-", "-"]
        else:
            stats = [
                min(sublist),
                max(sublist),
                round(np.mean(sublist), 2),
                round(np.median(sublist), 2),
                round(max(sublist) - min(sublist), 2),
            ]
        print(row_format.format(i+1, *stats))

def evaluate_curve(value):
    return value#0.5 + 0.5 * math. erf(value-0.01763/(math.sqrt(2)*0.12085))

def simulate_quota_growth(days, initial_quota=130):
    quota = initial_quota
    quotas:list[int|float] = [quota]
    
    for day in range(1, days + 1):
        time_multiplier = 1 + (day ** 2) / 16
        time_multiplier = min(time_multiplier, 10**4)  # Clamping to 10^4
        
        luck = 1
        
        random_factor = random.uniform(-0.503, 0.503)
        randomized_offset = 100 * time_multiplier * ((abs(luck-1)+1)*(1 + evaluate_curve(random_factor)))
        
        quota += randomized_offset
        quota = min(quota, 10**9)  # Clamping to max limit
        
        quotas.append(quota)
    
    return quotas
# Max: 1462
# Min: 4159
# Example usage
days = 10

attempts = 10**6
all = []
for _ in range(attempts):
    last = 130
    quotas = simulate_quota_growth(days, last)
    # for day, quota in enumerate(quotas, 1):
    #     print(f"Day {day}: {quota} ({quota - last})")
    #     last = quota
    all.append([int(quota) for quota in quotas])

final = []

for day in range(days):
    quoatas_of_today = [day_quota[day] for day_quota in all]
    final.append(quoatas_of_today)
    # print_list_stats(quoatas_of_today)
    #print(f"Day {day}: Min: {min(quoatas_of_today)}, Max: {max(quoatas_of_today)}, Average: {sum(quoatas_of_today) / len(quoatas_of_today)}, Median: {sorted(quoatas_of_today)[len(quoatas_of_today) // 2]}")

display_stats(final)
