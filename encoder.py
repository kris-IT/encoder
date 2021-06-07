#!/usr/bin/python
# -*- coding: utf-8 -*-

# Импортирование функции findall из модуля ‘регулярные выражения’
from re import findall
# Словарь вида → символ_алфавита : 5символов_шифра
keysBacon = {
    'A':"AAAA", 'B':"AAAAB", 'C':"AAABA",
    'D':"AAABB", 'E':"AABAA", 'F':"AABAB",
    'G':"AABBA", 'H':"AABBB", 'I':"ABAAA",
    'J':"ABAAB", 'K':"ABABA", 'L':"ABABB",
    'M':"ABBAA", 'N':"ABBAB", 'O':"ABBBA",
    'P':"ABBBB", 'Q':"BAAAA", 'R':"BAAAB",
    'S':"BAABA", 'T':"BAABB", 'U':"BABAA",
    'V':"BABAB", 'W':"BABBA", 'X':"BABBB",
    'Y':"BBAAA", 'Z':"BBAAB", ' ':"BBABA"
}
# Переключатель шифрования/расшифрования
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit
# Сообщение для шифрования/расшифрования
startMessage = input("Write the message: ").upper()
# Функция регулярного выражения, помогающая расшифровывать сообщение деля
#зашифрованное сообщение по 5 символов.
def regular(text):
      template = r"[A-Z]{5}"
      return findall(template, text)
# Функция с 3 аргументами.
def encryptDecrypt(mode, message, final = ""):
      if mode == 'E': # Если переключатель равен ‘E’, то сделать посимвольный
                      # перебор сообщения
            for symbol in message:
                  if symbol in keysBacon: final += keysBacon[symbol]
      else:
# Если переключатель равен ‘D’, то сделать перебор сообщения
#через регулярное выражение
            for symbolsFive in regular(message):
                  for key in keysBacon:
                        if symbolsFive == keysBacon[key]: final += key
      return final # Вернуть получившееся сообщение
print("Final message:",encryptDecrypt(cryptMode, startMessage))
