import strawberry

from api.types.playlist import Playlist


@strawberry.type
class AddItemsToPlaylistPayload:
    code: int = strawberry.field(description="The HTTP status code.")
    success: bool = strawberry.field(description="Whether the playlist was successfully updated.")
    message: str = strawberry.field(description="The message returned by the API.")

    playlist: Playlist | None = strawberry.field(description="The playlist that was updated or inserted.")