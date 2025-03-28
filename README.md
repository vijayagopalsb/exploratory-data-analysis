## Exploratory Data Analysis (EDA) Pipeline

Exploratory Data Analysis (EDA) is a critical step in any data science project. It involves summarizing the dataset, detecting patterns, and uncovering relationships before applying ML Models.

### Project Overview

This project implements an **Exploratory Data Analysis (EDA) Pipeline** using a **Chain of Responsibility** pattern. The pipeline consists of multiple handlers that sequentially process a dataset, performing various data analysis tasks such as handling missing values, univariate analysis, bivariate analysis, and correlation analysis.

### Directory Structure

<pre>
exploratory-data-analysis/
│── main.py
│── logging_config.py
│── README.md
│── LICENSE
|
└── handlers/
    │── base_handler.py
    │── understand_data.py
    │── handle_missing_values.py
    │── univariate_analysis.py
    │── bivariate_analysis.py
    │── correlation_analysis.py
</pre>

### Installation & Setup

#### Prerequisites

Ensure you have Python 3.8+ installed and the required libraries:

```python
pip install pandas numpy seaborn matplotlib
```

### Running the Project

```python
python main.py
```

---

### Components & Handlers

1. **Base Handler (base_handler.py)**

    Defines the base class EDAHandler, which serves as the foundation for all other handlers.

2. **Understanding Dataset (understand_data.py)**

    - Logs dataset information such as column names, data types, and missing values.

    - First step in the EDA pipeline.

3. **Handling Missing Values (handle_missing_values.py)**

    - Replaces missing values using a specified strategy (mean, median, mode).

    - Passes the processed data to the next handler.

4. **Univariate Analysis (univariate_analysis.py)**

    - Generates histograms for numeric columns.

    - Displays basic distribution of individual features.

5. **Bivariate Analysis (bivariate_analysis.py)**

    - Analyzes relationships between the target column and numerical variables.

    - Converts categorical variables to string format to avoid plotting issues.

6. **Correlation Analysis (correlation_analysis.py)**

    - Computes and visualizes correlation matrices using heatmaps.

7. **Logging Configuration (logging_config.py)**

    - Manages logging of pipeline execution steps and errors.

---

### EDA Pipeline Execution

The pipeline follows a Chain of Responsibility pattern:

```python
# Initialize Handlers
correlation_analysis = CorrelationAnalysis()

bivariate_analysis = BivariateAnalysis(target_column="survived", next_handler=correlation_analysis)

univariate_analysis = UnivariateAnalysis(next_handler=bivariate_analysis)

handle_missing_values = HandleMissingValues(strategy="mean", next_handler=univariate_analysis)

pipeline = UnderstandDataset(next_handler=handle_missing_values)


# Start the pipeline with the dataset
pipeline.handle(df)
```
---

### Example Log Output

Upon execution, logs provide insights into the pipeline process:

<pre>
2025-03-28 21:31:30,544 - INFO ->>> Starting EDA Pipeline ...
2025-03-28 21:31:30,544 - INFO ->>> Step 1: -->> Understanding the dataset ...
2025-03-28 21:31:30,544 - INFO ->>>
Display Features of Dataset:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   survived     891 non-null    int64
 1   pclass       891 non-null    int64
 2   sex          891 non-null    object
 3   age          714 non-null    float64
 4   sibsp        891 non-null    int64
 5   parch        891 non-null    int64
 6   fare         891 non-null    float64
 7   embarked     889 non-null    object
 8   class        891 non-null    category
 9   who          891 non-null    object
 10  adult_male   891 non-null    bool
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object
 13  alive        891 non-null    object
 14  alone        891 non-null    bool
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB
2025-03-28 21:31:30,560 - INFO ->>> None
2025-03-28 21:31:30,561 - INFO ->>>
Summary Statistics:
2025-03-28 21:31:30,575 - INFO ->>>           survived      pclass   sex         age       sibsp       parch        fare  ...  class  who adult_male deck  embark_town alive alone
count   891.000000  891.000000   891  714.000000  891.000000  891.000000  891.000000  ...    891  891        891  203          889   891   891
unique         NaN         NaN     2         NaN         NaN         NaN         NaN  ...      3    3          2    7            3     2     2
top            NaN         NaN  male         NaN         NaN         NaN         NaN  ...  Third  man       True    C  Southampton    no  True
freq           NaN         NaN   577         NaN         NaN         NaN         NaN  ...    491  537        537   59          644   549   537
mean      0.383838    2.308642   NaN   29.699118    0.523008    0.381594   32.204208  ...    NaN  NaN        NaN  NaN          NaN   NaN   NaN
std       0.486592    0.836071   NaN   14.526497    1.102743    0.806057   49.693429  ...    NaN  NaN        NaN  NaN          NaN   NaN   NaN
min       0.000000    1.000000   NaN    0.420000    0.000000    0.000000    0.000000  ...    NaN  NaN        NaN  NaN          NaN   NaN   NaN
25%       0.000000    2.000000   NaN   20.125000    0.000000    0.000000    7.910400  ...    NaN  NaN        NaN  NaN          NaN   NaN   NaN
50%       0.000000    3.000000   NaN   28.000000    0.000000    0.000000   14.454200  ...    NaN  NaN        NaN  NaN          NaN   NaN   NaN
75%       1.000000    3.000000   NaN   38.000000    1.000000    0.000000   31.000000  ...    NaN  NaN        NaN  NaN          NaN   NaN   NaN
max       1.000000    3.000000   NaN   80.000000    8.000000    6.000000  512.329200  ...    NaN  NaN        NaN  NaN          NaN   NaN   NaN

