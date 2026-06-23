drop database if exists WorldCup2026;
create database WorldCup2026;
use WorldCup2026;

create table Equipe (
	nome varchar(15) not null primary key,
    titulos int not null
);

create table Jogador (
	BID int not null primary key auto_increment,
    nome varchar(20) not null,
    idade int not null,
    nomeTime varchar(15) null,
    constraint fk_Equipe foreign key (nomeTime)
	references Equipe(nome) on delete cascade
);

insert into Equipe values('Alemanha', 4),
						 ('Brasil', 5),
                         ('França', 3);

select * from Equipe;