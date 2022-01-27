#include <stdio.h>


void afficher_resultat(int signe, int signe_gagnant){

        
        char  signes[][10] =  {"Ciseaux","Cailloux","Papier"};

        if(signe == signe_gagnant){
                printf("Egalité ! J'ai fait : %s\n", signes[signe_gagnant]);
        
        }else if(signe_gagnant == (signe + 1) %3){
                printf("J'ai gagné ! J'ai fait : %s\n", signes[signe_gagnant]);
        
        }else{
                printf("Tu as gagné ! J'ai fait : %s\n", signes[signe_gagnant]);
        }
        

}


int main(){
        int signe;
        puts("Choisissez votre nombre :");
        do{
                puts("Ciseaux (0), Cailloux (1) ou Papier (2) ?");
                scanf("%i",&signe);
                while(getchar() != '\n');
        }while(signe > 2 || signe < 0);
        
        int signe_gagnant = (signe + 1) %3;//papier par defaut
        
        afficher_resultat(signe, signe_gagnant);
        

}
