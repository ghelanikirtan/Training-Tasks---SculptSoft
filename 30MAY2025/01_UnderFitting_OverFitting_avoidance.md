## To Tackle UnderFitting and OverFitting Problem [Regularization]:

- We use Regularization Methods to tackle such problems.

1. Lasso Regression (L1):

- Least Absolute Shrinkage and Selection (abs value of magnitude - penalty)
- `sklearn.linear_model.Lasso`
- we fit splitted data here...

2. Ridge Regression (L2):

- Squared magnitude of coeff. (penalty)
- `sklearn.linear_model.Ridge`

3. Elastic Net Regression.

- combination of L1 and L2.
- `sklearn.linear_model.ElasticNet`

4. Dropout Layers

5. Early Stopping.

### More methods:

Overfitting Tackle:

- Use shallow models...
- Use less and relevant features...
- Early Stopping
- Cross Validation
- Data Augmentation

Underfitting Tackle:

- Train longer
- Feature engg...
- Remove Regularization (L1, L2)
- Reduce Noise
