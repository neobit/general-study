package main

import "fmt"

func main() {
	var prova1, prova2, atv1, atv2 float64
	fmt.Print("Digite a sua nota da primeira prova: ")
	fmt.Scanln(&prova1)
	fmt.Print("Digite a sua nota da segunda prova: ")
	fmt.Scanln(&prova2)
	fmt.Print("Digite a sua nota do seu primeiro exercicio: ")
	fmt.Scanln(&atv1)
	fmt.Print("Digite a sua nota do seu segundo exercicio: ")
	fmt.Scanln(&atv2)

	media := (prova1 + prova2 + atv1 + atv2) / 4

	fmt.Println("Sua media é igual a:", media)
}
