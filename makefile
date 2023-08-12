
install:
	python3.10 -m virtualenv .venv && \
	source .venv/bin/activate && \
	.venv/bin/pip3 install --upgrade pip && \
	.venv/bin/pip3 install -r requirements.txt

clean:
	rm -rf .venv/

format:

lint:

test:
