# CLI modifications to Craedl-SDK

## Installation

Clone the project and run `pip install --user --upgrade .` int the project folder.

## Usage:

### Upload:
```craedl source project:destination```

### Download
```craedl project:destination source```

### Download a specific version
```craedl project:destination@123 source```

### Use a particular group
```craedl project:destination@123 source --group=group```

### Configuration
configure the tool in `.config/Craedl/craedl.yml`
```
token: your-api-token
group: default-group
```
You can leave group blank and specify with the command if you want. No group will use your profile's projects.

## TODO:
Implement local caching like from official repository

---

# Previous Readme

## Craedl Python SDK

The Craedl Python SDK (Software Development Kit) enables Craedl users to access
their [Craedl](https://craedl.org) accounts using the Python programming
language. This provides a mechanism for using Craedl on computers without access
to a web browser (such as a high-performance computing cluster) and to automate
common Craedl project manipulations (such as file uploads and downloads) within
a Python script.

### Quick start

Get started with the Craedl Python SDK by obtaining it via
[PyPI](https://pypi.org/project/craedl/):

```
pip install craedl
```

Log into your Craedl account at [Craedl.org](https://craedl.org) and generate an API access token by
clicking the key icon in the `My Craedl` card. Copy your token and paste it when
prompted after running the following command:

```
python -m craedl
```

Now you can use Python to access your Craedl, for example:

```
import craedl
profile = craedl.auth()
for project in profile.get_projects():
    print(project.name)
```

### More information

For more information about the Craedl Python SDK, refer to
[our documentation](https://craedl-sdk-python.readthedocs.io). The source code
is hosted on [GitHub](https://github.com/craedl/craedl-sdk-python).
