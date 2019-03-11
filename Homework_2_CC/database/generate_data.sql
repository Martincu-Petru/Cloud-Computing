use database_cloud_computing;

set foreign_key_checks = 0;

drop table if exists artists;
drop table if exists playlist_tracks;
drop table if exists playlist_user;
drop table if exists playlists;
drop table if exists tracks;
drop table if exists users;

create table artists
(
  artist_id   int         not null,
  artist_name varchar(25) not null,
  constraint artists_artist_id_uindex
    unique (artist_id)
);

alter table artists
  add primary key (artist_id);

create table playlists
(
  playlist_id   int         not null,
  playlist_name varchar(50) not null,
  constraint playlists_playlist_id_uindex
    unique (playlist_id)
);

alter table playlists
  add primary key (playlist_id);

create table tracks
(
  track_id   int         not null,
  track_name varchar(50) not null,
  artist_id  int         not null,
  constraint tracks_track_id_uindex
    unique (track_id),
  constraint tracks_artists_artist_id_fk
    foreign key (artist_id) references artists (artist_id)
);

alter table tracks
  add primary key (track_id);

create table playlist_tracks
(
  playlist_id int not null,
  track_id    int not null,
  constraint playlist_tracks_playlists_playlist_id_fk
    foreign key (playlist_id) references playlists (playlist_id),
  constraint playlist_tracks_tracks_track_id_fk
    foreign key (track_id) references tracks (track_id)
);

create table users
(
  user_id       int         not null,
  first_name    varchar(25) not null,
  last_name     varchar(25) not null,
  date_of_birth date        not null,
  is_premium    tinyint(1)  not null,
  constraint users_user_id_uindex
    unique (user_id)
);

alter table users
  add primary key (user_id);

create table playlist_user
(
  user_id     int not null,
  playlist_id int not null,
  constraint playlist_user_playlists_playlist_id_fk
    foreign key (playlist_id) references playlists (playlist_id),
  constraint playlist_user_users_user_id_fk
    foreign key (user_id) references users (user_id)
);


set foreign_key_checks = 1;

insert into artists (artist_id, artist_name) values (1, 'Alyse Paschke');
insert into artists (artist_id, artist_name) values (2, 'Alleyn Ottewill');
insert into artists (artist_id, artist_name) values (3, 'Lian Moller');
insert into artists (artist_id, artist_name) values (4, 'Humfried Opdenorth');
insert into artists (artist_id, artist_name) values (5, 'Emalia Bruyett');
insert into artists (artist_id, artist_name) values (6, 'Reuven Piegrome');
insert into artists (artist_id, artist_name) values (7, 'Tedmund Pauley');
insert into artists (artist_id, artist_name) values (8, 'Clari Pippin');
insert into artists (artist_id, artist_name) values (9, 'Claudio Browning');
insert into artists (artist_id, artist_name) values (10, 'Annalee Ratcliff');
insert into artists (artist_id, artist_name) values (11, 'Alfonse Mungin');
insert into artists (artist_id, artist_name) values (12, 'Emma Meeron');
insert into artists (artist_id, artist_name) values (13, 'Mikel Colnet');
insert into artists (artist_id, artist_name) values (14, 'Leeanne Flanagan');
insert into artists (artist_id, artist_name) values (15, 'Darb Bartelet');
insert into artists (artist_id, artist_name) values (16, 'Johnny Gyppes');
insert into artists (artist_id, artist_name) values (17, 'Patin Stoner');
insert into artists (artist_id, artist_name) values (18, 'Merry Conaghy');
insert into artists (artist_id, artist_name) values (19, 'Gusty Tomkowicz');
insert into artists (artist_id, artist_name) values (20, 'Zara Orta');
insert into artists (artist_id, artist_name) values (21, 'Hurleigh Cleave');
insert into artists (artist_id, artist_name) values (22, 'Peyton Kinglake');
insert into artists (artist_id, artist_name) values (23, 'Adrea Kwietak');
insert into artists (artist_id, artist_name) values (24, 'Stafani Alflatt');
insert into artists (artist_id, artist_name) values (25, 'Elysha Fronczak');

