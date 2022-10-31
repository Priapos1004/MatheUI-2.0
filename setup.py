from setuptools import find_packages, setup

setup(
    name="matheUI_backend",
    version="0.1.0",
    description="little funny games package created by Samuel Brinkmann",
    packages=find_packages(),
    package_data={},
    scripts=[],
    install_requires=[
        "pandas",
        "numpy",
        "tqdm",
    ],
    extras_require={"test": ["pytest", "pylint!=2.5.0"],},
    author="Samuel Brinkmann",
    license="MIT",
    tests_require=["pytest==4.4.1"],
    setup_requires=["pytest-runner"],
)
