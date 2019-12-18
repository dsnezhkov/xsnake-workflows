# PoC

## Overview

This PoC takes a domain name and generates a list of ports and services per IP on hosts belonging to the domain.
This is accomplished by running a set of well defined commands a pentester would normally run manually, followed by one or more transformations on data produced by the commands.

A sample workflow in this PoC takes the following steps:
- Runs a domain name through `dnsmap`
- Merges the list of IPs with an additional scope file with IPs not part of the prior discovery step
- Transforms the output into the input to `nmap`, and runs Nmap on targets
- Parses `nmap` output into a table of ports and services. 


The workflow file is documented with the steps and dependencies. 

Additionally, an exmaple of creating a png of a workflow dependencies is provided in the reports folder.
The jobs in the workflow showcase a few ways of invoking external commands that could be useful in building complex workflows.


## Pre-requisites


```bash
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
$ chmod +x Miniconda3-latest-Linux-x86_64.sh && ./Miniconda3-latest-Linux-x86_64.sh
$ conda install -c bioconda -c conda-forge snakemake
$ conda create -n venv python
$ conda activate venv

```
```bash
$ pip install python-libnmap
```

```
# python -V
Python 3.6.8 :: Anaconda, Inc.
```

## Invoking Workflow

### Rerun simulation of jobs
```bash
snakemake --snakefile Workflow.0x0 -np data/nmap.tbl
```

### Rerun one intermediate job
```bash
snakemake --snakefile Workflow.0x0 -p data/ipranges
```

### Rerun all jobs (force deletion of artifacts)
```bash
snakemake --snakefile Workflow.0x0 -p data/nmap.tbl --forceall
```

## See Workflow graph

```bash
snakemake --snakefile Workflow.0x0 -p reports/Workflow.0x0.dot
```

