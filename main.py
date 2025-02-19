from datetime import date
from tkinter import *
from tkinter import messagebox, ttk

from PIL import ImageTk, Image

from database import Database
from macros import Food, Drink
from meal import Meal



# A global list to store the Meal objects
completed_meals = []


#------------------------------------------------------------------#
#------------------ EXPORT TO .txt DAILY TOTAL FUNCTION -----------#
def export_daily_totals(total_macros, filename="dailyTotals.txt"):
    """
    Exports total macros of day to a txt file, in the following format:
    DD/MM/YYYY - Total daily macros:
    Calories: xkcal
    Protein: xg
    Carbs: xg
    Fats: xg
    -Potential to change/remove later when all input will be saved in the database.
    :param total_macros: Dictionary with macros keys and values.
    :param filename: The name of the file. Set default: dailyTotals.txt
    """
    today_str = date.today().strftime("%d/%m/%Y")

    with open(filename, "a") as file:
        file.write(f"{today_str} - Total daily macros:\n")
        file.write(f"Calories: {total_macros['kcal']:.2f}kcal\n")
        file.write(f"Protein: {total_macros['protein']:.2f}g\n")
        file.write(f"Carbs: {total_macros['carbs']:.2f}g\n")
        file.write(f"Fats: {total_macros['fats']:.2f}g\n\n")


#------------------------------------------------------------------#
#---------------------- MEAL WINDOW FUNCTION ----------------------#
def open_meal_window(meal_type, db_to_use, parent):
    """
    Opens a new window for entering items for the specified meal.
    Provides an autocomplete combo box for the food/drink name
    and an entry for the weight/volume.
    - Potential for add buttons to add items to the database, copy same items of different day other functionalities, better visual presentation.
    """
    meal = Meal(meal_type)
    meal_windw = Toplevel(parent)
    meal_windw.title(meal_type)
    meal_windw.geometry("400x400+700+300")
    meal_windw.grid_columnconfigure(0, weight=1)

    Label(meal_windw, text=f"Add items for {meal.meal_type}", font=('Calibri', 13, 'bold')).grid(row=0, column=0, pady=5)
    Label(meal_windw, text="Food/Drink:").grid(row=1, column=0, sticky=W, padx=20)

    food_names = db_to_use.get_all_food_names()
    ingred_entry = ttk.Combobox(meal_windw, width=30, values=food_names)
    ingred_entry.grid(row=2, column=0, pady=5)

    def update_suggestions(event):
        """
        Dynamically updates combo box suggestions as the user types.
        """
        typed_text = ingred_entry.get()
        filtered_list = [item for item in food_names if typed_text.lower() in item.lower()]
        ingred_entry["values"] = filtered_list

    ingred_entry.bind("<KeyRelease>", update_suggestions)

    Label(meal_windw, text="Weight/Volume (grams/ml):").grid(row=3, column=0, sticky=W, padx=20)
    value_entry = Entry(meal_windw, width=30)
    value_entry.grid(row=4, column=0, pady=5)

    items_text = Text(meal_windw, height=8, width=40)
    items_text.grid(row=5, column=0, padx=20, pady=5)

    def add_item():
        """
        Adds the item (Food or Drink) to the current meal.
        Validates user input and retrieves item data from the database.
        """
        item_name = ingred_entry.get().strip()
        value_str = value_entry.get().strip()

        if not item_name or not value_str:
            messagebox.showerror("Input Error", "Both name and weight/volume required.", parent=meal_windw)
            return

        try:
            value = float(value_str)
        except ValueError:
            messagebox.showerror("Input Error", "Weight/Volume must be numeric.", parent=meal_windw)
            return

        item_data = db_to_use.get_item(item_name)
        if not item_data:
            messagebox.showerror("Item Not Found", f"'{item_name}' not found in database.", parent=meal_windw)
            return

        kcal, protein, carbs, fats, category = item_data

        if category.lower() == "drink":
            item = Drink(item_name, kcal, protein, carbs, fats, value)
            unit = "ml"
        else:
            item = Food(item_name, kcal, protein, carbs, fats, value)
            unit = "g"

        meal.add_component(item)
        items_text.insert(END, f"{item.name} - {value} {unit}\n")

        ingred_entry.delete(0, END)
        value_entry.delete(0, END)
        ingred_entry.focus_set()

    def saved_meal():
        """
        Finalizes and saves the meal into the global 'completed_meals' list,
        notifies the user, displays total macros of set meal, then closes the window.
        """
        completed_meals.append(meal)
        display_meal_total = meal.meal_total()
        messagebox.showinfo("Meal saved", f"{meal.meal_type} has been saved.\n\n {display_meal_total}", parent=meal_windw)
        meal_windw.destroy()

    add_button = Button(meal_windw, text="Add Item", command=add_item)
    add_button.grid(row=6, column=0, pady=2)

    save_button = Button(meal_windw, text="Save Meal", command=saved_meal)
    save_button.grid(row=7, column=0, pady=2)

    ingred_entry.bind("<Return>", lambda event: value_entry.focus_set())
    value_entry.bind("<Return>", lambda event: add_item())


