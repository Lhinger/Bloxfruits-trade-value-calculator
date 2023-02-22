# made by lhinger, Discord: SausageGobbler#8015

def price_of(fruit_name: str) -> int: return name_to_price[fruit_name]


name_to_price = {
    "blank": 0, "none": 0, "0": 0, "nothing": 0, "no": 0,
    "kilo": 7500,
    "spin": 10000,
    "chop": 100000,
    "spring": 20000,
    "bomb": 30000,
    "smoke": 200000,
    "spike": 100000,
    "flame": 450000,
    "falcon": 200000, "bird: falcon": 200000,
    "ice": 800000,
    "sand": 750000,
    "dark": 1000000,
    "revive": 450000,
    "diamond": 550000, "daimond": 550000, "dimond": 550000,
    "light": 900000,
    "love": 350000,
    "rubber": 400000,
    "barrier": 400000,
    "magma": 1100000,
    "quake": 1100000,
    "buddha": 2300000, "human: buddha": 2300000, "buddah": 2300000, "budha": 2300000,
    "string": 1600000,
    "phoenix": 1700000, "bird: pheonix": 1700000, "pheonix": 1700000, "phenix": 1700000, "fenix": 1700000,
    "portal": 2200000,
    "rumble": 2450000,
    "paw": 1750000,
    "blizzard": 2700000, "blizard": 2700000,
    "gravity": 2600000,
    "dough": 4400000,
    "shadow": 3300000,
    "venom": 4000000,
    "control": 2600000,
    "spirit": 2500000,
    "dragon": 4200000,
    "leopard": 7800000, "lepard": 7800000, "leo": 7800000
}

offerfruit1 = input("Enter the first fruit you are offering: ").lower()
offerfruit2 = input("Enter the second fruit you are offering: ").lower()
offerfruit3 = input("Enter the third fruit you are offering: ").lower()
offerfruit4 = input("Enter the fourth fruit you are offering: ").lower()

print(offerfruit1, price_of(offerfruit1), "+", offerfruit2, price_of(offerfruit2), "+", offerfruit3,
      price_of(offerfruit3), "+", offerfruit4, price_of(offerfruit4), "=",
      price_of(offerfruit1) + price_of(offerfruit2) + price_of(offerfruit3) + price_of(offerfruit4))

offertotal = price_of(offerfruit1) + price_of(offerfruit2) + price_of(offerfruit3) + price_of(offerfruit4)

receivefruit1 = input("Enter the first fruit you are receiving: ").lower()
receivefruit2 = input("Enter the second fruit you are receiving: ").lower()
receivefruit3 = input("Enter the third fruit you are receiving: ").lower()
receivefruit4 = input("Enter the fourth fruit you are receiving: ").lower()

receivetotal = price_of(receivefruit1) + price_of(receivefruit2) + price_of(receivefruit3) + price_of(receivefruit4)

if offertotal < (40 / 100 * receivetotal):
    print("\033[1;31;40m Offer must be more than 40% of receiving value. \n")
else:
    print(receivefruit1, price_of(receivefruit1), "+", receivefruit2, price_of(receivefruit2), "+", receivefruit3,
          price_of(receivefruit3), "+", receivefruit4, price_of(receivefruit4), "=",
          price_of(receivefruit1) + price_of(receivefruit2) + price_of(receivefruit3) + price_of(receivefruit4))

if offertotal >= (40/100 * receivetotal) and receivetotal >= (110/100 * offertotal):
    print("\033[1;32;40m W trade :) \n")
elif offertotal >= (40/100 * receivetotal) and (90 / 100 * offertotal) < receivetotal < (110 / 100 * offertotal):
    print("\033[1;33;40mFair trade")
elif offertotal >= (40/100 * receivetotal) and receivetotal < (90/100 * offertotal):
    print("\033[1;31;40m L trade :( \n")
