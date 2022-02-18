import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Any, Callable, TypeVar

T = TypeVar('T')

def find_index(cond: Callable[[T], bool], el_list: list[T]):
    """Проверяет наличие элемента в списке, который соответствует условию в переданной функции. При отсутствии элемента возвращает -1

    Args:
        cond (Callable[[T], bool]): Условие, которому должен удовлетворять искомый элемент
        el_list (list[T]): Список элементов

    Returns:
        int: Индекс искомого элемента, -1 при его отсутствии в списке
    """

    for i, el in enumerate(el_list):
        if cond(el):
            return i

    return -1

def create_axes(size=(10, 5)):
    fig = plt.figure(figsize=size, facecolor='white')
    axes = fig.add_axes([0, 0, 1, 1])

    return axes

def outliers_z_score(data: pd.DataFrame, feature: str, left=3, right=3, log_scale=False):
    x = np.log(data[feature]) if log_scale else data[feature]

    mu = x.mean()
    sigma = x.std()

    return data[(x < mu - sigma * left) | (x > mu + sigma * right)]

def write_plotly_html(fn: Callable[[pd.DataFrame], Any]):
    def write_html_wrapper(data: pd.DataFrame):
        plot = fn(data)
        plot.write_html(f'plotly/{fn.__name__}.html')

        return plot

    return write_html_wrapper