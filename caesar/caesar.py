import time

SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя,.:_-?!@" '
SYMBOLS_DICT = {ch: i for i, ch in enumerate(SYMBOLS)}
MAX_KEY_SIZE = len(SYMBOLS)
MODE_ENCODE = 1
MODE_DECODE = 2
def getMode():
	while True:
		print('Зашифровать или расшифровать?')
		mode = input().lower()
		if mode in ['зашифровать', 'з', '1']:
			return MODE_ENCODE
		elif mode in ['расшифровать', 'р', '2']:
			return MODE_DECODE
		else:
			print('Значение должно быть расшифровать, р или 2 для расшифровки и зашифровать, з или 1 соответственно.')

def getKey():
	key = 0
	while True:
		print('Введите ключ шифрования (1-%s)' % (MAX_KEY_SIZE-1))
		try:
			key = int(input())
		except ValueError:
			print('Ожидаются цифры')
			continue
		if key >= 1 and key < MAX_KEY_SIZE:
			return key

def getMessage():
	while True:
		print('Введите сообщение')
		message = input()
		if set(message)-set(SYMBOLS):
			print('Неподдерживаемые символы')
			time.sleep(3)
			print('Поддержи символы объятием')
		else:
			return message
def getTranslatedMessage(mode, message, key):
	if mode == MODE_DECODE:
		key = -key
	translated = ''

	for s in message:
		sIndex = SYMBOLS_DICT[s]
		if sIndex == -1:
			translated += s
		else:
			sIndex += key + len(SYMBOLS)
			sIndex %= len(SYMBOLS)
			
#			if sIndex >= len(SYMBOLS):
#				sIndex -= len(SYMBOLS)
#			elif sIndex < 0:
#				sIndex += len(SYMBOLS)

			translated  += SYMBOLS[sIndex]
	return translated

if __name__ == '__main__':
	mode = getMode()
	key = getKey()
	message = getMessage()


	print('Преобразованный текст: ' + getTranslatedMessage(mode, message, key))


