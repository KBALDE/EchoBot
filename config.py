#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "2a7366dc-d983-4f54-85b3-804452d4a32c")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", ".N17Q~UC2GJjSHVsnDLpuNGzb-UDvbMATJ_vm")
