### - MANTRA - MAcro Nutritional TRacker App - ###



## Brief Introduction:
 I chose this project because I am someone who exercises regularly and follows a controlled diet. I have studied nutrition in my free time, and this application
 aims to automate the daily calculations and records I keep to achieve my goals. For this reason, the database focuses on foods that are primarily high in protein.

Although there are many applications that do the same or even more (e.g., using AI to estimate macros from a meal photo), my goal is to create a tool that meets 
my specific daily needs while ensuring a level of accuracy that other applications may not provide. To achieve this precision, the ingredients in the database—apart 
from a few beverages included for testing purposes—are items I consume regularly. Their nutritional values come directly from product labels rather than generic 
reference values.

In summary, this project is about creating something I will actively use and that provides the most precise tracking possible for my daily nutrition.



## Program Functionality:
- Register ingredients and quantities (g/ml) for a meal, save the meal, and print its macro values.
- After entering one or multiple meals, the program calculates, displays, and saves the total daily macros in a `.txt` file.

## Growth Potential:
- **Market Expansion:** Despite the existence of similar tools, focusing on **accuracy** and **user simplicity** can attract a growing audience. The increasing 
popularity of **fitness and diet tracking** suggests that this trend will continue, as it provides significant health benefits.
- **Planned Improvements:**
    - **Graphical Design:** The current interface is simple and lacks visual appeal.
    - **User Interface Enhancement:** Consider restructuring the main screen, for example:
      `Add Meal -> List of Meals/Records -> View Daily Entries -> Select Date, etc.`
    - **Convenience:** Some shortcuts have been implemented (e.g., pressing `Enter` to move between fields or add an item), but additional features could 
enhance user experience.
    - **Customization:** Allow users to modify macro values and personalize the application based on their preferences and frequently used products.

- **New Platforms:** Developing a **mobile application (Android/iOS)**, as mobile devices are the most commonly used and convenient platforms for **fitness & health** 
tracking applications.



####   IMPORTANT:   #####

## Requirements:
- Python 3.8+
- PostgreSQL
- `psycopg2` (for database connectivity)
- `Pillow` (for image processing)
- `Tkinter` (for GUI development)


## How to Run:
1. Run the `food.sql` script to create the database table.
   - If this is not possible, use the SQL queries listed at the end of this document (or use file "table queries") to create the table manually.
2. Update the database access credentials in the main script (`main.py`):
   - **Database Name:** Update `db_name` in `main.py`.
   - **Username:** Update `user` in `main.py`.
   - **Password:** Update `password` in `main.py`.
   - **Host & Port:** If different from default (`localhost`, `5432`), update in `database.py`.
3. Navigate to the project directory and run:
   ```
   python main.py
   ```





#### PostgreSQL queries: 


CREATE TABLE food (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    kcal NUMERIC(10, 2) NOT NULL,
    carbs NUMERIC(10, 2) NOT NULL,
    protein NUMERIC(10, 2) NOT NULL,
    fats NUMERIC(10, 2) NOT NULL,
    category VARCHAR(50) NOT NULL
);

