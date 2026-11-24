-- Write your query below


SELECT first_name, last_name, city, state -- columns we want on final table; SELECT picks columns from the combined result of JOIN
FROM person
LEFT JOIN address
    ON person.person_id = address.person_id ; -- match rows by shared person_id
