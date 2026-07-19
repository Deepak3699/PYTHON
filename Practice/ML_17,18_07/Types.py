# 1. SUPERVISED   → Teacher hai (data + answers dono)
# 2. UNSUPERVISED → No teacher (sirf data, khud groups banao)
# 3. REINFORCEMENT → Game khelo, reward lo, seekho


## -----------------STEP 1 ---------------------
# Soch tu ghar ki price predict karna chahta hai
# Tere paas ye data hai:

# Ghar ka Size (sqft) → Price (Rs.)
# 1000 sqft          → 50 Lakh
# 1500 sqft          → 75 Lakh
# 2000 sqft          → 1 Crore
# 2500 sqft          → 1.25 Crore

# Tu pattern dekh raha hai?
# Jitna bada ghar → Utni zyada price

# Yahi ML seekhta hai!
# INPUT  = Size (sqft)   → isko X kehte hain
# OUTPUT = Price (Rs.)   → isko y kehte hain



#----------------- STEP 2 ---------------------
# pip install numpy 
import numpy as np

# Apna data banate hain
# X = Ghar ka size (sqft)
X = np.array([1000, 1500, 2000, 2500, 3000])

# y = Ghar ki price (lakhs mein)
y = np.array([50, 75, 100, 125, 150])

print("Ghar sizes:", X)   # Ghar sizes: [1000 1500 2000 2500 3000]
print("Ghar prices:", y)  # Ghar prices: [ 50  75 100 125 150]

#-------------------  STEP 3 -----------------------
from sklearn.linear_model import LinearRegression
import numpy as np 
#Data
X = np.array([1000,2000,3000,4000])
y = np.array([50,60,70,80])

# sklearn ko 2D array chahiye, isliye reshape karte hain
# -1 matlab "khud calculate kar rows"
# 1 matlab "1 column"
X = X.reshape(-1, 1)
print(" X kae first 5 rows ",X.shape)  # (5, 1) - 5 rows, 1 column

model = LinearRegression()
# Ye ek empty model hai, abhi kuch nahi jaanta

# MODEL TRAIN KARO
model.fit(X, y)
# ^ fit() matlab "X dekh aur y seekh"
# Model ne pattern pakad liya!

print("Training ho gayi!")

# -------------------- STEP 4 ---------------------
# prediction
# Naya ghar - 1800 sqft
# Price kya hogi?

naya_ghar = np.array([[1800]])  # 2D banana padega

price = model.predict(naya_ghar)

print(f"1800 sqft ghar ki predicted price: {price[0]:.0f} Lakh")

# Model ne khud calculate kiya!
# Humne koi formula nahi bataya
# Data dekh ke seekha!

# OUTPUT :-  1800 sqft ghar ki predicted price: 90 Lakh


# ------------------------- STEP 5 ----------------------


# Model ke andar kya formula bana?
print(f"Coefficient (slope): {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")

# Iska matlab:
# Price = slope × size + intercept
# Price = 0.05 × 1800 + 0 = 90

# Model ne khud ye formula seekha!




# -----------------------  OVERFITTING --------------------
