# -*- coding: utf-8 -*-
"""
    Settings.utils
    ~~~~~~~~~~~~~~

    Esse arquivo possui funções de utilitário para usar em outros arquivos
    do settings.
    Nesse caso temos apenas o LOCAL que é uma função que dado uma caminho de
    arquivo ou diretório X (uma string), ele retorna o caminho completo para
    este.
    Assim, ao usar LOCAL('sqlite.bd'), temos a string que seria algo do tipo:
    '/home/usuario/meusprojetos/esporte-tec/esporte_tec/sqlite.db'

    isso facilita muito, já que para mim o caminho completo para o projeto é um
    e para outros é outro, isso deixa independente, e é gerado na hora em que é carregado
    settings =)


    :copyright: (c) 2013 by arruda.
"""

import os
LOCAL = lambda x: os.path.join(os.path.sep.join(
                os.path.abspath(
                    os.path.dirname(__file__)).split(os.path.sep)[:-1]), x)

