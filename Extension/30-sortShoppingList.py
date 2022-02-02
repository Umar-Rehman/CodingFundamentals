# Sorted shopping list

from difflib import get_close_matches

stock = ["apples", "avocado", "bananas", "carrots",
        "celery", "dates", "eggs", "garlic", "grapes",
        "kale", "milk", "spinach", "yoghurt"]

orderDict = {key:val for val,key in enumerate(stock)}

def sort_basket():
    basket = []

    while True:
        item = (input("Enter an item to add to basket (or END to finish): ").lower())

        if item == "end":
            break
        else:
            item = get_close_matches(item, stock)[0]
        if item not in stock:
            print(f"Sorry we don't sell {item}!")
        elif item in stock:
            basket.append(item)
            print(f"{item} added to basket!")

    basket.sort(key=orderDict.get)

    print(f"Your basket: {basket}")
    return basket

sort_basket()