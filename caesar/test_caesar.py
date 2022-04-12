import pytest
from caesar import getTranslatedMessage, MODE_ENCODE, MODE_DECODE

@pytest.mark.parametrize('mode, message, key, expected', [
			[MODE_ENCODE, 'абв', 1, 'бвг'], 
			[MODE_DECODE, 'бвг', 1, 'абв'],
			[MODE_ENCODE, '@" ', 1, '" А'],
			[MODE_DECODE, 'АБВ', 1, ' АБ'],
])
def test_1(mode, message, key, expected):
	assert getTranslatedMessage(mode, message, key) == expected

