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

import getpass
import os
import stat
import sys
import hydra

def create_default(token_path):
    argv = sys.argv

    if len(argv) > 1 and not os.path.exists(os.path.dirname(token_path)):
        sys.exit(
            'craedl-token configures your Craedl authentication token, which you can obtain\n'
            'from your Craedl account. Visit https://craedl.org/docs#api-access for more information.'
        )

    token = getpass.getpass('Enter your token: ')

    if len(token) != 40:
        sys.exit('The provided token is invalid.')

    if not os.path.exists(os.path.dirname(token_path)):
        os.makedirs(os.path.dirname(token_path))

    f = open(token_path, 'w+')
    f.write(f"token: {token}")
    f.close()

    os.chmod(token_path, stat.S_IREAD | stat.S_IWRITE)


def default_path():
    if sys.platform == 'win32':
        token_path = os.path.abspath(
            os.path.join(os.sep, 'Users', os.getlogin(), 'AppData', 'Local',
                         'Craedl', 'craedl.yml'))
    elif sys.platform == 'darwin':
        token_path = os.path.abspath(
            os.path.join(os.sep, 'Users', os.getlogin(), 'Library',
                         'Preferences', 'Craedl', 'craedl.yml'))
    else:
        token_path = os.path.expanduser('~/.config/Craedl/craedl.yml')

    # Set up default config if one does not exist
    if not os.path.exists(token_path):
        create_default(token_path)

    return token_path


TOKEN_PATH = default_path()


@hydra.main(config_path=TOKEN_PATH)
def craedl(cfg, project=None, folder="/home", upload=None):
    """
    The ``craedl-token`` console script entry point for configuring the Craedl
    authentication token.
    """
    print(cfg)
    print(cfg.token)


if __name__ == "__main__":
    craedl()
