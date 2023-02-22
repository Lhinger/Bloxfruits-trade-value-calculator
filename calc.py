# made by lhinger

def price_of(fruit_name: str) -> int: return name_to_price[fruit_name] 
    
name_to_price = {
    "blank":    0,
    "none": 0,
    "kilo":  7500, "Kilo": 7500,
    "spin": 10000, "Spin": 10000,
    "chop": 100000, "Chop": 100000,
    "spring": 20000, "Spring": 20000,
    "bomb": 30000, "Bomb": 30000,
    "smoke": 200000, "Smoke": 200000,
    "spike": 100000, "Spike": 100000,
    "flame":450000, "Flame":450000,
    "falcon": 200000, "Falcon": 200000,
    "bird: falcon": 200000, "bird: falcon": 200000,
    "ice": 800000, "Ice": 800000,
    "sand": 750000, "Sand": 750000,
    "dark": 1000000, "Dark": 1000000,
    "revive": 450000, "Revive": 450000,
    "diamond": 550000, "Diamond": 550000, "daimond": 550000, "dimond": 550000,
    "light": 900000, "Light": 900000,
    "love": 350000, "Love": 350000,
    "rubber": 400000, "Rubber": 400000,
    "barrier": 400000, "Barrier": 400000,
    "magma": 1100000, "Magma": 1100000,
    "quake": 1100000, "Quake": 1100000,
    "buddha": 2300000, "Buddha": 2300000, "human: buddha": 2300000, "buddah": 2300000, "budha": 2300000,
    "string": 1600000, "String": 1600000,
    "phoenix": 1700000, "Phoenix": 1700000, "bird: pheonix": 1700000, "pheonix": 1700000, "phenix": 1700000, "fenix": 1700000,
    "portal": 2200000, "Portal": 2200000,
    "rumble": 2450000, "Rumble": 2450000,
    "paw": 1750000, "Paw": 1750000,
    "blizzard": 2700000, "Blizzard": 2700000, "blizard": 2700000,
    "gravity": 2600000, "Gravity": 2600000,
    "dough": 4400000, "Dough": 4400000,
    "shadow": 3300000, "Shadow": 3300000,
    "venom": 4000000, "Venom": 4000000,
    "control": 2600000, "Control": 2600000,
    "spirit": 2500000, "Spirit": 2500000,
    "dragon": 4200000, "Dragon": 4200000,
    "leopard": 7800000, "Leopard": 7800000, "lepard": 7800000, "leo": 7800000
}  

fruit1 = input("Enter first fruit: " )
fruit2 = input("Enter second fruit: ")
fruit3 = input("Enter third fruit: ")
fruit4 = input("Enter fourth fruit: ")

print(fruit1, price_of(fruit1), "+", fruit2, price_of(fruit2), "+", fruit3, price_of(fruit3), "+", fruit4, price_of(fruit4), "=", price_of(fruit1) + price_of(fruit2) + price_of(fruit3) + price_of(fruit4))
