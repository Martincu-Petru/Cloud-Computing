create table users
(
	user_id int not null,
	first_name varchar(25) not null,
	last_name varchar(25) not null,
	date_of_birth date not null,
	is_premium tinyint(1) not null,
	constraint users_user_id_uindex
		unique (user_id)
);

alter table users
	add primary key (user_id);

