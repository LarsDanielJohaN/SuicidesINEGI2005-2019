#Code by: Lars Daniel Johansson Nino, economics undergrad from Instituto Tecnologico Autonomo de Mexico ITAM
#Date: March 2022
#Purpose: To create a data base with selected observations on deaths by suicide from INEGIs defunctions registry
import pandas as pd
from simpledbf import Dbf5
import csv
def main():
    columnsFin = ['ENT_REGIS', 'MUN_REGIS', 'ENT_RESID', 'MUN_RESID','TLOC_RESID', 'LOC_RESID','ENT_OCURR','MUN_OCURR','TLOC_OCURR','LOC_OCURR','CAUSA_DEF','LISTA_MEX','SEXO','EDAD','DIA_OCURR','MES_OCURR','ANIO_REGIS','DIA_NACIM','MES_NACIM',
    'ANIO_NACIM','OCUPACION','ESCOLARIDA','EDO_CIVIL','PRESUNTO','OCURR_TRAB','LUGAR_OCUR','NECROPSIA','ASIST_MEDI','SITIO_OCUR','COND_CERT','NACIONALID','DERECHOHAB','EMBARAZO','REL_EMBA','HORAS','MINUTOS','CAPITULO','GRUPO','LISTA1',
    'GR_LISMEX', 'VIO_FAMI', 'AREA_UR', 'EDAD_AGRU','COMPLICARO','DIA_CERT','MES_CERT','ANIO_CERT','MATERNAS','DIS_RE_OAX']
    datafinal = pd.DataFrame(columns = columnsFin)
    param = '54'
    csv_path = r'\Users\Dani Johansson\Desktop\DATA N RESEARCH\SyD\DATA20052019SUIC.csv'

    for i in range(5,20):
        print("Gathering data for year: ",i)
        temp = dbfreader(i,param,datafinal,columnsFin)
        datafinal = temp
        print("Done for year: ",i," Current observations: ",len(datafinal))
    datafinal.to_csv(csv_path)
    print("Done")

def dbfreader(value,param,datafinal,columnsFin):
    if value < 10:
        vas = '0'+str(value)
    else:
        vas = str(value)
    folder1= 'd20'+vas
    file = 'DEFUN'+str(vas)+'.dbf'
    root01= rf"\Users\Dani Johansson\Desktop\DATA N RESEARCH\SyD\DefuncionesINEGI\{folder1}\{file}"
    root = str(root01)
    dbf = Dbf5(root)
    df = dbf.to_dataframe()
    datafinal = pd.concat([datafinal, df[df.LISTA_MEX == '54'] ], ignore_index = True)

    return datafinal
main()
