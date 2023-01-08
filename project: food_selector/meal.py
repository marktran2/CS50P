from food import Food
from menu import Menu

def main():
    menu = get_food_list()
    list = choose_food(menu)
    print("///////////////////////////////////  LOADING FOOD  /////////////////////////////////////////")
    i = 1
    for item in list:
        print(f"{i}. {item}")
        i += 1

def choose_food(menu):

    while True:
        preference_today = input("What to choose from today: type, style or both? ")
        if preference_today != "type" and preference_today != "style" and preference_today != "both":
            print("Invalid choice. Please choose again.")
        else:
            break

    while True and (preference_today == "type" or preference_today == "both"):
        preference_type = input("What meat would you like today? ").lower().strip()
        if preference_type in ["seafood", "fish", "pork", "beef", "chicken", "duck", "quail", "lamb", "vegetarian", "venison"]:
            break
        else:
            print("Invalid preference. Please try again.")

    while True and (preference_today == "style" or preference_today == "both"):
        preference_style = input("How would you like it to be made? ").lower().strip()
        if preference_style in ["fried", "stir-fried", "steamed", "boiled", "soup", "wrapped", "grilled", "caramelized", "salad", "stew"]:
            break
        else:
            print("Invalid preference. Please try again.")

    variety = []
    for item in menu.foodlist:
        if preference_today == "both":
            if item.type == preference_type and item.style == preference_style:
                variety.append(item.name)
        elif preference_today == "type":
            if item.type == preference_type:
                variety.append(item.name)
        elif preference_today == "style":
            if item.style == preference_style:
                variety.append(item.name)

    return variety

def get_food_list():

    eats = Menu()
    eats.add_food("Pho", "beef", "soup")
    eats.add_food("Bun Bo Hue", "pork", "soup")
    eats.add_food("Beef Stew (Bo Kho)", "beef", "stew")
    eats.add_food("Rice Paper Rolls", "pork", "wrapped")
    eats.add_food("Sweet & Sour Soup (Canh Chua)", "fish", "soup")
    eats.add_food("Udon Soup (Banh Canh)", "pork", "soup")
    eats.add_food("Broken Rice", "pork", "grilled")
    eats.add_food("Salt & Pepper Shrimp (Tom Rang Muoi)", "seafood", "stir-fried")
    eats.add_food("Shaking Beef (Bo Luc Lac)", "beef", "stir-fried")
    eats.add_food("Grilled Basa Fillet", "fish", "grilled")
    eats.add_food("Caramelized Salty Pork (Thit Kho Tieu)", "pork", "caramelized")
    eats.add_food("Caramelized Salty Fish (Ca Kho Tieu)", "fish", "caramelized")
    eats.add_food("Steamed Fish (Ca Hap)", "fish", "steamed")
    eats.add_food("Fried Fish (Ca Chien)", "fish", "fried")
    eats.add_food("Wok-tossed Pippies", "seafood", "stir-fried")
    eats.add_food("Fish Cake Soup with Veggies", "vegetarian", "soup")
    eats.add_food("BBQ Chicken (Ga Nuong)", "chicken", "grilled")
    eats.add_food("Steamed Rice Rolls (Banh Cuon)", "vegetarian", "salad")
    eats.add_food("Chicken Rice Porridge (Chao Ga)", "chicken", "soup")
    eats.add_food("Duck Rice Porridge (Chao Vit)", "duck", "soup")
    eats.add_food("Duck Vermicelli Noodle Soup", "duck", "soup")
    eats.add_food("Chicken Vermicelli Noodle Soup", "chicken", "soup")
    eats.add_food("Caramelized Salty Duck (Vit Xao Mang)", "duck", "caramelized")
    eats.add_food("Marinated Grilled Porkchops (Thit Nuong)", "pork", "grilled")
    eats.add_food("Marinated Fried Porkchops (Thit Chieng)", "pork", "fried")
    eats.add_food("Stir Fried Crispy Noodes (Mi Xao Gion)", "seafood", "stir-fried")
    eats.add_food("Combination Seafood Stir Fried", "seafood", "stir-fried")
    eats.add_food("Beef Curry", "beef", "stew")
    eats.add_food("Chicken Curry", "chicken", "stew")
    eats.add_food("Venison Curry", "venison", "stew")
    eats.add_food("Pork Stew Soup", "pork", "soup")
    eats.add_food("Hai Nam Chicken w/ Rice", "chicken", "boiled")
    eats.add_food("Seafood Fried Rice", "seafood", "fried")
    eats.add_food("BBQ Pork Belly", "pork", "bbq")
    eats.add_food("BBQ Duck", "duck", "bbq")
    eats.add_food("Caramelized Salty Chicken w/ Lemongrass", "chicken", "caramelized")
    eats.add_food("Fried Salmon", "fish", "fried")
    eats.add_food("Grilled Lamb Chops", "lamb", "grilled")
    eats.add_food("Combination Vegetarian Stir Fry", "vegetarian", "stir-fried")
    eats.add_food("Fish Cake w/ Bittermelon", "fish", "soup")
    eats.add_food("Caramelized Pork Belly w/ Eggs (Thit Kho Nuoc Dua)", "pork", "caramelized")
    eats.add_food("Ca Kho Lac", "fish", "soup")
    eats.add_food("Vernison Light Stew (Dê Xào Lăn)", "venison", "stew")
    eats.add_food("Fermented Fish Noodle Soup (Bun Mam)", "seafood", "soup")
    eats.add_food("Rice & Egg Noodle Seafood Combination Soup (Hu Tieu Mi)", "seafood", "soup")
    eats.add_food("Vermicelli Noodes w/ Stir-fried Beef", "beef", "salad")
    eats.add_food("Caramelized Ginger Duck", "duck", "caramelized")
    eats.add_food("Teriyaki Chicken", "chicken", "grilled")
    eats.add_food("Teriyaki Duck", "duck", "grilled")
    eats.add_food("Chicken Ragu", "chicken", "stew")
    eats.add_food("Salty Prawns (Tom Rau Man)", "seafood", "stir-fried")
    eats.add_food("Salt & Pepper Squid", "seafood", "fried")
    eats.add_food("Home-made BBQ Pork Belly (Xuong Nuong)", "pork", "bbq")
    eats.add_food("Grilled Beef Wrapped in Piper Lolot Leaves (Bò nướng lá lốt)", "beef", "grilled")
    eats.add_food("Udon Noodles w/ Creamy Coconut & Seafood Mix (Banh Tam Bi)", "seafood", "salad")
    eats.add_food("Hokkien Stir-fried Noodles", "seafood", "stir-fried")
    eats.add_food("Classic Viet Vermicelli Noodle Salad", "seafood", "salad")
    # eats.add_food("")
    # eats.add_food("")

    return eats

if __name__ == "__main__":
    main()