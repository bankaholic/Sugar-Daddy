# SPDX-License-Identifier: BUSL-1.1
import os

from brownie import accounts, VeSugar, LpSugar


def main():
    contract_name = str(os.getenv('CONTRACT')).lower()

    if os.getenv('PROD'):
        account = accounts.load('sugar')
    else:
        account = accounts[0]

    if 'lp' in contract_name:
        LpSugar.deploy(
            os.getenv('VOTER_ADDRESS'),
            os.getenv('REGISTRY_ADDRESS'),
            os.getenv('CONVERTOR_ADDRESS'),
            {'from': account}
        )

    if 've' in contract_name:
        VeSugar.deploy(
            os.getenv('VOTER_ADDRESS'),
            os.getenv('DIST_ADDRESS'),
            {'from': account}
        )

    if 've' not in contract_name and 'lp' not in contract_name:
        print('Set the `CONTRACT` environment variable to deploy a contract.')
