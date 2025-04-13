# -*- coding: utf-8 -*-
#
# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations


def get_api_url(host: str, port: int | str, path: str) -> str:
    return f"https://{host}:{port}/api2/json{path}"
