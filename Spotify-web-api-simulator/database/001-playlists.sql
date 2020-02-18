create table playlists
(
	playlist_id int not null,
	playlist_name varchar(50) not null,
	constraint playlists_playlist_id_uindex
		unique (playlist_id)
);

alter table playlists
	add primary key (playlist_id);

