# idade = 42  # Tipágem implícita ou dinâmica

# print(type(idade))

# idade = 'Quarenta e dois'

# print(type(idade))

if True:
    resultado = 1 + 'Geek'  # Se for True irá apresentar um erro
else:
    resultado = 1 + 41

print(resultado)

# Em linguagens que utilizam a tipágem estática, a verificação será feita
# durante a compilação.

# Exemplo em Java (Tipágem Estática):
"""
public class TipoJava{
    
    public static void main(String[] args){
        String nome = "Geek University";
        
        nome = 42; # Irá apresentar um erro de "incompatible types"
        
        System.out.println(nome);
    }
}
"""
