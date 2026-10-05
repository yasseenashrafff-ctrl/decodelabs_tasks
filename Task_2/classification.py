from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# 1. Load the dataset
iris = load_iris()

X = iris.data
y = iris.target

print("Dataset loaded successfully!")
print("Number of samples:", len(X))
print("Number of features:", X.shape[1])


# 2. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# 3. Create the classification model
model = DecisionTreeClassifier(random_state=42)


# 4. Train the model
model.fit(X_train, y_train)


# 5. Make predictions
predictions = model.predict(X_test)


# 6. Evaluate the model
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")


# 7. Test the model with a new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_flower)

print("Predicted flower:", iris.target_names[prediction[0]])
