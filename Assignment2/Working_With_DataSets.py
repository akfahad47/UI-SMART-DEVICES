from sklearn import datasets

# List all available datasets
print(dir(datasets))

# Load the iris dataset
iris = datasets.load_iris()

# Print the dataset features
print("Feature Names:", iris.feature_names)
print("File Name:", iris.filename)
print("Data (first 5 rows):\n", iris.data[:5])
print("Target:\n", iris.target)
print("Target Names:", iris.target_names)