#------------------------------------------------------------------#
#------------------ DISPLAY DAILY TOTAL FUNCTION ------------------#
def display_daily_total():
    """
    Summarizes and displays the total macros from all saved meals in a message box.
    If no meals have been completed, it alerts the user.
    -Potential to add goals. Ex. "2200 out of 2500kcal"
    """
    total_macros = {"kcal": 0, "protein": 0, "carbs": 0, "fats": 0}

    if not completed_meals:
        messagebox.showinfo("Daily Total", "No meals have been completed yet.")
        return

    for meal in completed_meals:
        macros = meal.total_macros()
        for key in total_macros:
            total_macros[key] += macros[key]

    total = (f"Total Daily Macros:\n"
             f"Calories: {total_macros['kcal']:.2f}kcal\n"
             f"Protein: {total_macros['protein']:.2f}g\n"
             f"Carbs: {total_macros['carbs']:.2f}g\n"
             f"Fats: {total_macros['fats']:.2f}g")

    messagebox.showinfo("Daily Total", total)

    export_daily_totals(total_macros, filename="dailyTotals.txt")




#------------------------------------------------------------------#
#-------------------------- MAIN FUNCTION -------------------------#
def main():
    """
    The main function that establishes the database connection,
    sets up the Tkinter interface, and starts the GUI loop.
    """

    db_to_use = Database(db_name="postgres", user="postgres", password="SQLLearn")

    window = Tk()
    window.title("MANTRA")
    window.geometry("500x400+700+300")

    try:
        mantraImage = Image.open("mantra.png")
        icon = ImageTk.PhotoImage(mantraImage)
        window.iconphoto(True, icon)
    except Exception as e:
        print(f"Icon image not found/ error loading image: {e}")

    mantraImage = mantraImage.resize((50, 50))
    logo = ImageTk.PhotoImage(mantraImage)

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=0)
    window.grid_columnconfigure(2, weight=1)

    app_box = Label(window, text="MANTRA: A tool for Consistency!", font=('Calibri', 15, 'bold'), image=logo,
                    compound='top')
    app_box.grid(row=0, column=0, columnspan=3, pady=15, padx=50, sticky=N)

    row_index = 1
    for meal_type in Meal.VALID_MEALS:
        button = Button(window, text=meal_type, width=20,
                        command=lambda mt=meal_type: open_meal_window(mt, db_to_use, window))
        button.grid(row=row_index, column=1, pady=1)
        row_index += 1

    daily_total_button = Button(window, text="Daily Total", width=20, command=display_daily_total)
    daily_total_button.grid(row=row_index, column=1, pady=20)
    row_index += 1

    exit_button = Button(window, text="Exit", width=20,
                         command=lambda: (db_to_use.close_connection(), window.destroy()))
    exit_button.grid(row=row_index, column=1, pady=15)

    window.mainloop()



#------------------------------------------------------------------#
#----------------------------- MAIN -------------------------------#

if __name__ == "__main__":
    main()