[11 rows x 15 columns]
2025-03-28 21:31:30,579 - INFO ->>> 
Missing Values:
2025-03-28 21:31:30,579 - INFO ->>> survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
2025-03-28 21:31:30,579 - INFO ->>> Step 2: -->> Handling missing values using mean strategy ...
2025-03-28 21:31:30,596 - INFO ->>> Step 3: -->> Performimg Univariate Analysis ...
2025-03-28 21:31:34,699 - INFO ->>> Step 4: -->> Performing bivariate analysis with target 'survived'...
2025-03-28 21:31:34,700 - INFO ->>> Seaborn version: 0.13.2, Matplotlib version: 3.10.1
2025-03-28 21:31:34,700 - INFO ->>> Original type of 'survived': int64
2025-03-28 21:31:34,700 - INFO ->>> Sample of 'survived': [0, 1, 1, 1, 0]
2025-03-28 21:31:34,700 - INFO ->>> Plotting pclass vs survived...
2025-03-28 21:31:34,700 - INFO ->>> Type of 'survived' before plotting: int64
2025-03-28 21:31:38,734 - INFO ->>> Plotting age vs survived...
2025-03-28 21:31:38,735 - INFO ->>> Type of 'survived' before plotting: int64
2025-03-28 21:31:40,756 - INFO ->>> Plotting sibsp vs survived...
2025-03-28 21:31:42,255 - INFO ->>> Plotting parch vs survived...
2025-03-28 21:31:42,256 - INFO ->>> Type of 'survived' before plotting: int64
2025-03-28 21:31:43,735 - INFO ->>> Plotting fare vs survived...
2025-03-28 21:31:43,736 - INFO ->>> Type of 'survived' before plotting: int64
2025-03-28 21:31:46,462 - INFO ->>> Step 5: -->> Performing correlation analysis...
2025-03-28 21:31:48,645 - INFO ->>> EDA Pipeline Completed Successfully!
PS D:\my_github_projects> & "C:/Users/VIJAYAGOPAL S/AppData/Local/Programs/Python/Python312/python.exe" d:/my_github_projects/exploratory-data-analysis/main.py
2025-03-28 21:39:14,359 - INFO ->>> Starting EDA Pipeline ...
2025-03-28 21:39:14,359 - INFO ->>> Step 1: -->> Understanding the dataset ...
2025-03-28 21:39:14,359 - INFO ->>>
Display Features of Dataset:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   survived     891 non-null    int64
 1   pclass       891 non-null    int64
 2   sex          891 non-null    object
 3   age          714 non-null    float64
 4   sibsp        891 non-null    int64
 5   parch        891 non-null    int64
 6   fare         891 non-null    float64
 7   embarked     889 non-null    object
 8   class        891 non-null    category
 9   who          891 non-null    object
 10  adult_male   891 non-null    bool
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object
 13  alive        891 non-null    object
 14  alone        891 non-null    bool
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB
2025-03-28 21:39:14,369 - INFO ->>> None
2025-03-28 21:39:14,369 - INFO ->>>
Summary Statistics:
2025-03-28 21:39:14,382 - INFO ->>>           survived      pclass   sex         age       sibsp       parch        fare embarked  class  who adult_male deck  embark_town alive alone
count   891.000000  891.000000   891  714.000000  891.000000  891.000000  891.000000      889    891  891        891  203          889   891   891
unique         NaN         NaN     2         NaN         NaN         NaN         NaN        3      3    3          2    7            3     2     2
top            NaN         NaN  male         NaN         NaN         NaN         NaN        S  Third  man       True    C  Southampton    no  True
freq           NaN         NaN   577         NaN         NaN         NaN         NaN      644    491  537        537   59          644   549   537
mean      0.383838    2.308642   NaN   29.699118    0.523008    0.381594   32.204208      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
std       0.486592    0.836071   NaN   14.526497    1.102743    0.806057   49.693429      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
min       0.000000    1.000000   NaN    0.420000    0.000000    0.000000    0.000000      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
25%       0.000000    2.000000   NaN   20.125000    0.000000    0.000000    7.910400      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
50%       0.000000    3.000000   NaN   28.000000    0.000000    0.000000   14.454200      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
75%       1.000000    3.000000   NaN   38.000000    1.000000    0.000000   31.000000      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
max       1.000000    3.000000   NaN   80.000000    8.000000    6.000000  512.329200      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
2025-03-28 21:39:14,394 - INFO ->>> 
Missing Values:
2025-03-28 21:39:14,394 - INFO ->>> survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
2025-03-28 21:39:14,394 - INFO ->>> Step 2: -->> Handling missing values using mean strategy ...
2025-03-28 21:39:14,394 - INFO ->>> Step 3: -->> Performimg Univariate Analysis ...
2025-03-28 21:39:18,726 - INFO ->>> Step 4: -->> Performing bivariate analysis with target 'survived'...
2025-03-28 21:39:18,726 - INFO ->>> Seaborn version: 0.13.2, Matplotlib version: 3.10.1
2025-03-28 21:39:18,727 - INFO ->>> Original type of 'survived': int64
2025-03-28 21:39:18,728 - INFO ->>> Sample of 'survived': [0, 1, 1, 1, 0]
2025-03-28 21:39:18,728 - INFO ->>> Plotting pclass vs survived...
2025-03-28 21:39:18,729 - INFO ->>> Type of 'survived' before plotting: int64
2025-03-28 21:39:20,743 - INFO ->>> Plotting age vs survived...
2025-03-28 21:39:20,744 - INFO ->>> Type of 'survived' before plotting: int64
2025-03-28 21:39:22,164 - INFO ->>> Plotting sibsp vs survived...
2025-03-28 21:39:22,164 - INFO ->>> Plotting sibsp vs survived...
2025-03-28 21:39:22,164 - INFO ->>> Plotting sibsp vs survived...
2025-03-28 21:39:22,164 - INFO ->>> Plotting sibsp vs survived...
2025-03-28 21:39:22,164 - INFO ->>> Plotting sibsp vs survived...
2025-03-28 21:39:22,164 - INFO ->>> Plotting sibsp vs survived...
2025-03-28 21:39:22,164 - INFO ->>> Plotting sibsp vs survived...
2025-03-28 21:39:22,165 - INFO ->>> Type of 'survived' before plotting: int64
2025-03-28 21:39:23,652 - INFO ->>> Plotting parch vs survived...
2025-03-28 21:39:23,653 - INFO ->>> Type of 'survived' before plotting: int64
2025-03-28 21:39:24,926 - INFO ->>> Plotting fare vs survived...
2025-03-28 21:39:24,926 - INFO ->>> Type of 'survived' before plotting: int64
2025-03-28 21:39:26,041 - INFO ->>> Step 5: -->> Performing correlation analysis...
2025-03-28 21:39:28,204 - INFO ->>> EDA Pipeline Completed Successfully!
</pre>

---

###  Future Enhancements

    - Outlier Detection & Treatment

    - Feature Engineering & Selection

    - Automated Report Generation

For contributions, feel free to fork the repository and submit pull requests!
