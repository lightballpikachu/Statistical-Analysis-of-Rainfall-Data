import os
import numpy as np
import pandas as pd

def interarrival_analysis(folder_path):
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
    binary = (rain > threshold).astype(int)

    extreme_indices = np.where(binary == 1)[0]

    if len(extreme_indices) < 2:
        return None

    tau = np.diff(extreme_indices)

    return {
        "Mean_Gap": np.mean(tau),
        "Min_Gap": np.min(tau),
        "Max_Gap": np.max(tau),
        "Num_Intervals": len(tau)
    }


if __name__ == "__main__":
    results = interarrival_analysis("path_to_year_folder")
    print(results)