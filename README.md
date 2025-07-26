# Web-scraping
Project 2: Web Scraping and Data Analysis (Simulation)
Project Goal

The goal of this project is to demonstrate the ability to automatically collect data from the internet (web scraping simulation) and to clean, explore, and visualize it using Python and the pandas, matplotlib, and seaborn libraries.

In this project, we simulate the process of fetching book data (title, author, price, rating, publisher) from a fictional website.
Technologies

    Python 3.x

    pandas: For data manipulation and analysis.

    matplotlib: For creating data visualizations.

    seaborn: For creating aesthetically pleasing statistical visualizations.

    numpy: For numerical operations (used indirectly by pandas).

File Structure

    price_scraper.py: A script responsible for simulating data fetching and saving it to a CSV file.

    prices.csv: A CSV file containing the generated (simulated) book price data. This file is created by price_scraper.py.

    price_analysis.py: A Python script that acts as a Jupyter notebook. It contains code for loading data, cleaning it, exploring, and visualizing.

    README.md: This file, containing the project description and instructions.

How to Run the Project

To run the project, follow these steps:

    Ensure you have Python installed (version 3.x).

    Install the required libraries, if you don't have them already:

    pip install pandas matplotlib seaborn numpy

    Generate the data by running the price_scraper.py script:

    python price_scraper.py

    This will create the prices.csv file in the same directory.

    Perform the analysis by running the price_analysis.py script:

    python price_analysis.py

    This script will load prices.csv, perform the analysis, and display the plots. The plots will open in separate windows.

Analysis Description

The price_analysis.py script performs the following steps:

    Data Loading: Loads data from the prices.csv file into a pandas DataFrame.

    Data Cleaning:

        Handles missing values (e.g., fills missing ratings with the median, missing authors with 'No data').

        Converts the 'Price (PLN)' column to a numeric type, removing rows with invalid values.

        Removes duplicate rows.

    Data Exploration:

        Displays basic descriptive statistics for prices.

        Identifies the most expensive and highest-rated books.

        Analyzes the number of books per publisher.

        Calculates the average price and average rating per author/publisher.

    Data Visualization:

        Price distribution histogram: Shows how book prices are distributed in the dataset.

        Bar chart of the number of books per publisher: Presents the top 5 publishers with the most books.

        Bar chart of the average rating per author: Shows the top 5 authors with the highest average rating.

        Box plot of prices by publisher: Illustrates the price distribution for the top 3 publishers, helping to identify price variance.

This project provides a solid foundation for further, more advanced analyses and expansion with real web scraping.