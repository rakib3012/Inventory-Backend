/* indexing er jonno kisu shotorkota obolombon kortay hobay..
 1. small table 
 2. crate operation bashi but select operation kom
 3. duplicate index
 4. khub boro ba kom useable column
 5. shob gula column a index kora jabay nah 

*/

-- login optimise er jonno indexing....
CREATE INDEX idx_users_email ON users(email)

-- category table indexing korar jonno user_id column gula dea indexing korlay category data optimise hobay..
CREATE INDEX idx_categories_user_id ON categories(user_id)

-- customer table indexing er jonno user_id, email, mobile/phone column gula dea indexing koray customer data ka optimise kora jay..
CREATE INDEX idx_customers_user_id ON customers(user_id)

CREATE INDEX idx_customers_emai ON customers(email)

CREATE INDEX idx_customers_phone ON customers(phone)

-- product table indexing korar jonno user_id, name, category_id column gula dea indexing koraly product table er data optimise hoia jabay...
CREATE INDEX idx_products_user_id ON products(user_id)

CREATE INDEX idx_products_category_id ON products(category_id)

CREATE INDEX idx_products_name ON products(name)


-- invoices table indexing er jonno user_id customer_id column gula dea indexing korlay proudct table er data optimese hoia jabay ...

CREATE INDEX idx_invoices_user_id ON invoices(user_id)

create INDEX idx_invoices_customer_id ON invoices(customer_id)

CREATE INDEX idx_invoices_create_at ON invoices(create_at)


-- invoice_products table indexing er jonno user_id product_id invoice_id column gula dea indexing korlay invoice_product table ta optimise hoia jabay.

CREATE INDEX idx_invoice_products_user_id ON invoice_products (user_id)

CREATE INDEX idx_invoice_products_product_id ON invoice_products (product_id)

CREATE INDEX idx_invoice_products_invoice_id ON invoice_products (invoice_id)