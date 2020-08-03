import pandas as pd
import numpy as np


def get_epl_data(season=1920) -> pd.Series:
    """Download EPL season results data."""
    url = "https://www.football-data.co.uk/mmz4281/{}/E0.csv".format(season)
    data = pd.read_csv(url, converters={"Date": pd.to_datetime})

    data = data[["HomeTeam", "AwayTeam", "FTR", "Date"]]

    data.loc[:, "ph"] = data["FTR"].map({"H": 3, "A": 0, "D": 1})
    data.loc[:, "pa"] = data["FTR"].map({"A": 3, "H": 0, "D": 1})

    data = data.set_index(["HomeTeam", "AwayTeam"])
    res = data["ph"] + \
        data["pa"].swaplevel().rename_axis(["HomeTeam", "AwayTeam"])

    return res


if __name__ == '__main__':
    print(get_epl_data(1920))
