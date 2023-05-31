# Multi environment Dataset

This file contains the instructions to download and setup the data of the multi environment dataset, published in:

> Baha’A, A., Almazari, M. M., Alazrai, R., & Daoud, M. I. (2020). A dataset for Wi-Fi-based human activity recognition in line-of-sight and non-line-of-sight indoor environments. Data in Brief, 33, 106534.

## Download

Dowload the dataset using the follwing [Mendeley Data link](https://data.mendeley.com/datasets/v38wjmz6f6/1).

## Setup

1. Unzip the data of each directory and subdirectory, except `ENVIRONMENT 3`, which will not be used.
2. Place the folder `ENVIRONMENT 1` (make sure the subdirectories are uncompressed) into the folder `01_DATA/02_MULTI-ENV`.
3. Place the folder `ENVIRONMENT 2` (make sure the subdirectories are uncompressed) into the folder `01_DATA/02_MULTI-ENV`.
4. Load the data using the functions provided in `01.2_multi-env-evaluation.ipynb`.