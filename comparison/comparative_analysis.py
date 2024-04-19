from sklearn.metrics import accuracy_score

# Compare VoteFlow with baseline solutions
baseline_predictions = baseline_model.predict(X_test)
voteflow_predictions = voteflow_model.predict(X_test)

# Calculate accuracy
baseline_accuracy = accuracy_score(y_test, baseline_predictions)
voteflow_accuracy = accuracy_score(y_test, voteflow_predictions)

print("Baseline Model Accuracy:", baseline_accuracy)
print("VoteFlow Model Accuracy:", voteflow_accuracy)
