import pandas as pd
import numpy as np

def estimate_distribution_parameters(file_path):
    df = pd.read_csv(file_path)

    sigma2_ln = np.log(1 + df["Variance"] / (df["Mean"] ** 2))
    df["mu_lognormal"] = np.log(df["Mean"]) - 0.5 * sigma2_ln
    df["sigma_lognormal"] = np.sqrt(sigma2_ln)

    df["gamma_k"] = (df["Mean"] ** 2) / df["Variance"]
    df["gamma_theta"] = df["Variance"] / df["Mean"]

    return df


if __name__ == "__main__":
    estimate_distribution_parameters(
        "rainfall_statistics_summary.csv"
    ).to_csv("rainfall_with_distribution_parameters.csv", index=False)