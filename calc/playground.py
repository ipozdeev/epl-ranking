import pandas as pd

from core import get_first_eigenvector, get_epl_data


def sandbox():
    """
    """
    data = get_epl_data(1920)
    data_mx = data.unstack(level="AwayTeam").fillna(value=0.0) \
        .sort_index(axis=0).sort_index(axis=1)
    eig = get_first_eigenvector(data_mx)
    rnk = eig.sort_values(ascending=False)

    print(rnk)


if __name__ == '__main__':
    sandbox()
