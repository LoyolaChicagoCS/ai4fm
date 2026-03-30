build:
	git describe --tags --abbrev=0 | tail -n 1 | xargs -I % uv version %
	rm -rf dist/
	rm -rf build/
	sphinx-build -vvv --write-all --fresh-env src build

create-dev:
	pre-commit install
	pre-commit autoupdate
	uv sync
	uv build

serve:
	sphinx-autobuild src build

clean:
	rm -rf build/
