# Object-Detection-on-Raspberry-Pi-5
Stray dog detection systems can help improve public safety by alerting authorities or concerned citizens about the presence of stray dogs in specific areas.
This project can aid in better animal control measures, reducing the risk of dog bites, and potentially improving the overall well-being of both humans and stray dogs and importantly also educates on deployment of ml models on resource constrained devices such as the Raspberry Pi

## Download Dataset
Note: The best.pt trained yolon11 model has already been provided along with the Jupyter notebook comprising the code for how to train the model
You can download the dataset for this project from the following link if you wish to train the model yourself:

https://universe.roboflow.com/majalberkane/dog_detection_drone/browse?queryText=&pageSize=200&startingIndex=0&browseQuery=true

 
## Running Code on Pi by typing the following on the Pi CMD:
* Activate the virtual environment by writing the following command:
  ```bash
  workon pyt
  ```
* Write the next command to run the python script
  ```bash
  python Stray_Detection.py
  ```

## Create virtual environment to install dependencies by writing the following commands in Raspberry Pi CMD:
Running an object detection script within a virtual environment on a Raspberry Pi is essential for isolating project dependencies, ensuring consistent behavior across environments, and maintaining a clean system by preventing conflicts with other projects or the system-wide Python installation.

```bash
sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.old
```
```bash
python3 --version
```
```bash
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python" >> ~/.bashrc
```
```bash
source ~/.bashrc
```
```bash
sudo apt-get install python3-virtualenv
```
```bash
sudo apt-get install python3-virtualenvwrapper
```
```bash
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
```
```bash
echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc
```
```bash
source ~/.bashrc
```
