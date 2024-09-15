"""
We test here

"""

from mylib.lib import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_std_deviation,
    grab_min,
    grab_max,
)

test_dataset = "dataset/police_killings.csv"


def testing_summary_statistics():
    """testing if statistics are properly being calculated"""
    content_df = load_dataset(test_dataset)
    testing_mean = grab_mean(content_df, "day")
    testing_median = grab_median(content_df, "day")
    testing_std_deviation = grab_std_deviation(content_df, "day")
    testing_min = grab_min(content_df, "day")
    testing_max = grab_max(content_df, "day")
    describe_test = content_df.describe()
    assert describe_test.loc["mean", "day"] == testing_mean
    assert describe_test.loc["50%", "day"] == testing_median
    assert describe_test.loc["std", "day"] == testing_std_deviation
    assert describe_test.loc["min", "day"] == testing_min
    assert describe_test.loc["max", "day"] == testing_max


if __name__ == "__main__":
    testing_summary_statistics()
