#!/usr/bin/python

from jinja2 import Environment, FileSystemLoader

from yaml import safe_load

pkgs = safe_load(open('./packages.yml', 'r'))
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')
open('issues.html', 'w').write(template.render(pkgs=pkgs))
