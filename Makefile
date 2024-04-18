start-cvat:
	cd cvat && CVAT_HOST=localhost sudo docker compose up -d

stop-cvat:
	cd cvat && CVAT_HOST=localhost sudo docker compose down