CREATE TABLE tbUsers(
	id_aluno 	SERIAL 			PRIMARY KEY,
	curso 		VARCHAR(1000) 	NOT NULL,
	matricula 	BIGINT 			NOT NULL,
	senha		VARCHAR(255)	NOT NULL,
	data_nasc 	DATE
);
