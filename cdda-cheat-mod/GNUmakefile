cheat.json: %.json: %.json.in
	grep -vE '^[[:space:]]*(//|$$)' <$< | jq . >/dev/null
	grep -vE '^[[:space:]]*(//|$$)' <$< | jq . >$@
