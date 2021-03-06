# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class Disk(Model):
    """A Disk.

    :param disk_type: The storage type for the disk (i.e. Standard, Premium).
     Possible values include: 'Standard', 'Premium'
    :type disk_type: str or :class:`StorageType
     <azure.mgmt.devtestlabs.models.StorageType>`
    :param disk_size_gi_b: The size of the disk in GibiBytes.
    :type disk_size_gi_b: int
    :param leased_by_lab_vm_id: The resource ID of the VM to which this disk
     is leased.
    :type leased_by_lab_vm_id: str
    :param disk_blob_name: When backed by a blob, the name of the VHD blob
     without extension.
    :type disk_blob_name: str
    :param disk_uri: When backed by a blob, the URI of underlying blob.
    :type disk_uri: str
    :param created_date: The creation date of the disk.
    :type created_date: datetime
    :param host_caching: The host caching policy of the disk (i.e. None,
     ReadOnly, ReadWrite).
    :type host_caching: str
    :param managed_disk_id: When backed by managed disk, this is the ID of the
     compute disk resource.
    :type managed_disk_id: str
    :param provisioning_state: The provisioning status of the resource.
    :type provisioning_state: str
    :param unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :type unique_identifier: str
    :param id: The identifier of the resource.
    :type id: str
    :param name: The name of the resource.
    :type name: str
    :param type: The type of the resource.
    :type type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    """

    _attribute_map = {
        'disk_type': {'key': 'properties.diskType', 'type': 'str'},
        'disk_size_gi_b': {'key': 'properties.diskSizeGiB', 'type': 'int'},
        'leased_by_lab_vm_id': {'key': 'properties.leasedByLabVmId', 'type': 'str'},
        'disk_blob_name': {'key': 'properties.diskBlobName', 'type': 'str'},
        'disk_uri': {'key': 'properties.diskUri', 'type': 'str'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'host_caching': {'key': 'properties.hostCaching', 'type': 'str'},
        'managed_disk_id': {'key': 'properties.managedDiskId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, disk_type=None, disk_size_gi_b=None, leased_by_lab_vm_id=None, disk_blob_name=None, disk_uri=None, created_date=None, host_caching=None, managed_disk_id=None, provisioning_state=None, unique_identifier=None, id=None, name=None, type=None, location=None, tags=None):
        self.disk_type = disk_type
        self.disk_size_gi_b = disk_size_gi_b
        self.leased_by_lab_vm_id = leased_by_lab_vm_id
        self.disk_blob_name = disk_blob_name
        self.disk_uri = disk_uri
        self.created_date = created_date
        self.host_caching = host_caching
        self.managed_disk_id = managed_disk_id
        self.provisioning_state = provisioning_state
        self.unique_identifier = unique_identifier
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.tags = tags
