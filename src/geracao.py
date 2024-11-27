from typing import List
import pandas as pd
import remover_duplicatas as rd

class Geracao:
    def __init__(self, files:List[str]) -> None:
        self.files = files


    def primeiro_passo(self, coluna:str):
        return rd.remove_duplicatas(self.files[0], coluna)
        
    


