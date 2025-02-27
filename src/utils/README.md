# Utils Directory

The `utils` directory contains utility functions and helper scripts used across the project. These scripts provide common functionalities that are reused in different parts of the project.

## Python Files

- **file_utils.py**: Functions for file operations.
- **data_utils.py**: Helper functions for data manipulation.
- **model_utils.py**: Utility functions for model operations.

## Functions

### file_utils.py

- `read_file(file_path: str) -> str`: Reads the content of a file.
  - **Parameters**: `file_path` (str) - Path to the file.
  - **Returns**: Content of the file as a string.

### data_utils.py

- `split_data(df: pd.DataFrame, test_size: float) -> Tuple[pd.DataFrame, pd.DataFrame]`: Splits the DataFrame into training and testing sets.
  - **Parameters**: `df` (pd.DataFrame) - Input DataFrame.
  - **test_size** (float) - Proportion of the data to include in the test split.
  - **Returns**: Tuple containing training and testing DataFrames.

### model_utils.py

- `save_model(model: Model, file_path: str) -> None`: Saves the trained model to a file.
  - **Parameters**: `model` (Model) - Trained machine learning model.
  - **file_path** (str) - Path to save the model file.
