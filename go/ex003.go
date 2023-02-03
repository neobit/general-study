// Exercício: Crie um programa que leia três números inteiros e determine se eles podem formar os lados de um triângulo equilátero. Em seguida, imprima "É triângulo equilátero" ou "Não é triângulo equilátero".

package main

import (
	"fmt"
)

func main() {
	var num1, num2, num3 float64
	fmt.Print("Digite o primeiro lado do triângulo: ")
	fmt.Scanln(&num1)
	fmt.Print("Digite o segundo lado do triângulo: ")
	fmt.Scanln(&num2)
	fmt.Print("Digite o terceiro lado do triângulo: ")
	fmt.Scanln(&num3)

	if num1 < num2 + num3 && num2 < num1 + num3 && num3 < num1 + num2 {
		fmt.Print("É um triangulo!")
		if num1 == num2 && num1 == num3 && num2 == num3 {
			fmt.Print("E esse triângulo, é um triângulo Equilátero!\n")
		} else if num1 != num2 && num1 != num3 && num2 != num3 {
			fmt.Print("E esse triângulo, é um triângulo Escaleno!\n")
		} else {
			fmt.Print("E esse triângulo, é um triângulo Isósceles!\n")
		}
	} else {
		fmt.Print("Não é um triangulo.")
	}
}