create table playlist_user
(
	user_id int not null,
	playlist_id int not null,
	constraint playlist_user_playlists_playlist_id_fk
		foreign key (playlist_id) references playlists (playlist_id),
	constraint playlist_user_users_user_id_fk
		foreign key (user_id) references users (user_id)
);