INSERT INTO food (id, name, kcal, carbs, protein, fats, category)
VALUES
    (25, 'Milk', 47.00, 4.80, 3.40, 0.90, 'drink'),
    (28, 'Water', 0.00, 0.00, 0.00, 0.00, 'drink'),
    (29, 'Black Coffee', 0.83, 0.00, 0.12, 0.00, 'drink'),
    (30, 'Milk', 62.08, 4.88, 3.21, 3.33, 'drink'),
    (31, 'Coke', 39.44, 10.99, 0.00, 0.00, 'drink'),
    (32, 'Diet Coke', 0.00, 0.00, 0.00, 0.00, 'drink'),
    (33, 'Coke Zero', 0.00, 0.00, 0.00, 0.00, 'drink'),
    (34, 'Sprite Zero', 0.00, 0.00, 0.00, 0.00, 'drink'),
    (35, 'Red Bull', 45.07, 11.27, 0.34, 0.00, 'drink'),
    (36, 'Red Bull Light', 4.23, 1.13, 0.00, 0.00, 'drink'),
    (37, 'Monster', 63.00, 11.42, 0.00, 0.00, 'drink'),
    (38, 'Monster Ultra', 2.11, 0.63, 0.00, 0.00, 'drink'),
    (2, 'Organic Spinach', 19.00, 0.20, 2.60, 0.60, 'food'),
    (3, 'HP Plain Yogurt', 65.00, 4.10, 11.00, 0.20, 'food'),
    (4, 'Chicken Breast', 106.00, 0.00, 24.00, 1.10, 'food'),
    (5, 'Chicken Thigh', 109.00, 0.00, 20.90, 2.80, 'food'),
    (6, 'Greek Yogurt 0%', 54.00, 3.00, 10.30, 0.00, 'food'),
    (7, 'Eggs', 131.00, 0.00, 12.60, 9.00, 'food'),
    (8, 'Egg Whites', 48.00, 0.00, 10.90, 0.20, 'food'),
    (9, 'Minced Beef', 130.00, 0.00, 21.90, 4.20, 'food'),
    (10, 'Onions', 39.00, 8.60, 1.10, 0.10, 'food'),
    (11, 'Sweet Potato', 84.00, 20.50, 1.10, 0.30, 'food'),
    (12, 'Peanut Butter', 629.00, 14.40, 24.30, 51.20, 'food'),
    (13, 'Cottage Cheese', 78.00, 4.70, 13.60, 2.20, 'food'),
    (14, 'Skyr', 63.00, 4.10, 11.00, 0.20, 'food'),
    (15, 'Broccoli', 28.00, 2.80, 3.30, 0.50, 'food'),
    (16, 'Avocado', 190.00, 1.90, 1.90, 19.50, 'food'),
    (17, 'Flour', 352.00, 80.90, 10.00, 1.40, 'food'),
    (18, 'Lamb Chops', 277.00, 0.00, 17.60, 23.00, 'food'),
    (19, 'Fillet Steak', 140.00, 0.00, 21.20, 6.10, 'food'),
    (20, 'Ribeye', 153.00, 0.00, 22.60, 7.00, 'food'),
    (21, 'Peppers Mixed', 20.00, 2.60, 0.60, 0.10, 'food'),
    (22, 'Blueberries', 40.00, 9.10, 0.80, 0.20, 'food'),
    (23, 'Skyr Raspberry', 57.00, 4.60, 8.90, 0.20, 'food'),
    (24, 'Salmon', 199.00, 0.00, 22.10, 12.10, 'food'),
    (26, 'Tenderstem Broccoli', 57.00, 4.00, 4.40, 0.90, 'food'),
    (27, 'Basmati Rice', 360.00, 77.07, 8.51, 0.90, 'food'),
    (1, 'Parmigiano Reggiano', 402.00, 0.10, 32.40, 29.70, 'food'),
    (39, 'ESN protein alm & coco' 381.00, 7.10, 73.00, 5.60, 'food'),
    (40, 'Banana', 89.00, 22.84, 1.10, 0.00, 'food'),
    (41, 'Olive Oil', 822.00, 00.00, 00.00, 00.00, 'drink');

    

---

## Credits:

This project was developed as part of my learning process in Python, focusing on object-oriented programming (OOP), GUI development using Tkinter, and database interaction with PostgreSQL.

The main goal of this project was to build an interactive and practical application that allows users to track their daily nutritional intake in an efficient and structured way. The project integrates various OOP principles such as inheritance, polymorphism, and encapsulation to create a modular and scalable codebase.

Additionally, working with Tkinter for GUI development helped enhance my understanding of event-driven programming and user interface design, while PostgreSQL provided hands-on experience in database management and query execution.

**Key Learning Areas:**  
- Object-Oriented Programming (OOP)  
- GUI development with Tkinter  
- Database integration with PostgreSQL  
- File handling and data persistence  
- Interactive command processing  

**Developer:** [Toma Paraschiv]
