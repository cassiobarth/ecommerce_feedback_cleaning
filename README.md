# E-commerce Customer Feedback Data Cleaning Project

This repository contains a simple, yet realistic, project focused on cleaning raw customer feedback data. The primary goal is to take a messy dataset with common issues—like missing values, inconsistent formatting, and extraneous characters—and transform it into a clean, structured format suitable for further analysis, such as sentiment analysis or business intelligence reporting.

## Project Contents

- `data/`: Holds the original raw dataset (`raw_feedback.csv`) and the cleaned output file (`clean_feedback.csv`).
- `scripts/`: Contains the Python script (`clean_feedback.py`) that performs the data cleaning tasks using the pandas library.
- `.gitignore`: Specifies files and folders to be ignored by Git.
- `LICENSE`: The license for the project (e.g., MIT).
- `README.md`: This file, providing an overview of the project.

## Data Issues Addressed

The `raw_feedback.csv` dataset has the following known data quality problems:

- **Missing Values:** The `rating` and `feedback_text` columns contain missing entries.
- **Inconsistent Formatting:** The `source_channel` column has a mix of uppercase and lowercase letters.
- **Irregular Data:** The `customer_name` column includes periods and extra spaces.
- **Unstructured Text:** The `feedback_text` has unnecessary commas and leading/trailing spaces.

## How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install dependencies:**
    This project requires the `pandas` library. Install it using pip:
    ```bash
    pip install pandas
    ```

3.  **Execute the cleaning script:**
    From the project root directory, run the script:
    ```bash
    python scripts/clean_feedback.py
    ```

After running the script, a new file named `clean_feedback.csv` will be created in the `data/` directory.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.