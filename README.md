# Thepeer Python SDK

![GitHub issues](https://img.shields.io/github/issues/Emmarex/thepeer-sdk-python)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/thepeer-sdk)
![PyPI](https://img.shields.io/pypi/v/thepeer-sdk)
![PyPI - Downloads](https://img.shields.io/pypi/dm/thepeer-sdk)
![PyPI - License](https://img.shields.io/pypi/l/thepeer-sdk)
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
    : Index a particular user on Thepeer

    **parameters**:
    - name(str)
    - identifier(str)
    : unique user identifier
    - email(str)

    **returns**: dict

- list_users
    : Get the list of all indexed users

    **parameters**:
    - page(int)
    : page number to return
    - perPage(int)
    : amount of records to return per page

    **returns**: dict

- update_user
    : Update your user's identifier when they make a profile update to their identifier on your platform.

    **parameters**:
    - user_ref(str)
    : the reference returned when the user was indexed
    - user_identifier(str)
    : unique user identifier

    **returns**: dict

- delete_user
    : Delete a user in the event that a user deactivates their account on your platform

    **parameters**:
    - user_ref(str)
    : the reference returned when the user was indexed

    **returns**: dict

#### Link
- get_user_links
    : This returns all linked accounts associated with a user.

    **parameters**:
    - user_ref(str)
    : the reference returned when the user was indexed

    **returns**: dict

- get_link
    : Get a linked account details

    **parameters**:
    - link_id(str)
    : link ID

    **returns**: dict

#### Send
- verify_receipt
    : Verify a particular receipt.

    **parameters**:
    - receipt_ref(str)
    : reference of the receipt to process

    **returns**: dict

- process_receipt
    : Process receipts generated from Thepeer inline.

    **parameters**:
    - receipt_ref(str)
    : reference of the receipt to process
    - event(str)

    **returns**: dict

#### Direct Charge
- charge_link
    : Charge your user's linked account at any time

    **parameters**:
    - link_id(str)
    : id of the link to charge
    - amount(int)
    : amount to charge
    - remark(str)
    : narration of the charge

    **returns**: dict

- authorize_charge
    : authorize direct charge request via webhooks

    **parameters**:
    - charge_ref(str)
    : direct charge reference
    - event(str)

    **returns**: dict

## Upgrade

```bash
pip install --upgrade thepeer-sdk
```

## Extra

Visit the official [Thepeer documentation](https://docs.thepeer.co/) for more information.


## License
See LICENSE.
