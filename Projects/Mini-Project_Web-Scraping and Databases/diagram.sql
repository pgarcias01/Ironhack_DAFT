CREATE TABLE "cdi" (
  "id" SERIAL PRIMARY KEY,
  "data" date,
  "mesano" text,
  "valor" double
);

CREATE TABLE "dolar" (
  "id" SERIAL PRIMARY KEY,
  "data" date,
  "mesano" text,
  "cotacao" double
);

CREATE TABLE "dowjones" (
  "id" SERIAL PRIMARY KEY,
  "data" date,
  "mesano" text,
  "valor" double
);

CREATE TABLE "euro" (
  "id" SERIAL PRIMARY KEY,
  "data" date,
  "mesano" text,
  "cotacao" double
);

CREATE TABLE "ibov" (
  "id" SERIAL PRIMARY KEY,
  "data" date,
  "mesano" text,
  "valor" double
);

CREATE TABLE "igpm" (
  "id" SERIAL PRIMARY KEY,
  "mesano" text,
  "valor" double
);

CREATE TABLE "ipca" (
  "id" SERIAL PRIMARY KEY,
  "mesano" text,
  "valor" double
);

CREATE TABLE "poupanca" (
  "id" SERIAL PRIMARY KEY,
  "mesano" text,
  "valor" double
);

ALTER TABLE "dolar" ADD FOREIGN KEY ("data") REFERENCES "cdi" ("data");

ALTER TABLE "dowjones" ADD FOREIGN KEY ("data") REFERENCES "dolar" ("data");

ALTER TABLE "euro" ADD FOREIGN KEY ("data") REFERENCES "dowjones" ("data");

ALTER TABLE "ibov" ADD FOREIGN KEY ("data") REFERENCES "euro" ("data");

ALTER TABLE "ibov" ADD FOREIGN KEY ("mesano") REFERENCES "poupanca" ("mesano");

ALTER TABLE "ipca" ADD FOREIGN KEY ("mesano") REFERENCES "poupanca" ("mesano");

ALTER TABLE "igpm" ADD FOREIGN KEY ("mesano") REFERENCES "ipca" ("mesano");

ALTER TABLE "cdi" ADD FOREIGN KEY ("mesano") REFERENCES "igpm" ("mesano");
