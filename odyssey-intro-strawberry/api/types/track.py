import strawberry


@strawberry.type(description="A single audio file, usually a song.")
class Track:
    id: strawberry.ID = strawberry.field(description="The unique identifier for the track.")
    artist_name: list[str] | None = strawberry.field(description="The name of the artists.")
    uri: str = strawberry.field(description="The URI to the track.")
    name: str = strawberry.field(description="The name of the track.")
    duration_ms: float = strawberry.field(description="The duration of the track in milliseconds.")
    explicit: bool = strawberry.field(description="Whether the track is explicit or not.")
