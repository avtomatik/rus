#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 11:59:12 2023

@author: green-machine
"""

from pathlib import Path

from core.classes import Token

ARCHIVE_NAME_UTILISED = 'dataset_rus_m1.zip'

FILE_NAME_UTILISED = 'dataset_rus_grigoriev_v.csv'

MAP_KWARGS = {
    Token.RUS_GRIGORIEV: {
        'filepath_or_buffer': Path(__file__).parent.parent.parent.joinpath('data').joinpath(FILE_NAME_UTILISED),
        'index_col': 1,
        'usecols': range(2, 5)
    },
    Token.RUS_IS_LM: {
        'filepath_or_buffer': Path(__file__).parent.parent.parent.joinpath('data').joinpath(ARCHIVE_NAME_UTILISED),
        'names': ('period', 'prime_rate', 'm1'),
        'index_col': 0,
        'skiprows': 1,
        'parse_dates': True
    }
}
