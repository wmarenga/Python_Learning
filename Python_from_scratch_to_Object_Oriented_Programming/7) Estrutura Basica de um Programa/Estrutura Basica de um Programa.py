"""
Linguagem de Alto Nivel e Baixo Nivel:


Ola Mundo!!! em Java (Alto Nivel):

class MeuPrograma {
    public static void main(String args[]) {
        System.out.println("Ola Mundo!!!");
    }
}

Ola Mundo!!! em C# (Alto Nivel):

using System;
namespace MeuPrograma {
    class OlaMundo {
        static void Main(string[] args) {
            console.WriteLine("Ola Mundo!!!");
            console.ReadKey();
        }
    }
}

Ola Mundo!!! em Python (Alto Nivel):

print("Ola Mundo!!!")


Ola Mundo!!! em Assembly (Baixo Nivel):

section         .text
global          _start

__start:

    mov         edx,len
    mov         ecx,msg
    mov         ebx,1
    mov         eax,4
    int         0x80
    
    mov         eax,1
    int         0x80
    
section         .data 

msg      db   'Ola, Mundo!!!,0xa
len      equ  $ - msg

"""