# -*- coding: utf-8 -*-
#
# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
options: {}
attributes:
  check_mode:
    description: >-
      Can run in C(check_mode) and return changed status prediction without
      modifying target.
  diff_mode:
    description: >-
      Will return details on what has changed (or possibly needs changing in
      C(check_mode)), when in diff mode.
"""

    INFO = r"""
options: {}
attributes:
  check_mode:
    support: full
    details:
      - This action does not modify state.
  diff_mode:
    support: N/A
    details:
      - This action does not modify state.
"""
