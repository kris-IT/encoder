# encoder
encoding and decoding The Bacon Cipher

## Что умеет: умеет шифровать и дешифровать текст.

Здесь используется шифр Бэкона. Шифр Бэкона является шифром замены, который можно представить в виде двоичного кода, где A = 0, B = 1. 
Используется алфавитный метод. Для кодирования сообщений Фрэнсис Бэкон предложил каждую букву текста заменять на группу из пяти символов «A» или «B» (так как последовательностью из пяти двоичных символов можно закодировать 25 = 32 символа, что достаточно для шифрования 26 букв английского алфавита).
Данный код можно запускать с терминала без установок дополнительных программ, библиотек и прочих расширений, что является огромным плюсом и экономит много времени.

Весь код находится в "encoder.py"

## Импортирование функции findall из модуля "регулярные выражения"
from re import findall
## Словарь вида → символ_алфавита : 5символов_шифра
keysBacon = {
    'A':"AAAAA", 'B':"AAAAB", 'C':"AAABA",
    'D':"AAABB", 'E':"AABAA", 'F':"AABAB",
    'G':"AABBA", 'H':"AABBB", 'I':"ABAAA",
    'J':"ABAAB", 'K':"ABABA", 'L':"ABABB",
    'M':"ABBAA", 'N':"ABBAB", 'O':"ABBBA",
    'P':"ABBBB", 'Q':"BAAAA", 'R':"BAAAB",
    'S':"BAABA", 'T':"BAABB", 'U':"BABAA",
    'V':"BABAB", 'W':"BABBA", 'X':"BABBB",
    'Y':"BBAAA", 'Z':"BBAAB", ' ':"BBABA"
}
## Переключатель шифрования/дешифрования
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit
## Сообщение для шифрования/дешифрования
startMessage = input("Write the message: ").upper()
## Есть функция регулярного выражения, помогающая дешифровывать сообщение


