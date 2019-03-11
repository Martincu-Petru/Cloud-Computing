create table artists
(
	artist_id int not null,
	artist_name varchar(25) not null,
	constraint artists_artist_id_uindex
		unique (artist_id)
);

alter table artists
	add primary key (artist_id);

