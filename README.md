# Thepeer Python SDK

![GitHub issues](https://img.shields.io/github/issues/Emmarex/thepeer-sdk-python)
![PyPI - Downloads](https://img.shields.io/pypi/dm/thepeer-sdk)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Python SDK for [Thepeer](https://thepeer.co/).

## Quick Start

1. Install thepeer-sdk

```bash
pip install thepeer-sdk
```

2. Signup to get your API keys [here](https://dashboard.thepeer.co/login)

## Usage


### Initiate
```python
from thepeer_sdk import ThepeerSdkClient

thepeer_sdk_client = ThepeerSdkClient(
    secret_key="SECRET_KEY_GOES_HERE"
)

# Get the list of all indexed users
thepeer_sdk_client.list_users()
```

### Available Methods
#### User
- index_user
- list_users
- update_user
- delete_user

## Upgrade

```bash
pip install --upgrade thepeer-sdk
```

## Extra

Visit the official [Thepeer documentation](https://docs.thepeer.co/) for more information.


## License
See LICENSE.
