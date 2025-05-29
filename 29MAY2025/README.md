# TOPICS [29TH MAY 2025] - [Theoretical Only]:

- Confusion Matrix
- Evaluation Metrices:
  - Accuracy.
  - Precision.
  - Recall.
  - F1-Score.
  - ROC Curve
- Bias, Variance and Bias-Variance trade off.
- Feature Engineering.

## TASKS:

- To clear all the Theoretical (Mathematical) Concepts mentioned above...

---

# Notes:

## 1. Confusion Matrix:

- `N x N` matrix where `N` is number of predicted classes.

- `TP (True Positive)`: Model predicted correctly a positive outcome (actual outcome was positive)

- `TN (True Negative)`: Model predicted correctly a negative outcome (actual outcome was negative)

- `FP (False Positive)`: Model INCORRECTLY predicted a positive outcome. (actual outcome was negative) - **TYPE-I ERROR**

- `FN (False Negative)`: Model INCORRECTLY predicted a negative outcome. (actual outcome was positive) - **TYPE-II ERROR**

- Confusion Matrix is used to calculate the measures like accuracy, precision, recall, F1-score, and many more...

## 2. Evaluation Metrices:

- Model performance and effectiveness quantitative measures.

### 2.1. Accuracy:

- This is overall measure of the model (how many predictions are correct)

- `Accuracy = (TP + TN) / (TP + TN + FP + FN)`

### 2.2. Precision:

- Precision focuses on the quality of model's positive predictions.
- how many positive predictions were actually correct.
- eg. spam detection / fraud detection / etc...

- `Precision = TP / (TP + FP)`

### 2.3 Recall:

- Proportion of True Positives detected out of all the actual positive instances.
- How good the model is at predicting positives (i.e. one class)
- `Recall = TP / (TP + FN)`

### 2.4 F1-Score:

- Combination of precision and recall into single metric to balance their trade-off.
- Overall performance [particularly for imbalance data].
- Helpful when FP and FN both are important.

- `F1-Score = (2 * Precision * Recall) / (Precision + Recall)`

## 2.5 ROC Curve:

- AUC (Area Under the Curve)
- ROC (Receiver Operating Characteristic Curve)

- It's graph representing the trade-off between TPR (True Positive Rate / Recall / Sensitivity) and FPR (False Positive Rate)

- TPR = (TP / (TP+FN))

- FPR = (FP / (TN+FP)) = 1 - specificity = 1 - (TN / (TN+FP))

  - AUC: range(0,1)
  - AUC = 1 (perfect model)
  - AUC = 0.5 (random guessing)
  - AUC = <0.5 (worst / confused model)

- src: [analyticsvidhya.com](https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/)

## 3. Bias, Variance and Bias-Variance trade off:

- These (Bias & Variance trade-off)'s main aim is to balance the underfitting & overfitting.

### 3.1 Bias:

- inability of model to predict the values correctly...
- High Bias leads to underfitting. [more assumptions are taken to build the target function]
- Low Bias means lower assumptions taken...

### 3.2 Variance:

- Measure of spread of data from mean position. (model being too sensitive to small fluctuations in the training data.)

- High variance leads to learn noise (OVERFITTING)

### 3.3 Bias-Variance Trade-off [Regularization]:

- Ideal model state: [low bias, low variance]

- Here we try to reduce bias and variance both by performing trade-off between them.

- We visualize them via Error v/s Model Complexity.

- This method is known as Regularization. which include many methods like:
  - L1 Regularization (Lasso)
  - L2 Regularization (Ridge)
  - Elastic Net (L1 + L2)
  - Dropout Layers (for NNs)
  - Early Stopping

## 4. Feature Engineering:

- Transforming Raw-Data into Meaningful data...
- This includes handling missing values, encoding variables, scaling, and creating interaction terms.
- It is performed to improve overall model performance

### 4.1 Handling Missing Values:

- For this one thing we can do is to delete the columns by setting up the thresholds like 70-80% depending upon use-case.

- Or Impute the missing values for continous variables by using various imputation methods (few already learned previously).

- Dropping the rows containing the missing categorical values or assigning a new category to the missing categorical values.

### 4.2 Encoding the Categorical Data.

- Basically we perform different encodings here like one-hot encoding or Label Encoding.

### 4.3 Last Step of Feature Engineering [Feature Scaling]:

- Min-Max Scaling [0,1]
- Normalization [-1,1]
- Standardization

## Extra [BrainStorming]:

## Large Number of Outliers Handling Methods:

- Transformations (reduce the impact of extreme values).

  - Log(x) - log trans.
  - sqrt(x) - power trans.
  - Box-Cox - Trans. (auto. find the best trans. method)

- Using Scaling method less sensitive to outliers. [e.g. Robust Scaler incase of LR/SVM]

- Using Less Sensitive to outlier models.

- Clustering Based Smoothing.
