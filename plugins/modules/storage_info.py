#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, annotations, division, print_function


DOCUMENTATION = r"""
module: storage_info
author: WaitingAtTheCrossroads (@WaitingAtTheCrossroads)
version_added: "1.0.0"
short_description: Get storage info from Proxmox Virtual Environment.
description:
  - >-
      This module uses proxmoxer to get storage information from Proxmox
      Virtual Environment.
options:
  storage:
    description:
      - The storage identifier (storage ID).
      - Mutually exclusive with O(type).
    type: str
  type:
    description:
      - Only list storage of specific type.
      - Mutually exclusive with O(storage).
    type: str
    choices:
      - btrfs
      - cephfs
      - cifs
      - dir
      - esxi
      - glusterfs
      - iscsi
      - iscsidirect
      - lvm
      - lvmthin
      - nfs
      - pbs
      - rbd
      - zfs
      - zfspool
seealso:
  - module: community.general.proxmox_storage_info
extends_documentation_fragment:
  - waitingatthecrossroads.proxmox_virtual_environment.api
  - waitingatthecrossroads.proxmox_virtual_environment.common
  - waitingatthecrossroads.proxmox_virtual_environment.common.info
"""

EXAMPLES = r"""
- name: List existing storages
  waitingatthecrossroads.proxmox_virtual_environment.storage_info:
    api_host: crossroads
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
  register: storages

- name: List NFS storages only
  waitingatthecrossroads.proxmox_virtual_environment.storage_info:
    api_host: crossroads
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
    type: nfs
  register: storages_nfs

- name: Retrieve information about the lvm2 storage
  waitingatthecrossroads.proxmox_virtual_environment.storage_info:
    api_host: crossroads
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
    storage: lvm2
  register: proxmox_storage_lvm
"""

RETURN = r"""
storages:
  description: List of storage pools.
  returned: on success
  type: list
  elements: dict
  contains:
    content:
      description: Proxmox content types available in this storage.
      returned: on success
      type: list
      elements: str
    digest:
      description: Storage's digest.
      returned: on success
      type: str
    nodes:
      description: List of nodes associated to this storage.
      returned: on success, if storage is not local
      type: list
      elements: str
    path:
      description: Physical path to this storage.
      returned: on success
      type: str
    prune-backups:
      description: Backup retention options.
      returned: on success
      type: list
      elements: dict
    shared:
      description: Is this storage shared.
      returned: on success
      type: bool
    storage:
      description: Storage name.
      returned: on success
      type: str
    type:
      description: Storage type.
      returned: on success
      type: str
"""

__metaclass__ = type  # pylint: disable=C0103

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.proxmoxticator import Proxmoxticator


def main():
    module = AnsibleModule(
        argument_spec=dict(
            api_host=dict(required=True, type="str"),
            api_password=dict(no_log=True, required=False, type="str"),
            api_port=dict(default=8006, required=False, type="int"),
            api_token_id=dict(required=False, type="str"),
            api_token_secret=dict(no_log=True, required=False, type="str"),
            api_user=dict(required=True, type="str"),
            storage=dict(required=False, type="str"),
            type=dict(
                required=False,
                type="str",
                choices=[
                    "btrfs",
                    "cephfs",
                    "cifs",
                    "dir",
                    "esxi",
                    "glusterfs",
                    "iscsi",
                    "iscsidirect",
                    "lvm",
                    "lvmthin",
                    "nfs",
                    "pbs",
                    "rbd",
                    "zfs",
                    "zfspool",
                ],
            ),
        ),
        supports_check_mode=True,
    )

    module.exit_json(changed=False, meta=dict())


if __name__ == "__main__":
    main()
