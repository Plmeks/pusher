from setuptools import setup

setup(
    name="test_preconditions",
    version="0.9.1",
    author="ivi.ru",
    description="tools for client check automation preconditions",
    packages=["test_preconditions",
              "test_preconditions.certificate",
              "test_preconditions.content_list_generation",
              "test_preconditions.purchase",
              "test_preconditions.user_creation",
              "test_preconditions.utils",
              "test_preconditions.pusher",
              "test_preconditions.exceptions",
              "test_preconditions.mailcatcher"],
    requires=['requests', 'psycopg2'],
    install_requires=['requests', 'psycopg2'],
)
