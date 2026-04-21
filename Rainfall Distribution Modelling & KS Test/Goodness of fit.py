import pandas as pd
import numpy as np
from scipy.stats import gamma, lognorm, kstest

def fit_and_test_distributions(file_path):
    data = pd.read_csv(file_path)
    rain = data["precipitationCal"]
    rain = rain[rain > 0.1]

    shape_g, loc_g, scale_g = gamma.fit(rain, floc=0)
    shape_ln, loc_ln, scale_ln = lognorm.fit(rain, floc=0)

    ks_gamma = kstest(rain, 'gamma', args=(shape_g, loc_g, scale_g))
    ks_lognorm = kstest(rain, 'lognorm', args=(shape_ln, loc_ln, scale_ln))

    return {
        "gamma_params": (shape_g, scale_g),
        "lognormal_params": (shape_ln, scale_ln),
        "gamma_ks": (ks_gamma.statistic, ks_gamma.pvalue),
        "lognormal_ks": (ks_lognorm.statistic, ks_lognorm.pvalue)
    }


if __name__ == "__main__":
    results = fit_and_test_distributions("ktest2.csv")
    print(results)