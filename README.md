# job_search
Looking for a job in this job climate


Downloading Anaconda:

# check to see if it is installed
conda --version

# On a windows, check to see where it is
where conda

# View a list of existing virtual environments:
conda info --envs

# Create a virtual environment. I've named mine first-env and specified the Python version

conda create -n first-env python=3.8

# Activate the virtual environment

conda activate first-env

# Don't forget to deactivate and delete the environment when done respectively

conda deactivate
conda env remove -n first-env

----------------------------------

# What to install:
pip install bs4

pip install requests


-------------------------------------

# How to test:
pip install -r requirements.txt

# remember to download the latest version of shub and to deploy it
pip install shub --upgrade

shub deploy