import psutil
from time import sleep

interval = 5

def main():
    period_min = int(input("Insira o período de tempo da verificação (em minutos): "))
    while period_min <= 0:
        period_min = int(input("Insira um número valido!! (maior que 0): "))
    
    period = period_min * 60
    exec_times = period/interval

    for i in exec_times:
        sleep(interval)
        # cpu_report
        # ram_report
        # disk_report
        # top_process
        # summary_table
        # generate_csv

        print("\n" + "="*10)
        print("Verificação concluída!")
        print("\n" + "="*10)


if __name__ == "__main__":
    main()