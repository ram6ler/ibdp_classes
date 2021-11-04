function ITEMS_DIVISIBLE_BY(ITEMS, N)
    // Where ITEMS is a collection of integers and N 
    // is an integer factor.
    RESULT = new Collection()
    ITEMS.resetNext()
    loop while ITEMS.hasNext()
        ITEM = ITEMS.getNext()
        if ITEM mod N = 0 then
            RESULT.addItem(ITEM)
        end if
    end loop
    return RESULT
end function

ITEMS = new Collection(7, 5, 3, 10, 15, 25, 16)
FILTERED = ITEMS_DIVISIBLE_BY(ITEMS, 5)

FILTERED.resetNext()
loop while FILTERED.hasNext()
    X = FILTERED.getNext()
    output X
end loop