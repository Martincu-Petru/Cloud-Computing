create table playlist_tracks
(
	playlist_id int not null,
	track_id int not null,
	constraint playlist_tracks_playlists_playlist_id_fk
		foreign key (playlist_id) references playlists (playlist_id),
	constraint playlist_tracks_tracks_track_id_fk
		foreign key (track_id) references tracks (track_id)
);

