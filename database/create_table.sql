BEGIN TRANSACTION;

create table intent (
    id int,
    intent_name varchar(100) not null,
    intent_examples text [],
    response text
);

COMMIT;

INSERT INTO
    intent (id, intent_name, intent_examples, response)
VALUES
    (
        0,
        'greet',
        ARRAY ['hi','hello'],
        'hello!'
    );

INSERT INTO
    intent (id, intent_name, intent_examples, response)
VALUES
    (
        1,
        'bye',
        ARRAY ['bye','salam'],
        'goodbye!'
    );