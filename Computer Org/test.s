.data
hdr: .ascii "A to the power of B Examples \n"
	 .asciiz "Enter value for A: "
secMsg: .asciiz "Enter value for B: "
ansMsg: .asciiz "A^B : "
value: .word 0 

.text
.globl main
.ent main
main: 
	li $v0, 4 #Syscall to display a string
	la $a0, hdr
	syscall
	li $v0, 5 #syscall to read a value for A
	syscall
	move $t0,$v0
	add $s0,$zero,$t0
	li $v0,4 #display the second string
	la $a0, secMsg
	syscall
	li $v0, 5 #Value for B
	syscall
	move $t1,$v0
	li $t2,1 # Value for i
loop:
	beq,$t1,$t2,exit
	mul $s0,$s0,$t0
	addi $t2,$t2,1
	j loop
exit:
	sw $s0, value #Save result to a variable
	li $v0,4
	la $a0,ansMsg
	syscall
	li $v0,1
	lw	$a0, value
	syscall	
	li $v0, 10
	syscall
.end main 
