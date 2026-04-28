import pandas as pd

# Example epitope dataset
data = {
    "Epitope": ["SEEVVKGDPTTYYTI", "FRAEYFSVL", "FSPYDDHYV"],
    "Antigenicity": [0.85, 0.72, 0.91],
    "Allergenicity": ["Non-allergen", "Non-allergen", "Allergen"],
    "Toxicity": ["Non-toxic", "Non-toxic", "Non-toxic"]
}

df = pd.DataFrame(data)

# Filter best epitopes
filtered = df[
    (df["Antigenicity"] > 0.7) &
    (df["Allergenicity"] == "Non-allergen") &
    (df["Toxicity"] == "Non-toxic")
]

print(filtered)

# Save results
filtered.to_csv("results/filtered_epitopes.csv", index=False)
