#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 17:43:23 2025

@author: alexandermikhailov
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

DATA_DIR = BASE_DIR.joinpath('data')

ARCHIVE_NAME_UTILISED = 'dataset_rus_m1.zip'

FILE_NAME_UTILISED = 'dataset_rus_grigoriev_v.csv'
