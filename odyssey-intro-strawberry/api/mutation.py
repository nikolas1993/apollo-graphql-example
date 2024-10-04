import strawberry

from api.types.add_items_to_playlist_input import AddItemsToPlaylistInput
from api.types.add_items_to_playlist_payload import AddItemsToPlaylistPayload
from api.types.playlist import Playlist
from mock_spotify_rest_api_client.api.playlists import add_tracks_to_playlist, get_playlist


@strawberry.type
class Mutation:
    @strawberry.mutation(description="Add one or more items to a user's playlist.")
    async def add_items_to_playlist(self, playlist_tracks: AddItemsToPlaylistInput, info) -> AddItemsToPlaylistPayload:
        spotify_client = info.context["spotify_client"]
        try:
            await add_tracks_to_playlist.asyncio(playlist_id=playlist_tracks.playlist_id,
                                                 uris=",".join(playlist_tracks.uris), client=spotify_client)

            data = await get_playlist.asyncio(client=spotify_client, playlist_id=playlist_tracks.playlist_id)

            if data is None:
                return AddItemsToPlaylistPayload(code=404, success=False, message="Playlist not found.", playlist=None)

            playlist = Playlist(id=strawberry.ID(data.id), name=data.name, description=data.description)

            return AddItemsToPlaylistPayload(code=200, success=True, message="Successfully added items to playlist.",
                                             playlist=playlist)
        except Exception as e:
            return AddItemsToPlaylistPayload(code=500, success=False, message=str(e), playlist=None)
