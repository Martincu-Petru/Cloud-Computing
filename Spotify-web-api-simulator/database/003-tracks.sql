create table tracks
(
	track_id int not null,
	track_name varchar(50) not null,
	artist_id int not null,
	constraint tracks_track_id_uindex
		unique (track_id),
	constraint tracks_artists_artist_id_fk
		foreign key (artist_id) references artists (artist_id)
);

alter table tracks
	add primary key (track_id);

