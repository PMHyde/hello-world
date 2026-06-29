# Step 1: variables hold a single piece of information
address = "123 Maple Street"
inspection_date = "2026-06-29"

print("Property:", address)
print("Inspected on:", inspection_date)

# Step 3: each issue is now a dictionary with a description and repair cost
issues_found = [
    {"description": "Cracked foundation corner", "repair_cost": 8500},
    {"description": "Outdated electrical panel", "repair_cost": 2200},
    {"description": "Roof shingles worn", "repair_cost": 6000},
]

print("\nIssues found:")
for issue in issues_found:
    print(f"- {issue['description']}: ${issue['repair_cost']:,}")

# Step 4: total cost, accumulated across the loop
total_repair_cost = 0
for issue in issues_found:
    total_repair_cost = total_repair_cost + issue["repair_cost"]

print(f"\nTotal estimated repair cost: ${total_repair_cost:,}")

# Step 5: a function packages logic so it can be reused with different inputs
def suggest_price_adjustment(asking_price, total_repair_cost):
    adjusted_price = asking_price - total_repair_cost
    percent_of_price = (total_repair_cost / asking_price) * 100

    if percent_of_price >= 5:
        recommendation = "Significant — recommend renegotiating price or repairs."
    else:
        recommendation = "Minor — unlikely to affect negotiations much."

    return adjusted_price, percent_of_price, recommendation


asking_price = 450000
adjusted_price, percent_of_price, recommendation = suggest_price_adjustment(
    asking_price, total_repair_cost
)

print(f"\nAsking price: ${asking_price:,}")
print(f"Repairs are {percent_of_price:.1f}% of asking price")
print(f"Suggested adjusted price: ${adjusted_price:,}")
print(f"Recommendation: {recommendation}")
