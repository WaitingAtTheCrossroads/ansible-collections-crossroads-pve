# Waitingatthecrossroads Proxmox_virtual_environment Collection

[![CI](https://github.com/WaitingAtTheCrossroads/ansible-collections-crossroads-pve/actions/workflows/tests.yml/badge.svg)](https://github.com/WaitingAtTheCrossroads/ansible-collections-crossroads-pve/actions/workflows/tests.yml)

This repository contains the
`waitingatthecrossroads.proxmox_virtual_environment` Ansible Collection.

## External requirements

Some modules and plugins require external libraries. Please check the
requirements for each plugin or module you use in the documentation to find out
which requirements are needed.

## Included content

Coming soon!

## Using this collection

```bash
ansible-galaxy collection install waitingatthecrossroads.proxmox_virtual_environment
```

You can also include it in a `requirements.yml` file and install it via
`ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
  - name: waitingatthecrossroads.proxmox_virtual_environment
```

To upgrade the collection to the latest available version, run the following
command:

```bash
ansible-galaxy collection install waitingatthecrossroads.proxmox_virtual_environment --upgrade
```

You can also install a specific version of the collection, for example, if you
need to downgrade when something is broken in the latest version (please report
an issue in this repository). Use the following syntax where `X.Y.Z` can be any
[available version][galaxy-this]:

```bash
ansible-galaxy collection install waitingatthecrossroads.proxmox_virtual_environment:==X.Y.Z
```

See [Ansible Using collections][ansible-using-collections] for more details.

## Release notes

See the [changelog][this-changelog].

<!--## Roadmap

Optional. Include the roadmap for this collection, and the proposed
release/versioning strategy so users can anticipate the upgrade/update cycle.
-->

## More information

<!-- List out where the user can find additional information, such as working
group meeting times, slack/IRC channels, or documentation for the product this
collection automates. At a minimum, link to: -->

- [Ansible Collection overview][ansible-collection-overview]
- [Ansible User guide][ansible-user-guide]
- [Ansible Developer guide][ansible-developer-guide]
- [Ansible Collections Checklist][ansible-collections-checklist]
- [Ansible Community code of conduct][ansible-community-code-of-conduct]
- [The Bullhorn (the Ansible Contributor
  newsletter)][ansible-contributor-newsletter]
- [News for Maintainers][ansible-news-for-maintainers]

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE][gnu-gpl3] to see the full text.

<!-- Links -->

[ansible-collection-overview]: (https://github.com/ansible-collections/overview)
[ansible-collections-checklist]: (https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst)
[ansible-community-code-of-conduct]: (https://docs.ansible.com/ansible/devel/community/code_of_conduct.html)
[ansible-contributor-newsletter]: (https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn)
[ansible-developer-guide]: (https://docs.ansible.com/ansible/devel/dev_guide/index.html)
[ansible-news-for-maintainers]: (https://github.com/ansible-collections/news-for-maintainers)
[ansible-user-guide]: (https://docs.ansible.com/ansible/devel/user_guide/index.html)
[ansible-using-collections]: (https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)

[galaxy-this]: (https://galaxy.ansible.com/waitingatthecrossroads/proxmox_virtual_environment)

[gnu-gpl3]: (https://www.gnu.org/licenses/gpl-3.0.txt)

[this-changelog]: (https://github.com/ansible-collections/waitingatthecrossroads.proxmox_virtual_environment/tree/main/CHANGELOG.rst)
