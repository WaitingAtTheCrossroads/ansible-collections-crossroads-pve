# -*- coding: utf-8 -*-
#
# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, annotations, division, print_function

from typing import TYPE_CHECKING

from proxmoxer import ProxmoxAPI


if TYPE_CHECKING:
    from ansible.module_utils.basic import AnsibleModule


class Proxmoxticator:
    def __init__(self, module: AnsibleModule):
        self.module = module

        self.api = self._connect()

    def _connect(self):
        return ProxmoxAPI(
            self.module.params.get("api_host"),
            password=self.module.params.get("api_password"),
            port=self.module.params.get("api_port"),
            token_name=self.module.params.get("api_token_id"),
            token_value=self.module.params.get("api_token_secret"),
            user=self.module.params.get("api_user"),
            verify_ssl=self.module.params.get("validate_certs"),
        )

    def storages_list(self) -> list[dict] | None:
        return self.api.storages.get()
