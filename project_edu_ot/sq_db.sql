CREATE TABLE  IF NOT EXISTS users(
    id integer  PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    firstname text NOT NULL,
    dateborn text NOT NULL,
    email text NOT NULL,
    hpsw text NOT NULL,
    time integer NOT NULL
);

CREATE TABLE  IF NOT EXISTS courses(
    id integer  PRIMARY KEY AUTOINCREMENT,
    themes text NOT NULL,
    edu_materials text NOT NULL,
    exsersis text NOT NULL,
    exzamen text NOT NULL,
    time integer NOT NULL
);

CREATE TABLE  IF NOT EXISTS docs(
    id integer  PRIMARY KEY AUTOINCREMENT,
    themes text NOT NULL,
    protocol blob NOT NULL,
    sertificate blob NOT NULL
);


