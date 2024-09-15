"""
Main cli or app entry point
"""

from mylib.lib import *


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
        "name": col,
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
    describe_df = general_describe(dataset, columns=["age", "gender", "raceethnicity"])
    summary_table = describe_df.to_markdown()
    chart_created(content_df, False)
    # Write the markdown table to a file
    with open(
        "killngs_by_police_officers_summary.md", "a", encoding="ISO-8859-1"
    ) as file:
        file.write("Describe:\n")
        file.write(summary_table)
        file.write("\n\n")  # Add a new line
        file.write("![age_image_fail_load](killings_per_age.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![race_gender_image_fail_load](killings_by_gender.png)\n")


if __name__ == "__main__":
    save_to_markdown(dataset)
