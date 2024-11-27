import pandas as pd

def remove_duplicatas(arquivo, coluna):
    df = pd.read_excel(arquivo)
    exceptions = df[df[coluna]==1]
    df_restante = df[df[coluna] != 1].drop_duplicates(subset=coluna)   
    df_final = pd.concat([exceptions, df_restante], ignore_index=True)
    return df_final