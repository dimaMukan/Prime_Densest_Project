function PrimeDenseWindows (S, W, N)

    If S contains any non-digit characters THEN
        RETURN  "0, 0: Invalid input"

    SET max_count TO 0
    SET best_index TO 0
    SET best_primes TO empty list

    FOR i FROM 0 TO length(S) - W

        SET current primes TO empty list

        FOR start FROM i TO i + W - 1
            FOR end FROM i TO i + W - 1

            SET sub TO substring of S from start to end
            SET number TO convert sub to integer

            IF number < N AND number > 1 THEN

                SET is_prime TO TRUE

                FOR k FROM 2 TO square root of number
                    IF number MOD k = 0 THEN
                        SET is_prime TO TRUE
                        BREAK
                    ENDIF
                ENDIF

            ENDIF
        ENDFOR
    ENDFOR