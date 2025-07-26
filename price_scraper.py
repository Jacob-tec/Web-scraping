import pandas as pd
import numpy as np
import os

# --- price_scraper.py ---
# Goal: Simulate fetching book price data and saving it to a CSV file.
# In a real project, you would use libraries like requests and BeautifulSoup
# to parse HTML from websites (e.g., Empik, OLX).
# Here, we generate synthetic data to demonstrate the analysis process.

def generate_and_save_prices_data(filename="prices.csv"):
    """
    Generates synthetic book price data and saves it to a CSV file.
    """
    print(f"Generating synthetic book price data to '{filename}'...")

    data = {
        'Title': [ # Changed 'Tytuł' to 'Title'
            'The Lord of the Rings', 'The Hobbit', 'Dune', 'Foundation', '1984',
            'Crime and Punishment', 'One Hundred Years of Solitude', 'The Master and Margarita', 'The Little Prince', 'Solaris',
            'The Witcher: The Last Wish', 'The Witcher: Sword of Destiny', 'The Witcher: Blood of Elves',
            'Harry Potter and the Philosopher\'s Stone', 'Harry Potter and the Chamber of Secrets',
            'A Game of Thrones', 'A Clash of Kings', 'A Storm of Swords', 'Assassin\'s Apprentice', 'Royal Assassin',
            'The Lord of the Rings', 'The Hobbit', 'Dune', '1984', 'Crime and Punishment' # Added duplicates and missing values
        ],
        'Author': [ # Changed 'Autor' to 'Author'
            'J.R.R. Tolkien', 'J.R.R. Tolkien', 'Frank Herbert', 'Isaac Asimov', 'George Orwell',
            'Fyodor Dostoevsky', 'Gabriel Garcia Marquez', 'Mikhail Bulgakov', 'Antoine de Saint-Exupéry', 'Stanisław Lem',
            'Andrzej Sapkowski', 'Andrzej Sapkowski', 'Andrzej Sapkowski',
            'J.K. Rowling', 'J.K. Rowling',
            'George R.R. Martin', 'George R.R. Martin', 'George R.R. Martin', 'Robin Hobb', 'Robin Hobb',
            'J.R.R. Tolkien', 'J.R.R. Tolkien', 'Frank Herbert', 'George Orwell', np.nan # np.nan for missing author
        ],
        'Price (PLN)': [ # Changed 'Cena (PLN)' to 'Price (PLN)'
            55.99, 39.99, 68.50, 45.00, 32.00,
            48.90, 62.00, 58.00, 29.99, 41.50,
            49.99, 49.99, 52.00,
            38.00, 39.50,
            75.00, 72.50, 78.00, 65.00, 60.00,
            'MISSING', 39.99, 68.50, 32.00, 48.90 # 'MISSING' as data error
        ],
        'Rating (1-5)': [ # Changed 'Ocena (1-5)' to 'Rating (1-5)'
            4.8, 4.7, 4.6, 4.5, 4.3,
            4.4, 4.7, 4.6, 4.9, 4.2,
            4.7, 4.7, 4.6,
            4.8, 4.7,
            4.9, 4.8, 4.9, 4.5, 4.4,
            4.8, 4.7, np.nan, 4.3, 4.4 # np.nan for missing rating
        ],
        'Publisher': [ # Changed 'Wydawnictwo' to 'Publisher'
            'Amber', 'Amber', 'Rebis', 'Rebis', 'Muza',
            'Znak', 'Muza', 'W.A.B.', 'Znak', 'Wydawnictwo Literackie',
            'SuperNowa', 'SuperNowa', 'SuperNowa',
            'Media Rodzina', 'Media Rodzina',
            'Zysk i S-ka', 'Zysk i S-ka', 'Zysk i S-ka', 'Mag', 'Mag',
            'Amber', 'Amber', 'Rebis', 'Muza', 'Znak'
        ]
    }

    df = pd.DataFrame(data)

    # Save to CSV file
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Data successfully saved to '{filename}'.")

if __name__ == "__main__":
    generate_and_save_prices_data()
