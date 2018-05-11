

all:
		docker build -t dev .

run:
	docker run -p 8000:8000 dev
