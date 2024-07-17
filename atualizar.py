def atualizar_lb2(self):
        senha_gerada = self.gerar_senha()
        self.lb2.config(text=senha_gerada)
