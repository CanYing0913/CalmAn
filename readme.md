# Pipeline Setup Instruction  
- Latest update on 2022.12.14, Docker is not set up yet, please follow to create conda environment.  
# roadmap
- update image generation to be consistent with [paper output](https://bmcneurosci.biomedcentral.com/articles/10.1186/s12868-017-0391-y/figures/7)    
- try multiple instances in caiman && free up RAM for each instance  
- add support for peak caller to handle multiple cmn_objs **(perhaps pipelined?)**
- test docker container / try Linux container(systemd)  
# Notes on performance  
- In cropping part, detecting bounding box of three images (shape `1500, 1038, 1376`) takes `6m16s`. Applying bb takes `15s`.  
- A notable thing is caiman requires same size if multiple images are passed in. Generate cropped results on multiple input will require cropping to do them at the same time instead of pipeline.
## In this project, we provide several ways for you to run the pipeline:  
1. You can directly run it on Google Colab [here](https://colab.research.google.com/drive/1BvHYZRoOla47MwVeV5_0H2-Vko1nm9yW?usp=sharing). See [Colab Instructions](#part-i-running-on-colab) to run it within Colab.  
2. You can run it using our Docker container [still during testing].
3. You can manually install all the dependencies to manually run it and further develop on it. See [Instructions on local](#part-iii-running-locally) for a detailed explanation.  
## Part I. Running on Colab
You will need to follow the link [here](https://colab.research.google.com/drive/1BvHYZRoOla47MwVeV5_0H2-Vko1nm9yW?usp=sharing) to our Colab notebook. Note that our Colab notebook is lightweight, free to go. Prior to run the pipeline on Colab, you should have your input files located in your Google Drive. At the beginning of the notebook, we will ask you for permissions to mount your Google Drive on Google Colab runtime.  
## Part II. Running on Docker  
TODO
## Part III. Running locally  
### 1. Check System Requirement  
It has been tested stable on Windows 10 and Linux.  
### 2. Create & Setup a new Python environment from Conda for this project.  
Note:  
- If you don't have `anaconda` (recommended) installed, You should get started by [here](https://www.anaconda.com/), and then get back to this readme file.  
- You can change your environment name by replacing `[env_name]` with your specified environment name when executing following commands.
- If you encounter any issues regarding installing `pyimagej`, `scpjava`, `xarray`, or any other ImageJ-related dependencies, please refer [pyimagej GitHub](https://github.com/imagej/pyimagej#readme) for help.
- There are in total of `#TODO` parts of dependencies need to be installed for complete execution of the pipeline: Auto-cropping, ImageJ-Stabilizer, caiman-related, and other general libraries regarding peak-caller.

1. Create environment using conda and mamba
2. Install Auto-cropping dependencies
3. Install ImageJ-related dependencies
4. Install caiman-related dependencies
5. Install peak-caller dependencies

```bash
# Once conda is intalled, you should install mamba to have a faster install time.
conda install mamba -n base -c conda-forge
mamba create -n [env_name] -c conda-forge \
    pyimagej \
    openjdk=8 \
    opencv \
    seaborn
conda activate [env_name]
```

### 3. Install Fiji ImageJ to local and add headless stabilizer plugin to ImageJ
- Download lastest fiji ImageJ [here](https://imagej.net/software/fiji/downloads) to your local computer.  
- After successfully installing Fiji ImageJ, download the compiled plugin file, [Image_Stabilizer_Headless.class](https://github.com/CanYing0913/CalmAn/raw/master/resource/Image_Stabilizer_Headless.class), and move it under ImageJ folder: `Fiji.app/plugins/Examples`.

### 4. Ways to run locally  
There are 2 ways for you to run the pipeline. An interactive way is to leverage Jupyter Notebook to customize IO, parameters, etc. Another "headless" way is to use Python script. While there is no difference between them, using Jupyter Notebook better visualize the intermediate and results for better quality control purposes. Python scripts provide a "one-click" automation.  
#### 4.a. Running in Jupyter Notebook  
To run the pipeline in Jupyter Notebook, open Anaconda Prompt, and type the following commands to activate your created environment and open notebook:
```
conda activate [env_name]
jupyter notebook
```
Navigate to the ipynb file of the pipeline, `main.ipynb` and open it.  
#### 4.b. Running from commandline or IDEs  
To run the pipeline as a script, you can directly use the script, `main.py` as a command-line script, or run it within any IDE (e.g. [PyCharm](https://www.jetbrains.com/pycharm/))  
### 5. Running the pipeline  
For both notebook and script, you should either modify the following parameters or pass parameters as arguments to the script:  
```
work_dir: str, the path to a folder where most of results get stored. (not used in Jupyter Notebook)
app_path: str, the path to local installation of Fiji ImageJ, fiji.app
#TODO

```
