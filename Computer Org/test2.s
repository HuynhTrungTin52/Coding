.data
    list: .word 2, 4, 3, 6, 1

.text
.globl main

main:
    la $s6, list
    
    lb $t5, 16($s6)        # put a[3] into a[4]
    lb $t6, 12($s6)
    sb $t6, 16($s6)        
    sb $t5, 12($s6)
    
    lb $t5, 0($s6)        # swap a[3] and a[0]
    lb $t6, 12($s6)
    sb $t6, 0($s6)         
    sb $t5, 12($s6)         
    
    lb $t5, 4($s6)        # swap a[1] and a[3]
    lb $t6, 12($s6)
    sb $t6, 4($s6)         
    sb $t5, 12($s6)        

    lb $t0, 0($s6)
    lb $t2, 4($s6)
    lb $t3, 8($s6)
    lb $t4, 12($s6)
    lb $t5, 16($s6)
    la $v0, 10
    syscall
    
.end main