insert into users (user_id, first_name, last_name, date_of_birth, is_premium) values (1, 'Rakel', 'Bawles', '1993-04-29', false);
insert into users (user_id, first_name, last_name, date_of_birth, is_premium) values (2, 'Lamont', 'Temporal', '1984-10-25', true);
insert into users (user_id, first_name, last_name, date_of_birth, is_premium) values (3, 'Laraine', 'Creser', '1988-01-22', true);
insert into users (user_id, first_name, last_name, date_of_birth, is_premium) values (4, 'Heloise', 'Bowcock', '1978-08-16', true);
insert into users (user_id, first_name, last_name, date_of_birth, is_premium) values (5, 'Merlina', 'Ind', '1986-08-25', true);
insert into users (user_id, first_name, last_name, date_of_birth, is_premium) values (6, 'Brit', 'Goney', '1985-12-06', false);
insert into users (user_id, first_name, last_name, date_of_birth, is_premium) values (7, 'Harald', 'Colnet', '2004-03-02', true);
insert into users (user_id, first_name, last_name, date_of_birth, is_premium) values (8, 'Ruthanne', 'Screwton', '2007-04-22', false);
insert into users (user_id, first_name, last_name, date_of_birth, is_premium) values (9, 'Cornelle', 'Lanon', '1976-03-24', false);
insert into users (user_id, first_name, last_name, date_of_birth, is_premium) values (10, 'Ker', 'Huortic', '1994-05-29', true);

insert into tracks (track_id, track_name, artist_id) values (1, 'Conroy, Erdman and Metz', 12);
insert into tracks (track_id, track_name, artist_id) values (2, 'Mayer Inc', 17);
insert into tracks (track_id, track_name, artist_id) values (3, 'Kreiger-Barrows', 6);
insert into tracks (track_id, track_name, artist_id) values (4, 'Blick-Streich', 14);
insert into tracks (track_id, track_name, artist_id) values (5, 'Vandervort, Wehner and Ullrich', 5);
insert into tracks (track_id, track_name, artist_id) values (6, 'Wilkinson-Dickens', 8);
insert into tracks (track_id, track_name, artist_id) values (7, 'Olson, Davis and Shields', 9);
insert into tracks (track_id, track_name, artist_id) values (8, 'Dicki, Stroman and Wiegand', 25);
insert into tracks (track_id, track_name, artist_id) values (9, 'Cole-Hermann', 4);
insert into tracks (track_id, track_name, artist_id) values (10, 'Wunsch-Hamill', 18);
insert into tracks (track_id, track_name, artist_id) values (11, 'DuBuque Inc', 22);
insert into tracks (track_id, track_name, artist_id) values (12, 'Barrows, Mante and Schmeler', 19);
insert into tracks (track_id, track_name, artist_id) values (13, 'Gislason, Legros and Huels', 1);
insert into tracks (track_id, track_name, artist_id) values (14, 'MacGyver Inc', 21);
insert into tracks (track_id, track_name, artist_id) values (15, 'Fisher, Casper and Reinger', 21);
insert into tracks (track_id, track_name, artist_id) values (16, 'Rohan LLC', 25);
insert into tracks (track_id, track_name, artist_id) values (17, 'Stracke, Koch and Schmidt', 25);
insert into tracks (track_id, track_name, artist_id) values (18, 'Ziemann LLC', 6);
insert into tracks (track_id, track_name, artist_id) values (19, 'Strosin-Grady', 16);
insert into tracks (track_id, track_name, artist_id) values (20, 'Ward, Klocko and Beier', 17);
insert into tracks (track_id, track_name, artist_id) values (21, 'Dickinson, Fritsch and Pacocha', 18);
insert into tracks (track_id, track_name, artist_id) values (22, 'Eichmann-Rutherford', 17);
insert into tracks (track_id, track_name, artist_id) values (23, 'Steuber Group', 13);
insert into tracks (track_id, track_name, artist_id) values (24, 'Baumbach, Kunze and Barton', 5);
insert into tracks (track_id, track_name, artist_id) values (25, 'Powlowski Inc', 14);
insert into tracks (track_id, track_name, artist_id) values (26, 'O''Hara-Carroll', 6);
insert into tracks (track_id, track_name, artist_id) values (27, 'Jacobs-Parker', 14);
insert into tracks (track_id, track_name, artist_id) values (28, 'Kilback and Sons', 20);
insert into tracks (track_id, track_name, artist_id) values (29, 'Kunde, Reynolds and Hyatt', 9);
insert into tracks (track_id, track_name, artist_id) values (30, 'Gleason-Gutmann', 15);
insert into tracks (track_id, track_name, artist_id) values (31, 'Jacobson, Goldner and Maggio', 15);
insert into tracks (track_id, track_name, artist_id) values (32, 'Cummings-Kulas', 18);
insert into tracks (track_id, track_name, artist_id) values (33, 'Kessler, Rempel and Simonis', 15);
insert into tracks (track_id, track_name, artist_id) values (34, 'Funk-Mayer', 15);
insert into tracks (track_id, track_name, artist_id) values (35, 'Barrows-Mraz', 7);
insert into tracks (track_id, track_name, artist_id) values (36, 'Raynor-Bosco', 10);
insert into tracks (track_id, track_name, artist_id) values (37, 'Bogan LLC', 11);
insert into tracks (track_id, track_name, artist_id) values (38, 'Smitham-Schamberger', 4);
insert into tracks (track_id, track_name, artist_id) values (39, 'Auer and Sons', 18);
insert into tracks (track_id, track_name, artist_id) values (40, 'Boyer-Stokes', 5);
insert into tracks (track_id, track_name, artist_id) values (41, 'Witting-Schuppe', 14);
insert into tracks (track_id, track_name, artist_id) values (42, 'Stracke Inc', 8);
insert into tracks (track_id, track_name, artist_id) values (43, 'Balistreri, Goldner and Denesik', 19);
insert into tracks (track_id, track_name, artist_id) values (44, 'West Group', 21);
insert into tracks (track_id, track_name, artist_id) values (45, 'Kub and Sons', 5);
insert into tracks (track_id, track_name, artist_id) values (46, 'Dooley-Ortiz', 7);
insert into tracks (track_id, track_name, artist_id) values (47, 'Waters, Leannon and Nienow', 19);
insert into tracks (track_id, track_name, artist_id) values (48, 'Grimes-Rath', 3);
insert into tracks (track_id, track_name, artist_id) values (49, 'Zulauf-Lakin', 7);
insert into tracks (track_id, track_name, artist_id) values (50, 'Larkin-Hudson', 23);

