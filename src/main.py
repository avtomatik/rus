# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 21:04:02 2019

@author: Alexander Mikhailov
"""


from core.classes import Token
from core.funcs import plot_rus_grigoriev, plot_rus_is_lm, read

if __name__ == '__main__':
    read(Token.RUS_GRIGORIEV).sort_index().pipe(plot_rus_grigoriev)
    read(Token.RUS_IS_LM).pipe(plot_rus_is_lm)
