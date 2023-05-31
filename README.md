# Reproducible package for _"Temporal Stability on Human Activity Recognition based on Wi-Fi CSI"_

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/GeoTecINIT/stability-csi-har/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/zenodo/10.5281/zenodo.7991716/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7991716.svg)](https://doi.org/10.5281/zenodo.7991716)


This repository is the reproducibility package for the paper _“Temporal Stability on Human Activity Recognition based on Wi-Fi CSI"_, submitted to the 13th International Conference on Indoor Positioning and Indoor Navigation (IPIN 2023).

You can explore the data and code used to obtain the results presented in the paper. To properly view the Jupyter Notebook files with their rendered figures, click on the "nbviewer" badge above.

## Reproducibility 

### Reproduce online 

Click the on the "Binder" badge above to open an interactive Jupyter environment with all required software installed.

### Reproduce locally
Install Python 3.9, download the repository, open a command line in the root of the directory and install the required software by executing:

```bash
pip install -r requirements.txt
```

### Reproduce locally with Docker
Install [Docker](https://www.docker.com) for building an image based on a `Dockerfile` with a Jupyter environment and running a container based on the image.

Download the repository, open a command line in the root of the directory and:

1. Build the image:

```bash
docker build . --tag stability-csi-har-rp
```

2. Run the image:

```bash
docker run -it -p 8888:8888 stability-csi-har-rp
```

3. Click on the login link (or copy and paste in the browser) shown in the console to access to a Jupyter environment.

### Reproduce the analysis
Open the desired Jupyter Notebook (*.ipynb) file. The notebook contains the code used for the analysis and its outputs. You can execute the code to reproduce the obtained results presented in the paper.

> **Note**: when executing code with a component of randomness (i.e., ML models training), the obtained results could be slightly different than the reported ones. Notwithstanding, the conclusions should be similar as the reported ones.


## Repository structure

Common files:
- [`Dockerfile`](./Dockerfile): a recipe for the computational environment using Docker.
- [`requirements.txt`](./requirements.txt): file with the dependencies and versions used through all the code.


Jupyter Notebooks:

- [`01.1_stanwifi-evaluation.ipynb`](./01.1_stanwifi-evaluation.ipynb): Jupyter Notebook containing the code for evaluating the proposed preprocessing pipeline and the CNN model using the [StanWiFi dataset](https://github.com/ermongroup/Wifi_Activity_Recognition) and a 10-fold cross validation. Results are stored in [`02_RESULTS/01_STANWIFI/01_MODEL-REPORTS/reports.json`](./02_RESULTS/01_STANWIFI/01_MODEL-REPORTS/reportS.json). The summary results at the end are the ones incorporated in **Table III** (StanWiFi > This work) of the paper.
  > **Note**: to reproduce this notebook, please follow the [instructions](./01_DATA/01_STANWIFI/README.md) to download and setup the StanWiFi dataset.
- [`01.2_multi-env-evaluation.ipynb`](./01.2_multi-env-evaluation.ipynb): Jupyter Notebook containing the code for evaluating the proposed preprocessing pipeline and the CNN model using the [multi-environment dataset](https://doi.org/10.1016/J.DIB.2020.106534) and a 10-fold cross validation. Results are stored in [`02_RESULTS/02_MULTI-ENV/01_MODEL-REPORTS/e1-reports.json`](./02_RESULTS/02_MULTI-ENV/01_MODEL-REPORTS/e1-reports.json) and [`02_RESULTS/02_MULTI-ENV/01_MODEL-REPORTS/e2-reports.json`](./02_RESULTS/02_MULTI-ENV/01_MODEL-REPORTS/e2-reports.json) for _ENVIRONMENT 1_ and _ENVIRONMENT 2_, respectively. The summary results at the end are the ones incorporated in **Table III** (Multi-environment (E1/E2) > This work) of the paper.
  > **Note**: to reproduce this notebook, please follow the [instructions](./01_DATA/01_MULTI-ENV/README.md) to download and setup the multi-environment dataset.
- [`02_collected-data-processing.ipynb`](./02_collected-data-processing.ipynb): Jupyter Notebook containing the code for preprocessing the collected dataset. The notebook loads the data in [`01_DATA/03_COLLECTED-DATASET/01_RAW`](./01_DATA/03_COLLECTED-DATASET/01_RAW) and generates four labelled datasets (_D1_, _D2_, _D3_ and _D4_) in [`01_DATA/03_COLLECTED-DATASET/02_LABELLED`](./01_DATA/03_COLLECTED-DATASET/02_LABELLED). The data is labelled accordingly to the activity the user was performing at each moment: _seated_rx_, _standing_up_rx_, _walking_tx_, _turn_tx_, _sitting_down_tx_, _seated_tx_, _standing_up_tx_, _walking_rx_, _turn_rx_ and _sitting_down_rx_. It also aranges the data in each dataset in windows of 50 samples with 50% overlap in [`01_DATA/03_COLLECTED-DATASET/03_WINDOWED`](./01_DATA/03_COLLECTED-DATASET/03_WINDOWED). It also contains the **Table II** (samples per activity and dataset) of the paper.
- [`03_evaluation-localized-har.ipynb`](./03_evaluation-localized-har.ipynb): Jupyter Notebook containing the code to evaluate the classification accuracy of the CNN model using five evaluation approaches:
  - 10-fold cross validation: results stored in [`02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS/cv_report.json`](./02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS/cv_report.json).
  - First 80% of _D1T_ for training, the remaining 20% for testing (_D1E_): results stored in [`02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS/d1_report.json`](./02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS/d1_report.json) and [`02_RESULTS/03_COLLECTED-DATASET/02_CONFUSION_MATRIXES/d1_cfm.pdf`](./02_RESULTS/03_COLLECTED-DATASET/02_CONFUSION_MATRIXES/d1_cfm.pdf).
  - Training wiht _D1T_, evaluation with _D2_: results stored in [`02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS/d2_report.json`](./02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS/d2_report.json) and [`02_RESULTS/03_COLLECTED-DATASET/02_CONFUSION_MATRIXES/d2_cfm.pdf`](./02_RESULTS/03_COLLECTED-DATASET/02_CONFUSION_MATRIXES/d2_cfm.pdf).
  - Training wiht _D1T_, evaluation with _D3_: results stored in [`02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS/d3_report.json`](./02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS/d3_report.json) and [`02_RESULTS/03_COLLECTED-DATASET/02_CONFUSION_MATRIXES/d3_cfm.pdf`](./02_RESULTS/03_COLLECTED-DATASET/02_CONFUSION_MATRIXES/d3_cfm.pdf).
  - Training wiht _D1T_, evaluation with _D4_: results stored in [`02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS/d4_report.json`](./02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS/d4_report.json) and [`02_RESULTS/03_COLLECTED-DATASET/02_CONFUSION_MATRIXES/d4_cfm.pdf`](./02_RESULTS/03_COLLECTED-DATASET/02_CONFUSION_MATRIXES/d4_cfm.pdf).
  The results obtained in this notebook are included in the **Table IV** (summary metrics), **Table V** (decrement), **Figure 5** and **Figure 6** (confusion matrixes).


Directories:

- [`01_DATA`](./01_DATA): 
  - [`01_STANWIFI`](./01_DATA/01_STANWIFI): contains a [README](./01_DATA/01_STANWIFI/README.md) explaining how to download and setup the dataset.
  - [`02_MULTI-ENV`](./01_DATA/02_MULTI-ENV): contains a [README](./01_DATA/02_MULTI-ENV/README.md) explaining how to download and setup the dataset.
  - [`03_COLLECTED-DATASET`](./01_DATA/03_COLLECTED-DATASET):
    - [`01_RAW`](./01_DATA/03_COLLECTED-DATASET/01_RAW) (**First unzip the compressed file**): contains the collected raw dataset with the Wi-Fi CSI data ([`01_dataset.csv`](./01_DATA/03_COLLECTED-DATASET/01_RAW/01_dataset.csv)) and four files containing information for data segmentation. 
    - [`02_LABELLED`](./01_DATA/03_COLLECTED-DATASET/02_LABELLED): contains the four labelled datasets (_D1_, _D2_, _D3_ and _D4_) obtained from the raw dataset. Each folder, contains file of the form e{XX}_{rx_tx|tx_rx}-{x|y}.npy where:
      - {XX}: execution id.
      - {rx_tx|tx_rx}: indicates the direction of the execution, i.e., rx_tx, goes from rx to tx.
      - {x|y}: x files contain amplitudes (CSI data) and y files contain their associated labels.
    - [`03_WINDOWED`](./01_DATA/03_COLLECTED-DATASET/03_WINDOWED): contains the data of each dataset arranged in windows of 50 samples with 50% overlap. Each folder contains files with the same name pattern as the previous ones.
    - [`amplitudes-heatmap.pdf`](./01_DATA/03_COLLECTED-DATASET/amplitudes-heatmap.pdf): plot showing the first and last sequence of activities from _D1_ and _D4_, respectively. It corresponds with the **Figure 7** of the paper.
- [`02_RESULTS`](./02_RESULTS): 
  - [`01_STANWIFI`](./02_RESULTS/01_STANWIFI): contains the generated results in [`01.1_stanwifi-evaluation.ipynb`](./01.1_stanwifi-evaluation.ipynb). Used to generate StanWiFi > This work (**Table III**). 
  - [`02_MULTI-ENV`](./02_RESULTS/02_MULTI-ENV): contains the generated results in [`01.2_multi-env-evaluation.ipynb`](./01.2_multi-env-evaluation.ipynb). Used to generate Multi-environment (E1/E2) > This work (**Table III**). 
  - [`03_COLLECTED-DATASET`](./02_RESULTS/03_COLLECTED-DATASET): contains the generated results in [`03_evaluation-localized-har.ipynb`](./03_evaluation-localized-har.ipynb).
    - [`01_MODEL-REPORTS`](./02_RESULTS/03_COLLECTED-DATASET/01_MODEL-REPORTS): contains the classification reports of each evaluation approach. Used to generate **Table IV** and **Table V**.
    - [`02_CONFUSION-MATRIXES`](./02_RESULTS/03_COLLECTED-DATASET/02_CONFUSION-MATRIXES): contains the confusion matrixes of each evaluation approach (except 10-fold cross validation). Used to generate **Figure 5** and **Figure 6**.
- [`functions`](./functions): contains several Python files defining common functions used in the notebooks:
  - [`filters`](./functions/filters): includes a DBSCAN based filtering and a discrete wavelet transform (DWT) based filter.
  - [`json`](./functions/json): utils for loading and storing json-based data.
  - [`ml`](./functions/ml): includes functions for cross validation, model evaluation, building classification reports, etc.
  - [`random`](./functions/random): includes function for fixing the random seeds.
  - [`report_metrics`](./functions/report_metrics): functions for summarizing classification reports in table format.


## License 
The documents in this repository are licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

All contained code is licensed under the [Apache License 2.0](./LICENSE).

All data used in this repository is licensed under [Open Data Commons Attribution License](http://opendatacommons.org/licenses/by/1.0/).
