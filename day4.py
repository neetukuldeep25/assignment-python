vehicle_type = input("Enter vehicle type: ")
fastag_active = input("Is FASTag active? (yes/no): ")
is_national_holiday = input("Is it a national holiday? (yes/no): ")

if vehicle_type == "car" and fastag_active == "yes" and is_national_holiday == "yes":
    print("50% discount")

elif vehicle_type == "car" and fastag_active == "yes":
    print("20% discount")

elif vehicle_type == "truck":
    print("Toll = ₹200")

else:
    print("Toll = ₹100")