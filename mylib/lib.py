"""
    library file
"""

# Import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading the data
dataset = "dataset/police_killings.csv"


def load_dataset(dataset):
    """loads the dataset"""
    content_df = pd.read_csv(dataset, encoding="ISO-8859-1")
    # Clean the age column by removing unknown references
    content_df["age"] = pd.to_numeric(
        content_df["age"].replace("Unknown", pd.NA), errors="coerce"
    )
    return content_df


# Data Calculation
def grab_mean(content_df, col):
    """returns the mean of a column"""
    col_mean = content_df[col].mean()
    return col_mean


def grab_median(content_df, col):
    """returns the median of a column"""
    col_median = content_df[col].median()
    return col_median


def grab_std_deviation(content_df, col):
    """returns the standard deviation of a column"""
    col_std_deviation = content_df[col].std()
    return col_std_deviation


def grab_min(content_df, col):
    """returns the minimum value inside a column"""
    col_min = content_df[col].min()
    return col_min


def grab_max(content_df, col):
    """returns the maximum value inside a column"""
    col_max = content_df[col].max()
    return col_max


# Data Visualization: Distribution of police killings by age
def age_histogram(content_df, show_plot):

    # Create generational categories based on age
    bins = [0, 12, 28, 44, 60, 79, 100]  # Age gropu by generations
    labels = [
        "Gen Alpha",
        "Gen Z",
        "Millenials",
        "Gen X",
        "Baby Boomers",
        "Silent Generation",
    ]
    content_df["generation"] = pd.cut(
        content_df["age"], bins=bins, labels=labels, right=False
    )
    # Plot the count of killings per generation

    plt.figure(figsize=(10, 6))
    content_df["generation"].value_counts(sort=False).plot(
        kind="bar", edgecolor="black"
    )
    plt.title("Distribution of Police Killings by Generation")
    plt.xlabel("Generation")
    plt.ylabel("Number of People Killed")
    plt.grid(True)

    # Save the plot and dispaly it if a column is selected
    plt.savefig("killings_per_age.png")

    if show_plot:
        plt.show()


# Data Visualization: Distribution of police killings across gender and race
def gender_pie_chart(content_df, show_plot=True):
    gender_counts = content_df["gender"].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(
        gender_counts,
        labels=gender_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["blue", "pink"],
        wedgeprops={"edgecolor": "black"},
    )
    plt.title("Police Killings by Gender (in percent %)")
    plt.xlabel("Gender")
    plt.grid(True)

    # Save the plot and dispaly it if a column is selected
    plt.savefig("killings_by_gender.png")

    if show_plot:
        plt.show()
