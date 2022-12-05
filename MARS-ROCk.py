import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

identifier = sys.argv[1]
dirname = os.path.dirname(__file__)
models = {}
for i in range(2, len(sys.argv)):
    df = pd.read_csv(os.path.join(dirname, sys.argv[i]))
    models[os.path.splitext(os.path.basename(sys.argv[i]))[0]] = {}
    models[os.path.splitext(os.path.basename(sys.argv[i]))[0]]["df"] = df

thresholds = [round(i, 2) for i in np.flip(
    np.arange(start=0.0, stop=1.05, step=0.05))]

for model in models.values():

    df = model["df"]
    truePositives = []

    for i in np.flip(np.arange(start=0.0, stop=1.05, step=0.05)):
        i = round(i, 2)
        truePositive = set()

        # Step 1: Create sets of true positives for each algorithm at each probability threshold
        for _, row in df.iterrows():
            if (row.probability >= i and row.actual_label == 1):
                truePositive.add(int(row.id))

        truePositives.append(truePositive)

    model["true_positives"] = truePositives


cummUniqueTPs = []
observations = []

for model1Name, model1Info in models.items():
    for model2Name, model2Info in models.items():
        if model1Name != model2Name:
            cummUniqueTP = []
            observation = []
            m1TruePositives = model1Info["true_positives"]
            m2TruePositives = model2Info["true_positives"]
            for k, _ in enumerate(m1TruePositives):
                truePositive1 = m1TruePositives[k]
                truePositive2 = m2TruePositives[k]

                # Step 2: Find the UNIQUE set of true positives for that algorithm
                uniqueTP = truePositive1.difference(truePositive2)

                cummUniqueTP.append(len(uniqueTP))
                observation.append(
                    ", ".join(map(str, list(uniqueTP))))

            model1Info["cumm_unique_tp"] = cummUniqueTP
            model1Info["observations"] = observation

result_df = {
    "prob_threshold": thresholds,
}

for modelName, modelInfo in models.items():
    result_df[f"cumm_unique_tp_{modelName}"] = modelInfo["cumm_unique_tp"]
    result_df[f"observations_{modelName}"] = modelInfo["observations"]


marsRockDf = pd.DataFrame(result_df)


for model in models:
    plt.plot(marsRockDf["prob_threshold"],
             marsRockDf[f"cumm_unique_tp_{model}"], marker="o", label=model)

plt.xlabel("Probability Threshold")
plt.ylabel("Cumulative Unique True Positives")
plt.title("Cumulative Unique True Positives Vs. Probability Threshold")
plt.legend()
plt.gca().invert_xaxis()

plt.savefig("MARS-ROCk-graph.png")

marsRockDf.to_csv("MARS-ROCk.csv", index=False)
sys.stdout.flush()
