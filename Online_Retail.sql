DROP DATABASE IF EXISTS Retail;
CREATE database Retail;
USE Retail;

CREATE table banks (								
	buyer_ID		int auto_increment,
	account_num		int,
    bank_name		varchar(20),
    primary key 	(buyer_ID, account_num)
) AUTO_INCREMENT = 1000;

CREATE table buyers (
	buyer_ID		int auto_increment,
	first_name		varchar(40) CHARACTER SET ucs2,
    last_name		varchar(40) CHARACTER SET ucs2,
    login_ID		varchar(40) CHARACTER SET ucs2,
    passw			varchar(40) CHARACTER SET ucs2,
    phone			varchar(20),
    email			varchar(40) CHARACTER SET ucs2,
    address			varchar(60) CHARACTER SET ucs2,
    primary key 	(buyer_ID)
    # foreign key 	(buyer_ID) references banks(buyer_ID)
) AUTO_INCREMENT = 1000;

CREATE table disc_category (
	category_ID		int,
    category		varchar(40),
    disc_percent	float,
    active			bool,
    primary key 	(category_ID)
);

CREATE table vendors (
	vendor_ID		varchar(40),
    phone			varchar(20),
    email			varchar(40),
    primary key 	(vendor_ID)
);

CREATE table products (
    item_ID			int auto_increment,
    category_ID		int,
    product_name	varchar(40),
    unit_price		float,
    primary key 	(item_ID),
    key				(category_ID),
    foreign key 	(category_ID) references disc_category(category_ID)
)  AUTO_INCREMENT = 10000;

CREATE table supply_stock (
	item_ID			int auto_increment,
    vendor_ID		varchar(40),
    quantity		int,
    primary key 	(vendor_ID, item_ID),
    foreign key 	(vendor_ID) references vendors(vendor_ID),
    foreign key 	(item_ID)   references products(item_ID)
) AUTO_INCREMENT = 10000;

CREATE table cart (
	buyer_ID		int,
    item_ID			int,
    quantity		int,
    primary key 	(buyer_ID),
    key				(item_ID),
    foreign key 	(buyer_ID) references banks(buyer_ID),
    foreign key 	(item_ID)  references products(item_ID)
);

CREATE table payments (
    buyer_ID		int auto_increment,
    payment_ID		int,
    paid_amount		float,
    paid_date		varchar(10),
    primary key 	(payment_ID),
    key				(buyer_ID),
    foreign key 	(buyer_ID) references cart(buyer_ID)
) AUTO_INCREMENT = 1000;

CREATE table invoices (
	payment_ID		int,
    item_ID			int,
    category_ID		int,
    quantity		int,
    disc_amount		float,
    total_price		float,
    primary key 	(payment_ID, item_ID),
    key				(category_ID),
    foreign key 	(item_ID)     references cart(item_ID),
    foreign key 	(category_ID) references products(category_ID),
    foreign key 	(payment_ID)  references payments(payment_ID)
) AUTO_INCREMENT = 100;


