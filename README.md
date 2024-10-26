![License](https://img.shields.io/static/v1?label=license&message=CC-BY-NC-4.0&color=green)

# External Validation of Predictive Models for Diagnosis, Management and Severity of Pediatric Appendicitis

This repository accompanies the paper "*External Validation of Predictive Models for Diagnosis, Management and Severity of Pediatric Appendicitis*".

**Abstract**

*Background.* Appendicitis is a common condition among children and adolescents. Machine learning models can offer much-needed tools for improved diagnosis, severity assessment and management guidance for pediatric appendicitis. However, to be adopted in practice, such systems must be reliable, safe and robust across various medical contexts, e.g., hospitals with distinct clinical practices and patient populations.

*Methods.* We performed external validation of models predicting the diagnosis, management and severity of pediatric appendicitis. Trained on a cohort of 430 patients admitted to the Children's Hospital St. Hedwig (Regensburg, Germany), the models were validated on an independent cohort of 301 patients from the Florence Nightingale Hospital (Düsseldorf, Germany). The data included demographic, clinical, scoring, laboratory and ultrasound parameters. In addition, we explored the benefits of model retraining and inspected variable importance.

*Results.* The distributions of most parameters differed between the datasets. Consequently, we saw a decrease in predictive performance for diagnosis, management and severity across most metrics. After retraining with a portion of external data, we observed gains in performance, which, nonetheless, remained lower than in the original study. Notably, the most important variables were consistent across the datasets.

*Conclusions.* While the performance of transferred models was satisfactory, it remained lower than on the original data. This study demonstrates challenges in transferring models between hospitals, especially when clinical practice and demographics differ or in the presence of externalities such as pandemics. We also highlight the limitations of retraining as a potential remedy since it could not restore predictive performance to the initial level.

### Requirements

All the libraries required to run this code are in the conda environment [`environment.yml`](environment.yml). To install it, follow the instructions below:
```
conda env create -f environment.yml   # install dependencies
conda activate app-ext-val            # activate environment
```

### Data

The data for both Regensburg and Düsseldordf cohorts is available in an anonymized format in the [`data`](data) folder as CSV files.

### Usage

- [`utils`](utils) folder contains utility functions and scripts
- [`notebooks`](notebooks) folder contains Jupyter notebooks for the analysis
- [`summary_statistics.ipynb`](notebooks/summary_statistics.ipynb) performs exploratory data analysis
- [`external_validation.ipynb`](notebooks/external_validation.ipynb) performs external validation of the predictive models
- [`retraining.ipynb`](notebooks/retraining.ipynb) explores model retraining
- [`variable_importance.ipynb`](notebooks/variable_importance.ipynb) explores variable importance

### Maintainer 

This repository is maintained by Ričards Marcinkevičs ([richard.martsinkevich@gmail.com](mailto:richard.martsinkevich@gmail.com)).

### Citation

Coming soon...

### Copyright

This repository is additionally licensed under CC-BY-NC-4.0.
