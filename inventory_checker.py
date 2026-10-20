# Product inventory checker
import os
import sys

# ---------- Inventory database ----------
# Keys = product names (str), values = units in stock (int)
inventory = {
    "apple": 12,
    "banana": 3,
    "milk": 0,
    "bread": 7,
    "eggs": 4,
    "cheese": 0,
    "orange": 9,
    "grapes": 2,
    "strawberry": 6,
    "watermelon": 1,
    "carrot": 11,
    "tomato": 0,
    "potato": 8,
    "rice": 10,
    "honey": 3,
    "cookies": 5,
}

# Keys = product names (str), values = emoji icons (str)
icons = {
    "apple": "🍎",
    "banana": "🍌",
    "milk": "🥛",
    "bread": "🍞",
    "eggs": "🥚",
    "cheese": "🧀",
    "orange": "🍊",
    "grapes": "🍇",
    "strawberry": "🍓",
    "watermelon": "🍉",
    "carrot": "🥕",
    "tomato": "🍅",
    "potato": "🥔",
    "rice": "🍚",
    "honey": "🍯",
    "cookies": "🍪",
}

# ---------- Settings ----------
LOW_STOCK_THRESHOLD = 5
BAR_LENGTH = max(inventory.values())  # bar is as long as the biggest stock count

# Terminal setup. Not every Python environment supports these,
# so if one fails we skip it instead of crashing.
try:
    os.system("")  # turns on colour support in the Windows terminal
except Exception:
    pass

try:
    sys.stdout.reconfigure(encoding="utf-8")  # lets emojis and box lines print
except Exception:
    pass

# Colour codes for the terminal
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def stock_bar(stock):
    """Draw a bar showing stock compared to the best-stocked product."""
    return "█" * stock + "░" * (BAR_LENGTH - stock)


# ---------- Welcome screen ----------
print(CYAN + "╔══════════════════════════════════════════════╗")
print("║       🛒  WELCOME TO THE STOCK CHECKER  🛒      ║")
print("╚══════════════════════════════════════════════╝" + RESET)
print("Hi there! Curious whether something is on the shelf?")
print("Type a product name and I'll check the stockroom for you.")
print()
print(BOLD + "📋 Products you can check:" + RESET)
for name in inventory:
    print(f"   {icons[name]}  {name}")
print()
print(DIM + "Tip: type the name exactly as listed (e.g. 'eggs', not 'egg')." + RESET)
print(DIM + "Capital letters don't matter." + RESET)
print()
print(BOLD + "🚦 What the results mean:" + RESET)
print(f"   {GREEN}● IN STOCK{RESET}      {LOW_STOCK_THRESHOLD} or more units")
print(f"   {YELLOW}● LOW STOCK{RESET}     fewer than {LOW_STOCK_THRESHOLD} units")
print(f"   {RED}● OUT OF STOCK{RESET}  0 units")
print()
print(f"{BOLD}👋 Finished? Type {CYAN}quit{RESET}{BOLD} at any time to exit.{RESET}")
print(CYAN + "─" * 48 + RESET)

# ---------- Main loop ----------
checks = 0

while True:
    print()
    product = input("Product name: ").strip().lower()

    if product == "quit":
        break

    if product == "":
        print("   Oops, you didn't type anything. Give it another go!")
        continue

    checks += 1

    if product not in inventory:
        print(f"   {RED}❓ Hmm, '{product}' isn't on our list.{RESET}")
        print("   Did you mean one of these? " + ", ".join(inventory))
    else:
        stock = inventory[product]
        label = f"{icons[product]}  {product.title()}"
        if stock == 0:
            print(f"   {label}  {RED}{stock_bar(stock)}  ✖ OUT OF STOCK{RESET}")
            print("   Sorry, we've run out. Check back soon!")
        elif stock < LOW_STOCK_THRESHOLD:
            print(f"   {label}  {YELLOW}{stock_bar(stock)}  ⚠ LOW STOCK ({stock} left){RESET}")
            print("   Better be quick, it's almost gone!")
        else:
            print(f"   {label}  {GREEN}{stock_bar(stock)}  ✔ IN STOCK ({stock} units){RESET}")
            print("   Plenty available, good news!")

# ---------- Goodbye ----------
print()
print(CYAN + "─" * 48 + RESET)
print(f"✨ Thanks for stopping by! You checked {checks} product(s) today.")
print("   See you next time! 👋")
print(CYAN + "─" * 48 + RESET)