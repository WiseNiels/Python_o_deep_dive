
# **Lista de Exercícios – Iteradores e Iteráveis Personalizados em Python**  

## **Básico**  

### **1. Criando um Iterável Básico**  
Crie uma classe chamada `MeuIteravel` que implemente `__iter__` e retorne um iterador. O iterador deve percorrer uma lista de números de 1 a 5.  

### **2. Criando um Iterador Personalizado**  
Implemente uma classe `Contador` que recebe um valor inicial e um valor final e itera de forma crescente. Utilize os métodos `__iter__` e `__next__`.  

---

## **Intermediário**  

### **3. Iterador Reverso**  
Crie um iterador chamado `Reverso` que recebe uma string e a percorre de trás para frente.  

### **4. Iterador Infinito**  
Implemente um iterador `Ciclo` que recebe uma lista e percorre infinitamente seus elementos.  

### **5. Iterador de Múltiplos**  
Crie um iterador `MultiplosDeN` que recebe um número `n` e gera múltiplos desse número até um limite especificado.  

---

## **Avançado**  

### **6. Criando um Iterável com Suporte a Slices**  
Implemente uma classe `FaixaNumerica` que funciona como `range()`, permitindo iteração e suporte a fatiamento (`obj[1:4]`).  

### **7. Iterador com Cache**  
Crie um iterador que memoriza os últimos 5 valores iterados e pode exibir esses valores sob demanda.  

