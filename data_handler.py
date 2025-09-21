import pandas as pd
import json

# Enhanced inputs for 3D/blueprints
budget = float(input("Enter budget (INR): "))
requirements = input("Enter requirements (e.g., '3 bedrooms, wiring, eco-materials'): ")
location = input("Enter location (e.g., Mumbai): ")
plot_size = float(input("Enter plot size (sq ft): "))
num_rooms = int(input("Enter number of rooms: "))
rooms = []
for i in range(num_rooms):
    name = input(f"Enter room {i+1} name: ")
    size = float(input(f"Enter {name} size (sq ft): "))
    rooms.append({"name": name, "size": size})

# Validation
if budget <= 0 or plot_size <= 0 or any(room["size"] <= 0 for room in rooms):
    print("Error: Values must be positive!")
    exit()
total_room_size = sum(room["size"] for room in rooms)
if total_room_size > plot_size:
    print("Warning: Rooms exceed plot—consider 3D stacking!")

# Structure DataFrame
df = pd.DataFrame(rooms)
df["plot_size"] = plot_size
df["budget"] = budget
df["requirements"] = requirements
df["location"] = location

# Save to CSV and JSON
df.to_csv("layout_data.csv", index=False)
with open("layout_data.json", "w") as f:
    json.dump(df.to_dict("records"), f, indent=4)

# Simplified insight (based on requirements)
if "eco" in requirements.lower() or "sustain" in requirements.lower():
    savings = budget * 0.1  # Mock 10% savings for eco-materials
    print(f"Insight: Eco-materials in requirements could save ~{savings} INR (e.g., Samsung smart lights).")
print("Data ready for backend (2-3 blueprints with wiring/3D):\n", df)
