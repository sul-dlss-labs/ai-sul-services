# AI SUL Services for Library Patrons and Staff
A guiding assumption of AI access is that we need systems and services across 
a spectrum of requirements and access modalities driven by the library's stakeholders.
To meet these needs in a rapidly changing environment this proof-of-concept provides
a `docker-compose.yml` for most of the stack below for demonstration purposes.

## Dedicated Resources for AI Work (broadly defined)
- Available GPUs for training models
- [Jupyter Hub][IPYNB_HUB] for hosting 
  shared Jupyter notebooks with access to GPUs and external AI services
- [Airflow][AIRFLOW] for managing repeatable ML workflows on collections with
  access to GPUs
- [Streamlit][STREAMLIT] dedicated data applications for visualization and training
- [Intake][INTAKE] for serving dataframes for use by Airflow, 
  Jupyter notebooks, and Streamlit apps
- [Dask][DASK] for distributed workloads, use in conjunction with Intake and Airflow
- [MLFlow][MLFLOW] for managing end-to-end machine learning workflows

## Use Cases

### Library Services Platform
1. Enhancement and automation of physical material workflows
  1. Acquisition staff member initiates a book order in FOLIO, many of the values in the order have 
     suggested values based on predicative model from historical and current orders. When staff
     member changes or rejects any of these values, the resulting order is used to further train 
     the model. 
  1. The model is managed in the [MLFlow][MLFLOW] with incremental training driven by an [Airflow][AIRFLOW]
     sensor that responds to the updated order action. 
  1. When the book arrives into processing, copy cataloger enhances the predicted metadata 
   
### Hopkins Marine Station Species Occurrence
1. Collection of Student Reports
  1. Intake provides DataFrames
  1. MLFlow registry of Models 

### SDR Intake Catalog

### Known Systemic Racism Project
1. Metadata for visualization and access - SB978 California Law Enforcement Agency Policy and Training Manuals 
  1. Watch for changes in published documents and pull changes
  2. Automate metadata extraction based on source URL and structured data in the document
  3. Streamlit app for search

[AIRFLOW]: https://airflow.apache.org/
[DASK]: https://dask.org/
[INTAKE]: https://intake.readthedocs.io/en/latest/
[IPYNB_HUB]: https://jupyterhub.readthedocs.io/en/latest/
[MLFLOW]: https://mlflow.org/
[STREAMLIT]: https://streamlit.io/
