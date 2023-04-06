import time
import pandas as pd


def convert_time_to_more_readable(seconds):
    struct_time = time.gmtime(seconds)
    print("\033[7m {}h:{}m:{}s \033[0m".format(struct_time.tm_hour, struct_time.tm_min, struct_time.tm_sec))


def time_average(values_of_time):
    return sum(values_of_time) / len(values_of_time)


def porcentagem_do_todo(total, parcial):
    total = total[0][0]
    parcial = parcial[0][0]
    
    t = 100/total
    return parcial * t

def percentage_of_time(file_name):
    file_result = "./outputs/time_result/" + file_name
    tempos = pd.read_csv(file_result)

    media = tempos.iloc[-1:, :]

    gn_perc = porcentagem_do_todo(media.iloc[:, 1:2].values, media.iloc[:, 2:3].values)
    gn1_perc = porcentagem_do_todo(media.iloc[:, 1:2].values, media.iloc[:, 3:4].values)
    ot_perc = porcentagem_do_todo(media.iloc[:, 1:2].values, media.iloc[:, 4:5].values)
    op_perc = porcentagem_do_todo(media.iloc[:, 1:2].values, media.iloc[:, 5:6].values)
    
    print(f'função  | tempo (s) | porcentagem (%)')
    print(f'j1      | {media.iloc[:, 1:2].values[0][0]:.3f}    | 100')
    print(f'gn      | {media.iloc[:, 2:3].values[0][0]:.3f}    | {gn_perc:.3f}')
    print(f'gn1     | {media.iloc[:, 3:4].values[0][0]:.3f}    | {gn1_perc:.3f}')
    print(f'ot      | {media.iloc[:, 4:5].values[0][0]:.3f}     | {ot_perc:.3f}')
    print(f'op      | {media.iloc[:, 5:6].values[0][0]:.3f}     | {op_perc:.3f}')