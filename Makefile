test:
	pytest -vv
format:
	black freebilly
format-check:
	black -v --check freebilly
