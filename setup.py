from setuptools import setup

VERSION = "0.4"

setup(
    name="datasette-plugin-demos",
    description="Examples of plugins for Datasette",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-plugin-demos",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_plugin_demos"],
    entry_points={"datasette": ["plugin_demos = datasette_plugin_demos"]},
    package_data={
        "datasette_plugin_demos": ["static/plugin.js", "templates/show_json.html"],
    },
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio", "httpx"]},
    tests_require=["datasette-plugin-demos[test]"],
)
