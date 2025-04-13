# -*- coding: utf-8 -*-
#
# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from urllib.parse import urlunparse

from pytest import fixture
from responses import activate as responses_activate
from responses import get as responses_get


class TestStorageInfo:
    @fixture
    def data_storages_all(self):
        return [
            {
                "content": "snippets,iso,backup,vztmpl,rootdir,images",
                "digest": "a14a2d7b21f650708c9aca7e5e46cc2c7e656a1a",
                "disable": 1,
                "path": "/var/lib/vz",
                "prune-backups": "keep-all=1",
                "storage": "local",
                "type": "dir",
            },
            {
                "content": "images,rootdir,vztmpl,iso,backup",
                "digest": "a14a2d7b21f650708c9aca7e5e46cc2c7e656a1a",
                "path": "/var/lib/pve/local-btrfs",
                "storage": "local-btrfs",
                "type": "btrfs",
            },
        ]

    @fixture
    def data_storages_dir(self, data_storages_all):
        return data_storages_all[0]

    @fixture
    def data_storages_local_btrfs(self, data_storages_all):
        return data_storages_all[1]

    @responses_activate
    def test_storages_all(self, api_conf, api_url, localhost, storages_all):
        responses_get(api_url("/storage"), json=storages_all)
