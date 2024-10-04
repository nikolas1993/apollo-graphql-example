import strawberry

from api.types.playlist import Playlist
from api.types.track import Track
from mock_spotify_rest_api_client.api.playlists import get_featured_playlists, get_playlist


@strawberry.type
class Query:
    @strawberry.field(description="Playlists hand-picked to be featured to all users.")
    async def featured_playlists(self, info: strawberry.Info) -> list[Playlist]:
        spotify_client = info.context["spotify_client"]
        data = await get_featured_playlists.asyncio(client=spotify_client)
        items = data.playlists.items if data is not None else []
        playlists = [
            Playlist(id=strawberry.ID(playlist.id), name=playlist.name, description=playlist.description)
            for
            playlist in items]
        return playlists

    @strawberry.field(description="Retrieves a specific playlist.")
    async def playlist(self, id: strawberry.ID, info: strawberry.Info) -> Playlist | None:
        spotify_client = info.context["spotify_client"]
        data = await get_playlist.asyncio(client=spotify_client, playlist_id=id)
        if data is None:
            return None
        playlist = Playlist(id=strawberry.ID(data.id), name=data.name, description=data.description)
        return playlist

    @strawberry.field(description="Retrieves tracks from a specific playlist.")
    async def tracks(self, playlist_id: strawberry.ID, info: strawberry.Info) -> list[Track] | None:
        spotify_client = info.context["spotify_client"]
        data = await get_playlist.asyncio(client=spotify_client, playlist_id=playlist_id)
        if data is None or data.tracks is None or data.tracks.items is None:
            return None
        tracks_data = data.tracks.items
        tracks: list[Track] = []
        for track_data in tracks_data:
            artist_names = [artist.name for artist in track_data.track.artists]
            track = Track(id=strawberry.ID(track_data.track.id), artist_name=artist_names,
                          uri=track_data.track.uri, name=track_data.track.name,
                          duration_ms=track_data.track.duration_ms, explicit=track_data.track.explicit)
            tracks.append(track)
        return tracks
