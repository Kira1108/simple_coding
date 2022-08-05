# Python-Coding-Step-By-Step

## Introduction
This repository contains progressivly optimized projects, which will help you to build larger projects.

## Steps
```bash
cd /path/to/simple_coding

# setup a virtual environment
python -m venv venv

# if you have conda environment activated.
conda deactivate

# activate you virtual environment named "venv"
source venv/bin/activate # on linux or mac
./venv/Scripts/activate # on windows

# install dependencies
pip install -r requirements.txt

# you will see an folder named venv appeared
.
├── README.md
├── requirements.txt
├── venv
├── version1
├── version2
├── version3
├── version4
└── version5

# on you terminal you should see something like 
(venv) PS C:\Users\somepath\simple_coding>....
```


## VirtualEnv - Slim version of a python version
```bash
venv
├── Include
├── Lib
│   └── site-packages
├── Scripts
│   ├── Activate.ps1
│   ├── activate
│   ├── activate.bat
│   ├── deactivate.bat
│   ├── easy_install-3.8.exe
│   ├── easy_install.exe
│   ├── f2py.exe
│   ├── fonttools.exe
│   ├── pip.exe                  # you use this pip to install things
│   ├── pip3.8.exe
│   ├── pip3.exe
│   ├── py.test.exe
│   ├── pyftmerge.exe
│   ├── pyftsubset.exe
│   ├── pytest.exe
│   ├── python.exe              # you use this python to run your program
│   ├── pythonw.exe
│   └── ttx.exe
├── etc
│   └── jupyter
├── pyvenv.cfg
└── share
    ├── jupyter
    └── man
```

Ok, that's everything required for virtualenv.


## Benefits of virtualenv
Others can reproduce your environment and dependecies by simply running
```bash
python -m venv venv
activate....
pip install -r requirements.txt
run your program
```

## Inconvinence of virtualenv
No control over OS level dependencies.
install pymc3 - require gcc
install tensorflow-gpu - require cuda, cudnn, nvidia-cuda-toolkit, and all version properly orginized.
plot a <V,E> graph - require graphviz...
```bash
sudo apt install graphgiz
sudo apt-get install gcc
export envrionment_varialble
export envrionment_varialble
export envrionment_varialble
....
....
```
*Still hard to reproduce your environment*



## Start you dev tour
Suppose your boss want you to write code that plot the temerature of london city, you write the following code, present a beautiful matplotlib plot
```python
class App:
    """App read data and plot data"""
    
    def read(self, file_name):
        temperatures_by_hour = {}
        with open(Path(BASE_DIR).joinpath(file_name), 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                hour = datetime.datetime.strptime(row[0], '%d/%m/%Y %H:%M').isoformat()
                temperature = float(row[2])
                temperatures_by_hour[hour] = temperature

        return temperatures_by_hour

    def draw(self, temperatures_by_hour):
        dates = []
        temperatures = []

        for date, temperature in temperatures_by_hour.items():
            dates.append(datetime.datetime.fromisoformat(date))
            temperatures.append(temperature)

        dates = matplotlib.dates.date2num(dates)
        matplotlib.pyplot.plot_date(dates, temperatures, linestyle='-')
        matplotlib.pyplot.show()
```

Someday, your boss says, that plotting tool is fantastic, use that tool to draw another json dataset.    
Then you will have to rewrite the read function to adapt json file format.       
Maybe add some if statement to check the file type, followed by logics on different cases.
Finally, your read function become longer and longer, dealing with mysql, hdf5, json, yaml, txt, xml, csv, parquet handling logics.
