from setuptools import setup  # noqa: D100

setup(
    name="download_tools",
    version="0.0.1",
    packages=["download_tools", "download_tools.plugins"],
    url="",
    license="",
    author="Rationality Enhancement Group",
    author_email="",
    description="",
    install_requires=[
        "numpy",
        "pandas<2.0",
        # https://stackoverflow.com/a/75316945
        "sqlalchemy<=1.4",
        "python-dotenv",
        "psycopg2-binary",
        "dill",
    ],
)
