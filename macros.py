#------------------------------------------------------------------#
#-------------------------- MACROS CLASS --------------------------#
class Macros:
    def __init__(self, name, kcal, protein, carbs, fats):
        """
        A base class to hold essential nutritional information.

        :param name: Name of the food/drink (string)
        :param kcal: Calories per 100g/ml (float or numeric)
        :param protein: Protein per 100g/ml (float or numeric)
        :param carbs: Carbs per 100g/ml (float or numeric)
        :param fats: Fats per 100g/ml (float or numeric)
        """
        self.name = name
        self.kcal = kcal
        self.protein = protein
        self.carbs = carbs
        self.fats = fats


    def macros_calculator(self, factor):
        """
        Scales the macros by a specified factor.

        :param factor: Scaling factor (float)
        :return: A dictionary with scaled macros.
        """
        return {
            "kcal": float(self.kcal) * factor,
            "protein": float(self.protein) * factor,
            "carbs": float(self.carbs) * factor,
            "fats": float(self.fats) * factor
        }



#------------------------------------------------------------------#
#--------------------------- FOOD CLASS ---------------------------#
class Food(Macros):
    def __init__(self, name, kcal, protein, carbs, fats, weight):
        """
        Represents a food item with a specific weight in grams.
        Inherits from the Macros class.
        -Potential to add cooked method and return different macros
        """
        super().__init__(name, kcal, protein, carbs, fats)
        self.weight = weight

    def scale_factor(self):
        """
        For food, the factor is weight in grams / 100 (since macros are per 100g).
        :return: A dictionary with scaled macros.
        """
        factor = self.weight / 100
        return self.macros_calculator(factor)



#------------------------------------------------------------------#
#-------------------------- DRINK CLASS ---------------------------#
class Drink(Macros):
    def __init__(self, name, kcal, protein, carbs, fats, volume):
        """
        Represents a drink item with a specific volume in milliliters.
        Inherits from the Macros class.
        -Potential to add caffeine method, hydration level
        """
        super().__init__(name, kcal, protein, carbs, fats)
        self.volume = volume

    def volume_factor(self):
        """
        For a drink, the factor is volume in milliliters / 100 (since macros are per 100ml).
        :return: A dictionary with scaled macros.
        """
        factor = self.volume / 100
        return self.macros_calculator(factor)
