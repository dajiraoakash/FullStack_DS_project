# Pipelines Directory

The `pipelines` directory houses end-to-end machine learning pipelines that combine data processing and model training. These scripts automate the entire workflow from raw data to model deployment.

## Python Files

- **data_pipeline.py**: End-to-end data processing pipeline.
- **training_pipeline.py**: End-to-end model training pipeline.
- **deployment_pipeline.py**: Scripts for deploying trained models.

## Functions

### data_pipeline.py

- `run_data_pipeline() -> pd.DataFrame`: Executes the data processing pipeline.
  - **Returns**: Processed DataFrame ready for model training.

### training_pipeline.py

- `run_training_pipeline() -> Model`: Executes the model training pipeline.
  - **Returns**: Trained machine learning model.

### deployment_pipeline.py

- `deploy_model(model: Model) -> None`: Deploys the trained model to a production environment.
  - **Parameters**: `model` (Model) - Trained machine learning model.
