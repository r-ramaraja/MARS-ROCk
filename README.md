# MARS-charts

Implementation of MARS charts and MARS metrics for evaluating classifier exclusivity: the comparative uniqueness of binary classifier predictions.

## Requirements

Python 3.9.12
Pandas 1.5.1
Matplotlib 3.6.2
Numpy 1.23.4

## Dataset

Performed classification on breast cancer dataset from scikit learn using Logistic Regression and k-NN. 

## License

Distributed under the MIT License.

## Input

The input to the software application is a set of comma-separated value(.csv) files. Since we are doing a comparative model analysis, the minimum number of files to be uploaded is two, and the maximum is five. Each file would contain the following columns:

- id: Unique identifier assigned to each observation/instance in dataset
- actual_label: Refers to the observation’s (instance’s) actual class value (formatted as 0 or 1)
- probability: The probability of the predicted class value(between 0 and 1)

Also, the number of observations per file should be limited to one thousand. If the number of observations exceeds one thousand, the user must take a sample for the comparative analysis. The output would be a .png file of the MARS ROCk graph and a .csv file with the MARS ROCk points and the list of instance ids of the respective model’s unique true positives at the given probability threshold.

## Web application

<https://mars-rock.onrender.com>
An easy-to-use web interface where the user can upload their datasets and generate the MARS ROCk chart.

## CLI Application

```python MARS-ROCk.py <path_to_dataset1> <path_to_dataset2> ...```
Eg. ```python MARS-ROCk.py knn_safety_concerns.csv logReg_safety_concerns.csv```

The input to the CLI command is a set of absolute file paths to the .csv file of the model results. The file's name would be used as the legend in the graph provided as the output. The output would be the generation and saving of the .png file of the MARS ROCk graph and a .csv file with the MARS ROCk points.

## Function

```def MARSROCk(classifier_ results)```

The function can be found in the `MARS-ROCk.ipynb` file.
The input to the function is a dictionary, where the key is the model's name and the value is the absolute path to the file. The key would be used as a legend in the graph that’s provided as the output. The output would be the generation and saving of the .png file of the MARS ROCk graph and a .csv file with the MARS ROCk points.
