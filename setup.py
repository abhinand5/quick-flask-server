import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quick-flask-server",
    version="1.1.2",
    author="Abhinand Balachandran",
    description="Quickly serve your flask apps using ngrok",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhinand5/quick-flask-server.git",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords='flask ngrok server utility',
    install_requires=['Flask>=0.8', 'requests'],
    py_modules=['quick_flask_server']
)
