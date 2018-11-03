import pandas as pd
import matplotlib as plt

original_dataset = "dataset/credit_default_train.csv"

df = pd.read_csv(original_dataset)

'''Data Understanding: provides general information about the data: existence of missing values,
    the existence of outliers, the character of attributes, dependencies between attributes'''


def get_graphs(dataframe):

    # TODO: see https://stackoverflow.com/questions/40783669/stacked-bar-plot-by-group-count-on-pandas-python
    fig = plt.figure(figsize=(10, 10))
    fig_dims = (3, 2)

    # Histogram: Limit
    plt.subplot2grid(fig_dims, (0, 0))
    df["limit"].hist()
    plt.title("Limit Histogram")
    plt.show()

    # Gender counts
    df["sex"].value_counts().plot(kind="bar", title="Gender Counts")
    plt.show()

    # For stacked barplor: obtain count of possible att values
    n_male = int(df[df["sex"] == "male"]["sex"].value_counts())
    n_female = int(df[df["sex"] == "female"]["sex"].value_counts())


def data_understanding(dataframe):
    print(dataframe.info())
    null_elem = pd.isnull(dataframe).sum()
    graphs = get_graphs(dataframe)