insert into playlists (playlist_id, playlist_name) values (1, 'customer loyalty');
insert into playlists (playlist_id, playlist_name) values (2, 'national');
insert into playlists (playlist_id, playlist_name) values (3, 'hardware');
insert into playlists (playlist_id, playlist_name) values (4, 'Advanced');
insert into playlists (playlist_id, playlist_name) values (5, 'national');
insert into playlists (playlist_id, playlist_name) values (6, 'Multi-tiered');
insert into playlists (playlist_id, playlist_name) values (7, 'Versatile');
insert into playlists (playlist_id, playlist_name) values (8, 'policy');
insert into playlists (playlist_id, playlist_name) values (9, 'Cross-platform');
insert into playlists (playlist_id, playlist_name) values (10, 'Mandatory');
insert into playlists (playlist_id, playlist_name) values (11, 'zero defect');
insert into playlists (playlist_id, playlist_name) values (12, 'task-force');
insert into playlists (playlist_id, playlist_name) values (13, 'mission-critical');
insert into playlists (playlist_id, playlist_name) values (14, 'human-resource');
insert into playlists (playlist_id, playlist_name) values (15, 'installation');
insert into playlists (playlist_id, playlist_name) values (16, 'eco-centric');
insert into playlists (playlist_id, playlist_name) values (17, 'Up-sized');
insert into playlists (playlist_id, playlist_name) values (18, 'homogeneous');
insert into playlists (playlist_id, playlist_name) values (19, 'Visionary');
insert into playlists (playlist_id, playlist_name) values (20, 'uniform');
insert into playlists (playlist_id, playlist_name) values (21, 'Open-source');
insert into playlists (playlist_id, playlist_name) values (22, 'hardware');
insert into playlists (playlist_id, playlist_name) values (23, 'asymmetric');
insert into playlists (playlist_id, playlist_name) values (24, 'Multi-tiered');
insert into playlists (playlist_id, playlist_name) values (25, 'Realigned');
insert into playlists (playlist_id, playlist_name) values (26, 'Function-based');
insert into playlists (playlist_id, playlist_name) values (27, 'Multi-channelled');
insert into playlists (playlist_id, playlist_name) values (28, 'Enhanced');
insert into playlists (playlist_id, playlist_name) values (29, 'extranet');
insert into playlists (playlist_id, playlist_name) values (30, 'Self-enabling');
insert into playlists (playlist_id, playlist_name) values (31, 'Profound');
insert into playlists (playlist_id, playlist_name) values (32, 'Versatile');
insert into playlists (playlist_id, playlist_name) values (33, 'Sharable');
insert into playlists (playlist_id, playlist_name) values (34, 'product');
insert into playlists (playlist_id, playlist_name) values (35, 'Mandatory');
insert into playlists (playlist_id, playlist_name) values (36, 'paradigm');
insert into playlists (playlist_id, playlist_name) values (37, 'multi-state');
insert into playlists (playlist_id, playlist_name) values (38, 'zero administration');
insert into playlists (playlist_id, playlist_name) values (39, 'Customizable');
insert into playlists (playlist_id, playlist_name) values (40, 'artificial intelligence');
insert into playlists (playlist_id, playlist_name) values (41, 'client-driven');
insert into playlists (playlist_id, playlist_name) values (42, 'encompassing');
insert into playlists (playlist_id, playlist_name) values (43, 'superstructure');
insert into playlists (playlist_id, playlist_name) values (44, 'middleware');
insert into playlists (playlist_id, playlist_name) values (45, 'mobile');
insert into playlists (playlist_id, playlist_name) values (46, 'support');
insert into playlists (playlist_id, playlist_name) values (47, 'adapter');
insert into playlists (playlist_id, playlist_name) values (48, 'zero defect');
insert into playlists (playlist_id, playlist_name) values (49, 'utilisation');
insert into playlists (playlist_id, playlist_name) values (50, 'conglomeration');

