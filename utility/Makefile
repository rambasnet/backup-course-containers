
.PHONY: all
all: test clean
	@echo "All done!"

.PHONY: test
test:
	@echo "Running tests..."
	pytest -v .

.PHONY: clean
clean:
	rm -rf __pycache__ .pytest_cache
