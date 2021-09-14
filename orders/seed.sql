INSERT INTO 
    orders_menu (menu_name)
VALUES 
    ('Georgian cuisine'),
    ('Burgers Menu'),
    ('Pizza'),
    ('Hot Dogs'),
    ('Salades'),
    ('Coffee menu'),
    ('Chicken meals');

INSERT INTO 
    orders_restaurant (restaurant_name, menu_id)
VALUES 
    ('Georgian Heaven', (SELECT id FROM orders_menu WHERE menu_name='Georgian cuisine')),
    ('Tasty Burgers', (SELECT id FROM orders_menu WHERE menu_name='Burgers Menu')),
    ('Papa Pizza', (SELECT id FROM orders_menu WHERE menu_name='Pizza')),
    ('Very Hot Dog', (SELECT id FROM orders_menu WHERE menu_name='Hot Dogs')),
    ('Unusual Salades', (SELECT id FROM orders_menu WHERE menu_name='Salades')),
    ('Hot n Cold Coffee', (SELECT id FROM orders_menu WHERE menu_name='Coffee menu')),
    ('Chickenough', (SELECT id FROM orders_menu WHERE menu_name='Chicken meals'));

INSERT INTO 
    orders_item (item_name, item_price, menu_id)
VALUES 
    ('Shashlik', '400', (SELECT id FROM orders_menu WHERE menu_name='Georgian cuisine')),
    ('Potatoes', '300', (SELECT id FROM orders_menu WHERE menu_name='Georgian cuisine')),
    ('Georgian Salade', '250', (SELECT id FROM orders_menu WHERE menu_name='Georgian cuisine')),
    ('Small Burger', '100', (SELECT id FROM orders_menu WHERE menu_name='Burgers Menu')),
    ('Medium Burger', '150', (SELECT id FROM orders_menu WHERE menu_name='Burgers Menu')),
    ('Big Burger', '200', (SELECT id FROM orders_menu WHERE menu_name='Burgers Menu')),
    ('Gigantic Burger', '250', (SELECT id FROM orders_menu WHERE menu_name='Burgers Menu')),
    ('Margarita', '200', (SELECT id FROM orders_menu WHERE menu_name='Pizza')),
    ('Ham and cheese', '250', (SELECT id FROM orders_menu WHERE menu_name='Pizza')),
    ('Summer present', '300', (SELECT id FROM orders_menu WHERE menu_name='Pizza')),
    ('Carbonara', '300', (SELECT id FROM orders_menu WHERE menu_name='Pizza')),
    ('Short hot dog', '250', (SELECT id FROM orders_menu WHERE menu_name='Hot Dogs')),
    ('Long hot dog', '250', (SELECT id FROM orders_menu WHERE menu_name='Hot Dogs')),
    ('Spicy hot dog', '250', (SELECT id FROM orders_menu WHERE menu_name='Hot Dogs')),
    ('Fruit Salade', '250', (SELECT id FROM orders_menu WHERE menu_name='Salades')),
    ('Rich Salade', '250', (SELECT id FROM orders_menu WHERE menu_name='Salades')),
    ('Flavoured Salade', '250', (SELECT id FROM orders_menu WHERE menu_name='Salades')),
    ('Black Coffee', '100', (SELECT id FROM orders_menu WHERE menu_name='Coffee menu')),
    ('Espresso', '140', (SELECT id FROM orders_menu WHERE menu_name='Coffee menu')),
    ('Latte', '110', (SELECT id FROM orders_menu WHERE menu_name='Coffee menu')),
    ('Cappuccino', '130', (SELECT id FROM orders_menu WHERE menu_name='Coffee menu')),
    ('Macchiato', '120', (SELECT id FROM orders_menu WHERE menu_name='Coffee menu')),
    ('Baked chicken', '250', (SELECT id FROM orders_menu WHERE menu_name='Chicken meals')),
    ('Spicy chicken ', '250', (SELECT id FROM orders_menu WHERE menu_name='Chicken meals')),
    ('Chicken chops', '250', (SELECT id FROM orders_menu WHERE menu_name='Chicken meals'));