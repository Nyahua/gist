## conda tips
### [creating environment in `conda`](https://conda.io/docs/user-guide/tasks/manage-environments.html)
1. To create an environment:
```bash
conda create --name myenv
```
2. Activating an environment:
```bash
activate myenv # windows
source activate myenv # linux
```
3. Deactivating an environment
```bash
deactivate # windows
source deactivate # linux
```
4. Viewing a list of your environments
```bash
conda info --envs
```
OR
```bash
conda env list
```

5. Removing an environment

```bash
conda remove --name myenv --all
```
You may instead use 
```bash
conda env remove --name myenv.
```


### [set local mirror](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
```bash
conda config --add channels https://mirrors.cloud.tencent.com/anaconda/pkgs/free/
conda config --add channels https://mirrors.cloud.tencent.com/anaconda/pkgs/main/
conda config --set show_channel_urls yes
# Conda Forge
conda config --add channels https://mirrors.cloud.tencent.com/anaconda/cloud/conda-forge/

```

## [jupyter configuration](https://jupyter-notebook.readthedocs.io/en/stable/config_overview.html)
### Configuring the Notebook server
To create a jupyter_notebook_config.py file, with all the defaults commented out, you can use the following command line:
```sh
$ jupyter notebook --generate-config
```

### Specify what command to use to invoke a web browser when opening the notebook
```python
## Specify what command to use to invoke a web browser when opening the notebook.
#  If not specified, the default browser will be determined by the `webbrowser`
#  standard library module, which allows setting of the BROWSER environment
#  variable to override it.
#c.NotebookApp.browser = ''
import webbrowser
webbrowser.register('chrome', None, webbrowser.GenericBrowser( r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
c.NotebookApp.browser = 'chrome'
```

### [Change Jupyter Notebook startup folder (Windows)](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html#change-jupyter-notebook-startup-folder-windows)

- Copy the Jupyter Notebook launcher from the menu to the desktop.
- Right click on the new launcher and change the Target field, change `%USERPROFILE%` to the full path of the folder which will contain all the notebooks.
- Double-click on the Jupyter Notebook desktop launcher (icon shows [IPy]) to start the Jupyter Notebook App. The notebook interface will appear in a new browser window or tab. A secondary terminal window (used only for error logging and for shut down) will be also opened.


###  list all of the possible locations for everything it uses to run: kernels, extensions, pidfiles, etc.
```sh
jupyter --paths
```

### [Install TensorFlow in Anaconda](https://www.anaconda.com/tensorflow-in-anaconda/)
```bash
conda create -n tensorflow_env tensorflow
conda activate tensorflow_env
```