insert into playlist_user (user_id, playlist_id) values (3, 30);
insert into playlist_user (user_id, playlist_id) values (2, 20);
insert into playlist_user (user_id, playlist_id) values (9, 11);
insert into playlist_user (user_id, playlist_id) values (9, 45);
insert into playlist_user (user_id, playlist_id) values (2, 19);
insert into playlist_user (user_id, playlist_id) values (2, 13);
insert into playlist_user (user_id, playlist_id) values (10, 32);
insert into playlist_user (user_id, playlist_id) values (8, 22);
insert into playlist_user (user_id, playlist_id) values (5, 33);
insert into playlist_user (user_id, playlist_id) values (3, 20);
insert into playlist_user (user_id, playlist_id) values (8, 12);
insert into playlist_user (user_id, playlist_id) values (5, 12);
insert into playlist_user (user_id, playlist_id) values (6, 38);
insert into playlist_user (user_id, playlist_id) values (4, 37);
insert into playlist_user (user_id, playlist_id) values (2, 39);
insert into playlist_user (user_id, playlist_id) values (2, 29);
insert into playlist_user (user_id, playlist_id) values (6, 2);
insert into playlist_user (user_id, playlist_id) values (7, 43);
insert into playlist_user (user_id, playlist_id) values (8, 36);
insert into playlist_user (user_id, playlist_id) values (8, 35);
insert into playlist_user (user_id, playlist_id) values (1, 29);
insert into playlist_user (user_id, playlist_id) values (2, 19);
insert into playlist_user (user_id, playlist_id) values (10, 35);
insert into playlist_user (user_id, playlist_id) values (1, 9);
insert into playlist_user (user_id, playlist_id) values (2, 36);
insert into playlist_user (user_id, playlist_id) values (4, 42);
insert into playlist_user (user_id, playlist_id) values (8, 15);
insert into playlist_user (user_id, playlist_id) values (5, 38);
insert into playlist_user (user_id, playlist_id) values (4, 10);
insert into playlist_user (user_id, playlist_id) values (5, 47);
insert into playlist_user (user_id, playlist_id) values (4, 3);
insert into playlist_user (user_id, playlist_id) values (10, 43);
insert into playlist_user (user_id, playlist_id) values (2, 2);
insert into playlist_user (user_id, playlist_id) values (2, 36);
insert into playlist_user (user_id, playlist_id) values (9, 15);
insert into playlist_user (user_id, playlist_id) values (4, 44);
insert into playlist_user (user_id, playlist_id) values (6, 33);
insert into playlist_user (user_id, playlist_id) values (3, 25);
insert into playlist_user (user_id, playlist_id) values (8, 12);
insert into playlist_user (user_id, playlist_id) values (9, 25);
insert into playlist_user (user_id, playlist_id) values (7, 4);
insert into playlist_user (user_id, playlist_id) values (4, 3);
insert into playlist_user (user_id, playlist_id) values (10, 46);
insert into playlist_user (user_id, playlist_id) values (4, 14);
insert into playlist_user (user_id, playlist_id) values (1, 10);
insert into playlist_user (user_id, playlist_id) values (1, 26);
insert into playlist_user (user_id, playlist_id) values (6, 37);
insert into playlist_user (user_id, playlist_id) values (1, 13);
insert into playlist_user (user_id, playlist_id) values (1, 35);
insert into playlist_user (user_id, playlist_id) values (2, 37);

