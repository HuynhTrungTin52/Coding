#include <stdio.h>
int main()
{
	// Teaching portfolio : The final class is on 26/12/2024
	//Computer Organisation: Understanding the inner workings of a computer
	// Theory : 45 periods; Pratcial : 30  
	// email: lephuc@tdtu.edu.vn; number : 0907677675; Office : A0404(Department for Computing and Computer Services)
	// programming here is just used for understanding how a computer works
	// Basic gates : Not, AND, OR, XOR, NAND -> CPU which makes Logic Gates that allows basic math operations
	// Basic components of comouter : CPU, Memory, etc... DATA PATH which is ised for MIPS instructions sets -> Assembly Language
	// Reading materials : Digital Logic Design(main), Computer Organisation and Design : The hardware/Software Interface
	// Credits policy :
		// P.E 1 : 10%(Just be in classs)
		// P.E 2 : 20%(Do the labs session, do the exercises)
		// Mid Exam test(multi-choices) will be taken in the middle of the courses : 20%
		// Final Examin(multi-choices) will be taken at the end : 50%(Understand all of the chapters
	// We will be using MIPS Assembler and C(low level of the high level programming)



// Unit 1 : Number Systems and Codes

	// Policies : Don't share the slides nor modify em to share, just don't share
					// You can also use ChatGPT for homework and exercises
	// Why learn Computer Org ?
		// is the foundation to other software engineer courses
	// A computer must have a CPU, a storage, a software system. Because of this, many devices have a computer inside -> Embeded Computer
	// A computer is a device capable of solving problems according to designed programs. It simply augments our power of storage and speed of calculation
	// PC was built by IBM in 1981; Mac was built by Apple in 1984
	// The latest pc uses LCD monitor, different from CRT monitor
	// A PC always has a Motherboard/Mainboard
	// CPU : Control, Datapath; Memory; Devices : Input and output
	// Abstration : 
		// Delving into depth reveals more infor
		// Abstraction omits unnecessary details
		// High-Level Language -> Assembly Language -MIPS Assembler> Machine Language
	// Transistors -> Logic Gates -> CPU
	// Levels of Representsation 
		// High Level Language Program -> Assembly Language Program -> Machine Language Program -> Jardware Architecture Descruption -> Logic Circuit Description
	// Pratical Aspects
		// Experience : Logisim Sofware, PC Spim software, Logic Design Experiments
		// Prepare for the labs
			// Download Logisim(Only for learning) : You need Java Runtime Engine or Java Data Key(warning : Big file)
			// Spim :  You need to have MIPs(Million instructions per seconds), recommend using QTSpim 
	// Information representation :
		// Numbers are important to computers : Represent Information Precisely and can be processed
		// Examples : yes or no can be used as 0 and 1; Reoresent the 4 seasons : 0,1,2,3
		//Bit(Binary Digit) : 0,1; Represent false and true and logic; Represent the low and high states in electronic devices
		// Other bits :
			// Byte : 8 bits
			// Nibble : 4 bits(seldom used)
			// Word : Multiple of byte, depending on the architecture of the computer system
			// Bit -> Byte -> word -> Registry(Word Sife ???) of CPU(32 bits) or mostly(64 bits)
	// To represent M values, log2(M) bits are required
	// Decimal(Base 10)
		//How to turn a binary into a decimal :
		// 1(2)0(1)1(0) : 1*2^2+0*2^1+1*2^0 = 5
		//This formula is used for other number systems as well
		//762(Octal to decimal) : 7*8^2+6*7^1+2*8^1
	// Hexadecimal(hexa,hex) 16 Base : 0->9, A->F(1*16^1)



/* Unit 2 : Boolean Algebra
 Digital Circuits are circuits digitalize inside of a computer, resulting in two types of Signals 
 Digital Signal : Transmit data in a discrete function of time
 Analog Signals : Transmit counters in a continuous function of time

 Logic Blocks are blocks that compute inputs/data via logics, also having two types :
 Combinational : No memory, depends on solely on the input to make an output
 - Gates
 - Decoders, Multiplexers
 - Adders, Multipliers

 Sequential : With memory, output depends on both input and current state
 - Counters, Registers
 - Memories

 Boolean Algebra
 AND operator/Conjunction : A.B; AB; A big ass ^B
 OR operator : A+B, A big ass ^ but upside down B
 NOT operator : A', A with a big ass line ontop

 Order of Boolean
 Not;ANd;Or
NANO
Parenthesis to overwite precedence

Truth table is used for providing a list of every possible combinations of inputs and corresponding outputs
Example is in slid Chapter 2





*/
} 	
