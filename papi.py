
import pandas as pd

from analysis import (
    average_alcohol,
    maximum_alcohol,
    minimum_alcohol,
    alcohol_quality_correlation,
    average_alcohol_high_quality,
    count_high_quality,
    count_lower_quality,
    average_quality,
    alcohol_quality_regression,
    alcohol_quality_r_squared,
    median_alcohol
)

from charts import (
    plot_average_quality,
    plot_average_alcohol,
    plot_alcohol_distribution,
    plot_alcohol_quality_relationship,
    plot_alcohol_boxplot,
    plot_quality_counts
)


# Load datasets
red_wine = pd.read_csv("winequality-red.csv", sep=";")
white_wine = pd.read_csv("winequality-white.csv", sep=";")


# Process user questions
def answer_question(question, dataset):

    question = question.lower()

    # GRAPH REQUESTS
    if any(word in question for word in [
        "chart", "graph", "plot", "visualization",
        "histogram", "distribution", "boxplot", "box plot"
    ]):

        if "distribution" in question or "histogram" in question:
            plot_alcohol_distribution(red_wine, white_wine)
            return "Here is the alcohol distribution chart."

        elif "boxplot" in question or "box plot" in question:
            plot_alcohol_boxplot(red_wine, white_wine)
            return "Here is the alcohol box plot."

        elif "count" in question:
            plot_quality_counts(red_wine, white_wine)
            return "Here is the wine quality count chart."

        elif "relationship" in question or "regression" in question or "correlation" in question:
            plot_alcohol_quality_relationship(red_wine, white_wine)
            return "Here is the alcohol and quality regression graph."

        elif "alcohol" in question and "quality" not in question:
            plot_average_alcohol(red_wine, white_wine)
            return "Here is the average alcohol chart."

        elif "quality" in question:
            plot_average_quality(red_wine, white_wine)
            return "Here is the average quality chart."

        return "Please specify which graph you would like to see."

    # NUMERICAL ANALYSIS REQUESTS

    elif "regression equation" in question or "regression model" in question:
        slope, intercept = alcohol_quality_regression(dataset)

        return (
            f"The regression equation is: "
            f"Predicted quality = {intercept} + {slope} * Alcohol."
        )

    elif "r-squared" in question or "r squared" in question or "r2" in question:
        result = alcohol_quality_r_squared(dataset)
        return f"The R-squared value is {result}."

    elif any(word in question for word in ["correlation", "relationship", "related"]):
        result = alcohol_quality_correlation(dataset)
        return f"The correlation between alcohol and quality is {result}."

    elif "median" in question and "alcohol" in question:
        return f"The median alcohol content is {median_alcohol(dataset)}%."

    elif any(word in question for word in ["average", "mean"]) and "alcohol" in question and (
        "high quality" in question or "quality 7" in question
    ):
        return (
            f"The average alcohol content for high-quality wines "
            f"is {average_alcohol_high_quality(dataset)}%."
        )

    elif any(word in question for word in ["average", "mean"]) and "alcohol" in question:
        return f"The average alcohol content is {average_alcohol(dataset)}%."

    elif any(word in question for word in ["highest", "maximum", "max"]) and "alcohol" in question:
        return f"The highest alcohol content is {maximum_alcohol(dataset)}%."

    elif any(word in question for word in ["lowest", "minimum", "min"]) and "alcohol" in question:
        return f"The lowest alcohol content is {minimum_alcohol(dataset)}%."

    elif any(word in question for word in ["average", "mean"]) and "quality" in question:
        return f"The average wine quality is {average_quality(dataset)}."

    elif any(word in question for word in ["count", "how many"]) and (
        "high quality" in question or "quality 7" in question
    ):
        return f"There are {count_high_quality(dataset)} high-quality wines."

    elif any(word in question for word in ["count", "how many"]) and (
        "low quality" in question or "lower quality" in question
    ):
        return f"There are {count_lower_quality(dataset)} lower-quality wines."

    else:
        return (
            "Sorry, I did not understand that question. "
            "Try asking about alcohol, quality, correlation, regression, or a graph."
        )


# Start interactive chatbot
def start_chatbot():

    dataset = red_wine
    current_wine = "Red"

    print("\n=== Welcome to Papi: DataChat ===")
    print("Ask questions about wine quality and alcohol.")
    print("Type 'exit' to finish.")
    print(f"Current dataset: {current_wine} wine")

    while True:

        question = input("\nYou: ").lower()

        if question == "exit":
            print("Papi: Thank you for using DataChat!")
            break

        elif "switch to white" in question:
            dataset = white_wine
            current_wine = "White"
            print("Papi: Switched to white wine dataset.")
            continue

        elif "switch to red" in question:
            dataset = red_wine
            current_wine = "Red"
            print("Papi: Switched to red wine dataset.")
            continue

        # Allow users to select a dataset by mentioning its type
        if "white wine" in question:
            dataset = white_wine
            current_wine = "White"

        elif "red wine" in question:
            dataset = red_wine
            current_wine = "Red"

        answer = answer_question(question, dataset)

        print(f"Papi: {answer}")


