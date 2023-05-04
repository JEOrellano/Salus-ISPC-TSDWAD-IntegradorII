-- CREAMOS BASE
CREATE DATABASE IF NOT EXISTS SALUS_E;
-- drop database SALUS_E;

-- USAMOS BASE
USE SALUS_E;

/* CREAR TABLAS */
-- TABLA  Cuentas
CREATE TABLE IF NOT EXISTS Cuentas(/*ver que no se aplique misma cuenta usuarios*/
CodCuenta_C CHAR(6) NOT NULL,
Saldo_C DECIMAL(18,2) NULL DEFAULT 0,
PRIMARY KEY(CodCuenta_C)
);
-- drop table Cuentas;
insert into Cuentas(CodCuenta_C)
values('001');
/*insert into Cuentas
values('001',100);*/
select * from cuentas;

-- TABLA  UsuariosMedicos
CREATE TABLE IF NOT EXISTS UsuariosMedicos(
  Dni_UM CHAR(8) NOT NULL,
  Matricula_UM CHAR(8) NOT NULL,
  Nombre_UM VARCHAR(45) NOT NULL,
  Apellido_UM VARCHAR(45) NOT NULL,
  Celular_UM VARCHAR(45) NOT NULL,
  Direccion_UM VARCHAR(100) NOT NULL,
  Localidad_UM VARCHAR(45) NOT NULL,
  Email_UM VARCHAR(45) NOT NULL,
  CodCuenta_UM CHAR(6) NOT NULL,
  PRIMARY KEY(Dni_UM),
  FOREIGN KEY(CodCuenta_UM) REFERENCES Cuentas(CodCuenta_C)
  );
-- drop table UsuariosMedicos;
insert into UsuariosMedicos
values ('1','1','MedicoNom1','MedicoApe1','MedCel1','MedDir1','MedLoc1','MedMail1','001');
select * from UsuariosMedicos;

-- TABLA UsuariosPacientes
CREATE TABLE IF NOT EXISTS UsuariosPacientes(
Dni_UP CHAR(8) NOT NULL,
Nombre_UP VARCHAR(45) NOT NULL,
Apellido_UP VARCHAR(45) NOT NULL,
Celular_UP VARCHAR(45) NOT NULL,
Direccion_UP VARCHAR(45) NOT NULL,
Localidad_UP VARCHAR(45) NOT NULL,
Email_UP VARCHAR(45) NOT NULL,
CodCuenta_UP char(6) NOT NULL,
PRIMARY KEY(Dni_UP),
FOREIGN KEY(CodCuenta_UP) REFERENCES Cuentas(CodCuenta_C)
);
-- drop tables UsuariosPacientes;
insert into UsuariosPacientes
values ('1','PasNom1','PasApe1','CelPas1','DirPas1','LocPas1','MailPas1','001');
select * from UsuariosPacientes;

-- TABLA MedicosPacientes
CREATE TABLE IF NOT EXISTS MedicosPacientes(
Dni_UM_MP CHAR(8) NOT NULL,
Dni_UP_MP CHAR(8) NOT NULL,
PRIMARY KEY(Dni_UM_MP, Dni_UP_MP),
FOREIGN KEY(Dni_UM_MP) REFERENCES UsuariosMedicos(Dni_UM),
FOREIGN KEY(Dni_UP_MP) REFERENCES UsuariosPacientes(Dni_UP)
);
-- drop table MedicosPacientes;
insert into MedicosPacientes
values('1','1');
select * from MedicosPacientes;

-- TABLA TiposEstudios
CREATE TABLE IF NOT EXISTS TiposEstudios(
CodEstudio_TE CHAR(6) NOT NULL,
NombreEstudio_TE VARCHAR(45) NOT NULL,
Descripcion_TE VARCHAR(45) NOT NULL,
PRIMARY KEY(CodEstudio_TE)
);
-- drop table TiposEstudios;
insert into TiposEstudios
values('1','Estudio01','DescripcionEstudio01');
select * from TiposEstudios;

