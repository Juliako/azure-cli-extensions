# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SubscriptionMediaServiceCollection(Model):
    """A collection of Media Services accounts.

    :param value: A collection of Media Services accounts.
    :type value: list[~accounts.models.SubscriptionMediaService]
    :param odatanext_link: A link to the next page of the collection (when the
     collection contains too many results to return in one response).
    :type odatanext_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SubscriptionMediaService]'},
        'odatanext_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(self, value=None, odatanext_link=None):
        super(SubscriptionMediaServiceCollection, self).__init__()
        self.value = value
        self.odatanext_link = odatanext_link
