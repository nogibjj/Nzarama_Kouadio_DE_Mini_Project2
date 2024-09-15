"""
Main cli or app entry point
"""

import pandas as pd
from mylib.lib import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_std_deviation,
    grab_min,
    grab_max,
    age_histogram,
    gender_pie_chart,
)

# Loading the data
dataset = "dataset/police_killings.csv"


def general_describe(dataset, columns=None):
    content_df = load_dataset(dataset)
    # Clean the age column by removing unknown references
    content_df["age"] = pd.to_numeric(
        content_df["age"].replace("Unknown", pd.NA), errors="coerce"
    )
    # If columns are specified, select only those columns
    if columns:
        content_df = content_df[columns]
    return content_df.describe()


def custom_describe(dataset, col):
    content_df = load_dataset(dataset)
    descriptive_dict = {
        "category": col,
        "mean": grab_mean(content_df, col),
        "median": grab_median(content_df, col),
        "std": grab_std_deviation(content_df, col),
        "min": grab_min(content_df, col),
        "max": grab_max(content_df, col),
    }
    return descriptive_dict


def chart_created(content_df, show_plot=False):
    """Gather all charts"""
    age_histogram(content_df, show_plot)
    gender_pie_chart(content_df, show_plot)


def save_to_markdown(dataset):
    """save summary report to markdown"""
    content_df = load_dataset(dataset)
    # Generate individual column statistics
    age_stats = custom_describe(dataset, "age")
    gender_distribution = content_df["gender"].value_counts()
    chart_created(content_df, False)
    # Write the markdown table to a file
    with open(
        "killngs_by_police_officers_summary.md", "a", encoding="ISO-8859-1"
    ) as file:
        # Write header
        file.write("# Police Killings Summary Report:\n\n")

        # Write summary statitics for age
        file.write("# Summary statistics of age of people killed by police\n")
        for key, value in age_stats.items():
            file.write(f"{key.capitalize()}: {value}\n")
        file.write("\n\n")  # Add a new line

        # Write summary statitics for age
        file.write("# Gender Distribution of People Killed by Police:\n")
        file.write(gender_distribution.to_markdown())
        file.write("\n\n")

        # Include charts
        file.write("![age_image_fail_load](killings_per_age.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![gender_image_fail_load](killings_by_gender.png)\n")


if __name__ == "__main__":
    save_to_markdown(dataset)
