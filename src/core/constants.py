#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 11:59:12 2023

@author: green-machine
"""

from core.classes import Token
from core.config import ARCHIVE_NAME_UTILISED, DATA_DIR, FILE_NAME_UTILISED

MAP_KWARGS = {
    Token.RUS_GRIGORIEV: {
        'filepath_or_buffer': DATA_DIR.joinpath(FILE_NAME_UTILISED),
        'index_col': 1,
        'usecols': range(2, 5)
    },
    Token.RUS_IS_LM: {
        'filepath_or_buffer': DATA_DIR.joinpath(ARCHIVE_NAME_UTILISED),
        'names': ['period', 'prime_rate', 'm1'],
        'index_col': 0,
        'skiprows': 1,
        'parse_dates': True
    }
}
