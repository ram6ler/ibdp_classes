function IS_CORRECT(EXPRESSION, N)
    SYMBOLS = new Stack()
    TOOLS = new Array("(", ")", "[", "]", "{", "}", "<", ">")
    loop I from 0 to N - 1
        C = EXPRESSION[I]
        if C = "(" or C = "[" or C = "{" or C = "<" then
            SYMBOLS.push(C)
        end if
        loop J from 0 to 3
            if EXPRESSION[I] = TOOLS[2 * J + 1] then
                if SYMBOLS.isEmpty() then
                    return false
                end if
                if SYMBOLS.pop() ≠ TOOLS[2 * J] then
                    return false
                end if
            end if
        end loop
    end loop
    return SYMBOLS.isEmpty()
end function

EXPRESSION = new Array("(", "[", "]", "<", ">", ")")
output "EXPRESSION: ", EXPRESSION
output IS_CORRECT(EXPRESSION, 6)

EXPRESSION = new Array("(", "[", "]", "<", ">", "(")
output "EXPRESSION: ", EXPRESSION
output IS_CORRECT(EXPRESSION, 6)