insert into playlist_tracks (playlist_id, track_id) values (22, 29);
insert into playlist_tracks (playlist_id, track_id) values (50, 49);
insert into playlist_tracks (playlist_id, track_id) values (37, 39);
insert into playlist_tracks (playlist_id, track_id) values (50, 10);
insert into playlist_tracks (playlist_id, track_id) values (13, 3);
insert into playlist_tracks (playlist_id, track_id) values (1, 44);
insert into playlist_tracks (playlist_id, track_id) values (15, 25);
insert into playlist_tracks (playlist_id, track_id) values (11, 32);
insert into playlist_tracks (playlist_id, track_id) values (5, 23);
insert into playlist_tracks (playlist_id, track_id) values (23, 46);
insert into playlist_tracks (playlist_id, track_id) values (10, 9);
insert into playlist_tracks (playlist_id, track_id) values (1, 10);
insert into playlist_tracks (playlist_id, track_id) values (43, 48);
insert into playlist_tracks (playlist_id, track_id) values (30, 46);
insert into playlist_tracks (playlist_id, track_id) values (50, 3);
insert into playlist_tracks (playlist_id, track_id) values (25, 9);
insert into playlist_tracks (playlist_id, track_id) values (36, 1);
insert into playlist_tracks (playlist_id, track_id) values (10, 11);
insert into playlist_tracks (playlist_id, track_id) values (17, 40);
insert into playlist_tracks (playlist_id, track_id) values (22, 8);
insert into playlist_tracks (playlist_id, track_id) values (27, 14);
insert into playlist_tracks (playlist_id, track_id) values (26, 14);
insert into playlist_tracks (playlist_id, track_id) values (48, 11);
insert into playlist_tracks (playlist_id, track_id) values (30, 29);
insert into playlist_tracks (playlist_id, track_id) values (30, 2);
insert into playlist_tracks (playlist_id, track_id) values (15, 45);
insert into playlist_tracks (playlist_id, track_id) values (6, 26);
insert into playlist_tracks (playlist_id, track_id) values (38, 45);
insert into playlist_tracks (playlist_id, track_id) values (41, 43);
insert into playlist_tracks (playlist_id, track_id) values (18, 46);
insert into playlist_tracks (playlist_id, track_id) values (22, 16);
insert into playlist_tracks (playlist_id, track_id) values (5, 4);
insert into playlist_tracks (playlist_id, track_id) values (15, 33);
insert into playlist_tracks (playlist_id, track_id) values (48, 20);
insert into playlist_tracks (playlist_id, track_id) values (4, 33);
insert into playlist_tracks (playlist_id, track_id) values (14, 45);
insert into playlist_tracks (playlist_id, track_id) values (47, 39);
insert into playlist_tracks (playlist_id, track_id) values (2, 41);
insert into playlist_tracks (playlist_id, track_id) values (14, 28);
insert into playlist_tracks (playlist_id, track_id) values (29, 1);
insert into playlist_tracks (playlist_id, track_id) values (12, 5);
insert into playlist_tracks (playlist_id, track_id) values (19, 2);
insert into playlist_tracks (playlist_id, track_id) values (36, 26);
insert into playlist_tracks (playlist_id, track_id) values (50, 43);
insert into playlist_tracks (playlist_id, track_id) values (48, 50);
insert into playlist_tracks (playlist_id, track_id) values (47, 39);
insert into playlist_tracks (playlist_id, track_id) values (12, 25);
insert into playlist_tracks (playlist_id, track_id) values (44, 33);
insert into playlist_tracks (playlist_id, track_id) values (12, 32);
insert into playlist_tracks (playlist_id, track_id) values (17, 45);
insert into playlist_tracks (playlist_id, track_id) values (27, 43);
insert into playlist_tracks (playlist_id, track_id) values (41, 25);
insert into playlist_tracks (playlist_id, track_id) values (23, 14);
insert into playlist_tracks (playlist_id, track_id) values (46, 44);
insert into playlist_tracks (playlist_id, track_id) values (40, 39);
insert into playlist_tracks (playlist_id, track_id) values (14, 24);
insert into playlist_tracks (playlist_id, track_id) values (1, 16);
insert into playlist_tracks (playlist_id, track_id) values (11, 10);
insert into playlist_tracks (playlist_id, track_id) values (21, 34);
insert into playlist_tracks (playlist_id, track_id) values (43, 50);
insert into playlist_tracks (playlist_id, track_id) values (44, 21);
insert into playlist_tracks (playlist_id, track_id) values (12, 39);
insert into playlist_tracks (playlist_id, track_id) values (39, 48);
insert into playlist_tracks (playlist_id, track_id) values (38, 26);
insert into playlist_tracks (playlist_id, track_id) values (46, 15);
insert into playlist_tracks (playlist_id, track_id) values (50, 30);
insert into playlist_tracks (playlist_id, track_id) values (3, 47);
insert into playlist_tracks (playlist_id, track_id) values (36, 36);
insert into playlist_tracks (playlist_id, track_id) values (12, 48);
insert into playlist_tracks (playlist_id, track_id) values (44, 49);
insert into playlist_tracks (playlist_id, track_id) values (37, 20);
insert into playlist_tracks (playlist_id, track_id) values (43, 41);
insert into playlist_tracks (playlist_id, track_id) values (3, 19);
insert into playlist_tracks (playlist_id, track_id) values (43, 25);
insert into playlist_tracks (playlist_id, track_id) values (43, 47);
insert into playlist_tracks (playlist_id, track_id) values (7, 33);
insert into playlist_tracks (playlist_id, track_id) values (8, 17);
insert into playlist_tracks (playlist_id, track_id) values (36, 35);
insert into playlist_tracks (playlist_id, track_id) values (32, 15);
insert into playlist_tracks (playlist_id, track_id) values (24, 38);
insert into playlist_tracks (playlist_id, track_id) values (34, 23);
insert into playlist_tracks (playlist_id, track_id) values (12, 9);
insert into playlist_tracks (playlist_id, track_id) values (8, 7);
insert into playlist_tracks (playlist_id, track_id) values (8, 31);
insert into playlist_tracks (playlist_id, track_id) values (30, 7);
insert into playlist_tracks (playlist_id, track_id) values (29, 23);
insert into playlist_tracks (playlist_id, track_id) values (5, 24);
insert into playlist_tracks (playlist_id, track_id) values (38, 6);
insert into playlist_tracks (playlist_id, track_id) values (20, 21);
insert into playlist_tracks (playlist_id, track_id) values (21, 40);
insert into playlist_tracks (playlist_id, track_id) values (46, 20);
insert into playlist_tracks (playlist_id, track_id) values (26, 43);
insert into playlist_tracks (playlist_id, track_id) values (21, 34);
insert into playlist_tracks (playlist_id, track_id) values (35, 27);
insert into playlist_tracks (playlist_id, track_id) values (46, 29);
insert into playlist_tracks (playlist_id, track_id) values (43, 4);
insert into playlist_tracks (playlist_id, track_id) values (7, 27);
insert into playlist_tracks (playlist_id, track_id) values (3, 15);
insert into playlist_tracks (playlist_id, track_id) values (2, 11);
insert into playlist_tracks (playlist_id, track_id) values (40, 49);