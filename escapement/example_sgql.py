from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from sgqlc_schemas import github_schema

op = Operation(github_schema.query_type)
op.viewer().login()
endpoint = HTTPEndpoint('https://api.github.com/graphql', {'Authorization': f'bearer {token}'})
data = endpoint(op)
