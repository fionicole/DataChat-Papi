# DataChat Papi – CSV Data Analysis Chatbot

## Project Description

DataChat Papi is a Python-based chatbot that allows users to explore and analyze CSV datasets through natural-language questions. The project combines keyword recognition, Pandas data analysis functions, and Matplotlib visualizations to make basic data exploration more accessible without requiring users to write Python code.

The current implementation uses the UCI Wine Quality datasets, which include red and white wine samples and their physicochemical properties.

## Features

- Load and analyze red and white wine CSV datasets.
- Calculate descriptive statistics, including averages, minimums, and maximums.
- Examine correlations and linear regression between alcohol content and wine quality.
- Classify wine samples into high-quality (score ≥ 7) and lower-quality (score < 7) categories.
- Generate visualizations using Matplotlib.
- Ask supported questions through a rule-based chatbot.
- Switch between red and white wine datasets.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

## Project Structure

```text
DataChat/
│
├── main.py
├── papi.py
├── analysis.py
├── charts.py
├── winequality-red.csv
├── winequality-white.csv
├── winequality.names 
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/fionicole/DataChat-Papi.git
```

2. Navigate to the project directory:

```bash
cd DataChat-Papi
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

4. Install the required libraries:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the following command from the project directory:

```bash
python main.py
```

The chatbot will start in the terminal and allow users to ask supported questions about the wine datasets.

## Dataset Source

The project uses the Wine Quality dataset from the UCI Machine Learning Repository.

Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Modeling wine preferences by data mining from physicochemical properties. *Decision Support Systems, 47*(4), 547–553.

https://doi.org/10.1016/j.dss.2009.05.016

## Current Limitations

DataChat uses a rule-based keyword recognition system and does not integrate an external AI service or large language model. Therefore, it recognizes supported question patterns rather than interpreting every possible natural-language question. The current analysis focuses primarily on alcohol content and wine quality.