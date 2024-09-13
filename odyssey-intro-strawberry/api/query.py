import strawberry

from api.types.playlist import Playlist


@strawberry.type
class Query:
    @strawberry.field(description="Playlists hand-picked to be featured to all users.")
    def featured_playlists(self) -> list[Playlist]:
        return [
            Playlist(id=strawberry.ID("1"), name="GraphQL Groovin'", description=None),
            Playlist(id=strawberry.ID("2"), name="Graph Explorer Jams", description=None),
            Playlist(id=strawberry.ID("3"), name="Interpretive GraphQL Dance", description=None),
        ]
