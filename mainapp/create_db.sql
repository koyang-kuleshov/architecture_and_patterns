PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS person;
CREATE TABLE items (item_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, category_id INTEGER, item_idx INTEGER, item_style VARCHAR (32), item_name VARCHAR (32), item_size VARCHAR (32));
INSERT INTO items (category_id, item_idx, item_style, item_name, item_size) VALUES (0, 0, '1BLCNVIS', 'Куртка', 'S');
INSERT INTO items (category_id, item_idx, item_style, item_name, item_size) VALUES (0, 1, '1BLCNVIM', 'Куртка', 'M');
INSERT INTO items (category_id, item_idx, item_style, item_name, item_size) VALUES (0, 2, '1BLCNVIXL', 'Куртка', 'XL');
INSERT INTO items (category_id, item_idx, item_style, item_name, item_size) VALUES (0, 3, '2BLCNVIM', 'Футболка', 'M');
INSERT INTO items (category_id, item_idx, item_style, item_name, item_size) VALUES (0, 4, '3BLCNVIM', 'Брюки', 'M');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
