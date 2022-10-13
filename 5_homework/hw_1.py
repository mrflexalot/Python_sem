# 38. Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

input_text = input("Type in your text to remove 'абв' words from it:")

def words_delete(input_text):
    input_text = list(filter(lambda x: 'абв' not in x, input_text.split()))
    return " ".join(input_text)

input_text = words_delete(input_text)
print(input_text)