
#   CLI tool to generate new csv with SHA256 encryption

This project is a CLI tool that takes in a `.csv` file as input and returns a new `.csv` file with a column conttaining the `sha256` encryption of a CHIP-0007 compatible json generated for each row in the input csv. The generated csv is saved as `filename.output.csv` where `filename` is the name of the input csv
## Installation

To run this project, python needs to be installed. Python 3.9.2 can be downloaded [here](https://www.python.org/downloads/release/python-392/)

    
## Run Locally

Clone the project

```bash
  git clone https://github.com/datalordstephen/HNG-sha256.git
```

Go to the project directory

```bash
  cd HNG-sha256
```

Run the script

```bash
  py script.py
```


## Appendix
This project was created in the backend track, stage 2 of the `HNG-i9` internship.

