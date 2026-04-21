import os
import numpy as np
import pandas as pd

def lag1_correlation(main_folder):
    results = []

    for folder in sorted(os.listdir(main_folder)):
        folder_path = os.path.join(main_folder, folder)

        if os.path.isdir(folder_path) and folder.startswith("kcsv"):
            time_series = []

            for file in sorted(os.listdir(folder_path)):
                if file.endswith(".csv"):
                    try:
                        data = pd.read_csv(
                            os.path.join(folder_path, file),
                            usecols=["precipitationCal"],
                            on_bad_lines="skip",
                            engine="python"
                        ).values.flatten()

                        time_series.append(np.mean(data))
                    except Exception:
                        continue

            rain = np.array(time_series)

            if len(rain) < 100:
                continue

            corr = np.corrcoef(rain[:-1], rain[1:])[0, 1]

            results.append({
                "Year": folder,
                "Lag1_Correlation": corr
            })

    return pd.DataFrame(results)


if __name__ == "__main__":
    df = lag1_correlation("path_to_main_folder")
    df.to_csv("lag1_correlation_summary.csv", index=False)