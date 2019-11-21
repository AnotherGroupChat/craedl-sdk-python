# Copyright 2019 The Johns Hopkins University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

class CraedlException(Exception):
    """Base exception that all other exceptions should inherit from."""
    def __init__(self):
        self.message = "Craedl Error."

    def __str__(self):
        return self.message

class Connection_Refused_Error(CraedlException):
    def __init__(self):
        self.message = 'Failed to establish a connection to https://api.craedl.org.'

class Invalid_Token_Error(CraedlException):
    def __init__(self):
        self.message = 'Your configured authentication token is invalid.\n'
        self.message += '  Use `python -m craedl` to configure your authentication token.'

class Missing_Token_Error(CraedlException):
    def __init__(self):
        self.message = 'You have not configured an authentication token.\n'
        self.message += '  Use `python -m craedl` to configure your authentication token.'

class Not_Found_Error(CraedlException):
    def __init__(self):
        self.message = 'The requested resource was not found.'

class Other_Error(CraedlException):
    def __init__(self):
        self.message = 'New error encountered. Determine the response error code and create a new error class.'

class Parse_Error(CraedlException):
    def __init__(self, details=None):
        self.message = 'Your request included invalid parameters.'
        self.details = details

    def __str__(self):
        return self.message + ' ' + self.details

class File_Error(CraedlException):
    def __init__(self, details=None):
        self.message = 'Cannot upload an empty file.'
        self.details = details

    def __str__(self):
        return self.message + ' file: ' + self.details

class Server_Error(CraedlException):
    def __init__(self, details=None):
        self.message = 'The server at https://api.craedl.org has encountered an error.'

class Unauthorized_Error(CraedlException):
    def __init__(self):
        self.message = 'You are not authorized to access the requested resource.'
