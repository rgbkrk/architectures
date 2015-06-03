# Jupyter Temporary Notebook Environments

## Diagram

![Temporary Notebook System](https://cloud.githubusercontent.com/assets/836375/5911140/c53e3978-a587-11e4-86a5-695469ef23a5.png)

## Deployment

### Ansible

* [Community playbook](https://github.com/jupyter/tmpnb-deploy) for [tmpnb.org](https://tmpnb.org)

## Specification

### DNS
- DNS domain entry for website
- "A" record that points to 

### Docker image for notebook users

TODO: Write up about building a docker image

### Shared compute amongst users

Users of individual notebook servers are subdivided amongst resources. The bigger the group/demo size, the bigger the backing compute should be.

The demo server [https://try.jupyter.org](https://try.jupyter.org), done in coordination with the Jupyter project, subdivides an OnMetal memory server with 512GB of RAM amongst 512 concurrent users (per backing compute server). Each user gets 1GB of memory. CPUs are divided up with a bit more overprovisioning, since interaction is intermittent and the OS can schedule processes. The current implementation gives every user 1/32 of the overall 24 processors (each with 6 cores -> 144 total cores). 

## Notes

### DNS management

The end-user's request is first routed through Cloud DNS, a globally distributed service which allows a great degree of control over where requests are routed to.  Records can be associated with other Rackspace infrastructure.

#### CDN

For resources that are accessed a lot, but do not change in content, performance can be improved by caching them in a globally distributed CDN. Content will be cached in local edge nodes, improving redundancy and reducing latency - meaning a better overall experience for your end-users. Using the new Rackspace CDN service, you have greater control over what aspects of your website is cached.

#### Asset storage

Static assets (images, stylesheets and JavaScript files) can be stored in Rackspace Cloud Files, a highly available and redundant file storage service. Doing this will reduce the compute load on your web nodes since they are no longer handling superfluous web requests for static assets.
