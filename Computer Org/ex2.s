.data
hdr: .ascii "Check if a number is prime \n"
	 .asciiz "Enter a value : "
trueMsg: .asciiz "The number above is prime"
falseMsg: .asciiz "The number above isn't prime"
value: .word 0

.text
.globl main
.ent main
main:
	li $v0,4
	la $a0,hdr
	syscall
	li $v0,5
	syscall
	move $s0,$v0 #Value is in s0
	li $t0,2 #Call i as 2
loop:
	beq $s0,$t0,true 
	div $t1,$s0,$t0
	mfhi $t2
	beq $t2,$zero, false
	addi $t0,1
	j loop

true:
	li $v0,4
	la $a0,trueMsg
	syscall
	j exit
false:
	li $v0,4
	la $a0,falseMsg
	syscall
	j exit

exit:
	li $v0,10
	syscall
.end main