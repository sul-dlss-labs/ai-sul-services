# AI Access for Library Staff
A guiding assumption of AI access is that we need systems and services across 
a spectrum of requirements and access modalities driven by the library's stakeholders.
To meet these needs in a rapidly changing 

## Dedicated Resources for AI Work (broadly defined)
- Available GPUs for training models
- [Jupyter Hub](https://jupyterhub.readthedocs.io/en/latest/) for hosting 
  shared Jupyter notebooks with access to GPUs and external AI services
- [Airflow](https://airflow.apache.org/) for managing repeatable ML workflows on collections with
  access to GPUs
- [Streamlit](https://streamlit.io/) dedicated data applications for visualization and training
- [Intake](https://intake.readthedocs.io/en/latest/) for serving dataframes for use by Airflow, 
  Jupyter notebooks, and Streamlit apps
- [Dask](https://dask.org/) for distributed workloads, use in conjunction with Intake and Airflow
- [MLFlow][MLFLOW]

## Use Cases

### Library Services Platform
1. Enhancement and automation of physical material workflows
  1. Acquisition staff member initiates a book order in FOLIO, many of the values in the order have 
     suggested values based on predicative model from historical and current orders. When staff
     member changes or rejects any of these values, the resulting order is used to further train 
     the model. 
  1. The model is managed in the [MLFlow][MLFLOW] with incremental training driven by an Airflow
     sensor that responds to the updated order action. 
  1. When the book arrives into processing, copy cataloger enhances the predicted metadata 
   
### Hopkins Marine Station Species Occurrence
1. Collection of Student Reports
  1. Intake provides DataFrames
  1. MLFlow registry of Models 


[MLFLOW]: https://mlflow.org/

