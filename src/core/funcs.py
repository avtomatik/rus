#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 11:47:51 2023

@author: green-machine
"""

import matplotlib.pyplot as plt
import pandas as pd

from core.classes import Token
from core.constants import MAP_KWARGS


def read(token: Token) -> pd.DataFrame:
    """
    Read Selected Files.

    Parameters
    ----------
    token : Token
        kwargs Token.

    Returns
    -------
    pd.DataFrame
        DESCRIPTION.

    """
    return pd.read_csv(**MAP_KWARGS.get(token))


def pull_by_series_id(df: pd.DataFrame, series_id: str) -> pd.DataFrame:
    """


    Parameters
    ----------
    df : pd.DataFrame
        ================== =================================
        df.index           Period
        df.iloc[:, 0]      Series IDs
        df.iloc[:, 1]      Values
        ================== =================================
    series_id : str

    Returns
    -------
    pd.DataFrame
        ================== =================================
        df.index           Period
        df.iloc[:, 0]      Series
        ================== =================================
    """
    assert df.shape[1] == 2
    return df[df.iloc[:, 0] == series_id].iloc[:, [1]].rename(
        columns={"value": series_id}
    )


def plot_rus_grigoriev(df: pd.DataFrame) -> None:
    for series_id in sorted(set(df.loc[:, 'series'])):
        df.pipe(pull_by_series_id, series_id).plot(grid=True)


def plot_rus_is_lm(df: pd.DataFrame) -> None:
    """
    Plotting.

    Parameters
    ----------
    df : pd.DataFrame
        DESCRIPTION.
    Returns
    -------
    None
        DESCRIPTION.
    """
    plt.figure()
    plt.plot(df.iloc[:, 0], df.iloc[:, 1])
    plt.xlabel('Percentage')
    plt.ylabel('RUB, Millions')
    plt.title('M1 Dependency on Prime Rate')
    plt.grid()
    plt.show()
