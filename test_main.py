"""
Test goes here

"""

from main import general_describe, custom_describe, save_to_markdown

test_dataset = "dataset/police_killings.csv"


def testing_describe():
    """test .describe with custom describe function"""
    describe_test = general_describe(test_dataset)
    custom_test = custom_describe(test_dataset, "age")
    assert describe_test.loc["mean", "age"] == custom_test["mean"]
    assert describe_test.loc["std", "age"] == custom_test["std"]
    assert describe_test.loc["min", "age"] == custom_test["min"]


def testing_charts():
    """converts to markdown()"""
    save_to_markdown(test_dataset)


if __name__ == "__main__":
    testing_describe()
    testing_charts()
