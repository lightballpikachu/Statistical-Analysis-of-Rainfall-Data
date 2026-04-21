import os
import numpy as np
import pandas as pd

def conditional_rainfall(folder_path):
    rain_series = []

    for file in sorted(os.listdir(folder_path)):
        if file.endswith(".csv"):
            try:
                data = pd.read_csv(
                    os.path.join(folder_path, file),
                    usecols=["precipitationCal"],
                    on_bad_lines="skip",
                    engine="python"
                ).values.flatten()

                rain_series.append(np.mean(data))
            except Exception:
                continue

    rain = np.array(rain_series)

    threshold = np.percentile(rain, 90)

    heavy_next = []
    nonheavy_next = []

    for i in range(len(rain) - 1):
        if rain[i] > threshold:
            heavy_next.append(rain[i + 1])
        else:
            nonheavy_next.append(rain[i + 1])

    return {
        "Mean_After_Heavy": np.mean(heavy_next),
        "Mean_After_NonHeavy": np.mean(nonheavy_next)
    }


if __name__ == "__main__":
    results = conditional_rainfall("path_to_year_folder")
    print(results)