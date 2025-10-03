.data
array: .word 0, 0, 0, 0, 0
max: .word 0
hdr: .asciiz "The following program will find the biggest element in an array of 4 elements. \n Please enter the following inputs. \n Enter the starting number :"
secMsg: .asciiz "Enter the next number :"

.text
.globl main
.ent main
main:
	la $s1,array #Loading the array
	li $s2,4 #Loading the number of an array
	li $s0,0 #Initilizing i	
loopSet: #Reading int from users and turning them into registers
	beq $s0,$s2,loopFind
	li $v0,5
	syscall
	sw $v0, 0($s0) #Storing the reader's input into array
		


loopFind: 
	beq $s0, $s2,exit
	addi $s1,$s1,4 #Getting array[i]
	lb $s3, 0($s1) # Accessing array[i]
	slt $t2, $t0, $s3 #If array[i] > first ->1
	bne $t2,$zero,assign
	addi $s0,$s0,1
	j loopFind
assign:
	sw $s3,max
	move $t0,$s3
	addi $s0,$s0,1
	j loop
exit:	
	li $v0,1
	lw $a0,max
	syscall
li $v0,10
syscall
.end main