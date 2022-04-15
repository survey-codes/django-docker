init:
	test -n "$(name)"
	rm -rf ./.git
	find ./ -type f -exec perl -pi -e 's/project_name/$(name)/g' *.* {} \;
	mv ./project_name ./$(name)

superuser:
	docker exec -it project_name-web ./manage.py createsuperuser

bash:
	docker exec -it project_name-web bash

shell:
	docker exec -it project_name-web ./manage.py shell

makemigrations:
	docker exec -it project_name-web ./manage.py makemigrations

migrate:
	docker exec -it project_name-web ./manage.py migrate

test:
	docker exec -it project_name-web ./manage.py test

statics:
	docker exec -it project_name-web ./manage.py collectstatic --noinput

makemessages:
	docker exec -it project_name-web django-admin makemessages

compilemessages:
	docker exec -it project_name-web django-admin compilemessages
