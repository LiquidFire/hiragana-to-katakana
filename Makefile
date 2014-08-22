UNICODE_DATA = UnicodeData.txt
UNICODE_DATA_URL = http://unicode.org/Public/UNIDATA/UnicodeData.txt

MAPPING = hiragana-to-katakana-mapping.js
USER_SCRIPT = hiragana-to-katakana.user.js
USER_SCRIPT_META = hiragana-to-katakana.user.meta.js
USER_SCRIPT_BODY = hiragana-to-katakana.user.body.js

GENERATE_MAPPING = generate_mapping.py

CURL = curl
PYTHON = python
CAT = cat
RM = rm

default: $(USER_SCRIPT)

$(UNICODE_DATA):
	$(CURL) "$(UNICODE_DATA_URL)" -o "$@"

$(MAPPING): $(UNICODE_DATA) $(GENERATE_MAPPING)
	$(PYTHON) $(GENERATE_MAPPING) "$(UNICODE_DATA)" "$@"

$(USER_SCRIPT): $(MAPPING) $(USER_SCRIPT_META) $(USER_SCRIPT_BODY)
	$(CAT) $(USER_SCRIPT_META) $(MAPPING) $(USER_SCRIPT_BODY) > "$@"

clean:
	$(RM) -rf $(UNICODE_DATA) $(MAPPING) $(USER_SCRIPT)
