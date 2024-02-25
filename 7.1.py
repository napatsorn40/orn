cash = float(input("กรุณาระบุรายได้ : "))

if cash >= 15000 and cash < 20000:
    cardtype = "บัตร Sliver"
elif cash < 100000:
    cardtype = "บัตร Gold"
else:
    cardtype = "บัตร Platinum"

print(f"รายได้ของคุณ {cash:.2f} บาท สามารถทำ{creditcard} ได้")