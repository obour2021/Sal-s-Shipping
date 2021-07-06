weight = 41.5
cost_ground_premium_shipping = 125.00
print("The cost of ground shipping premium is $" + str(cost_ground_premium_shipping))
# Ground Shipping
if weight <= 2:
  cost_ground_shipping = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground_shipping = weight * 3.0 + 20
elif weight > 6 and weight <= 10:
  cost_ground_shipping = weight * 4.0 + 20
else:
  cost_ground_shipping = weight * 4.75 + 20
print("The cost of normal shipping for " + str(weight) + "lb is $" + str(cost_ground_shipping))

# Drone Shipping
if weight <= 2:
  cost_drone_shipping = weight * 4.5 + 0.0
elif weight > 2 and weight <= 6:
  cost_drone_shipping = weight * 9.0 + 0.0
elif weight > 6 and weight <= 10:
  cost_drone_shipping = weight * 12.0 + 0.0
else:
  cost_drone_shipping = weight * 14.25 + 0.0

print("The cost of drone shipping for " + str(weight) + "lb is $" + str(cost_drone_shipping))
