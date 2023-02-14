#include <stdio.h>
#include <string.h>

#define MAXSIZE 101
// Programa��o din�mica;
int matriz[MAXSIZE][MAXSIZE];
int memoria[MAXSIZE][MAXSIZE];

int calcula(int linha, int coluna);
int mim(int a, int b);

void main ()
{

	unsigned short i, j;
	unsigned short tamMatriz;

	scanf("%hu", &tamMatriz);

	for (i = 1; i <= tamMatriz; ++i)
		for (j = 1; j <= tamMatriz; ++j)
			scanf("%d", &matriz[i][j]);

	// Preenche a matriz mem�ria com -1 para sinalizar
	// Que o valor da c�lula ainda n�o foi calculado;
	memset(memoria, -1, sizeof(memoria));

	printf("%d\n", calcula(tamMatriz, 1));

}

int calcula(int linha, int coluna)
{

	int soma = 0;
	unsigned short i;

	// Se na posi��o [linha][coluna] da matriz memoria n�o tiver -1
	// Quer dizer que essa posi��o j� foi calculada, retorne essa posi��o;
	if (memoria[linha][coluna] != -1)
		return memoria[linha][coluna];

	// Se for a primeira linha (caso base), ent�o retorne a matriz mem�ria
	// com o elemento da matriz nessa posi��o;
	if (linha == 1)
		return memoria[linha][coluna] = matriz[linha][coluna];

	// Recorrencia;
	for (i = 0; i < linha; ++i)
		soma += matriz[linha][coluna + i];

	return memoria[linha][coluna] = soma + mim(calcula(linha - 1, coluna), calcula(linha - 1, coluna + 1));

}

int mim(int a, int b)
{

	if (a < b)
		return a;
	else
		return b;

}
