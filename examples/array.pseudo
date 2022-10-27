function CONTAINS(NEEDLE, HAYSTACK, N)
    FOUND = false
    loop K from 0 to N-1
        if HAYSTACK[K] = NEEDLE then
            FOUND = true
        end if
    end loop
    return FOUND
end function

HAYSTACK = new Array(2, 3, 5, 7, 11, 13, 17, 19)
output "HAYSTACK:", HAYSTACK
output "5 is in HAYSTACK?"
output CONTAINS(5, HAYSTACK, 8)
output "4 is in HAYSTACK?"
output CONTAINS(4, HAYSTACK, 8)