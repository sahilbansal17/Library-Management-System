-- question no. 3, designing and implementing the various tables in mysql database 'lms'
create database lms;

use lms;

create table Book(
	book_id int,
	title varchar(200),
	year int,
	isbn varchar(13),
	pages int,
	user_id int,
	add_time datetime,
	publisher_id int,
	issue_time datetime,
	primary key (book_id)
);

create table User(
	user_id int,
	name varchar(100),
	username varchar(50),
	password varchar(20),
	email varchar(50)
);

create table Periodical(
	periodical_id int,
	title varchar(200),
	year int,
	volume int,
	isbn varchar(13),
	user_id int,
	publisher_id int
);

create table Message(
	message_id int,
	text varchar(500),
	user_id int,
	time datetime
);

create table Author(
	author_id int,
	name varchar(100)
);

create table Paper(
	paper_id int,
	name varchar(100)
);

create table Publisher(
	publisher_id int,
	name varchar(200)
);

create table Tag(
	tag_id int,
	value varchar(100)
);

create table Book_and_Author(
	book_id int,
	author_id int
);

create table Paper_and_Author(
	paper_id int,
	author_id int
);

create table Book_and_Tag(
	book_id int,
	tag_id int
);

create table Periodical_and_Tag(
	periodical_id int,
	tag_id int
);

alter table Author add constraint PRIMARY KEY(author_id);
alter table Book_and_Author add constraint PRIMARY KEY(book_id, author_id);
alter table Paper_and_Author add constraint PRIMARY KEY(paper_id, author_id);
alter table Book_and_Tag add constraint PRIMARY KEY(book_id, tag_id);
alter table Periodical_and_Tag add constraint PRIMARY KEY(periodical_id, tag_id);
alter table Message add constraint PRIMARY KEY(message_id);
alter table Paper add constraint PRIMARY KEY(paper_id);
alter table Periodical add constraint PRIMARY KEY(periodical_id);
alter table Publisher add constraint PRIMARY KEY(publisher_id);
alter table Tag add constraint PRIMARY KEY(tag_id);
alter table User add constraint PRIMARY KEY(user_id);
alter table Book 		add constraint FOREIGN KEY 	(user_id) 		references 	User(user_id);
alter table Book add constraint FOREIGN KEY (publisher_id) references Publisher(publisher_id);
alter table Periodical add constraint FOREIGN KEY (user_id) references User(user_id);
alter table Periodical add constraint FOREIGN KEY (publisher_id) references Publisher(publisher_id);
alter table Message add constraint FOREIGN KEY (user_id) references User(user_id);
alter table Paper add periodical_id int;
alter table Paper add constraint FOREIGN KEY (periodical_id) references Periodical(periodical_id);

-- relationship tables
alter table Book_and_Author add constraint FOREIGN KEY (book_id) references Book(book_id);
alter table Book_and_Tag add constraint FOREIGN KEY (book_id) references Book(book_id);
alter table Book_and_Discipline add constraint FOREIGN KEY (book_id) references Book(book_id);
alter table Book_and_Author add constraint FOREIGN KEY (author_id) references Author(author_id);
alter table Paper_and_Author add constraint FOREIGN KEY (author_id) references Author(author_id);
alter table Paper_and_Author add constraint FOREIGN KEY (paper_id) references Paper(paper_id);
alter table Book_and_Tag add constraint FOREIGN KEY (tag_id) references Tag(tag_id);
alter table Periodical_and_Tag add constraint FOREIGN KEY (tag_id) references Tag(tag_id);
alter table Periodical_and_Tag add constraint FOREIGN KEY (periodical_id) references Periodical(periodical_id);

-- modifications 
alter table User add user_type enum('Student', 'Faculty', 'Staff', 'Guest');
create table Issue_Capacity(
	user_type enum('Student', 'Faculty', 'Staff', 'Guest'),
	max_books int,
	max_time int
);
insert into Issue_Capacity values ('Student', 3, 15), ('Faculty', 6, 30), ('Staff', 4, 30), ('Guest', 2, 7);
alter table Issue_Capacity add constraint PRIMARY KEY(user_type);

-- fixes
alter table Periodical add add_time datetime;
alter table Periodical add issue_time datetime;

-- question no. 7 : modify table Book to add a column 'Discipline'
alter table Book add discipline varchar(50);
alter table Book drop column discipline;
create table Book_and_Discipline(
	book_id int,
	discipline varchar(50),
	PRIMARY KEY(book_id, discipline)
);

-- generating some simple data
-- insert into Book values (1, 'abc', 2011, 1234567890, 1000, NULL, '2019-02-20 17:00:00', NULL, NULL);
-- insert into User values (1, 'xyz', 'xzy123', 'qwerty@123', 'xyz@gmail.com', 'Student');
-- insert into Periodical values (1, 'abc', 2011, 1, 1234567890, NULL, NULL);
-- insert into Periodical values (2, 'abc', 2011, 2, 1234567890, NULL, NULL);
-- insert into Author values (1, 'author1');
-- insert into Paper values (1, 'paper1', 1);
-- insert into Publisher values (1, 'pub1');

-- create separate relationship table for borrowing books and periodicals 
-- as it is required for several queries
create table Borrow_Book(
	borrow_id int,
	book_id int,
	user_id int,
	issue_time datetime,
	return_time datetime,
	due_amount int,
	primary key (borrow_id),
	foreign key (book_id) references Book(book_id),
	foreign key (user_id) references User(user_id)
);
create table Borrow_Periodical(
	borrow_id int,
	periodical_id int,
	user_id int,
	issue_time datetime,
	return_time datetime,
	due_amount int,
	primary key (borrow_id),
	foreign key (periodical_id) references Periodical(periodical_id),
	foreign key (user_id) references User(user_id)
);