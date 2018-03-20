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


class OutputFile(Model):
    """Represent an output file.

    :param track_labels: Gets the track labels.
    :type track_labels: list[str]
    """

    _attribute_map = {
        'track_labels': {'key': 'trackLabels', 'type': '[str]'},
    }

    def __init__(self, track_labels=None):
        super(OutputFile, self).__init__()
        self.track_labels = track_labels