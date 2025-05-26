# EDA - Exploratory Data Analysis:

- Method of analyzing dataset to understand their main characteristics.

## Types of EDA:

### 1. Univariate Analysis:

- Focuses on one variable to understanding its characteristics.
- Various common methods to show data: box plots to detect outliers & understand data spread & bar charts for categorical data.
- summary stats: mean, median, mode, variance, std. deviation.

### 2. Bivariate Analysis:

- Focuses on identifying the relationship between two variables to find the connections, **correlations**, and dependencies.

### 3. Multivariate Analysis:

- Focuses on identifying the r/s between two or more variables in the datasets.
- Techniques like: pair plots (for relationships), Principle Component Analysis (PCA) -> reducing the complexity of large datasets, Spatial Analysis -> geographical data, Time Series Analysis -> Time based data...

## Common Steps:

**1. Importing libraries**

**2. Understanding the problem and Reading Datasets:**

- `df.read_csv()`
- `df.head()`, `df.info()`, `df.describe()`
- Duplication check: `df.nunique()` | `df.isnull().sum()`

**3. Data Reduction:**

Available Options:

- Drop rows with null that are not adding any importance to the data.
- Drop Cols that are not relevant at all...
- Replace the null values with basic methods like (mean, median, mode) if required.
- Or implement appropriate imputation methods like regression imputation, KNN, Decision trees...

- **4. Feature Engineering & Feature Creation:**

- Create a meaningful data from the raw data...

**5. Data Cleaning:**

- Find & remove the duplicates (`.duplicated()` / `.unique()` / `.nunique()`).

**6. Performing Data Transformation:**

- `min-max scaling` / `standardization` - Scaling or normalizing numerical variables.
- Encoding categorial variables for ml like one-hot encoding or label encoding.
- Some mathematical transformations like logarithmic square root and all are also used to correct the skewness or non-linerity.
- Aggregation/grouping of data if required.

**7. Handling Outliers:**

- Outliers can be detected via Boxplot.
- We identify the outliers using methods like interquartile range (IQR), Z-scores, etc...

**8. Visualizing Relationship of Data:**

- Categorical Vairables: [frequency tables, bar plots, pie charts, etc...]
- Numerical Variables: [histograms, box plots, violin plots, density plots]
- Finding Relationship between variables: [scatter plots, correlation matrices, etc...]
