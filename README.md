# Google Maps Location Extractor (for USEBEQ)

Just launch this application with the given CSV file and would get the
needed coordinates for each workcenter by using the _EscuelasMex_ website.

## Installation

It is recommended to use a Pipenv for this. After activating it, run the
next command to install dependencies:

```bash
pip3 install -r requirements.txt
```

## Usage

For a given `escuelas.csv` input file, the command line is such as this:

```bash
python3 escuelas_google_maps.py --input escuelas.csv
```
