# -*- coding: utf-8 -*-
#
# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from typing import Callable

from pytest import fixture


@fixture
def api_conf() -> dict[str, int | str]:
    return dict(
        api_host="crossroads",
        api_user="root@pam",
        api_password="password",
        api_port=8006,
    )


@fixture
def api_url(api_conf) -> Callable[[str], str]:
    def inner(path: str):
        scheme = "https"
        host = api_conf.get["api_host"]
        port = api_conf.get["api_port"]

        return f"{scheme}://{host}:{port}/api2/json{path}"

    return inner
