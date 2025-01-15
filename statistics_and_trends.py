"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and make this a fully working, documented file.
You should NOT change any function or variable names, if they are given to you here.
Make use of the functions presented in the lectures and ensure your code is PEP-8 compliant, including docstrings.
"""
from typing import Tuple

from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis
import seaborn as sns


def plot_relational_plot(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots()
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots()
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots()
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df: pd.DataFrame) -> Tuple[float, float, float, float]:
    mean = np.mean(df[''])
    stddev = np.std(df[''])
    skewness = skew(df[''])
    excess_kurtosis = kurtosis(df[''])
    return mean, stddev, skewness, excess_kurtosis


def preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    return df


def main():
    df = pd.read_csv('data.csv')
    return


if __name__ == '__main__':
    main()
