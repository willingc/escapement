"""Main module."""
from decouple import config


GH_TOKEN = config('GH_TOKEN', default='')
GH_USER = config('GH_USER', default='')

print(f'GH_TOKEN: {GH_TOKEN}')
print(f'USER: {GH_USER}')

orgs = ['jupyterhub', 'jupyter', 'nteract', 'jupyter-widgets']
start_date = '2021-01-01'
end_date = '2021-01-21'
