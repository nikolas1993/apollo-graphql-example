import strawberry

from api.mutation import Mutation
from api.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
