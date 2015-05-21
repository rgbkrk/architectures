# Instructions

It's strongly recommended that you run these Ansible scripts from a server in the
same region you're deploying to, since the latency and network throughput will
generally be better.

0. Ensure pip is installed. If it isn't, follow [these instructions](https://pip.pypa.io/en/latest/installing.html#install-pip).

1. Install Ansible (at least v1.9.1):

  ```
  pip install ansible
  ```

2. Install pyrax:

  ```
  pip install pyrax
  ```

3. Ensure that `~/.rackspace_cloud_credentials` exists in your home directory, with the necessary credentials. You can copy the `.rackspace_cloud_credentials.sample` file in this directory for help.
4. In this directory, copy `creds.yml.sample` to `creds.yml` and fill in your API credentials.
5. Go through `vars.yml` and make sure you're happy with the configuration set out.
6. Run this:

  ```
  ansible-playbook -i inventory main.yml
  ```

## Troubleshooting

* If you're having trouble installing ansible for the first time with pip, and it
shows some kind of gcc error, try installing `python2.7-dev`

* If ansible is telling you that `requests` is too old (`python-novaclient` requires
  >=2.5.2), you can manually upgrade it to the newest version (2.7.0) like so:

  ```
  pip install requests==2.7.0
  ```

* If ansible is complaining about `pbr!=0.7,<1.0,>=0.6`, try upgrading the
  keystone client:

  ```
  pip install python-keystoneclient --upgrade -I
  ```
