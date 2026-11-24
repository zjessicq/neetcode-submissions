-- Write your query below

SELECT student_id, exam_id, score        -- outer query: only the columns we want (row_rank is dropped)
FROM (
    SELECT
        student_id,
        exam_id,
        score,

        ROW_NUMBER() OVER (              -- numbers the rows inside each group; starts counting from top so top row = 1 (highest score)
            PARTITION BY student_id            -- ONE column: makes a separate group per student
            ORDER BY score DESC,         -- 1st: score, direction? (we want the highest first)
                     exam_id ASC           -- 2nd: tie-breaker column, direction? (smallest first)
        ) AS row_rank                          -- row_rank is the row's rank within its student's group
    FROM exam_results
) t                                      -- subquery needs an alias (t)
WHERE row_rank = 1                          -- keep only the row ranked in this position
ORDER BY student_id