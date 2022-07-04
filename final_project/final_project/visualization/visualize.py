#Se deben definir los imports necesarios:

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Pandas es necesario, en este caso, para destacar que el objeto que necesita la función covid_time_series es un dataframe.

def covid_time_series(df):
    print("I can modify anything in the function because of the lines: %load_ext autoreload and %autoreload 2")
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");





def covid_countries_incidences(df_2, countries, processed_covid_df):
    df_2 = (
        processed_covid_df
        .select_columns(["country_region", "value"])
        .groupby(["country_region"])
        .aggregate("sum")
        .sort_values("value", ascending=False)
        .reset_index()
        .head(20)
        .transform_column(
            column_name="country_region",
            function=lambda x: "red" if x in countries else "lightblue",
            dest_column_name="color"
        )
    )

    sns.barplot(
        data=df_2,
        x="value",
        y="country_region",
        palette=df_2.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");