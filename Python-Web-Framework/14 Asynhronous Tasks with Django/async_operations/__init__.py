from .celery import app as celery_app

__all__ = ('celery_app',)

# 1. install celery
# 2. register celery in INSTALLED_APPS
# 3. set BROKER_URL
# 4. Create celery.py
# 5. projects '__init__.py' register **celery**
# 6. create 'shared_task's
