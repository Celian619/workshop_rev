#include <stdio.h>
#include <string.h>

int main(){

	FILE * monfichier = fopen("key.txt","r");
	
	if(monfichier !=NULL){
		char key[14]; 
		fscanf(monfichier,"%13s",key);
		
		
		
		int decalages[] = {0xf2,0x21,0xab,0x19,0x31,0xc9,0x15,0x99,0x15,0x88};
		
		char pass1[] = {0x9e,0x44,0xc6,0x7c,0x58,0xa5,0x79,0xfc,0x60,0xfa,0x9f,0x4e,0xdf,0x7d,0x54,0xb9,0x74,0xea,0x66,0xed,0};//"lemeilleurmotdepasse";
		char pass2[] = {0x98,0x40,0xc2,0x76,0x44,0xab,0x79,0xf0,0x70,0xe5,0x9d,0x4f,0xc6,0x7d,0x41,0};//"jaioubliemonmdp";
		
		int i = 0;
		while(pass1[i] != 0){
			pass1[i] = pass1[i] ^ decalages[i%10];
			i++;
		}
		i=0;
		while(pass2[i] != 0){
			pass2[i] = pass2[i] ^ decalages[i%10];
			i++;
		}
		
		
		if(strcmp(key, "127-FEVDC-937") == 0){
			printf("Mot de passe root-me: %s\n", pass1);
			printf("Mot de passe banque: %s\n", pass2);
		}else{
			printf("Clef invalide !\n");
		}
	}else{
		printf("Veuillez inserer la clef...\n");
	}
}	
