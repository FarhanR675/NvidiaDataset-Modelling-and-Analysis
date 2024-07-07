# Nvidia Dataset Modelling and Analysis

## Description
An analytical platform designed to analyze Nvidia stock data and predict future stock prices. This project leverages Python, Pandas, Matplotlib, and Scikit-learn to provide comprehensive data analysis, visualization, and predictive modeling.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Future Updates](#future-updates)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/nvidia-dataset-modelling-analysis.git
    ```

2. Navigate to the project directory:
    ```sh
    cd nvidia-dataset-modelling-analysis
    ```

3. Set up a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Download the Nvidia stock dataset and place it in the appropriate directory (if applicable).

## Usage

1. Run the data analysis and modeling script:
    ```sh
    python main.py
    ```

2. Example usage within a Python script:
    ```python
    from analysis import analyze_data
    from prediction import predict_stock_prices

    # Load and analyze data
    analyze_data('data/nvidia_stock_data.csv')

    # Predict future stock prices
    predict_stock_prices('data/nvidia_stock_data.csv')
    ```

## Features

- **Data Integration:** Models Nvidia stock data in Excel and processes it in Python.
- **Data Cleaning and Preprocessing:** Implements functions for data integrity checks and handling missing values.
- **Data Visualization:** Plots various stock price points using Matplotlib.
- **Predictive Analytics:** Uses a linear regression model to forecast future stock prices.

## Technologies Used

- **Programming Languages:** Python
- **Libraries and Tools:** Pandas, Matplotlib, Scikit-learn, PyCharm
- **Data Processing:** Excel for initial data modeling

## Future Updates

- **Correlation Heatmap:** Plan to implement a correlation heatmap for deeper analysis of stock data relationships.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License.

## Contact

Farhan Rahman - [farhanrahman675@gmail.com](mailto:farhanrahman675@gmail.com)

---
