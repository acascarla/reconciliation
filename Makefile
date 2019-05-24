run:
	docker-compose up

migrate:
	docker-compose exec django python manage.py migrate

createsuperuser:
	docker-compose run --rm django \
		bash -c "echo \"from django.contrib.auth import get_user_model; \
		get_user_model().objects.create_superuser('admin', 'admin@example.com', 'admin')\" \
		| python manage.py shell"

init: migrate createsuperuser

import:
	docker-compose exec django python manage.py import_works_metadata
