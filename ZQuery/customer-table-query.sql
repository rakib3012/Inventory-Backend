CREATE Table invoice (
    id INT PRIMARY KEY ,
    title VARCHAR(255),
    total_price DECIMAL(5,2),
    ceate_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL

)


CREATE Table invoice_product (
    id SERIAL PRIMARY KEY ,
    title VARCHAR(255),
    total_price DECIMAL(10,2),
    qty INT NOT NULL ,
    ceate_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)

ALTER TABLE invoice_product ADD  customer_name VARCHAR(255)

-- ALTER TABLE invoice_product ALTER COLUMN total_price TYPE DECIMAL(10,2);
-- ALTER COLUMN ceate_at SET DEFAULT TIMESTAMP;

-- ALTER COLUMN updated_at SET DEFAULT TIMESTAMP;

-- DROP TABLE invoice_product;


INSERT INTO invoice_product (customer_name,title,total_price,qty)
VALUES
('rakib', 't-shirt', 2000.00, 5),
('shakib', 'pent', 5000.00, 4),
('tanim', 'shirt', 2000.00, 3),
('rakib', 't-shirt', 2000.00, 5);



SELECT total_price FROM invoice_product WHERE total_price>2000


-- total price colum er akta data updata korar command

-- UPDATE invoice_product
-- SET total_price = 2500 WHERE id=

-- DELETE from invoice_product WHERE id=2

-- DELETE from invoice_product

-- TRUNCATE TABLE invoice_product RESTART IDENTITY

SELECT
total_price ,
total_price * 0.15 AS bonus_price
FROM invoice_product

DELETE FROM customers

TRUNCATE TABLE customers RESTART IDENTITY

DROP TABLE customers,invoice,invoice_product

DROP TABLE my_users;
DROP TABLE products
