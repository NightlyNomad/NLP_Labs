import pandas as pd
frame = pd.read_csv(r'C:\Users\NIGHT\Desktop\NLP\lr2\bigramm_count.csv')

bigramm = frame['N-gramm'].to_list()
line = bigramm[0]
while True:
    second_word= line.split(' ')[-1]
    try:
        second_phrase = [el for el in bigramm if el.split(' ')[0] == second_word][0]
    except:
        break
    bigramm.remove(second_phrase)
    line += f" {second_phrase.split(' ')[-1]}"
print(line)
print(len(line.split(' ')))