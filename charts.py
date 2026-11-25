
import matplotlib.pyplot as plt

# 1. Bar chart: Compare average wine quality
def plot_average_quality(red_wine, white_wine):
    averages = [
        red_wine["quality"].mean(),
        white_wine["quality"].mean()
    ]

    wine_types = ["Red wine", "White wine"]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(wine_types, averages, width=0.5)

    ax.set_title("Average Wine Quality: Red vs. White")
    ax.set_ylabel("Average Quality Score")
    ax.set_ylim(0, 10)
    ax.bar_label(bars, fmt="%.2f", padding=4)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.show()


# 2. Bar chart: Compare average alcohol content
def plot_average_alcohol(red_wine, white_wine):
    averages = [
        red_wine["alcohol"].mean(),
        white_wine["alcohol"].mean()
    ]

    wine_types = ["Red wine", "White wine"]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(wine_types, averages, width=0.5)

    ax.set_title("Average Alcohol Content: Red vs. White")
    ax.set_ylabel("Alcohol Content (%)")
    ax.bar_label(bars, fmt="%.2f", padding=4)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.show()


# 3. Histogram: Show alcohol content distribution
def plot_alcohol_distribution(red_wine, white_wine):
    import numpy as np

    # Create the same 15 intervals for both datasets
    bins = np.linspace(
        min(red_wine["alcohol"].min(), white_wine["alcohol"].min()),
        max(red_wine["alcohol"].max(), white_wine["alcohol"].max()),
        16
    )

    plt.figure(figsize=(8, 5))

    plt.hist(
        red_wine["alcohol"],
        bins=bins,
        alpha=0.5,
        label="Red wine",
        color="blue",
        edgecolor="black"
    )

    plt.hist(
        white_wine["alcohol"],
        bins=bins,
        alpha=0.5,
        label="White wine",
        color="orange",
        edgecolor="black"
    )

    plt.title("Distribution of Alcohol Content")
    plt.xlabel("Alcohol Content (%)")
    plt.ylabel("Number of Wines")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()

# 4. Scatter plot with linear regression
def plot_alcohol_quality_relationship(red_wine, white_wine):
    import numpy as np
    import matplotlib.pyplot as plt

    plt.figure(figsize=(9, 6))

    # Red wine data
    red_x = red_wine["alcohol"]
    red_y = red_wine["quality"]

    # White wine data
    white_x = white_wine["alcohol"]
    white_y = white_wine["quality"]

    # Calculate regression lines
    red_slope, red_intercept = np.polyfit(red_x, red_y, 1)
    white_slope, white_intercept = np.polyfit(white_x, white_y, 1)

    # Calculate correlation
    red_r = red_x.corr(red_y)
    white_r = white_x.corr(white_y)

    # Calculate R-squared
    red_r_squared = red_r ** 2
    white_r_squared = white_r ** 2

    # Scatter points
    plt.scatter(red_x, red_y, alpha=0.25, label="Red wine")
    plt.scatter(white_x, white_y, alpha=0.25, label="White wine")

    # Regression lines
    red_line_x = np.linspace(red_x.min(), red_x.max(), 100)
    white_line_x = np.linspace(white_x.min(), white_x.max(), 100)

    plt.plot(
        red_line_x,
        red_slope * red_line_x + red_intercept,
        label="Red regression line"
    )

    plt.plot(
        white_line_x,
        white_slope * white_line_x + white_intercept,
        label="White regression line"
    )

    # Display equations and statistics
    red_equation = (
        f"Red: y = {red_slope:.3f}x + {red_intercept:.3f}\n"
        f"r = {red_r:.3f}, R² = {red_r_squared:.3f}"
    )

    white_equation = (
        f"White: y = {white_slope:.3f}x + {white_intercept:.3f}\n"
        f"r = {white_r:.3f}, R² = {white_r_squared:.3f}"
    )

    plt.text(
        0.02, 0.97, red_equation,
        transform=plt.gca().transAxes,
        verticalalignment="top"
    )

    plt.text(
        0.02, 0.85, white_equation,
        transform=plt.gca().transAxes,
        verticalalignment="top"
    )

    plt.title("Alcohol Content vs. Wine Quality")
    plt.xlabel("Alcohol Content (%)")
    plt.ylabel("Wine Quality Score")
    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()


# 5. Box plot: Compare alcohol content distributions
def plot_alcohol_boxplot(red_wine, white_wine):
    plt.figure(figsize=(8, 5))

    plt.boxplot(
        [
            red_wine["alcohol"],
            white_wine["alcohol"]
        ],
        tick_labels=["Red wine", "White wine"]
    )

    plt.title("Alcohol Content Distribution: Red vs. White")
    plt.ylabel("Alcohol Content (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()


# 6. Bar chart: Count wines by quality score
def plot_quality_counts(red_wine, white_wine):
    red_counts = red_wine["quality"].value_counts().sort_index()
    white_counts = white_wine["quality"].value_counts().sort_index()

    quality_scores = sorted(
        set(red_counts.index).union(set(white_counts.index))
    )

    red_values = red_counts.reindex(quality_scores, fill_value=0)
    white_values = white_counts.reindex(quality_scores, fill_value=0)

    x = range(len(quality_scores))
    width = 0.4

    plt.figure(figsize=(9, 5))

    plt.bar(
        [i - width / 2 for i in x],
        red_values,
        width,
        label="Red wine"
    )

    plt.bar(
        [i + width / 2 for i in x],
        white_values,
        width,
        label="White wine"
    )

    plt.title("Number of Wines by Quality Score")
    plt.xlabel("Quality Score")
    plt.ylabel("Number of Wines")
    plt.xticks(list(x), quality_scores)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()
