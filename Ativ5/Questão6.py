from estruturas_dados import Pilha

class Navegador:
    def __init__(self):
        self.historico_voltar = Pilha()
        self.historico_avancar = Pilha()
        self.pagina_atual = None

    def visitar_pagina(self, pagina):
        if self.pagina_atual:
            self.historico_voltar.empilhar(self.pagina_atual)
        self.pagina_atual = pagina
        self.historico_avancar = Pilha() 
        print(f"Visitando: {self.pagina_atual}")

    def voltar(self):
        if not self.historico_voltar.esta_vazia():
            self.historico_avancar.empilhar(self.pagina_atual)
            self.pagina_atual = self.historico_voltar.desempilhar()
            print(f"Voltando para: {self.pagina_atual}")
        else:
            print("Não há páginas para voltar.")

    def avancar(self):
        if not self.historico_avancar.esta_vazia():
            self.historico_voltar.empilhar(self.pagina_atual)
            self.pagina_atual = self.historico_avancar.desempilhar()
            print(f"Avançando para: {self.pagina_atual}")
        else:
            print("Não há páginas para avançar.")

    def status(self):
        print(f"\n--- Status do Navegador ---")
        print(f"Página atual: {self.pagina_atual}")
        print(f"Histórico de Voltar: {self.historico_voltar}")
        print(f"Histórico de Avançar: {self.historico_avancar}")
