from macros import *

#------------------------------------------------------------------#
# --------------------------- MEAL CLASS --------------------------#
class Meal:
    VALID_MEALS = ["Breakfast", "Pre-workout", "Post-workout", "Lunch", "Snack", "Dinner"]

    def __init__(self, meal_type):
        """
        Represents a meal that can hold multiple foods/drinks.
        :param meal_type: One of the valid meals (e.g., 'Breakfast').
        -Potential to add new meal types by user input.
        """

        self.meal_type = meal_type
        self.meal_components = []  # List of Food or Drink objects

    def add_component(self, item):
        """
        Adds a Food or Drink object to the meal.
        :param item: An instance of Food or Drink.
        """
        if isinstance(item, (Food, Drink)):
            self.meal_components.append(item)

    def total_macros(self):
        """
        Calculates total macros for all items in this meal.
        :return: Dictionary containing sum of kcal, protein, carbs, and fats.
        """
        total = {"kcal": 0, "protein": 0, "carbs": 0, "fats": 0}
        for item in self.meal_components:
            if isinstance(item, Food):
                macros = item.scale_factor()
            else:
                macros = item.volume_factor()

            # Accumulate macros
            for key in total:
                total[key] += macros[key]
        return total

    def meal_total(self):
        """
        Returns a formatted string containing:
        - The meal type (e.g., 'Breakfast')
        - All items in the meal, with their weights/volumes
        - The total macros for the entire meal
        """
        total = f"Meal Total: {self.meal_type}\n"
        for item in self.meal_components:
            if isinstance(item, Food):
                total += f" - {item.name} ({item.weight}g)\n"
            else:
                total += f" - {item.name} ({item.volume}ml)\n"

        total_macros = self.total_macros()
        total += (f"\nTotal meal Macros:\n"
                  f"Calories: {total_macros['kcal']:.2f}kcal\n"
                  f"Protein: {total_macros['protein']:.2f}g\n"
                  f"Carbs: {total_macros['carbs']:.2f}g\n"
                  f"Fats: {total_macros['fats']:.2f}g")
        return total