-- TABLA HistorialesMedicos
CREATE TABLE IF NOT EXISTS HistorialesMedicos(
Dni_UM_HM CHAR(8) NOT NULL,
Dni_UP_HM CHAR(8) NOT NULL,
CodEstudio_HM CHAR(6) NOT NULL,
URL_HM VARCHAR(100) NOT NULL,
PRIMARY KEY(Dni_UM_HM,Dni_UP_HM,CodEstudio_HM),
FOREIGN KEY(Dni_UM_HM,Dni_UP_HM) REFERENCES MedicosPacientes(Dni_UM_MP,Dni_UP_MP),
FOREIGN KEY(CodEstudio_HM) REFERENCES TiposEstudios(CodEstudio_TE)
);
-- drop table HistorialesMedicos;
insert into HistorialesMedicos
values('1','1','1','www.tuestudio1nube.com');
select * from HistorialesMedicos;

-- TABLA Ventas
CREATE TABLE IF NOT EXISTS Ventas(
NroVenta_V INT NOT NULL AUTO_INCREMENT,
FechaVenta_V DATETIME NULL DEFAULT NOW(),
TotalVenta_V DECIMAL(18,2) NOT NULL DEFAULT 0,
CodCuenta_C_V CHAR(6) NOT NULL,
PRIMARY KEY(NroVenta_V),
FOREIGN KEY(CodCuenta_C_V) REFERENCES Cuentas(CodCuenta_C)
);
-- drop table Ventas;
insert into ventas (TotalVenta_V,CodCuenta_C_V)
values(100,'001');
/*insert into ventas (FechaVenta_V, TotalVenta_V,CodCuenta_C_V)
values('2023-05-03',100,'001');
insert into ventas (FechaVenta_V, TotalVenta_V,CodCuenta_C_V)
values(NOW(),100,'001');*/
select * from Ventas;

-- TABLA Servicios
CREATE TABLE IF NOT EXISTS Servicios(
CodServicio_S CHAR(6) NOT NULL,
TipoServicio_S CHAR(20) NOT NULL,
Precio_S DECIMAL(18,2) NOT NULL,
PRIMARY KEY(CodServicio_S)
);
-- drop table Servicios;
insert into servicios
values('1','Basico',250),
	('2','Medio',500),
    ('3','Alto',1000);
select * from Servicios;

-- TABLA ServiciosXMedicos
CREATE TABLE IF NOT EXISTS ServiciosXMedicos(
CodServicio_SXM CHAR(6) NOT NULL,
Dni_UM_SXM CHAR(8) NOT NULL,
PRIMARY KEY(CodServicio_SXM,Dni_UM_SXM),
FOREIGN KEY(CodServicio_SXM) REFERENCES Servicios(CodServicio_S),
FOREIGN KEY(Dni_UM_SXM) REFERENCES UsuariosMedicos(Dni_UM)
);
-- drop table ServiciosXMedicos;
insert into ServiciosXMedicos
values('1','1');
select * from ServiciosXMedicos;

-- TABLE DetallesVentas
CREATE TABLE IF NOT EXISTS DetallesVentas(
NroVenta_DV INT NOT NULL,
CodServicio_SXM_DV CHAR(6) NOT NULL,
Dni_UM_SXM_DV CHAR(8) NOT NULL,
PrecioServi_DV DECIMAL(18,2) NOT NULL,
CantServi_DV INT NOT NULL,
PRIMARY KEY(NroVenta_DV,CodServicio_SXM_DV,Dni_UM_SXM_DV),
FOREIGN KEY(NroVenta_DV) REFERENCES Ventas (NroVenta_V),
FOREIGN KEY(CodServicio_SXM_DV,Dni_UM_SXM_DV) REFERENCES ServiciosXMedicos(CodServicio_SXM,Dni_UM_SXM)
);
-- drop table ServiciosXMedicos;
insert into DetallesVentas
values(1,'1','1',250,1);
select * from DetallesVentas;
