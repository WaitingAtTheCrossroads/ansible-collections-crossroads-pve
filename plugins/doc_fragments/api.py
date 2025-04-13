# -*- coding: utf-8 -*-
#
# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
options:
  api_host:
    description:
      - Specify the target host of the Proxmox VE cluster.
    required: true
    type: str
  api_password:
    description:
      - Specify the password to authenticate with.
      - You can use E(PROXMOX_PASSWORD) environment variable.
    type: str
  api_port:
    description:
      - Specify the target port of the Proxmox VE cluster.
      - Uses the E(PROXMOX_PORT) environment variable if not specified.
    type: int
    default: 8006
  api_token_id:
    description:
      - Specify the token ID.
    type: str
  api_token_secret:
    description:
      - Specify the token secret.
    type: str
  api_user:
    description:
      - Specify the user to authenticate with.
    type: str
    required: true
  validate_certs:
    description:
      - If V(false), SSL certificates will not be validated.
      - >-
          This should only be used on personally controlled sites using
          self-signed certificates.
    type: bool
    default: true

requirements:
  - proxmoxer
  - requests

attributes:
  action_group:
    description: >-
      Use C(group/waitingatthecrossroads.proxmox_virtual_environment.api)
      in C(module_default) to set defaults for this module.
    support: full
    membership:
      - waitingatthecrossroads.proxmox_virtual_environment.api
"""
