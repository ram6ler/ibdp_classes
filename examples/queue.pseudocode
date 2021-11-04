function BIGGEST_FIRST(C1, C2)
    Q = new Queue()
    C1.resetNext()
    C2.resetNext()
    loop while C1.hasNext() or C2.hasNext()
        if C1.hasNext() and C2.hasNext() then
            X = C1.getNext()
            Y = C2.getNext()
            if X > Y then
                Q.enqueue(X)
                Q.enqueue(Y)
            else
                Q.enqueue(Y)
                Q.enqueue(X)
            end if
        else
            if C1.hasNext() then
                Q.enqueue(C1.getNext())
            else
                Q.enqueue(C2.getNext())
            end if
        end if
    end loop
    return Q
end function

ITEMS_1 = new Collection(9, 10, 5, -1, 3)
output "ITEMS_1:", ITEMS_1 

ITEMS_2 = new Collection(5, 15, -4, 0, 5, 10)
output "ITEMS_2:", ITEMS_2

QUEUE = BIGGEST_FIRST(ITEMS_1, ITEMS_2)
output "QUEUE:"
loop while not QUEUE.isEmpty()
    output QUEUE.dequeue()
end loop