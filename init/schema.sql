CREATE TABLE IF NOT EXISTS natural_person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    monthly_income REAL NOT NULL,
    age INTEGER NOT NULL,  
    name TEXT NOT NULL,
    phone_number TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    category TEXT,
    balance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS legal_entity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    billing REAL NOT NULL,
    age INTEGER NOT NULL,
    trade_name TEXT NOT NULL,
    phone_number TEXT NOT NULL UNIQUE,
    corporate_email TEXT NOT NULL UNIQUE,
    category TEXT,
    balance REAL NOT NULL
);

INSERT INTO natural_person (monthly_income, age, name, phone_number, email, category, balance)
VALUES
(5000.00, 35, 'João da Silva', '9999-8888', 'joao@example.com', 'Category A', 10000.00),
(4000.00, 45, 'Maria Oliveira', '7777-6666', 'maria@example.com', 'Category B', 15000.00),
(6000.00, 28, 'Pedro Santos', '5555-4444', 'pedro@example.com', 'Category C', 8000.00);

INSERT INTO legal_entity (billing, age, trade_name, phone_number, corporate_email, category, balance)
VALUES
(100000.00, 10, 'Enterprise XYZ', '1111-2222', 'contact@enterprise.com', 'Category A', 50000.00),
(80000.00, 5, 'Enterprise ABC', '3333-4444', 'contact@abc.com', 'Category B', 70000.00),
(120000.00, 8, 'Enterprise 123', '5555-6666', 'contact@123.com', 'Category C', 90000.00);