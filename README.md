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

## Web application

https://mars-rock.herokuapp.com
An easy-to-use web interface where the user can upload their datasets and generate the MARS ROCk chart.

## CLI Application

```python MARS-ROCk.py <path_to_dataset1> <path_to_dataset2> ...```
Eg. ```python MARS-ROCk.py knn_predicted_cancer.csv logReg_predicted_cancer.csv```
