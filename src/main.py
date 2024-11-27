import pandas as pd
import geracao

def main():
    g = geracao.Geracao(['input/exemplo.xlsx'])
    df = g.primeiro_passo('MATRICULA')
    df.to_excel('output/no_duplicates.xlsx', index=False)

if __name__ == '__main__':
    main()