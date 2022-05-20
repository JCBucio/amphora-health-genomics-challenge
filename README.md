# 2022 Amphora Health's Data Challenge Internship

2022 Amphora Health's Data Challenge Internship to explore the information that exists in our cells and develop machine learning models that can predict the risk of developing or acquiring a given disease.

## Running the project
Download the [zip file](https://github.com/JCBucio/amphora-health-genomics-challenge/archive/refs/heads/main.zip) or use `git clone` to clone the repository to a working directory (e.g., `/Users/jcbucio/amphora-health-genomics-challenge/`). All the notebooks will be run from this directory, and all new files will be generated here.

The dependencies for this project can be easily installed via [pip](https://pypi.org/project/pip/) on the command line. I **highly** recommend using a virtual environment so that your dependencies does not conflict with other Python packages.
This can be done with the following commands:

First, we create a virtual environment located in our working directory:
```
$ python3 -m venv amphora-env
```

Now we activate the virtual environment:
```
$ source amphora-env/bin/activate
```

Then we install the dependencies located in the `requirements.txt` file:
```
$ python3 -m pip install -r requirements.txt
```
With this, we are ready to run the notebooks.

If you want to run the notebooks from the command line, you can use the following command:
```
$ jupyter run src/main.ipynb
```
This will run all the notebooks in the project. This process will take a while, so please be patient.

### Files Structure

This project is written in Jupyter Notebooks that follows an specific order to be run. Below is the tree of the structure of the notebooks:

src/
├── 0_preprocessing.ipynb
├── 1_data-augmentation.ipynb
├── 2_split-and-training.ipynb
├── 3_evaluate-model.ipynb
├── main.ipynb
├── tmp/
└── utils.py

To make possible the processing of all the notebooks from a single file I am using the [papermill](https://papermill.readthedocs.io/en/latest/) package. Each notebook accomplish a different task from the ones defined above. They are separated as follows:

- `src/main.ipynb`: This notebook contains the code to run all the notebooks in the project.
- `src/0_preprocessing.ipynb`: This notebook contains the code to merge all the files into a single table to construct a merged genotype file for several individuals, this will be used for the training datasets.
- `src/1_data-augmentation.ipynb`: This notebook contains the code to read from the ancestries file and extract the column called **Superpopulation Code** for the purpose of augmenting the training dataset.
- `src/2_split-and-training.ipynb`: This notebook contains the code to split the database into 80% for training and 20% for testing. In it we will perform the final formatting in our data prior to training the model. As well, we will train and save each one of the models in separates `.pkl` files.
- `src/3_evaluate-model.ipynb`: This notebook handles the evaluation and plots the results for a better understanding of the performance of each model.

Also, in the `src/utils.py` file we have the functions that will be imported and used in the notebooks to make repetitive tasks.

### Configuration File

There is a config file that contains the parameters that will be used in the notebooks. This parameters can be found in the `config/parameters.yml` file. The file is in **YAML** format and the parameters are defined as follows:

- **Input and output paths:**
    - `sample_data_path`: Path to the folder containing the sample data.
    - `output_data_path`: Path to the folder where the output data will be stored.

- **Specific files:**
    - `tsv_file`: Path to the file containing all patient IDs and their calculated genetic ancestry (e.g. European, Asian, African).
    - `master_file`: Path to the file containing all the genotype data.
    - `master_augmented`: Path to the file containing all the genotype data with the superpopulation code.
    - `master_augmented_2`: This file contains the same data as `master_augmented` but with a different approach for a better organization of the information.

- **Output models files:**
    - `afr_model`: Path to the file containing the trained model for African calculated genetic ancestry.
    - `eur_model`: Path to the file containing the trained model for European calculated genetic ancestry.
    - `sas_eas_model`: Path to the file containing the trained model for South Asian and East Asian calculated genetic ancestry.

- **CSV's ready for training and splitting:**
    - `afr_csv`: Path to the file containing the training dataset for African calculated genetic ancestry.
    - `eur_csv`: Path to the file containing the training dataset for European calculated genetic ancestry.
    - `sas_eas_csv`: Path to the file containing the training dataset for South Asian and East Asian calculated genetic ancestry.

### Data Structure

Below is the data structure that follows the project, all the files stored in the `data/output` folder will be generated in the project.

data/
├── ancestry-1000genome.tsv
├── input/
│   └── n-samples.csv
└── output/
    ├── afr_dataframe.csv
    ├── eur_dataframe.csv
    ├── sas_eas_dataframe.csv
    ├── master_augmented_2.csv
    ├── master_augmented.csv
    ├── master.csv
    └── models/
        ├── afr_model.pkl
        ├── eur_model.pkl
        └── sas_eas_model.pkl
    

## Running the project
Download the [zip file](https://github.com/JCBucio/amphora-health-genomics-challenge/archive/refs/heads/main.zip) or use `git clone` to clone the repository to a working directory (e.g., `/Users/jcbucio/amphora-health-genomics-challenge/`). All the notebooks will be run from this directory, and all new files will be generated here.

The dependencies for this project can be easily installed via [pip](https://pypi.org/project/pip/) on the command line. I **highly** recommend using a virtual environment so that your dependencies does not conflict with other Python packages.
This can be done with the following commands:

First, we create a virtual environment located in our working directory:
```
$ python3 -m venv amphora-env
```

Now we activate the virtual environment:
```
$ source amphora-env/bin/activate
```

Then we install the dependencies:
```
$ python3 -m pip install -r requirements.txt
```

With this, we are ready to run the notebooks.
If you want to run the notebooks from the command line, you can use the following command:
```
$ jupyter run src/main.ipynb
```
This will run all the notebooks in the project. This process will take a while, so please be patient.