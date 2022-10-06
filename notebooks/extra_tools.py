import pandas as pd
import numpy as np
from scipy.optimize import curve_fit


def get_dataframe(ds, out_vars=['life__taxon_id', 'life__ancestor_id', 'life__trait_elev', 'life__y', 'life__x']):
    """
    Method to extract variables from the output of adascape
    in xr.Dataset format and exported to pd.DataFrame.

    :param ds: xr.Dataset with results of a simulation using adascape
    :param out_vars: list with name of variables to export
    :return: pd.DataFrame with columns/variables as specified in out_vars
    """

    individuals_data = {}
    for i in range(ds.life__traits.shape[2]):
        individuals_data['life__' + str(ds.trait[i].values.astype(str))] = ds.life__traits[:, :, i]
    ds = ds.assign(individuals_data)
    out_ds = ds[out_vars]

    dtf = (
        out_ds
            .to_dataframe()
            .rename(columns=lambda name: name.replace('life__', ''))
            .reset_index()
            .dropna()
    )
    return dtf


def quad_func(x, a, b, c):
    """
    Second order polynomial to fit as function for non-linear regression
    see documentation scipy.optimize.curve_fit
    :param x: float,
              predictor
    :param a: float,
              unknown linear parameter
    :param b: float,
              unknown quadratic parameter
    :param c: float
              unknown parameter
    :return: float with result of the function for a given parameter values
    """
    return a * x + b * x ** 2 + c


def fit_nlsq(xdata, ydata, xmin, xmax, var_name):
    """
    Fit non-linear regression using scipy.optimize.curve_fit
    :param xdata: array-like
                  predictor data
    :param ydata: array-like
                  regressor data
    :param xmin: float
                 minimum value of x for the prediction
    :param xmax: float
                 maximum value of x for the prediction
    :param var_name: string
                     name of output predictor variable
    :return: pd.DataFrame with columns for the predictor variable and taxon richness
    """
    popt, pcov = curve_fit(quad_func, xdata, ydata)
    xfit = np.linspace(xmin, xmax, 1000)
    return pd.DataFrame({var_name: xfit, 'taxon_richness': quad_func(xfit, *popt)})
