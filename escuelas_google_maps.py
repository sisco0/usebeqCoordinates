# Find Google Maps locations from Workcenter keys

import argparse
import pandas as pd
import requests
import numpy as np
from lxml import html
import time

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Google Maps Solver!')
    parser.add_argument(
            '--input',
            dest='input')
    args = parser.parse_args()
    df = pd.read_csv(args.input,
            dtype={
                'clave': str,
                'lat': np.float64,
                'long': np.float64})
    for index, row in df.iterrows():
        # For each row make a request and obtain coordinates
        page = requests.get(
                'https://escuelasmex.com/directorio/{}'.format(
                    df.loc[index, 'clave']))
        tree = html.fromstring(page.content)
        try:
            coord_string = tree.xpath('//html/body/div[1]/div[2]/p[3]/text()[last()]')[0]
            coord_string = coord_string.strip()
            coords = coord_string.split(', ')
            df.loc[index, 'lat'] = float(coords[0])
            df.loc[index, 'long'] = float(coords[1])
        except Exception:
            print('Could not obtain coordinates for: {}'.format(
                    df.loc[index, 'clave']))
    print(df)
