create database aps6semestre;
use aps6semestre;

CREATE TABLE aps6semestre.USUARIO
(Id INTEGER UNIQUE,
Nome VARCHAR(100),
NivelAcesso INTEGER(1),
PRIMARY KEY (Id)
);

INSERT INTO USUARIO (Id, Nome, NivelAcesso) VALUES (1, 'Michael Polidoro', 3);
INSERT INTO USUARIO (Id, Nome, NivelAcesso) VALUES (2, 'Murilo Lucas', 2);
INSERT INTO USUARIO (Id, Nome, NivelAcesso) VALUES (3, 'Lucas Santos', 1);

CREATE TABLE aps6semestre.PRODUTORA
(Id INTEGER UNIQUE,
Nome VARCHAR(100),
Endereco VARCHAR(100),
Produtos VARCHAR(100),
ProducaoAnual DECIMAL(10,2),
DestinoProducao VARCHAR(30),
QtdEmpregados INTEGER,
QtdMaquinas INTEGER,
NivelAutomacao VARCHAR(100),
PRIMARY KEY (Id)
);

INSERT INTO PRODUTORA (Id, Nome, Endereco, Produtos, ProducaoAnual, DestinoProducao, QtdEmpregados, QtdMaquinas, NivelAutomacao)
 VALUES (1, 'Agro Milho', 'Avenida Brigadeiro Vitor', 'Milho', 100000.2, 'Interno', 100, 50, 'Medio');
/*INSERT INTO PRODUTORA (Id, Nome, Endereco, Produtos, ProducaoAnual, DestinoProducao, QtdEmpregados, QtdMaquinas, NivelAutomacao)
 VALUES (2, 'Produtora KEP Ltda.', 'Avenida Tiete', 'Soja', 150000.9, 'Externo', 1000, 90, 'Auto');
INSERT INTO PRODUTORA (Id, Nome, Endereco, Produtos, ProducaoAnual, DestinoProducao, QtdEmpregados, QtdMaquinas, NivelAutomacao)
 VALUES (3, 'Corteva S.A.', 'Avenida Padre Godofredo', 'Arroz', 3000000.0, 'Interno', 1100, 110, 'Baixo');*/

CREATE TABLE aps6semestre.IMPOSTOS
(Id INTEGER UNIQUE,
IncentivosFiscais  VARCHAR(100),
ImpostosMunicipais DECIMAL(10,2),
ImpostosEstadual DECIMAL(10,2),
ImpostosFederal DECIMAL(10,2),
TaxasFederal DECIMAL(10,2),
IdProdutora INTEGER,
PRIMARY KEY (Id)
);

INSERT INTO IMPOSTOS (Id, IncentivosFiscais, ImpostosMunicipais, ImpostosEstadual, ImpostosFederal, TaxasFederal, IdProdutora)
 VALUES (1, 'Incentivo a Agricultura', 9000.8, 15671.0, 108900.2, 80630.0, 1);

CREATE TABLE AGROTOXICO
(
Id INTEGER UNIQUE,
Descricao  VARCHAR(100),
IdProdutora INTEGER,
PRIMARY KEY (Id)
);

INSERT INTO AGROTOXICO (Id, Descricao, IdProdutora)
 VALUES (1, 'Glifosato', 1);
 
/*SELECT p.Nome, p.Endereco, p.Produtos, p.ProducaoAnual, p.DestinoProducao, p.QtdEmpregados, p.QtdMaquinas, 
p.NivelAutomacao, i.IncentivosFiscais, i.ImpostosMunicipais, i.ImpostosEstadual, i.ImpostosFederal, i.TaxasFederal, 
a.Descricao, a.IdProdutora
FROM PRODUTORA p, IMPOSTOS i, AGROTOXICO a
WHERE p.id = i.IdProdutora
AND      p.id = a.IdProdutora*/