import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. LOAD DATA
df = pd.read_csv("house_prices.csv")
print("=== Preview of Data ===")
print(df.head(), "\n")
print("Shape (rows, columns):", df.shape)

# 2. PREPROCESSING
# Convert Location (text) to numbers
location_map = {"CityCenter": 0, "Suburb": 1, "Outskirts": 2}
df["LocationCode"] = df["Location"].map(location_map)

# Features (X) and Target (y)
X = df[["Rooms", "Size_sqft", "Age", "LocationCode"]]
y = df["Price_lakhs"]

# 3. TRAIN/TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. BUILD & TRAIN MODEL
model = LinearRegression()
model.fit(X_train, y_train)

print("\n=== Model Coefficients ===")
print("Intercept:", model.intercept_)
print("Coefficients (Rooms, Size_sqft, Age, LocationCode):")
print(model.coef_)

# 5. EVALUATE MODEL
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n=== Evaluation ===")
print("Mean Absolute Error:", round(mae, 2), "lakhs")
print("R² Score:", round(r2, 3))

# 6. PLOT ACTUAL vs PREDICTED
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price (lakhs)")
plt.ylabel("Predicted Price (lakhs)")
plt.title("Actual vs Predicted House Prices")
plt.tight_layout()
plt.savefig("task2_actual_vs_predicted.png")
plt.show()

# 7. PREDICT A NEW HOUSE (UNIQUE TOUCH)
new_house = pd.DataFrame({
    "Rooms": [3],
    "Size_sqft": [1200],
    "Age": [8],
    "LocationCode": [location_map["Suburb"]],
})

pred_price = model.predict(new_house)[0]
print("\n=== Example Prediction ===")
print(
    f"Predicted price for 3 BHK, 1200 sqft, 8 years old in Suburb: "
    f"{pred_price:.2f} lakhs"
)