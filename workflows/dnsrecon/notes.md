# Notes on making a workflow

## Installation 
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
chmod +x ./Miniconda3-latest-MacOSX-x86_64.sh
./Miniconda3-latest-MacOSX-x86_64.sh
conda init fish
conda create -n venv python=3.6.8
conda activate venv
conda install -c bioconda -c conda-forge snakemake
conda install --name venv dnspython
conda update -n venv snakemake
```

## Running
```
snakemake --snakefile ./main.snake --forceall
```
