.data
hdr: .ascii "Squaring Examples \n"
	 .asciiz "Enter value : "
ansMsg: .asciiz "Value squared : "
value: .word 0 

.text
.globl main
.ent main
main: 
	li $v0, 4 #Syscall to display a string
	la $a0, hdr
	syscall
	li $v0, 5 #syscall to read a number
	syscall
	mul $t0, $v0, $v0
	sw $t0, value #Save result to a variable
	li $v0,4
	la, $v0,ansMsg
	li $v0,1
	lw	$a0, value
	syscall	
	li $v0, 10
	syscall
.end main 
