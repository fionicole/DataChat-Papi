
# Function to calculate average alcohol content
def average_alcohol(dataset):
    average = dataset["alcohol"].mean()
    return round(average, 2)


# Function to find the maximum alcohol content
def maximum_alcohol(dataset):
    maximum = dataset["alcohol"].max()
    return round(maximum, 2)


# Function to find the minimum alcohol content
def minimum_alcohol(dataset):
    minimum = dataset["alcohol"].min()
    return round(minimum, 2)


# Function to calculate correlation
def alcohol_quality_correlation(dataset):
    correlation = dataset["alcohol"].corr(dataset["quality"])
    return round(correlation, 2)


# Function to calculate average alcohol for quality 7 or higher
def average_alcohol_high_quality(dataset):
    high_quality = dataset[dataset["quality"] >= 7]
    average = high_quality["alcohol"].mean()
    return round(average, 2)


# Function to count wines with quality 7 or higher
def count_high_quality(dataset):
    count = (dataset["quality"] >= 7).sum()
    return int(count)


# Function to count wines with quality under 7
def count_lower_quality(dataset):
    count = (dataset["quality"] < 7).sum()
    return int(count)


# Function to calculate average quality
def average_quality(dataset):
    average = dataset["quality"].mean()
    return round(average, 2)


# Function to calculate the regression equation
def alcohol_quality_regression(dataset):
    import numpy as np

    slope, intercept = np.polyfit(
        dataset["alcohol"],
        dataset["quality"],
        1
    )

    return round(slope, 4), round(intercept, 4)


# Function to calculate R-squared
def alcohol_quality_r_squared(dataset):
    correlation = dataset["alcohol"].corr(dataset["quality"])
    return round(correlation ** 2, 4)


# Function to calculate median alcohol content
def median_alcohol(dataset):
    median = dataset["alcohol"].median()
    return round(median, 2)

