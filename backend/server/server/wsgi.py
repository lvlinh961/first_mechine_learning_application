"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

# ML Registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.income_classifier.extra_trees import ExtraTreesClassifier

try:
	registry = MLRegistry() # create ML registry
	# Random forest classifier
	rf = RandomForestClassifier()
	# add to ML registry
	registry.add_algorithm(
		endpoint_name="income_classifier",
		algorithm_object=rf,
		algorithm_name="random forest",
		algorithm_status="production",
		algorithm_version="0.0.1",
		owner="Piotr",
		algorithm_description="Random Forest with simple pre- and post-processing",
		algorithm_code=inspect.getsource(RandomForestClassifier)
	)

	# Extra trees classifier
	et = ExtraTreesClassifier()
	# add to ML registree
	registry.add_algorithm(
		endpoint_name="income_classifier",
		algorithm_object=et,
		algorithm_name="extra tree",
		algorithm_status="testing",
		algorithm_version="0.0.1",
		owner="Piotr",
		algorithm_description="Random Forest with simple pre- and post-processing",
		algorithm_code=inspect.getsource(ExtraTreesClassifier)
	)
except Exception as e:
	print("Exception while loading the algorithm to the registry,", str(e))