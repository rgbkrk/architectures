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
